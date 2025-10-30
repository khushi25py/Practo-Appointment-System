function register_doc(){
    console.log("inside register")
    var URL = "/register-doctor";
    var formData = new FormData();
    var name = document.getElementById("name").value;
    var email = document.getElementById("email").value;
    var qualification = document.getElementById("qualification").value;
    var specialty = document.getElementById("specialty").value;
    var phone_no = document.getElementById("phone_no").value;
    var year_of_experience = document.getElementById("year_of_experience").value;
    var gen = document.getElementsByName("gender");
    var gender = "";
    for(let i=0;i<gen.length;i++){
        if(gen[i].checked){
            gender = gen[i].value;
        }
    }
    var fee=document.getElementById("fee").value;
    var time=document.getElementById("time").value;
    var password=document.getElementById("password").value;
    formData.append("name",name);
    formData.append("email",email);
    formData.append("qualification",qualification);
    formData.append("specialty",specialty);
    formData.append("phone_no",phone_no);
    formData.append("year_of_experience",year_of_experience);
    formData.append("gender",gender);
    formData.append("fee",fee);
    formData.append("time",time);
    formData.append("password",password);
    formData.append("csrfmiddlewaretoken",document.getElementsByName("csrfmiddlewaretoken")[0].value);
    

    fetch(URL, {
    method: "POST",
    body: formData
        })
    .then(res => {
        if (!res.ok) throw new Error("Network response was not ok " + res.statusText);
        return res.json();
        })
    .then(json => {
        console.log(json); 
        alert(json.message);
        if (json.redirect) {
            window.location.href = json.redirect;
        } 
        else {
            document.getElementById("doc_form").reset();
        }
        })
    .catch(err => {
        console.error("Fetch error:", err);
        });
}







function register_pat(){
    var URL= "/register-patient";
    console.log("Register function called");
    var formData= new FormData();
    var name = document.getElementById("name").value;
    var email = document.getElementById("email").value;
    var phone_number= document.getElementById("phone_number").value;
    var gen = document.getElementsByClassName("gender");
    var gender = "";
    for(let i=0;i<gen.length;i++){
        if(gen[i].checked){
            gender = gen[i].value;
        }
    }
    var age= document.getElementById("age").value;
    var password=document.getElementById("password").value;
    formData.append("name",name);
    formData.append("email",email);
    formData.append("phone_number",phone_number);
    formData.append("gender",gender);
    formData.append("age",age);
    formData.append("password",password);
    formData.append("csrfmiddlewaretoken",document.getElementsByName("csrfmiddlewaretoken")[0].value);
    fetch(URL,{
        method:"POST",
        body:formData
    }).then(function(res){
        return res.json()
    }).then(function(json){
        console.log(json);
        alert(json.message);
        document.getElementById("pat_form").reset();
    })

  console.log("script loaded");

}   
console.log("script loaded");


