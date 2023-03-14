 function showPopup(url) {
      var popup = document.createElement("div");
      popup.id = "popup";

      var img = document.createElement("img");
      img.src = url;

      var close = document.createElement("button");
      close.id = "popup-close";
      close.innerHTML = "x";
      close.onclick = function() {
        popup.remove();
      };

      popup.appendChild(img);
      popup.appendChild(close);

      document.body.appendChild(popup);
    }
