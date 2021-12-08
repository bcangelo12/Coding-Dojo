console.log("page loaded...");

let first = document.getElementById("first-request")
let second = document.getElementById("second-request")
let edit = document.getElementById("edit-name")

function changeRequest(element) {
    element.remove();
}

function changeName() {
    console.log("button pressed");
    edit.innerText = "Brendan Angelo";
}


// solution from learn platform, handles changing numbers too

// var requestSpan = document.querySelector("#requests");
// var connectionSpan = document.querySelector("#connections");
// var username = document.querySelector("#username");

// function accept(id) {
//     var element = document.querySelector(id);
//     element.remove();
//     requestSpan.innerText--;
//     connectionSpan.innerText++;
// }

// function ignore(id) {
//     var element = document.querySelector(id);
//     element.remove();
//     requestSpan.innerText--;
// }

// function edit() {
//     username.innerText = "Marisa G";
// }