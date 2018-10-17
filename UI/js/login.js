document.getElementById("login_id").addEventListener("click",on_click_login);
function on_click_login() {
    let data={
    username:document.getElementById('usrnm').value,
    password:document.getElementById('pwd').value,
    };
    url='http://127.0.0.1:5000/api/v2/auth/login';
    fetch(url,{
        method: 'POST',
        body: JSON.stringify(data),
        headers:{
            'Content-Type': 'application/json'
        }
    }).then(res=>res.json())
    .then(response=>{
        
        alert("succussfully logged in !");
        localStorage.setItem("access_token",response.access_token);
        window.location.href="./UI/customer.html"
    })
    .catch(error=>alert("something went wrong"));
}