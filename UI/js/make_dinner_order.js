var dinnercancel_btn=document.getElementById("dinnercancel");
var dinner_btn=document.getElementById("dinner_btn_id");
var dinnermodal= document.getElementById('dinnermodal');
var make_order_btn=document.getElementById("submit_dinner")

dinner_btn.onclick =function() {
    dinnermodal.style.display = "block";
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
            if(data[i].category=="dinner"){
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
            document.getElementById("dtable").innerHTML = row+"</table>";         
        }
        
    })
        .catch(error=>alert("errors"));
    }

    make_order_btn.onclick=function(){   
        items_data={
         location:document.getElementById("dlocation").value,
         payment_mode:document.getElementById("dpayment").value,        
         order_items:document.getElementById("dselected").value
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
     
     dinnercancel_btn.onclick = function() {
        dinnermodal.style.display = "none";
    }