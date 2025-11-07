document.addEventListener('DOMContentLoaded', () => {
  const banner = document.getElementById('cookie-banner');
  if (!localStorage.getItem('swiftter_cookies')) {
    banner.style.display = 'flex';
  }
  document.getElementById('accept-cookies').onclick = () => {
    localStorage.setItem('swiftter_cookies', 'accepted');
    banner.style.display = 'none';
  };
  document.getElementById('decline-cookies').onclick = () => {
    localStorage.setItem('swiftter_cookies', 'declined');
    banner.style.display = 'none';
  };
  document.getElementById('cookie-options').onclick = () => {
    alert('Opties kunnen later worden uitgebreid.');
  };
});
