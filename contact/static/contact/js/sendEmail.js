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
        const newDiv = document.createElement("div");
        newDiv.classList.add("toast");
        newDiv.classList.add("light-green");
        newDiv.classList.add("black-text");
        // Success message to attach on the new div
        const newContent = document.createTextNode("Email successfully sent!");
        // add the text node to the newly created div
        newDiv.appendChild(newContent);
        // Add the new element to the parent div
        const parentDiv = document.getElementById("parent-container");
        parentDiv.parentNode.insertBefore(newDiv, parentDiv);
        // Set a timeout of 4 seconds and the remove the newDiv
        setTimeout(function () {
          if ($(newDiv).length > 0) {
            $(newDiv).remove();
          }
        }, 4000);
      },
      function (error) {
        console.log("FAILED", error);
        // Create new div for content to be displayed in
        const newDiv = document.createElement("div");
        newDiv.classList.add("toast");
        newDiv.classList.add("red");
        newDiv.classList.add("darken-1");
        newDiv.classList.add("black-text");
        // Success message to attach on the new div
        const newContent = document.createTextNode("Email could not be sent!");
        // add the text node to the newly created div
        newDiv.appendChild(newContent);
        // Add the new element to the parent div
        const parentDiv = document.getElementById("parent-container");
        parentDiv.parentNode.insertBefore(newDiv, parentDiv);
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
