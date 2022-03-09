# Python packages
# import datetime as dt
from datetime import date, datetime, timedelta

import json
from django.core.serializers.json import DjangoJSONEncoder

# Imports for Django views
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render
from django.http import Http404
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404

# Imports for django forms
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

# Imports for django models
from django.db.models import Count

# Django authentication and messaging features
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.core.paginator import Paginator

from .forms import *
from siteApp.models import *
from siteApp.querytools import getUsersPlacesAndAmenities
from mgmtApp.crud_views import new_place
# Create your views here.


def dashboard_view(request):
    page_title = "Your Management Dashboard"
    # # AMENITIES
    # amenity_relationships = AmenityProfileRelationship.objects.filter(
    #     profile=request.user.profile, profile_type__in=['0', '1', '2', '3', '4'])
    # amenities = [i.amenity for i in amenity_relationships]

    # # Grouping Amenities by Place
    # amenity_groupings = {}
    # for amenity in amenities:
    #     if amenity.place not in amenity_groupings:
    #         amenity_groupings[amenity.place] = [amenity]
    #     else:
    #         amenity_groupings[amenity.place].append(amenity)

    places, amenity_groupings = getUsersPlacesAndAmenities(request)

    # print(amenity_groupings)

    place_form = PlaceForm()
    # amenity_form = AmenityForm(request.user)
    new_place(request)

    context = {'page_title': page_title,
               'amenity_groupings': amenity_groupings,
               'place_form': place_form,
               #    'amenity_form': amenity_form,
               }

    template_name = 'mgmtApp/dashboard.html'
    return render(request, template_name, context)


def amenities_view(request):
    # Object data
    page_title = "Amenity Hub"
    page_subtitle = "Places and Amenities"

    # PLACES MANAGED
    try:
        place_relationships = PlaceProfileRelationship.objects.filter(
            profile=request.user.profile, profile_type__in=['0', '1', '2', '3', '4'])
        places_managed = [i.place for i in place_relationships]
    except:
        places_managed = None

    amenity_groupings = {}
    for place in places_managed:
        amenities = Amenity.objects.filter(
            place=place)
        if place not in amenity_groupings:
            amenity_groupings[place] = amenities

    # Forms & Interactions
    amenity_form = AmenityForm(request.user)
    new_amenity(request)

    place_form = PlaceForm()
    new_place(request)

    context = {
        'page_title': page_title,
        'amenity_form': amenity_form,
        'place_form': place_form,
        'amenity_groupings': amenity_groupings,
    }
    template_name = 'mgmtApp/amenities.html'
    return render(request, template_name, context)


def amenity_view(request, pk):
    # Object data
    amenity = Amenity.objects.get(id=pk)
    page_title = amenity.name
    page_subtitle = amenity.place.name

    amenity_form = AmenityForm(request.user, instance=amenity)
    if request.method == 'POST':
        amenity_form = AmenityForm(request.user, request.POST, request.FILES, instance=amenity)

        if amenity_form.is_valid():
            amenity = amenity_form.save()
            # return
            # return redirect(request.META['HTTP_REFERER'])

            return redirect(request.META['HTTP_REFERER'])
            # return redirect('dashboard')
        else:
            messages.error(request, "Amenity Form is invalid")

    context = {
        'page_title': page_title,
        'page_subtitle': page_subtitle,
        'amenity_form': amenity_form,
    }
    template_name = 'mgmtApp/amenity.html'
    return render(request, template_name, context)
