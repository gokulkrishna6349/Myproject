function validateregister(){
    
    email=document.getElementById('email').value
    pswd1=document.getElementById('pswd1').value
    pswd2=document.getElementById('pswd2').value
    if (email=="" || pswd1==""){
        document.getElementById('msg').innerHTML='please fill both'
        return false
    }else if(pswd1!=pswd2){
        document.getElementById('msg').innerHTML='both password must be same'
        return false
    }else{
        return true
    }

}