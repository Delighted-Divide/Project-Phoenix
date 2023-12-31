function setProgress(percent) {
  const circles = document.querySelectorAll(".progress-ring__circle");
  circles.forEach((circle) => {
    const circumference = 2 * Math.PI * circle.getAttribute("r");
    const offset = circumference - (percent / 100) * circumference;

    circle.style.strokeDasharray = `${circumference} ${circumference}`;
    circle.style.strokeDashoffset = offset;
  });
}

// Call this function with the desired percentage
setProgress(50); // for 50% progress
