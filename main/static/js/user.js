let categories = document.querySelectorAll(".main-content");
let links = document.querySelectorAll(".nav");

for (let i = 0; i < links.length; i++) {
  links[i].addEventListener("click", (e) => {
    if (e.target.textContent === "my pitches") {
      for (let j = 0; j < links.length; j++) {
        categories[j].classList.remove("active");
      }
      for (let k = 0; k < links.length; k++) {
        if (categories[k].id === "mypitches") {
          categories[k].classList.add("active");
        }
      }
    } else if (e.target.textContent === "all pitches") {
      for (let j = 0; j < links.length; j++) {
        categories[j].classList.remove("active");
      }
      for (let k = 0; k < links.length; k++) {
        if (categories[k].id === "allpitches") {
          categories[k].classList.add("active");
        }
      }
    } else if (e.target.textContent === "investors") {
      for (let j = 0; j < links.length; j++) {
        categories[j].classList.remove("active");
      }
      for (let k = 0; k < links.length; k++) {
        if (categories[k].id === "investors") {
          categories[k].classList.add("active");
        }
      }
    } else if (e.target.textContent === "customers") {
      for (let j = 0; j < links.length; j++) {
        categories[j].classList.remove("active");
      }
      for (let k = 0; k < links.length; k++) {
        if (categories[k].id === "customers") {
          categories[k].classList.add("active");
        }
      }
    } else if (e.target.textContent === "sales") {
      for (let j = 0; j < links.length; j++) {
        categories[j].classList.remove("active");
      }
      for (let k = 0; k < links.length; k++) {
        if (categories[k].id === "sales") {
          categories[k].classList.add("active");
        }
      }
    } else {
      for (let j = 0; j < links.length; j++) {
        categories[j].classList.remove("active");
      }
      for (let k = 0; k < links.length; k++) {
        if (categories[k].id === "employees") {
          categories[k].classList.add("active");
        }
      }
    }
  });
}
