//Getting the name and email from the DOM
let subject = document.getElementById("subject").value;
let name = document.getElementById("name").value;
let email = document.getElementById("email").value;
let message = document.getElementById("message").value;
//Getting the button from the DOM
let submitButton = document.getElementById("submit");

submitButton.addEventListener("click", function (event) {
  //prevent the reload of the page.
  event.preventDefault();
  //Sending the email with the name and email
  emailjs
    .send("gmail", "greenhouse", {
      subject: subject,
      from_name: name,
      from_email: email,
      message: message,
    })
    .then(
      function (response) {
        console.log("SUCCESS", response);
      },
      function (error) {
        console.log("FAILED", error);
      }
    );
});
