document.addEventListener('DOMContentLoaded', () => {
  $(document).ready(function () {
    // const url = 'https://fourtonfish.com/hellosalut/?lang=fr';
    // Above url redirects to the one that is not commented out below
    const url = 'https://stefanbohacek.com/hellosalut/?lang=fr';
    $.get(url, function (data) {
      $('#hello').text(data.hello);
    });
  });
});
