function showForgotPasswordPatient() {
    document.querySelector("form").style.display = "none";

    
    var container = document.createElement("div");
    container.id = "forgot-password-form";
    container.style.background = "#ffffff";
    container.style.padding = "30px 40px";
    container.style.borderRadius = "12px";
    container.style.boxShadow = "0 6px 15px rgba(0, 0, 0, 0.1)";
    container.style.width = "100%";
    container.style.maxWidth = "400px";
    container.innerHTML = `
        <h2>Reset Password</h2>
        <input type="email" id="email" placeholder="Enter Your Registered Email" required><br>
        <button onclick="sendOTPPatient()">Send OTP</button><br><br>
        <input type="text" id="otp" placeholder="Enter OTP"><br>
        <input type="password" id="new_password" placeholder="New Password"><br>
        <input type="password" id="confirm_password" placeholder="Confirm Password"><br>
        <button onclick="resetPasswordPatient()">Reset Password</button>
    `;
    document.body.appendChild(container);
}
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
function sendOTPPatient() {
    var email = document.getElementById("email").value;

    fetch("send_otp_patient/", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": getCookie('csrftoken'),
        },
        body: JSON.stringify({ email: email })
    })
    .then(res => res.json())
    .then(data => {
        if (data.success) {
            alert("OTP sent to your email.");
        } else {
            alert("Error: " + data.error);
        }
    })
}
function resetPasswordPatient() {
    var email = document.getElementById("email").value;
    var otp = document.getElementById("otp").value;
    var newPassword = document.getElementById("new_password").value;
    var confirmPassword = document.getElementById("confirm_password").value;

    const formData = new FormData();
    formData.append("email", email);
    formData.append("otp", otp);
    formData.append("new_password", newPassword);
    formData.append("confirm_password", confirmPassword);

    fetch("reset_password_patient", {
        method: "POST",
        body: formData
    })
    .then(res => res.text())
    .then(data => alert(data))
    .catch(err => console.error(err));
}