document.querySelectorAll('.lab-box').forEach(box => {
    box.addEventListener('click', function() {
        window.location.href =  '/laboratory/' + this.id;
    });
});