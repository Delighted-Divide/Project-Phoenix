// document.addEventListener("DOMContentLoaded", function () {
//   const hiddenSelect = document.getElementById("id_doctor-degrees");
//   const visibleSelect = document.getElementById("degree-select");
//   const tagsContainer = document.getElementById("degree-tags-container");

//   visibleSelect.addEventListener("change", function () {
//     const value = visibleSelect.value;
//     const text = visibleSelect.options[visibleSelect.selectedIndex].text;

//     if (value) {
//       // Create a new tag
//       const tag = document.createElement("span");
//       tag.textContent = text;
//       const closeButton = document.createElement("button");
//       closeButton.textContent = "×";
//       closeButton.addEventListener("click", function () {
//         tag.remove();
//         hiddenSelect.querySelector(`option[value="${value}"]`).selected = false;
//         visibleSelect.appendChild(new Option(text, value)); // Re-add the option to the visible select
//       });
//       tag.appendChild(closeButton);
//       tagsContainer.appendChild(tag);

//       // Update the hidden select
//       hiddenSelect.querySelector(`option[value="${value}"]`).selected = true;
//       visibleSelect.removeChild(
//         visibleSelect.options[visibleSelect.selectedIndex]
//       );
//     }
//   });
// });

document.addEventListener("DOMContentLoaded", function () {
  var tags = document.querySelectorAll(".degree-tag");
  tags.forEach(function (tag) {
    tag.addEventListener("click", function () {
      var value = this.getAttribute("data-value");
      var option = document.querySelector(
        '#id_doctor-degrees option[value="' + value + '"]'
      );
      if (option) {
        if (option.selected) {
          option.selected = false;
          this.classList.remove("selected");
        } else {
          option.selected = true;
          this.classList.add("selected");
        }
      }
    });
  });
  var tags = document.querySelectorAll(".subspeciality-tag");
  tags.forEach(function (tag) {
    tag.addEventListener("click", function () {
      var value = this.getAttribute("data-value");
      var option = document.querySelector(
        '#id_doctor-subspecialities option[value="' + value + '"]'
      );
      if (option) {
        if (option.selected) {
          option.selected = false;
          this.classList.remove("selected");
        } else {
          option.selected = true;
          this.classList.add("selected");
        }
      }
    });
  });
});

// document.addEventListener("DOMContentLoaded", function () {
//   var tags = document.querySelectorAll(".subspeciality-tag");
//   tags.forEach(function (tag) {
//     tag.addEventListener("click", function () {
//       var value = this.getAttribute("data-value");
//       var option = document.querySelector(
//         '#id_doctor-subspecialities option[value="' + value + '"]'
//       );
//       if (option) {
//         if (option.selected) {
//           option.selected = false;
//           this.classList.remove("selected");
//         } else {
//           option.selected = true;
//           this.classList.add("selected");
//         }
//       }
//     });
//   });
// });

function showStep(step) {
  // Hide all steps
  document.querySelectorAll(".form-step").forEach(function (el) {
    el.style.display = "none";
  });
  console.log(document.querySelectorAll(".form-step"));

  // Show the current step
  document.getElementById("step-" + step).style.display = "block";
}
