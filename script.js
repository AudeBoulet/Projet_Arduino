function declencherAlerte(type) {
  var encadreElement = document.getElementById(type).closest('.encadre');
  var messageElement = document.getElementById(type + '-message');
  var resolutionButton = document.getElementById(type + '-resolu-btn'); // Get the resolution button for the type

  encadreElement.className = 'encadre rouge';
  resolutionButton.style.display = 'block'; // Show the button when an alert is triggered

  var date = new Date();
  var heure = date.getHours().toString().padStart(2, '0') + ":" +
              date.getMinutes().toString().padStart(2, '0') + ":" +
              date.getSeconds().toString().padStart(2, '0');
  messageElement.textContent = "Attention " + type + " détecté à " + heure + ".";
}

function resoudreProbleme(type) {
  var encadreElement = document.getElementById(type).closest('.encadre');
  var messageElement = document.getElementById(type + '-message');
  var resolutionButton = document.getElementById(type + '-resolu-btn'); // Get the resolution button for the type

  encadreElement.className = 'encadre vert';
  resolutionButton.style.display = 'none'; // Hide the button once the problem is resolved

  messageElement.textContent = "Aucun " + type + " n'a été détecté.";
}

// Ensure the "Problème résolu" buttons are hidden on initial load
window.onload = function() {
  var resolutionButtons = document.querySelectorAll('button[id$="-resolu-btn"]');
  resolutionButtons.forEach(function(button) {
    button.style.display = 'none';
  });
};  

// Simulation code (if needed, it can be removed or commented out)
setTimeout(function() { declencherAlerte('bruit'); }, 5000);
setTimeout(function() { declencherAlerte('mouvement'); }, 8000);
setTimeout(function() { declencherAlerte('incendie'); }, 12000);
