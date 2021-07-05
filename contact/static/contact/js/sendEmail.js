function sendMail(contactForm) {
  emailjs
    .send("gmail", "greenhouse", {
      from_name: contactForm.name.value,
      from_email: contactForm.emailaddress.value,
      message: contactForm.message.value,
    })
    .then(
      function (response) {
        console.log("SUCCESS", response);
      },
      function (error) {
        console.log("FAILED", error);
      }
    );
  return false; // Block from loading a new page
}
