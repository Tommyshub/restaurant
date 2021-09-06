// Toggles the div for blog admin

function toggleBlogAdmin() {
  var x = document.getElementById("blogAdmin");
  if (x.style.display === "none") {
    x.style.display = "block";
  } else {
    x.style.display = "none";
  }
}
