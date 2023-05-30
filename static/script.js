
// Objekt in Browserkonsole
// console.log($("#terminal"));
// temp1.text("testetxt"); 


// GET report by button 
$("#report").on("click", function(){
    $.ajax({
        url: "/coffee_maker/",
        // context: document.body
    }).done(function(report_data) {
        console.log(report_data);
    });
});


// Invert variable RUNNING 
var ON = false;

$("#on_off").on("click", function(){
    
    function(){
    if( ON === false){
        RUNNING = true;
   } else{
        RUNNING = false;
   }
}
});
