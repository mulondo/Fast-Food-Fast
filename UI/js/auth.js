document.getElementById("signup").addEventListener("click",onclick_signup);
function onclick_signup(){
    var data={email:document.getElementById('mail').value,
    username:document.getElementById('usrn').value,
    password:document.getElementById('pwd').value,
    phone_number:document.getElementById('phno').value
    };
    // const url ='http://127.0.0.1:5000/api/v2/auth/signup';
    fetch('http://127.0.0.1:5000/api/v2/auth/signup',{
    method: 'POST',
    body: JSON.stringify(data),
    headers:{
        'Content-Type': 'application/json'
        }
    }).then(res=>res.json())
    .then((response)=>{
        var msg=(response);
        if (msg.message=="succussfully registered"){
            alert("you have succussfully created an account");
            window.location.href="customer.html";
        }
        else{
            alert("please try again");
        }
    })   
    .catch(error=>alert("errors"));
  
}
