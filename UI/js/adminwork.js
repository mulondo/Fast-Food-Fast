function onclick_order_items() {
    document.getElementById("order_items_dropdown").classList.toggle("show");
} 
function onclick_order_items2() {
    document.getElementById("order_items_dropdowns").classList.toggle("show");
}
window.onscroll = function() {myFunction()};

var header = document.getElementById("myHeader");
var add_modal = document.getElementById('add');    
window.onclick = function(event) {
    if (event.target == add_modal) {
        modal.style.display = "none";
    }
}
var add_btn=document.getElementById("add_btn");
add_btn.onclick=function(){    
    items_data={
        price:document.getElementById("price").value,
        item:document.getElementById("item").value,
        quantity:document.getElementById("quantity").value,        
        category:document.getElementById("category").value
    }
    fetch('https://real-fast-food-fast.herokuapp.com/api/v2/menu',{
        method: 'POST',
        body: JSON.stringify(items_data),
        headers:{
            'Content-Type':'application/json',
            'Authorization': `Bearer ${localStorage.getItem('accessToken')}`
        }
    }).then(res=>res.json())
    .catch(error=>alert("errors"));

}
var get_items_btn=document.getElementById("get_items");
get_items_btn.onclick=function(){    
    fetch('https://real-fast-food-fast.herokuapp.com/api/v2/menu',{
        method: 'GET',
        body: JSON.stringify(items_data),
        headers:{
            'Content-Type':'application/json',
            'Authorization': `Bearer ${localStorage.getItem('accessToken')}`
        }
    }).then(res=>res.json())
    .catch(error=>alert("errors"));

}
