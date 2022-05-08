loginToggle = document.querySelector("#login-toggle");
signupToggle = document.querySelector("#signup-toggle");

loginForm = document.querySelector("#login-form");
signupForm = document.querySelector("#signup-form");

loginToggle.addEventListener("click", () => {
  signupForm.style.display = "none";
  loginForm.style.display = "flex";
});

signupToggle.addEventListener("click", () => {
  loginForm.style.display = "none";
  signupForm.style.display = "flex";
});
