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
from siteApp.querytools import *
from mgmtApp.crud_views import new_place
# Create your views here.


def dashboard_view(request):
    page_title = "Dashboard"
    page_subtitle = "Manage"
    places, amenity_groupings = getUsersPlacesAndAmenities(request, 2)

    print("\n\n\n\nDashboard loaded\n\n\n\n")
    # print(amenity_groupings)
    if request.method == "POST":
        place_form = PlaceForm(request.POST, request.FILES)
        print("\n\nMethod is post (place)\n\n")
        if place_form.is_valid():
            # place = place_form.save()
            print("\n\nPlace Supposedly saved\n\n")
            place = place_form.save(commit=False)
            place.owner = request.user.profile
            place.save()
            return redirect('manage:manage-dashboard')
        else:
            print("\n\nPlace form is Invalid\n\n")
            messages.error(request, "Place Form is invalid")

    place_form = PlaceForm()
    # new_place(request)

    context = {
        'page_title': page_title,
        'page_subtitle': page_subtitle,
        'amenity_groupings': amenity_groupings,
        'place_form': place_form,
        #    'amenity_form': amenity_form,
    }

    template_name = 'mgmtApp/dashboard.html'
    return render(request, template_name, context)


def places_view(request):
    # Object data
    page_title = "Places & Amenities"
    page_subtitle = "Manage"
    places, amenity_groupings = getUsersPlacesAndAmenities(request)

    # Forms & Interactions
    amenity_form = AmenityForm(request.user)
    if request.method == 'POST':
        amenity_form = AmenityForm(request.POST, request.FILES)

        if amenity_form.is_valid():
            amenity = amenity_form.save()
            return redirect(request.META['HTTP_REFERER'])
            # return redirect('dashboard')
        else:
            messages.error(request, "Amenity Form is invalid")

    new_place(request)

    context = {
        'page_title': page_title,
        'page_subtitle': page_subtitle,
        'amenity_form': amenity_form,
        # 'place_form': place_form,
        'amenity_groupings': amenity_groupings,
    }
    template_name = 'mgmtApp/places.html'
    return render(request, template_name, context)


def place_view(request, pk):
    # Object data
    place = Place.objects.get(id=pk)
    amenities = place.amenity_set.all()
    relationships =  PlaceProfileRelationship.objects.filter(place=place, profile_type__in=['4','5'] ).all()
    # members = [m.profile for m in r]
    place_form = PlaceForm(instance=place)

    if request.method == 'POST':
        place_form = PlaceForm(request.POST, request.FILES, instance=place)

        if place_form.is_valid():
            place = place_form.save()
            return redirect(request.META['HTTP_REFERER'])
        else:
            messages.error(request, "Place Form is invalid")

    context = {
        'place': place,
        'amenities': amenities,
        'relationships':relationships,
        'place_form': place_form,
    }
    template_name = 'mgmtApp/place.html'
    return render(request, template_name, context)


def amenity_view(request, pk):
    # Object data
    amenity = Amenity.objects.filter(id=pk).first()
    page_title = amenity.name
    page_subtitle = amenity.place.name

    form = AmenityForm(request.user, instance=amenity)
    if request.method == 'POST':
        form = AmenityForm(request.user, request.POST, instance=amenity)

        if form.is_valid():
            amenity = form.save()
            return redirect(request.META['HTTP_REFERER'])
        else:
            messages.error(request, "Amenity Form is invalid")

    context = {
        'page_title': page_title,
        'page_subtitle': page_subtitle,
        'amenity_form': form,
        'amenity': amenity,
        'jsonTimeslots': amenity.timeslots
    }
    template_name = 'mgmtApp/amenity.html'
    return render(request, template_name, context)


def joinrequests_view(request):
    # Object data
    page_subtitle = "Manage"
    page_title = "Join Requests"

    _, joinrequest_groupings = getUsersPlacesAndJoinRequest(request, 5)

    print(joinrequest_groupings)
    context = {
        'page_title': page_title,
        'page_subtitle': page_subtitle,
        'joinrequest_groupings': joinrequest_groupings
    }
    template_name = 'mgmtApp/joinrequests.html'
    return render(request, template_name, context)
