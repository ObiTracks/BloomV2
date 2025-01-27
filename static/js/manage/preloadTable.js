// METHOD 1 For getting dynamically added jquery dom elements

$("table").ready(function () {
    var tableBody = null;
    var tableHeaders = $("#table thead th");
    var tableRows = $(this).find("tbody tr");
    // var selectedCells = $("#table td.selected");
    // console.log("Yeo", tableRows);
    preLoadTable(tableHeaders, tableRows);
});


function preLoadTable(tableHeaders, tableRows) {
    // timeslotJson = JSON.parse($("#id_timeslots").text());
    var timeslotJson = jsonTimeslots;
    // console.log("Json timesLots: ", jsonTimeslots);

    // GOAL: Prefill the table with the amenity's previous timeslots
    //1. Loop through days in the json
    //1.1 Find the corresponding day column index
    // 2. Loop through the timeslot windows in the json
    // 3.Find each timestamp in the timeslot window
    // 3.1 Find the corresponding row index where the time is the same as the timestamp
    // 3.2 From this we can access the exact cell, then add the selected that cell in the dom

    // console.log("Hello");
    // console.log(Object.entries(timeslotJson));
    console.log(timeslotJson);
    timeslotJson.forEach((obj) => {
        var day = obj.day;
        var slots = obj.slots.map(slot => slot.window);
        var column_index = obj.index;
        console.log(column_index);

        // var column_index = tableHeaders.filter((x) => {
        //     return $(this).text() == day;
        // }).first().index();

        slots.forEach((slot) => {
            console.log(slot);
            curr_timeslot = timeConverter(slot[0], "f");
            timeslot_end = timeConverter(slot[1], "f");

            while (curr_timeslot <= timeslot_end) {
                row = tableRows.filter(function (x) {
                    return $(this).children().eq(0).text() == timeConverter(curr_timeslot, "s");
                }).first()
                cell = row.children().eq(column_index)
                cell.addClass("selected")

                curr_timeslot = curr_timeslot + (15 / 60);
            };
        });
    });

    // var testdata = {"Sun": [["01:00", "03:00"], ["05:00", "06:00"], ["07:45", "09:15"]], "Mon": [["03:15", "04:45"]], "Tues": [["03:15", "04:45"], ["06:30", "09:00"]], "Wed": [["03:15", "04:45"], ["06:30", "09:00"]], "Thurs": [["03:15", "04:45"]], "Fri": [["03:15", "04:45"], ["06:30", "09:00"]], "Sat": [["06:30", "09:00"]]};


    // Object.entries(timeslotJson).forEach(function ([day, windows]) {
    //         column_index = tableHeaders.filter(function (x) {
    //             return $(this).text() == day;
    //         }).first().index();

    //         windows.forEach(function (window) {
    //             curr_timeslot = timeConverter(window[0], "f");
    //             timeslot_end = timeConverter(window[1], "f");

    //             while (curr_timeslot <= timeslot_end) {
    //                 row = tableRows.filter(function (x) {
    //                     return $(this).children().eq(0).text() == timeConverter(curr_timeslot, "s");
    //                 }).first()
    //                 cell = row.children().eq(column_index)
    //                 cell.addClass("selected")

    //                 curr_timeslot = curr_timeslot + (15 / 60);
    //             }
    //         })
    // });
}


// $(document).ready(loadTable());



// var tableHeaders = $("#table thead th");
// var testHead = "Mon"

// var columnCells = ""



// var day = tableHeaders.eq(cell.index()).text();
// var timeslot = cell.parent().children().eq(0).text().trim();
// var test = timeConverter(timeslot, "f")

// if (!timeslotsDict.has(day)) {
//     timeslotsDict.set(day, [timeslot]);
//     var timeslots = timeslotsDict.get(day);
//     // console.log(day, timeslots);

// } else {
//     var timeslots = timeslotsDict.get(day);
//     timeslots.push(timeslot);
//     // console.log(day, timeslots);
// }


// var json = getSelectedTimeslotIntervals(timeslotsDict);
// console.log(json);
// $("#results").text(JSON.stringify(json));
// $("#id_timeslots").text(JSON.stringify(json));