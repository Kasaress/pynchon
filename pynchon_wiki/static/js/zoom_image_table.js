window.addEventListener('DOMContentLoaded', function() {
    var container = document.getElementById('image-container');
    var image = document.getElementById('image');

    var isDragging = false;
    var startX, startY;
    var translateX = 0, translateY = 0;
    var scale = 1.0;
    var isZoomed = false;
    var translationSpeed = 5;

    container.addEventListener('mousedown', function(event) {
        if (event.button === 0) {
            if (isZoomed) {
                isDragging = true;
                startX = event.clientX;
                startY = event.clientY;
                event.preventDefault();
            }
        }
    });

    container.addEventListener('mousemove', function(event) {
        if (isDragging) {
            var dx = event.clientX - startX;
            var dy = event.clientY - startY;

            translateX += dx / scale * translationSpeed;
            translateY += dy / scale * translationSpeed;

            updateTransform();
            startX = event.clientX;
            startY = event.clientY;
            event.preventDefault();
        }
    });

    container.addEventListener('mouseup', function(event) {
        if (event.button === 0) {
            if (isZoomed) {
                isDragging = false;
                event.preventDefault();
            }
        }
    });

    container.addEventListener('mouseleave', function(event) {
        if (isDragging) {
            isDragging = false;
            event.preventDefault();
        }
    });

    container.addEventListener('wheel', function(event) {
        var newScale = scale - event.deltaY * 0.01; // Инвертированное значение event.deltaY

        if (newScale > 1.0) {
            isZoomed = true;
        } else {
            isZoomed = false;
            translateX = 0;
            translateY = 0;
        }

        var containerWidth = container.offsetWidth;
        var containerHeight = container.offsetHeight;
        var imageWidth = image.offsetWidth;
        var imageHeight = image.offsetHeight;

        var minScale = Math.max(containerWidth / imageWidth, containerHeight / imageHeight);
        scale = Math.max(minScale, newScale);

        updateTransform();
        event.preventDefault();
    });

    function updateTransform() {
        image.style.transform = 'translate(' + translateX + 'px, ' + translateY + 'px) scale(' + scale + ')';
    }
});