const sideMenu = document.querySelector('aside');
const menuBtn = document.getElementById('menu-btn');
const closeBtn = document.getElementById('close-btn');

const darkMode = document.querySelector('.dark-mode');

menuBtn.addEventListener('click', () => {
    sideMenu.style.display = 'block';
});

closeBtn.addEventListener('click', () => {
    sideMenu.style.display = 'none';
});

darkMode.addEventListener('click', () => {
    document.body.classList.toggle('dark-mode-variables');
    darkMode.querySelector('span:nth-child(1)').classList.toggle('active');
    darkMode.querySelector('span:nth-child(2)').classList.toggle('active');
})
function login_page() {
    document.getElementById("popup").className = "popup-active";
};
function closePopup() {
    document.getElementById("popup").className = "popup-deactive";
}
function changeToRegisterPopup() {
    document.getElementById("login-title").innerText = "Register";
    document.getElementById('login-to-register-text').textContent = "You have an account?";
    document.getElementById("login-to-register-button").onclick = changeToLoginPopup;
    document.getElementById("login-input-submit").onclick = sendRegister;
    document.getElementById("login-to-register-div").className = "login-to-register-active";
};
function changeToLoginPopup() {
    document.getElementById("login-title").innerText = "Login";
    document.getElementById('login-to-register-text').textContent = "You don`t have an account?";
    document.getElementById("login-to-register-button").onclick = changeToRegisterPopup;
    document.getElementById("login-input-submit").onclick = sendLogin;
    document.getElementById("login-to-register-div").className = "login-to-register-deactive";
}
function sendLogin() {
    sendAjax(1, document.getElementById("login").value, document.getElementById("password").value);
};
function sendRegister() {
    sendAjax(2, document.getElementById("login").value,
    document.getElementById("password").value,
    document.getElementById("checkbox1").checked,
    document.getElementById("checkbox2").checked,
    document.getElementById("checkbox3").checked,
    document.getElementById("checkbox4").checked,
    document.getElementById("checkbox5").checked);
}
function sendAjax(loginStatus, login, password, interest1="None", interest2="None", interest3="None", interest4="None", interest5="None") {
    let xhttp = new XMLHttpRequest();
    xhttp.open("POST", "login");
    xhttp.setRequestHeader("Content-Type","application/x-www-form-urlencoded");
    xhttp.responseType = "json";
    xhttp.onreadystatechange = function() {
        if (xhttp.readyState == 4 && xhttp.status == 200) {
            let response = xhttp.response;
            alert(response);
        }
    };
    if (loginStatus == 1) {xhttp.send("action=login&"+"username="+login+"&"+"password="+password);}
    else if (loginStatus == 2) {xhttp.send("action=register&"+"username="+login+"&"+"password="+password+"&"+"interest1="+interest1+"&"+"interest2="+interest2+"&"+"interest3="+interest3+"&"+"interest4="+interest4+"&"+"interest5="+interest5);}
}
function open_article(id) {
    let xhttp = new XMLHttpRequest();
    xhttp.open("POST", "articles");
    xhttp.setRequestHeader("Content-Type","application/x-www-form-urlencoded");
    xhttp.responseType = "json";
    xhttp.onreadystatechange = function() {
        if (xhttp.readyState == 4 && xhttp.status == 200) {
            let response = xhttp.response;
            let content = document.getElementById("content");

            let popup = document.createElement("div");
            popup.className = "popup";
            popup.id = "popup";
            content.appendChild(popup);

            let articleContent = document.createElement("div");
            articleContent.className = "article-content";
            popup.appendChild(articleContent);

            let articleCloseButton = document.createElement('button');
            articleCloseButton.className = "closeDiv";
            articleCloseButton.id = "closeDiv";
            articleContent.appendChild(articleCloseButton);

            let articleClose = document.createElement("span");
            articleClose.className = "material-icons-sharp";
            articleClose.textContent = "close";
            articleCloseButton.appendChild(articleClose);

            let articleTitle = document.createElement("h1");
            articleTitle.className = "article-title";
            articleTitle.innerText = response["data"]["title"];
            articleContent.appendChild(articleTitle);

            let articleText = document.createElement("span");
            articleText.className = "article-text";
            articleText.innerText = response["data"]["text"];
            articleContent.appendChild(articleText);

            let button = document.getElementById("closeDiv");
            button.onclick = function(){
                document.getElementById("popup").remove();
            };
        }
    };
    xhttp.send("id="+id);
};