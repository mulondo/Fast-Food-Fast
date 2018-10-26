function onclick_order_items() {
    document.getElementById("order_items_dropdown").classList.toggle("show");
} 
function onclick_order_items2() {
    document.getElementById("order_items_dropdowns").classList.toggle("show");
}
window.onscroll = function() {
    myFunction()
};

var header = document.getElementById("myHeader");
var add_modal = document.getElementById('add');    
window.onclick = function(event) {
    if (event.target == add_modal) {
        modal.style.display = "none";
    }
}

var food_items=document.getElementById("food_items");
food_items.onclick=function(){
    document.getElementById('add').style.display='block';
    var table=document.getElementById("list_items");
   
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
            var newrow=table.insertRow(1);
            var item=newrow.insertCell(0);
            var category=newrow.insertCell(1);
            var quantity=newrow.insertCell(2);
            var price=newrow.insertCell(3);            
            item.innerHTML=data[i].item_name;
            category.innerHTML= data[i].category;
            price.innerHTML=data[i].price;
            quantity.innerHTML=data[i].quantity;

        //     // alert(JSON.stringify( data[i].category));
        }
      
    })
    .catch(error=>alert("errors"));
}

// var add_btn=document.getElementByn("add_btn");
add_btn.onclick=function(){    
    items_data={
        price:parseInt(document.getElementById("price").value),
        item:document.getElementById("item").value,
        quantity:document.getElementById("quantity").value,        
        category:document.getElementById("category").value
    }
    var token = localStorage.getItem("access_token");
    // alert(data)
    fetch('https://real-fast-food-fast.herokuapp.com/api/v2/menu',{
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
}


var get_items_btn=document.getElementById("get_items");
get_items_btn.onclick=function(){
    var table=document.getElementById("customer_orders");
    var newrow=table.insertRow(1);
    var orderid=newrow.insertCell(0);
    var date=newrow.insertCell(1);
    var customer_name=newrow.insertCell(2);
    var phone_number=newrow.insertCell(3);
    var payment_mode=newrow.insertCell(4);
    var order_items=newrow.insertCell(5);
    var status=newrow.insertCell(6);
    orderid.innerHTML='1';
    date.innerHTML="12/10/2018";
    customer_name.innerHTML="mulondo";
    phone_number.innerHTML="0703896312";
    payment_mode.innerHTML="mobile money";
    order_items.innerHTML="motooke";
    status.innerHTML="none";
    // fetch('https://real-fast-food-fast.herokuapp.com/api/v2/menu',{
    //     method: 'GET',
    //     headers:{
    //         'Content-Type':'application/json',
    //         'Authorization': `Bearer ${localStorage.getItem("access_token")}`,
	// 		'Access-Control-Allow-Origin': '*'
    //     }
    // }).then(res=>{
    //     console.log(res.json());
        
    // })
    // .catch(error=>alert("errors"));
    row += '<tr><td>'+data[i].item_name+'</td><td>'+data[i].price+'</td><td>'+data[i].quantity+'</td><td><button onclick="getId()">order_id</button></td></tr>';
}		
var close=document.getElementById("close");
close.onclick=function(){
    document.getElementById('add').style.display='none';
}
