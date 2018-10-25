// pick modals
var breakfastmodal = document.getElementById('breakfastmodal');



// pick buttons
var breakfast_btn = document.getElementById("breakfast_btns");
var breakcancel_btn=document.getElementById("breakcancel");
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
        var row = `<table id="breakfast">
                    <tr>                             
                    <th>Item</th>                                    
                    <th>Quantity</th>
                    <th>Price</th>                   
                    </tr>`;
        for (i=0;i<data.length;i++){             
            if(data[i].category=="breakfast"){
                var option=document.createElement("option");              
                option.textContent=data[i].item_name;
                option.value=data[i].item_name;
                selected.appendChild(option);
                row += '<tr><td>'+data[i].item_name+'</td><td>'+data[i].price+'</td><td>'+data[i].quantity+'</td></tr>';
                // row += '<tr><td>'+data[i].item_name+'</td><td>'+data[i].price+'</td><td>'+data[i].quantity+'</td><td><button onclick="getId()">order_id</button></td></tr>';
            }
            else{
                console.log("well");
            } 
            document.getElementById("table").innerHTML = row+"</table>";         
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