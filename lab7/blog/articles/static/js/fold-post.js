var foldBtns = document.getElementsByClassName("fold-button");
for (var i = 0; i < foldBtns.length; i++) {
    foldBtns[i].addEventListener("click", function (e) {
        if (e.target.parentElement.parentElement.className == "one-post") {
            e.target.innerHTML = "развернуть";
            e.target.parentElement.parentElement.className = "one-post folded";
        }
        else {
            e.target.innerHTML = "свернуть";
            e.target.parentElement.parentElement.className = "one-post";
        }
    });
}

