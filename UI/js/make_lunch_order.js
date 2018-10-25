var lunchcancel_btn=document.getElementById("lunchcancel");
var lunch_btn=document.getElementById("lunch_btn_id");
var lunchmodal= document.getElementById('lunchmodal');
var make_order_btn=document.getElementById("submit_lunch")

lunch_btn.onclick =function() {
    lunchmodal.style.display = "block";
    var selected=document.getElementById("lselected"); 
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
        var row = `<table>
                    <tr>                             
                    <th>Item</th>                                    
                    <th>Quantity</th>
                    <th>Price</th>                   
                    </tr>`;
        for (i=0;i<data.length;i++){             
            if(data[i].category=="lunch"){
                var option=document.createElement("option");              
                option.textContent=data[i].item_name;
                option.value=data[i].item_name;
                selected.appendChild(option);
                row += '<tr><td>'+data[i].item_name+'</td><td>'+data[i].price+'</td><td>'+data[i].quantity+'</td></tr>';
                // row += '<tr><td>'+data[i].item_name+'</td><td>'+data[i].price+'</td><td>'+data[i].quantity+'</td><td><button onclick="getId()">order_id</button></td></tr>';
            }
            else{
                console.log("something is wrong");
            } 
            document.getElementById("ltable").innerHTML = row+"</table>";         
        }
        
    })
        .catch(error=>alert("errors"));
    }

    make_order_btn.onclick=function(){   
        items_data={
         location:document.getElementById("llocation").value,
         payment_mode:document.getElementById("lpayment").value,        
         order_items:document.getElementById("lselected").value
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
     
     lunchcancel_btn.onclick = function() {
        lunchmodal.style.display = "none";
    }