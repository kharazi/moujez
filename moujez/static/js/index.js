$(function() {
  $('#send').bind('click', function() {
    $.getJSON('/_add_numbers', {
      a: $('#input').val(),
    }, function(data) {
      alert(data.result)
      article_html_content = '<ul>'
      for (var i=0, len=data.result.summarized.length; i<len; i++) {
        article_html_content += '<li>';
        article_html_content += data.result.summarized[i];
        article_html_content += '</li>'; 
      }
      article_html_content += '</ul>'
      $("#result").html(article_html_content);      
      $("#title").text(data.result.title);


      if (data.result.image){
        $("#image").attr("src", data.result.image);
      }

      // get tags
      if (data.result.tags){
        tags_html_content = "<h3>برچسب‌های خبر</h3><ul>"
        for (var i=0, len=data.result.tags.length; i<len; i++) {
        tags_html_content += '<li>';
        tags_html_content += data.result.tags[i];
        tags_html_content += '</li>';
      }
        tags_html_content += "</ul>"
      }
      $("#tags").html(tags_html_content);



    });
    return false;
  });
});