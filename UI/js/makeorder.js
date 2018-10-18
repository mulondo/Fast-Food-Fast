// pick modals
var breakfastmodal = document.getElementById('breakfastmodal');
var lunchmodal= document.getElementById('lunchmodal');
var dinnermodal= document.getElementById('dinnermodal');


// pick buttons
var breakfast_btn = document.getElementById("breakfast_btns");
var lunch_btn=document.getElementById("lunch_btn_id");
var dinner_btn=document.getElementById("dinner_btn_id");
var lunchcancel_btn=document.getElementById("lunchcancel");
var breakcancel_btn=document.getElementById("breakcancel");
var dinnercancel_btn=document.getElementById("dinnercancel");
var dinner_order_btn=document.getElementById("dinner_order");

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

// open modals when buttons are clicked  
breakfast_btn.onclick = function() {
    breakfastmodal.style.display = "block";
}
breakcancel_btn.onclick = function() {
    breakfastmodal.style.display = "none";
}
lunch_btn.onclick =function() {
    lunchmodal.style.display = "block";
}
lunchcancel.onclick =function() {
    lunchmodal.style.display = "none";
}
dinner_btn.onclick =function() {
    dinnermodal.style.display = "block";
}
dinnercancel_btn.onclick =function() {
    dinnermodal.style.display = "none";
}
dinner_order_btn.onclick=function(){
    var food=doucment.getElementById("chi").value;
    alert(food);
}

// function make_order(){
//     var 
// }