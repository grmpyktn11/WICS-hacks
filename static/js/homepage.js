window.addEventListener("scroll", function() {
    let header = document.querySelector(".sticky-header");
    let coverHeight = document.querySelector(".cover").offsetHeight;

    if (window.scrollY > coverHeight/2 ) {
        header.classList.add("visible");
    } else {
        header.classList.remove("visible");
    }
});