console.log("page loaded...")

// my method listed below, not optimal but it worked

// let first = document.querySelector("#likesNumber-1");
// let num1 = first.innerText
// console.log(num1)

// let second = document.querySelector("#likesNumber-2");
// let num2 = second.innerText
// console.log(num2)

// let third = document.querySelector("#likesNumber-3");
// let num3 = third.innerText
// console.log(num3)

// function likeFirst() {
//     console.log('button pressed')
//     num1++
//     first.innerText = num1
// }

// function likeSecond() {
//     console.log('button pressed')
//     num2++
//     second.innerText = num2
// }

// function likeThird() {
//     console.log('button pressed')
//     num3++
//     third.innerText = num3
// }

// new code based off of solution, more complex but verstile
// must call index value in onclick action in HTML if doing this way

var likes = [9, 12, 9]
var spans = [
    document.querySelector('#likesNumber-1'),
    document.querySelector('#likesNumber-2'),
    document.querySelector('#likesNumber-3')
];

function addLike(id) {
    likes[id]++;
    spans[id].innerHTML = likes[id];
}