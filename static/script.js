
// Objekt in Browserkonsole
// console.log($("#terminal"));
// temp1.text("testetxt"); 

$(function(){

    var $amount_coffee = $('#amount_coffee');
    var $amount_milk = $('#amount_milk');
    var $amount_water = $('#amount_water');

    // GET report of resources
    $("#report").on("click", function(){
        $.ajax({
            url: "/coffee_maker/",
        }).done(function(report_data) {
            // console.log(report_data)
            document.getElementById("terminal_text").innerHTML = 'Current resources available: ' + '<br>' + '<br>' + 'Water: ' + report_data.water + ' ml' + '<br>' + 'Milk: ' + report_data.milk + ' ml' + '<br>' + 'Coffee: ' + report_data.coffee + ' g'; 
        });
    });


    // GET report of current profit 
    $("#profit_report").on("click", function(){
        $.ajax({
            url: "/money_machine/",
        }).done(function(report_data) {
            document.getElementById("terminal_text").innerHTML = 'Current profit is: ' + '<br>' + '<br>' + report_data;
        });
    });


    // Refill resources 
    // Coffee 
    $("#refill_coffee").on("click", function(){

        amount = parseInt($amount_coffee.val())
        console.log(amount)
        console.log(typeof(amount))

        var myJSONObject = {"ingredient": "coffee", "amount": amount};
        console.log(typeof(myJSONObject))

        // var refill = myJSONObject;
        // console.log(typeof(refill))

        $.ajax({
            type: 'PUT',
            url: '/coffee_maker/coffee/', 
            data: myJSONObject, 
            success: function(){
                console.log("Refilled")
                // document.getElementById("terminal_text").innerHTML = 'Refilled: ' + '<br>' + didRefill.amount + 'g of ' + didRefill.ingredient;
                // document.getElementById("amount_coffee").innerHTML = 0;
            }
            });
        });


    // Invert variable ON for RUNNING 
    var ON = Boolean;

    $("#on_off").on("click", function(){
        console.log('first:' + ON)
        ON = !ON
        console.log('then: ' + ON)
    });


});