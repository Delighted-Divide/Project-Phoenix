// script.js
document.addEventListener('DOMContentLoaded', function() {
    var urlParams = new URLSearchParams(window.location.search);
    var activeTab = urlParams.get('tab');

    if (activeTab) {
        showTab(activeTab, document.getElementById(activeTab + '-tab'));
    } else {
        // Default to showing the first tab if no tab parameter is set
        showTab('planned', document.getElementById('planned-tab'));
    }
});



function showTab(tabName,element) {
    var i, tabcontent, tabbuttons;
    tabcontent = document.getElementsByClassName("tab-content");
    for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
    }
    tabbuttons = document.getElementsByClassName("tab-button");
    for (i = 0; i < tabbuttons.length; i++) {
        tabbuttons[i].style.borderBottom = "None";
    }
    document.getElementById(tabName).style.display = "block";
    console.log(element)
    element.style.borderBottom = "2px solid var(--fifth-color)"

    
}



