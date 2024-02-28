function validatelogin(){
    
    email=document.getElementById('email').value
    pswd1=document.getElementById('pswrd').value
    if (email=="" || pswd1==""){
        document.getElementById('message').innerHTML='please enter you email ID & password'
        return false
    }else{
        return true
    }
}
