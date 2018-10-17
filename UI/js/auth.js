document.getElementById("signup").addEventListener("click",onclick);
function onclick(){
    var data={email:document.getElementById('mail').value,
    username:document.getElementById('usrn').value,
    password:document.getElementById('pwd').value,
    phone_number:document.getElementById('phno').value
    }
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



function on_click_login() {
    var passwd = document.getElementById('pwd');
    var usern  = document.getElementById('usrn');
    var email_d = document.getElementById('mail');
    var phone = document.getElementById('phno');

     if (!usern.checkValidity()|| !passwd.checkValidity()|| !phone.checkValidity()){
         alert("username or password is empty");
         return false;
         }
    else if(!phone.checkValidity()){
            alert("phone number is empty or invalid");
            return false;
         }
    else if(!email_d.checkValidity()){
            alert("email is empty or invalid");
            return false;
    }
     else{
         window.location.href = "customer.html";                        
     }
     document.getElementById('display').innerHTML = value;
 }