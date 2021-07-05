function sendMail(contactForm) {
  emailjs
    .send("gmail", "greenhouse", {
      from_name: contactForm.name.value,
      subject: contactForm.subject.value,
      from_email: contactForm.email.value,
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
}
