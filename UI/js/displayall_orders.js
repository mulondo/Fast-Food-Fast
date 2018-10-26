fetch('https://real-fast-food-fast.herokuapp.com/api/v2/orders',{
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
    var row = `<table>
                <tr>                            
                <th>OrderId</th>
                <th>Date</th>
                <th>Customer name</th>
                <th>Phone number</th>           
                <th>Payment mode</th>
                <th>Order Items</th>
                <th>Location</th>
                <th>Status</th>
                <th>Options</th>                
                </tr>`;
for (i=0;i<data.length;i++){               
    row += '<tr><td>'+data[i].order_id+'</td><td>'+data[i].date+'</td><td>'+data[i].username+'</td><td>'+data[i].phone_number+'</td> <td>'+data[i].payment_mode+'</td> <td>'+data[i].order_items+'</td><td>'+data[i].location+'</td><td>'+data[i].status+'</td> <td><button onclick="decline('+data[i].order_id+')">decline</button> <button onclick="accept('+data[i].order_id+')">accept</button></td></tr>';           
}
document.getElementById("all_orders").innerHTML = row+"</table>";  
    
})

function decline(id){
    var id=id;
    data={
        status:"declined"     
    }
    fetch('https://real-fast-food-fast.herokuapp.com/api/v2/orders/'+id,{
        method: 'PUT',
        body: JSON.stringify(data),
        headers:{
            'Content-Type':'application/json',
            'Authorization': `Bearer ${localStorage.getItem("access_token")}`,
            'Access-Control-Allow-Origin': '*'
        }
        
    }).then(res=>res.json())
    .catch(error=>console.log("Error"));
    
    location.reload();
    
    alert("order is declined");
}

function accept(id){
    var id=id;
    data={
        status:"accepted"     
    }
    fetch('https://real-fast-food-fast.herokuapp.com/api/v2/orders/'+id,{
        method: 'PUT',
        body: JSON.stringify(data),
        headers:{
            'Content-Type':'application/json',
            'Authorization': `Bearer ${localStorage.getItem("access_token")}`,
            'Access-Control-Allow-Origin': '*'
        }
        
    }).then(res=>res.json())
    .catch(error=>console.log("Error"));
    
    location.reload();
    
    alert("order is accepted");
}