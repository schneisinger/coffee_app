
// Objekt in Browserkonsole
// console.log($("#terminal"));
// temp1.text("testetxt"); 


// GET report of resources
$("#report").on("click", function(){
    $.ajax({
        url: "/coffee_maker/",
    }).done(function(report_data) {
        console.log(report_data)
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
    $.post('/coffe_maker/coffee',  
            { amount: document.getElementById("amount_coffee") }, 
            ).done(function(amount) { 
                document.getElementById("terminal_text").innerHTML = 'Refilled: ' + '<br>' + amount + 'g of coffee';
                document.getElementById("amount_coffee").innerHTML = 0;
        });
    });


    // $.ajax('/jquery/submitData', {
    //     type: 'POST',  // http method
    //     data: { myData: 'This is my data.' },  // data to submit
    //     success: function (data, status, xhr) {
    //         $('p').append('status: ' + status + ', data: ' + data);
    //     },
    //     error: function (jqXhr, textStatus, errorMessage) {
    //             $('p').append('Error' + errorMessage);
    //     }
    // });


// Invert variable ON for RUNNING 
 var ON = Boolean;

$("#on_off").on("click", function(){
    console.log('first:' + ON)
    ON = !ON
    console.log('then: ' + ON)
});

