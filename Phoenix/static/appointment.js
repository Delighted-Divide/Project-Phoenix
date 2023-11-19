let appointments = JSON.parse(document.getElementById("profile-data").textContent);
console.log(appointments);


for (const [key, value] of Object.entries(appointments)) {
    const appointmentDiv = document.getElementById(key);
    if (appointmentDiv) {
        appointmentDiv.textContent = value;
    }
    appointmentDiv.style.backgroundColor = "var(--third-color)"
    appointmentDiv.style.border = "2px solid var(--primary-color)"

    appointmentDiv.classList.add('appointed');


    appointmentDiv.addEventListener('mouseenter', function() {
        this.style.backgroundColor = "var(--fifth-color)"; // Change to the desired hover background color
        this.style.color = "white"; // Change text color on hover
    });

    // Adding mouseleave event listener
    appointmentDiv.addEventListener('mouseleave', function() {
        this.style.backgroundColor = "var(--third-color)"; // Revert to original background color
        this.style.color = "white"; // Revert text color to initial
    });

}