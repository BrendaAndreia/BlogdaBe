$(document).ready(function() {
    // Add a class to social media icons on hover
    $('.social-media-icon').hover(function() {
      $(this).addClass('fa-spin');
    }, function() {
      $(this).removeClass('fa-spin');
    });
  });
