$(function() {
  $('#send').bind('click', function() {
    $.getJSON('/_add_numbers', {
      a: $('#input').val(),
    }, function(data) {
      $("#result").text(data.result);
    });
    return false;
  });
});