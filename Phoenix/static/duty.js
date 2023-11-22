document.addEventListener("DOMContentLoaded", function() {
    const leftArrow = document.querySelector('.left-arrow');
    const rightArrow = document.querySelector('.right-arrow');

    leftArrow.addEventListener('click', function() {
        rotateBoxes('right');
    });

    rightArrow.addEventListener('click', function() {
        rotateBoxes('left');
    });

    function rotateBoxes(direction) {
        let boxes = document.querySelectorAll('.container > .box');

        if (direction === 'left') {
            moveLeft(boxes);
        } else {
            moveRight(boxes);
        }
    }

    function moveLeft(boxes) {
        const container = document.querySelector('.container');
        container.insertBefore(boxes[2], boxes[0]);
        updateStyles(boxes);
    }

    function moveRight(boxes) {
        const container = document.querySelector('.container');
        container.appendChild(boxes[0]);
        updateStyles(boxes);
    }

    function updateStyles(boxes) {
        // Removing special design from all boxes first
        boxes.forEach(box => box.classList.remove('special-design'));

        // Re-querying the boxes as their order has changed
        let updatedBoxes = document.querySelectorAll('.container > .box');
        // Adding special design to the new middle box
        updatedBoxes[1].classList.add('special-design');
    }
});
