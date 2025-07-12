// Code to make the menu slide in and out
const menuStackButton = document.getElementById('menuStackButton');
const popOutMenu = document.getElementById("popoutMenu");
function menuSlideOn(){
    popOutMenu.classList.replace('menuClosed', 'menuOpen');
}
const menuCloseButton = document.getElementById('closeMenu');
function menuSlideOff(){
    popOutMenu.classList.replace('menuOpen', 'menuClosed');
}

// Adding event listeners on document load
document.addEventListener("DOMContentLoaded", function(){
    menuStackButton.addEventListener("click", function(){
        menuSlideOn();
    });
    menuCloseButton.addEventListener("click", function(){
        menuSlideOff();
    });
});
