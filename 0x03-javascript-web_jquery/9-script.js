document.addEventListener('DOMContentLoaded', () => {
  $(document).ready(function () {
    // const url = 'https://fourtonfish.com/hellosalut/?lang=fr';
    // Above url redirects to the one that is not commented out below
    // When we try this one, we don't get a response, but we do with the redirected
    const url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';
    $.get(url, function (data) {
      $('#hello').text(data.hello);
    });
  });
});
