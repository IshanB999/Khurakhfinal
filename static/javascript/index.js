function openDialog() {
    document.getElementById('dialogOverlay').classList.add('show');
}

function closeDialog() {
    document.getElementById('dialogOverlay').classList.remove('show');
}






function calculate_ticker(bmi=17){

const bmit = 37; // Example value for bmit

  let targetWidth = 0;

  // Determine the target width based on the bmit value
  if (bmit < 18.5) {
    targetWidth = (bmit / 18.5) * 25; // 0% to 25%
  } else if (bmit >= 18.5 && bmit < 25.0) {
    targetWidth = 25 + ((bmit - 18.5) / (24.9 - 18.5)) * 25; // 25% to 50%
  } else if (bmit >= 25.0 && bmit < 30.0) {
    targetWidth = 50 + ((bmit - 25.0) / (29.0 - 25.0)) * 25; // 50% to 75%
  } else if (bmit >= 30.0 && bmit < 40.0) {
    targetWidth = 75 + ((bmit - 30.0) / (40.0 - 30.0)) * 25; // 75% to 100%
  } else if (bmit >= 40.0) {
    targetWidth = 100; // 100%
  }


  console.log(targetWidth)
  document.getElementById('bmi-ticker').style.left = targetWidth + '%'

}

calculate_ticker()