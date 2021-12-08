function switchLogout(element) {
    if(element.innerText == "Login") {
        element.innerText = "Logout";
    } else {
        element.innerText = "Login";
    }
}

// added if statement after turning in

function hide(element) {
    element.remove();
}