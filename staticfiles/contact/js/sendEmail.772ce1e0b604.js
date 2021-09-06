function sendMail(contactForm) {
  emailjs
    .send("gmail", "greenhouse", {
      subject: contactForm.id_subject.value,
      from_name: contactForm.id_name.value,
      from_email: contactForm.id_email.value,
      message: contactForm.id_message.value,
    })
    .then(
      function (response) {
        // Clear form values
        id_subject.value = "";
        id_name.value = "";
        id_email.value = "";
        id_message.value = "";
        console.log("SUCCESS", response);
        // Create new div for content to be displayed in
        $(document).ready(function () {
          $(
            '<p id="messageParagraph" class="toast light-green black-text">Email successfully sent!</p>'
          ).appendTo("#messageContainer");
        });
        // Set a timeout of 4 seconds and the remove the newDiv
        setTimeout(function () {
          if ($(messageParagraph).length > 0) {
            $(messageParagraph).remove();
          }
        }, 4000);
      },
      function (error) {
        console.log("FAILED", error);
        // Create new div for content to be displayed in
        $(document).ready(function () {
          $(
            '<p id="messageParagraph" class="toast red darken-1 black-text">Email could not be sent!</p>'
          ).appendTo("#messageContainer");
        });
        // Set a timeout of 4 seconds and the remove the newDiv
        setTimeout(function () {
          if ($(newDiv).length > 0) {
            $(newDiv).remove();
          }
        }, 4000);
      }
    );
  return false;
}
