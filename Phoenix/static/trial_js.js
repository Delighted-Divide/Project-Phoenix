// Initial start ups of the app
// Nav start up
let navOpen = true;

// Menu start up
let menu = document.getElementById("start").firstElementChild;
menu.firstElementChild.classList.toggle("icon-active");
menu.classList.add("li-active");

window.addEventListener('load', function() {
  var loadingScreen = document.getElementById('loading-screen');
  if (loadingScreen) {
      // Fade out the loading screen
      loadingScreen.style.opacity = '0';
      loadingScreen.style.transition = 'opacity 5s ease';

      // Remove the loading screen after the transition
      setTimeout(function() {
          loadingScreen.parentNode.removeChild(loadingScreen);
      }, 500); // This should match the duration of the opacity transition
  }
});

// _________________________________________________________________________________________________________________________________________
// _________________________________________________________________________________________________________________________________________
// _________________________________________________________________________________________________________________________________________
// _________________________________________________________________________________________________________________________________________
// _________________________________________________________________________________________________________________________________________
// _________________________________________________________________________________________________________________________________________
// _________________________________________________________________________________________________________________________________________


function getTone(color, factor) {
  let colorValues = color.match(/\d+/g).map(Number); // Extract RGB values
  let isRGBA = colorValues.length === 4; // Check if it's RGBA
  let alpha = isRGBA ? colorValues.pop() : 1; // Get alpha value

  let tonedValues = colorValues.map(value => {
      let newValue = value * factor;
      return Math.min(255, Math.max(0, Math.round(newValue))); // Clamp between 0 and 255
  });

  return `rgba(${tonedValues.join(", ")}, ${alpha})`;
}

function setTones(baseColor,label) {
  for (let i = 1; i <= 10; i++) {
      // Lighter tones
      let lighterTone = getTone(baseColor, 1 + (0.1 * i)); // Incrementally lighter
      document.documentElement.style.setProperty(`--${label}-light-color-${i}`, lighterTone);
      console.log(`${label} Lighter Level ${i}:`, lighterTone);

      // Darker tones
      let darkerTone = getTone(baseColor, 1 - (0.1 * i)); // Incrementally darker
      document.documentElement.style.setProperty(`--${label}-dark-color-${i}`, darkerTone);
      console.log(`${label} Darker Level ${i}:`, darkerTone);
  }
}

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




// Function to get CSRF token from cookies
function getCSRFToken() {
  let cookies = document.cookie.split(';');
  for (let i = 0; i < cookies.length; i++) {
    let cookie = cookies[i].trim();
    if (cookie.startsWith('csrftoken=')) {
      return cookie.substring('csrftoken='.length, cookie.length);
    }
  }
  return null;
}
// _________________________________________________________________________________________________________________________________________
// _________________________________________________________________________________________________________________________________________
// _________________________________________________________________________________________________________________________________________
// _________________________________________________________________________________________________________________________________________
// _________________________________________________________________________________________________________________________________________
// _________________________________________________________________________________________________________________________________________

var color_lists = document.querySelectorAll("#colors li");
color_lists.forEach(function (list,index) {
  list.addEventListener("click", function () {
    color_lists.forEach(function (inactiveList) {
      inactiveList.classList.remove("li-active");
    });
    let selectedColor = this.firstElementChild.style.backgroundColor;
    document.documentElement.style.setProperty(
      "--third-color",
      this.firstElementChild.style.backgroundColor
    );
    setTones(selectedColor,"third");
    this.classList.add("li-active");

    fetch('/update-color-index/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': getCSRFToken() // Function to get CSRF token
      },
      body: JSON.stringify({ color_index: index }) // index of clicked color
    })
    .then(response => response.json())
    .then(data => console.log('Color index updated:', data))
    .catch(error => console.error('Error:', error));
  });
});

var color_lists2 = document.querySelectorAll("#colors2 li");
color_lists2.forEach(function (list,index) {
  list.addEventListener("click", function () {
    color_lists2.forEach(function (inactiveList) {
      inactiveList.classList.remove("li-active");
    });
    let selectedColor = this.firstElementChild.style.backgroundColor;
    document.documentElement.style.setProperty(
      "--fifth-color",
      this.firstElementChild.style.backgroundColor
    );
    setTones(selectedColor,"fifth");
    this.classList.add("li-active");

    fetch('/update-color2-index/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': getCSRFToken() // Function to get CSRF token
      },
      body: JSON.stringify({ color_index: index }) // index of clicked color
    })
    .then(response => response.json())
    .then(data => console.log('Color2 index updated:', data))
    .catch(error => console.error('Error:', error));
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
  doctor_page_content_wrapper = document.querySelector(".content-wrapper");
  if (doctor_page_content_wrapper) {
    // console.log(document.querySelector(".content-wrapper"));
    doctor_page_content_wrapper.style.width = "100%";
  }
  doctor_profile_content_wrapper = document.querySelector(".content");
  if (doctor_profile_content_wrapper) {
    // console.log(document.querySelector(".content-wrapper"));
    doctor_profile_content_wrapper.style.width = "100%";
  }
  patient_page_content_wrapper = document.querySelector(".cont");
  if (patient_page_content_wrapper) {
    // console.log(document.querySelector(".content-wrapper"));
    patient_page_content_wrapper.style.width = "100%";
  }
}

function navBarIn(nav, con) {
  nav.style.left = "0px";
  con.style.left = "250px";
  con.style.width = "calc(100% - 250px)";
  doctor_page_content_wrapper = document.querySelector(".content-wrapper");
  if (doctor_page_content_wrapper) {
    // console.log(document.querySelector(".content-wrapper"));
    doctor_page_content_wrapper.style.width = "90%";
  }
  doctor_profile_content_wrapper = document.querySelector(".content");
  if (doctor_profile_content_wrapper) {
    // console.log(document.querySelector(".content-wrapper"));
    doctor_profile_content_wrapper.style.width = "90%";
  }
  patient_page_content_wrapper = document.querySelector(".cont");
  if (patient_page_content_wrapper) {
    // console.log(document.querySelector(".content-wrapper"));
    patient_page_content_wrapper.style.width = "86%";
  }
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

  if (navOpen) {
    this.className = "fas fa-arrow-right";
    navBarOut(navBar, mainContent);
  } else {
    this.className = "fas fa-arrow-left";
    navBarIn(navBar, mainContent);
  }
  navOpen = !navOpen;
});
