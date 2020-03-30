$(document).foundation()

function myFunction() {
  if (confirm("New information has been added.")) {
  }
}

(function() {
  $('form > input').keyup(function() {

      var empty = false;
      $('form > input').each(function() {
          if ($(this).val() == '') {
              empty = true;
          }
      });

      if (empty) {
          $('#information').attr('disabled', 'disabled'); // updated according to http://stackoverflow.com/questions/7637790/how-to-remove-disabled-attribute-with-jquery-ie
      } else {
          $('#information').removeAttr('disabled'); // updated according to http://stackoverflow.com/questions/7637790/how-to-remove-disabled-attribute-with-jquery-ie
      }
  });
})()

// function checkform() {
//   var f = document.forms["theform"].elements;
//   var cansubmit = true;

//   for (var i = 0; i < f.length; i++) {
//       if (f[i].value.length == 0)
//           cansubmit = false;
//   }

//   document.getElementById('information').disabled = !cansubmit;
// }
// window.onload = checkform;