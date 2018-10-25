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
var make_order_btn=document.getElementById("submit_breakfast")

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

// open modals when buttons are clicked  
breakfast_btn.onclick = function() {
    breakfastmodal.style.display = "block";   
    var selected=document.getElementById("selected"); 
    breakfast_table=document.getElementById("breakfast");
    fetch('https://real-fast-food-fast.herokuapp.com/api/v2/menu',{
        method: 'GET',
        headers:{
            'Content-Type':'application/json',
            'Authorization': `Bearer ${localStorage.getItem("access_token")}`,
			'Access-Control-Allow-Origin': '*'
        }
    }).then(res=>res.json())
    .then(response=>{
        data=response.results;
        var i;
        for (i=0;i<data.length;i++){             
            if(data[i].category=="breakfast"){
                var option=document.createElement("option");
                var checkbox=document.createElement("input");
                checkbox.setAttribute('type','textarea');   
                var newrow=breakfast_table.insertRow(1);
                var item=newrow.insertCell(0);                
                var quantity=newrow.insertCell(1);
                var price=newrow.insertCell(2);
                var check=newrow.insertCell(3);
                check=checkbox;
                item.innerHTML=data[i].item_name;                
                price.innerHTML=data[i].price;
                quantity.innerHTML=data[i].quantity;
                option.textContent=data[i].item_name;
                option.value=data[i].item_name;
                selected.appendChild(option);
            }
            else{
                console.log("well");
            }          
        }
      
    })
    .catch(error=>alert("errors"));
}

make_order_btn.onclick=function(){   
   items_data={
    location:document.getElementById("location").value,
    payment_mode:document.getElementById("payment").value,        
    order_items:document.getElementById("selected").value
}
var token = localStorage.getItem("access_token");
// alert(data)
fetch('https://real-fast-food-fast.herokuapp.com/api/v2/users/orders',{
    method: 'POST',
    body: JSON.stringify(items_data),
    headers:{
        'Content-Type':'application/json',
        'Authorization': `Bearer ${localStorage.getItem("access_token")}`,
        'Access-Control-Allow-Origin': '*'
    }
    
}).then(res=>res.json())
.catch(error=>console.log("Error"));

location.reload();

    alert("order made succussfully");
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