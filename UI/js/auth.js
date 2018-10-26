document.getElementById("signup").addEventListener("click",onclick_signup);
function onclick_signup(){
    var data={email:document.getElementById('mail').value,
    username:document.getElementById('usrn').value,
    password:document.getElementById('pwd').value,
    phone_number:document.getElementById('phno').value
    };
    fetch('https://real-fast-food-fast.herokuapp.com/api/v2/auth/signup',{
    method: 'POST',
    body: JSON.stringify(data),
    headers:{
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*'
        }
    }).then(res=>res.json())
    .then((response)=>{
        var msg=(response);
        if (msg.message=="succussfully registered"){
            alert("you have succussfully created an account");
            window.location.href="../login.html";
        }
        else{
            alert("wrong input format, please check your inputs and try again!");
        }
    })   
    .catch(error=>alert("errors"));
  
}
