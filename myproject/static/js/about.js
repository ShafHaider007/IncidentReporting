// Initialize Leaflet Map
function initMap() {
  // Replace these coordinates with the actual location coordinates of your housing society
  var myLatLng = [40.7128, -74.006];

  var map = L.map("map").setView(myLatLng, 14);

  L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
    attribution:
      '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
  }).addTo(map);

  L.marker(myLatLng).addTo(map).bindPopup("Your Housing Society").openPopup();
}

// Contact Form Submission
document.addEventListener("DOMContentLoaded", function () {
  var contactForm = document.getElementById("contactForm");

  if (contactForm) {
    contactForm.addEventListener("submit", function (e) {
      e.preventDefault();

      var formData = new FormData(contactForm);

      fetch(contactForm.getAttribute("action"), {
        method: contactForm.getAttribute("method"),
        body: formData,
      })
        .then(function (response) {
          return response.text();
        })
        .then(function (data) {
          document.getElementById("form-message-warning").style.display =
            "none";
          document.getElementById("form-message-success").innerHTML = data;
          document.getElementById("form-message-success").style.display =
            "block";
        })
        .catch(function (error) {
          document.getElementById("form-message-success").style.display =
            "none";
          document.getElementById("form-message-warning").innerHTML = error;
          document.getElementById("form-message-warning").style.display =
            "block";
        });
    });
  }
});
