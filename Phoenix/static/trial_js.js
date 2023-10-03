// Initial start ups of the app
// Nav start up
let navOpen = true;

// Menu start up
let menu = document.getElementById("start").firstElementChild;
menu.firstElementChild.classList.toggle("icon-active");
menu.classList.add("li-active");

//color setup
let page_color = document.querySelectorAll("#colors li")[1];
page_color.classList.add("li-active");

// _________________________________________________________________________________________________________________________________________
// _________________________________________________________________________________________________________________________________________
// _________________________________________________________________________________________________________________________________________
// _________________________________________________________________________________________________________________________________________
// _________________________________________________________________________________________________________________________________________
// _________________________________________________________________________________________________________________________________________
// _________________________________________________________________________________________________________________________________________

// Get all the lists in the start bar
var lists = document.querySelectorAll(".start li");

// Add a click event listener to each list
lists.forEach(function (list) {
  list.addEventListener("click", function () {
    // Toggle the 'list-active' class on the clicked list
    lists.forEach(function (inactiveList) {
      inactiveList.firstElementChild.classList.remove("icon-active");
      inactiveList.classList.remove("li-active");
      var chosen_bar = document.querySelector(
        `#${inactiveList.firstElementChild.innerHTML}`
      );
      chosen_bar.style.display = "none";
    });

    this.firstElementChild.classList.toggle("icon-active");
    this.classList.add("li-active");

    var chosen_bar = document.querySelector(
      `#${this.firstElementChild.innerHTML}`
    );
    chosen_bar.style.display = "flex";

    if (this.parentElement.lastElementChild == this) {
      this.style.borderRight = "none";
      //   setTimeout(() => {
      //     this.style.borderRight = "none";
      //   }, 500);
    } else if (this.parentElement.firstElementChild == this) {
      this.style.borderLeft = "none";
      //   setTimeout(() => {
      //     this.style.borderLeft = "none";
      //   }, 10);
    }
  });
});
// _________________________________________________________________________________________________________________________________________
// _________________________________________________________________________________________________________________________________________
// _________________________________________________________________________________________________________________________________________
// _________________________________________________________________________________________________________________________________________
// _________________________________________________________________________________________________________________________________________
// _________________________________________________________________________________________________________________________________________

var color_lists = document.querySelectorAll("#colors li");
color_lists.forEach(function (list) {
  list.addEventListener("click", function () {
    color_lists.forEach(function (inactiveList) {
      inactiveList.classList.remove("li-active");
    });
    document.documentElement.style.setProperty(
      "--third-color",
      this.firstElementChild.style.backgroundColor
    );
    this.classList.add("li-active");
  });
});

// _________________________________________________________________________________________________________________________________________
// _________________________________________________________________________________________________________________________________________
// _________________________________________________________________________________________________________________________________________
// _________________________________________________________________________________________________________________________________________
// _________________________________________________________________________________________________________________________________________
// _________________________________________________________________________________________________________________________________________
function navBarOut(nav, con) {
  nav.style.left = "-250px";
  con.style.left = "0";
  con.style.width = "100%";
}

function navBarIn(nav, con) {
  nav.style.left = "0px";
  con.style.left = "250px";
  con.style.width = "calc(100% - 250px)";
}

window.addEventListener("resize", function () {
  const navBar = document.getElementById("nav-bar");
  const mainContent = document.getElementById("main_content");

  // Calculate the percentage of the current window width relative to the screen's width
  const widthPercentage = (window.innerWidth / screen.width) * 100;

  // Set a threshold percentage, e.g., 70%. Adjust this value as needed.
  const thresholdPercentage = 60;

  if (widthPercentage <= thresholdPercentage && navOpen) {
    navBarOut(navBar, mainContent);
  } else if (navOpen) {
    navBarIn(navBar, mainContent);
  }
});
window.dispatchEvent(new Event("resize"));

// _________________________________________________________________________________________________________________________________________
// _________________________________________________________________________________________________________________________________________
// _________________________________________________________________________________________________________________________________________
// _________________________________________________________________________________________________________________________________________
// _________________________________________________________________________________________________________________________________________
// _________________________________________________________________________________________________________________________________________
var removeNav = document.querySelector("#page-title i");
removeNav.addEventListener("click", function () {
  const navBar = document.getElementById("nav-bar");
  const mainContent = document.getElementById("main_content");
  console.log(this);
  if (navOpen) {
    this.className = "fas fa-arrow-right";
    navBarOut(navBar, mainContent);
  } else {
    this.className = "fas fa-arrow-left";
    navBarIn(navBar, mainContent);
  }
  navOpen = !navOpen;
});
