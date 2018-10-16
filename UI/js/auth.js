document.getElementById("signup").addEventListener("click",onclick);
function onclick(){
    var data={email:document.getElementsByName("email").value,
    username:document.getElementsByName("username").value,
    passord:document.getElementsByName("passsword").value
    }
    // const url ='http://127.0.0.1:5000/api/v2/auth/signup';
    fetch('http://127.0.0.1:5000/api/v2/auth/signup',{
    method: 'POST',
    body: JSON.stringify(data),
    headers:{
        'Content-Type': 'application/json'
        }
    }).then(res=>res.json())
    .then(response=>console.log('succussfully registered! ',JSON.stringify(response)))
  
}