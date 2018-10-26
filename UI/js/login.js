document.getElementById("login_id").addEventListener("click",on_click_login);
function on_click_login() {
    let data={
    username:document.getElementById('usrnm').value,
    password:document.getElementById('pwd').value,
    };
    url='https://real-fast-food-fast.herokuapp.com/api/v2/auth/login';
    fetch(url,{
        method: 'POST',
        body: JSON.stringify(data),
        headers:{
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        }
    }).then(res=>res.json())
    .then(response=>{
        if(response.error=="user is not known"){
            alert("Please enter the right username or password");
        }
        else{
            alert("succussfully logged in !"+response.id);
            localStorage.setItem("access_token",response.access_token);
            window.location.href="./UI/customer.html"; 
        }
            
    })
    .catch(error=>alert("something went wrong"));
}
