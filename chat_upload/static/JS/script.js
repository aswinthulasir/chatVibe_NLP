let slideIndex = 0;
showSlides();

function showSlides() {
  let i;
  let slides = document.getElementsByClassName("mySlides");
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";
  }
  slideIndex++;
  if (slideIndex > slides.length) {
    slideIndex = 1;
  }
  slides[slideIndex - 1].style.display = "block";
  setTimeout(showSlides, 3000); // Change image every 2 seconds
}

function activateUpload() {
  document.getElementById("uploadbtn").click();
}

// Button placeholder

document.getElementById("uploadButton").addEventListener("click", function () {
  document.getElementById("fileInput").click();
});

document.getElementById("fileInput").addEventListener("change", function () {
  // Handle the selected file here, for example, display its name
  const selectedFile = this.files[0];
  if (selectedFile) {
    alert(`Selected file: ${selectedFile.name}`);
  }
});


