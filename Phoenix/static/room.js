document.addEventListener('DOMContentLoaded', function() {

    var form = document.getElementById('searchForm');
    var roomTypeSelect = document.getElementById('roomType');
    var searchBox = document.getElementById('searchBox');

    roomTypeSelect.addEventListener('change', function() {
        form.submit();
    });

    searchBox.addEventListener('keypress', function(event) {
        // Check if the key pressed is the Enter key
        if (event.key === 'Enter') {
            event.preventDefault(); // Prevent the default action to stop submitting the form directly
            form.submit();
        }
    });
});