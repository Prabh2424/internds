// Show loader when page starts loading
document.addEventListener("DOMContentLoaded", function() {
  document.querySelector('.banter-loader').style.display = 'flex';
  document.querySelector('.container-fluid').classList.add('d-none');
});

// Hide loader and show main content when page finishes loading
// Hide loader and show main content when page finishes loading
window.onload = function() {
  document.querySelector('.banter-loader').style.display = 'none';
  document.querySelector('.container-fluid').classList.remove('d-none');
};
