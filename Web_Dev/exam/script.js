console.log('page loaded...')

let previewImg = document.querySelector('#big-preview');
let cartNum = document.querySelector('#cart-total');

function changeLeft(element) {
    console.log('changing to stonepunk')
    previewImg.src = "./images/stonepunk.png"
}

function changeRight(element) {
    console.log('changing to pixel ninjas');
    previewImg.src = "./images/pixel-ninjas-2.png";
}

function addCart(element) {
    console.log('adding to cart total');
    cartNum.innerHTML++;
}