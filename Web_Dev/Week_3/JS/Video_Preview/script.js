console.log("page loaded...");

function over(element) {
    document.getElementById("myVideo").muted = true;
    element.play();
}

function out(element) {
    element.pause();
    document.getElementById("myVideo").muted = false;
    //added after turning in and seeing solution, resets time to beginning on mouse out
    element.currentTime = 0;
}