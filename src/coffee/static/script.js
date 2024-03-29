
// Objekt in Browserkonsole
// console.log($("#terminal"));
// temp1.text("testetxt");


delete_id = ""

function getID(clicked_id) {
    delete_id = document.getElementById(clicked_id)
    return delete_id
}


brew_id = ""


function getBREW(clicked_id) {
    brew_id = document.getElementById(clicked_id)
    return brew_id
}


$(function(){

    var $amount_coffee = $('#amount_coffee');
    var $amount_milk = $('#amount_milk');
    var $amount_water = $('#amount_water');

    // GET report of resources
    $("#report").on("click", function(){
        $.ajax({
            url: "/coffee_maker/",
        }).done(function(report_data) {
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
    $("#refill").on("click", function(){
        var coffee_amount = parseInt($amount_coffee.val());
        var water_amount = parseInt($amount_water.val());
        var milk_amount = parseInt($amount_milk.val());
        var myJSONObject = {"coffee": coffee_amount, "water": water_amount, "milk": milk_amount};

        $.ajax({
            type: 'PUT',
            url: '/coffee_maker/',
            dataType: "json",
            contentType: 'application/json; charset=utf-8',
            data: JSON.stringify(myJSONObject),
            success: function(){
                document.getElementById("terminal_text").innerHTML = 'Refilled: ' + '<br>' + '<br>' + coffee_amount + ' g of coffee.'
                                                                        + '<br>' + water_amount + ' ml of water.'
                                                                        + '<br>' + milk_amount + ' ml of milk.';
                default_coffee = document.getElementById("amount_coffee");
                default_water = document.getElementById("amount_water");
                default_milk = document.getElementById("amount_milk");
                default_coffee.value = default_coffee.defaultValue;
                default_water.value = default_water.defaultValue;
                default_milk.value = default_milk.defaultValue;
            },
            error: function() {
                alert('Refill failed')
            },
            });
        });


    // Edit recipes
    $("#edit_recipe").on("click", function(){
        var name_edit = document.getElementById("edit_name").value;
        var water_edit = document.getElementById("edit_water").value;
        var milk_edit = document.getElementById("edit_milk").value;
        var coffee_edit = document.getElementById("edit_coffee").value;
        var price_edit = document.getElementById("edit_price").value;
        var myJSONObject = {"name": name_edit, "water": water_edit, "milk": milk_edit, "coffee": coffee_edit, "price": price_edit};


    $.ajax({
        type: 'PUT',
        url: '/menu/',
        dataType: "json",
        contentType: 'application/json; charset=utf-8',
        data: JSON.stringify(myJSONObject),
        success: function(){
            console.log("Edit successfull. ")
        },
        error: function() {
            alert('Edit failed')
        },
        });
        location.reload();
    });


     // Brew drink
    $(".brew_button").on("click", function(){
        prod_brew = brew_id.id;

        $.ajax({
            type: 'PUT',
            url: '/coffee_maker/' + prod_brew,
            dataType: "json",
            contentType: 'application/json; charset=utf-8',
            data: prod_brew,
            success: function(){
                const regex = new RegExp("(?<=brew_).*");
                var product = regex.exec(prod_brew);
                // function capitalize(s){
                //         return s[0].toUpperCase() + s.slice(1);
                //     }
                // product = capitalize(re_product);
                document.getElementById("terminal_text").innerHTML = 'Please take your ' + '<br>' + '<br>' + product + ' ☕️ ' + '<br>' + '<br>' + 'Enjoy.';
            },
            error: function() {
                alert('Brew failed - please check & refill resources.')
            },
            });
        });

    // Delete recipes
    $(".delete_button").on("click", function(){
        prod_delete = delete_id.id;
        $.ajax({
            type: 'DELETE',
            url: '/menu/' + prod_delete,
            dataType: "json",
            contentType: 'application/json; charset=utf-8',
            data: prod_delete,
            success: function(){
                console.log("Delete successful.")
            },
            error: function() {
                alert('Delete failed')
            },
            });
        location.reload();
        });


    // Invert variable ON for RUNNING
    var ON = true
    $("#on_off").on("click", function(){
        ON = !ON
        var turn_off = document.getElementsByClassName('ON');
        if (ON === false) {
            for (var i = 0; i < turn_off.length; i ++) {
                turn_off[i].style.display = 'none';
            }
        }
        else {
            for (var i = 0; i < turn_off.length; i ++) {
                turn_off[i].style.display = 'initial'
            }
            document.getElementById("terminal_text").innerHTML = '<br>' + 'Hello world!' + '<br>' + '<br>' + 'This machine is under construction.';
        }
    });
});
