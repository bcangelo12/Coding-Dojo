console.log("page loaded...")

let likes = document.querySelector("#likesNumber");
let num = likes.innerText
console.log(num)

function addLike() {
    console.log('button pressed')
    num++
    likes.innerText = num
}