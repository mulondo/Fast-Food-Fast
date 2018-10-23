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
var add_btn=document.getElementById("add_btn");
add_btn.onclick=function(){
    // alert(localStorage.getItem("access_token"));    
    items_data={
        price:parseInt(document.getElementById("price").value),
        item:document.getElementById("item").value,
        quantity:document.getElementById("quantity").value,        
        category:document.getElementById("category").value
    }
    var token = localStorage.getItem("access_token");
    var data = JSON.stringify(items_data)
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
    .catch(error=>alert("errors"));
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

}

var fetch_items=document.getElementById("fetch_items");
fetch_items.onclick=function(){
    // var table=document.getElementById("list_items");
    // var newrow=table.insertRow(1);
    // var itemid=newrow.insertCell(0);
    // var item=newrow.insertCell(1);
    // var category=newrow.insertCell(2);
    // var price=newrow.insertCell(3);
    // var quantity=newrow.insertCell(4);
     fetch('https://real-fast-food-fast.herokuapp.com/api/v2/menu',{
        method: 'GET',
        headers:{
            'Content-Type':'application/json',
            'Authorization': `Bearer ${localStorage.getItem("access_token")}`,
			'Access-Control-Allow-Origin': '*'
        }
    }).then(res=>{
        data=res.results;
        console.log(data);
        
            // itemid.innerHTML=items.items_id;
            // item.innerHTML=items.item_name;
            // category.innerHTML=items.category;
            // price.innerHTML=items.price;
            // quantity.innerHTML=items.quantity;
      
    })
    .catch(error=>alert("errors"));
    
}		
