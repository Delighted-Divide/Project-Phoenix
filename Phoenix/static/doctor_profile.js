// let profile = JSON.parse(document.getElementById("profile-data").textContent);
// console.log(profile);

function toggleInfo(element, value) {
  if (element.getAttribute("data-toggled") !== "true") {
    element.textContent = value;
    element.style.color = "white";
    element.style.backgroundColor = "var(--third-color)";
    element.setAttribute("data-toggled", "true");
  } else {
    element.textContent = element.getAttribute("data-default");
    element.removeAttribute("data-toggled");
    element.style.color = "var(--secondary-color)";
    element.style.backgroundColor = "rgb(25, 31, 40)";
  }
}

// Initialize default values for each box
document.querySelectorAll(".info-box").forEach(function (box) {
  box.setAttribute("data-default", box.textContent);
});
