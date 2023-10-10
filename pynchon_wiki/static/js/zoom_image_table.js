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

  var zoomInButton = document.getElementById('zoom-in-button');
  zoomInButton.addEventListener('click', function(event) {
      var newScale = scale + 0.7;
      if (newScale <= 4.5) { 
          scale = newScale;
          isZoomed = true;
          updateTransform();
      }
  });

  var zoomOutButton = document.getElementById('zoom-out-button');
  zoomOutButton.addEventListener('click', function(event) {
      var newScale = scale - 0.7;
      if (newScale >= 0.7) { 
          scale = newScale;
          if (scale === 1.0) {
              isZoomed = false;
              translateX = 0;
              translateY = 0;
          } else {
              isZoomed = true;
          }
          updateTransform();
      }
  });

  function updateTransform() {
      var containerWidth = container.offsetWidth;
      var containerHeight = container.offsetHeight;
      var imageWidth = image.offsetWidth * scale;
      var imageHeight = image.offsetHeight * scale;

      var maxX = (imageWidth - containerWidth) / 2;
      var maxY = (imageHeight - containerHeight) / 2;

      translateX = Math.max(-maxX, Math.min(maxX, translateX));
      translateY = Math.max(-maxY, Math.min(maxY, translateY));

      image.style.transform = 'translate(' + translateX + 'px, ' + translateY + 'px) scale(' + scale + ')';
  }
});