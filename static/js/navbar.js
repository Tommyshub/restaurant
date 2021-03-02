function navSlide() {
  const burger = document.querySelector(".burger-menu");
  const nav = document.querySelector(".nav-ul");
  const navLinks = document.querySelectorAll(".nav-links");

  burger.addEventListener("click", () => {
    // toggle the sidenav
    nav.classList.toggle("nav-active");

    // animation for the links
    navLinks.forEach((link, index) => {
      if (link.style.animation) {
        link.style.animation = "";
      } else {
        link.style.animation = `navLinkFade 0.5s ease forwards ${
          index / 7 + 0.5
        }s`;
      }
    });
    // burger icon toggle
    burger.classList.toggle("toggle");
  });
}

navSlide();
