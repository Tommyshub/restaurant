// Get stripe public key
var stripePublicKey = $("#id_stripe_public_key").text().slice(1, -1);
// Get client secret key
var clientSecret = $("#id_client_secret").text().slice(1, -1);
// Conenct to stripe
var stripe = Stripe(stripePublicKey);
// Create an instance of the stripe elements
var elements = stripe.elements();
// Styling for the card element
var style = {
  base: {
    color: "#000",
    fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
    fontSmoothing: "antialiased",
    fontSize: "16px",
    "::placeholder": {
      color: "#aab7c4",
    },
  },
  invalid: {
    color: "#dc3545",
    iconColor: "#dc3545",
  },
};
var card = elements.create("card", { style: style });
card.mount("#card-element");

// Handle realtime validation errors on the card element
card.addEventListener("change", function (event) {
  var errorDiv = document.getElementById("card-errors");
  if (event.error) {
    var html = `
          <span class="icon" role="alert">
              <i class="fas fa-times"></i>
          </span>
          <span>${event.error.message}</span>
      `;
    $(errorDiv).html(html);
  } else {
    errorDiv.textContent = "";
  }
});

// Submitting the form
var style = {
  base: {
    color: "#000",
    fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
    fontSmoothing: "antialiased",
    fontSize: "16px",
    "::placeholder": {
      color: "#aab7c4",
    },
  },
  invalid: {
    color: "#dc3545",
    iconColor: "#dc3545",
  },
};
var card = elements.create("card", { style: style });
card.mount("#card-element");

// Handle validation errors on the card element
card.addEventListener("change", function (event) {
  var errorDiv = document.getElementById("card-errors");
  if (event.error) {
    var html = `
          <span class="icon" role="alert">
              <i class="fas fa-times"></i>
          </span>
          <span>${event.error.message}</span>
      `;
    $(errorDiv).html(html);
  } else {
    errorDiv.textContent = "";
  }
});

// Form submit
var form = document.getElementById("payment-form");

form.addEventListener("submit", function (ev) {
  ev.preventDefault();
  card.update({ disabled: true });
  $("#submit-button").attr("disabled", true);
  $("#payment-form").fadeToggle(100);
  $("#loading-overlay").fadeToggle(100);

  var SaveInfo = Boolean($("#id-save-info").attr("checked"));
  var csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
  var postData = {
    csrfmiddlewaretoken: csrfToken,
    client_secret: clientSecret,
    save_info: SaveInfo,
  };
  var url = "/checkout/cache_checkout_data";

  $.post(url, postData)
    .done(function () {
      stripe
        .confirmCardPayment(clientSecret, {
          payment_method: {
            card: card,
            billing_details: {
              name: $.trim(form.full_name.value),
              phone: $.trim(form.phone.value),
              email: $.trim(form.email.value),
              address: {
                line1: $.trim(form.address1.value),
                line2: $.trim(form.address2.value),
                city: $.trim(form.city.value),
                country: $.trim(form.country.value),
                state: $.trim(form.state.value),
              },
            },
          },
          shipping: {
            name: $.trim(form.full_name.value),
            phone: $.trim(form.phone.value),
            email: $.trim(form.email.value),
            address: {
              line1: $.trim(form.address1.value),
              line2: $.trim(form.address2.value),
              country: $.trim(form.country.value),
              city: $.trim(form.city.value),
              post_code: $.trim(form.post_code.value),
              state: $.trim(form.state.value),
            },
          },
        })
        .then(function (result) {
          if (result.error) {
            var errorDiv = document.getElementById("card-errors");
            var html = `
              <span class="icon" role="alert">
              <i class="fas fa-times"></i>
              </span>
              <span>${result.error.message}</span>`;
            $(errorDiv).html(html);
            $("#payment-form").fadeToggle(100);
            $("#loading-overlay").fadeToggle(100);
            card.update({ disabled: false });
            $("#submit-button").attr("disabled", false);
          } else {
            if (result.paymentIntent.status === "succeeded") {
              form.submit();
            }
          }
        });
    })
    // Reload the page and show django error message
    .fail(function () {
      location.reload();
    });
});
