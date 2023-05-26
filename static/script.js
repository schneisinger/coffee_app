
// TEST Output field 
// var canvas = document.getElementById("output_screen");
// var ctx = canvas.getContext("2d");
// ctx.font = "15px Arial";
// ctx.fillStyle = "lime";
// ctx.textAlign = "center";
// ctx.fillText("Hello, world. \nOutput & animations go here.", 200, 50);

// Objekt in Browserkonsole
// console.log($("#terminal"));
// temp1.text("testetxt"); 

$("#report").on("click", function(){
    $.ajax({
        url: "/coffee_maker/",
        // context: document.body
    }).done(function(report_data) {
        console.log(report_data);
    });
});
