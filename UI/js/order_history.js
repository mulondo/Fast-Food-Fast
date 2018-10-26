var histo=document.getElementById("history_link");
histo.onclick=function(){
    // window.location.href="history.html"
    fetch('https://real-fast-food-fast.herokuapp.com/api/v2/users/orders',{
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
                    <th>Order_Id</th>  
                    <th>Date</th>                                  
                    <th>Order_Items</th>
                    <th>Payment_mode</th>
                    <th>Location</th>
                    <th>Status</th>                  
                    </tr>`;
    for (i=0;i<data.length;i++){               
        row += '<tr><td>'+data[i].order_id+'</td><td>'+data[i].date+'</td><td>'+data[i].order_items+'</td><td>'+data[i].payment_mode+'</td><td>'+data[i].location+'</td><td>'+data[i].status+'</td></tr>';     
        document.getElementById("history").innerHTML = row+"</table>";         
    }
        
    })
    .catch(error=>alert("errors"));
    
}
