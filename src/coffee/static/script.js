
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

        var myJSONObject = {"coffee": amount};
        console.log(typeof(myJSONObject))

        // var refill = strin
        // console.log(typeof(refill))

        $.ajax({
            type: 'PUT',
            url: '/coffee_maker/', 
            dataType: "json",
            contentType: 'application/json; charset=utf-8',
            data: JSON.stringify(myJSONObject), 
            success: function(){
                console.log("Refilled")
                // document.getElementById("terminal_text").innerHTML = 'Refilled: ' + '<br>' + didRefill.amount + 'g of ' + didRefill.ingredient;
                // document.getElementById("amount_coffee").innerHTML = 0;
            },
            error: function() {
                alert('Refill failed')
            },
            });
        });


    // Invert variable ON for RUNNING    
    $("#on_off").on("click", function(){
        var ON = document.getElementsByClassName('ON');

        for (var i = 0; i < ON.length; i ++) {
            ON[i].style.display = 'none';
        }
    });

});
