
// Objekt in Browserkonsole
// console.log($("#terminal"));
// temp1.text("testetxt"); 


// GET report of resources
$("#report").on("click", function(){
    $.ajax({
        url: "/coffee_maker/",
    }).done(function(report_data) {
        document.getElementById("terminal_text").innerHTML = 'Current resources available: ' + '<br>' + '<br>' + 'Water: ' + report_data.water + '<br>' + 'Milk: ' + report_data.milk + '<br>' + 'Coffee: ' + report_data.coffee; 
    });
});


// GET report of current profit 
$("#profit_report").on("click", function(){
    $.ajax({
        url: "/money_machine/",
    }).done(function(report_data) {
        document.getElementById("terminal_text").innerHTML = 'Current profit is: ' + '<br>' + '<br>' + report_data
    });
});







// Invert variable ON for RUNNING 
 var ON = Boolean;

$("#on_off").on("click", function(){
    console.log('first:' + ON)
    ON = !ON
    console.log('then: ' + ON)
});

