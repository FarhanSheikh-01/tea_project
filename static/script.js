function handleFileUpload(event) {
    const file = event.target.files[0]; // Get the uploaded file
    if (file) {
      const formData = new FormData();
      formData.append("image", file);
  
      // Show the uploaded image inside the drag-and-drop container
      const reader = new FileReader();
      reader.onload = function (e) {
        // Update the drag-and-drop box with the uploaded image preview
        const imagePreview = document.getElementById("imagePreview");
        const dropZoneText = document.getElementById("dropZoneText");
        const cloudIcon = document.getElementById("cloudIcon");
        const uploadButton = document.getElementById("uploadButton");
  
        // Set the preview image source and display it
        imagePreview.src = e.target.result;
        imagePreview.style.display = "block";
  
        // Hide placeholder elements
        dropZoneText.style.display = "none";
        cloudIcon.style.display = "none";
        uploadButton.style.display = "none";
      };
      reader.readAsDataURL(file);
  
      // Send the file to the backend
      fetch("/predict_sickness/", {
        method: "POST",
        body: formData,
        headers: {
          "X-CSRFToken": "{{ csrf_token }}", // Include CSRF token
        },
      })
        .then((response) => response.json())
        .then((data) => {
          const resultText = document.getElementById("resultText");
          if (data.status === "success") {
            // Delay showing the prediction result by 1 second
            setTimeout(() => {
              resultText.innerText = `Prediction: ${data.result} (Confidence: ${data.confidence})`;
            }, 1000);
          } else {
            // Delay showing the error message by 1 second
            setTimeout(() => {
              resultText.innerText = `Error: ${data.message}`;
            }, 1000);
          }
        })
        .catch((error) => {
          const resultText = document.getElementById("resultText");
          setTimeout(() => {
            resultText.innerText = `Error: ${error}`;
          }, 1000);
        });
    }
  }
  
  function handleDrop(event) {
    event.preventDefault();
    const file = event.dataTransfer.files[0];
    const input = document.getElementById("imageInput");
    if (file) {
      const dataTransfer = new DataTransfer();
      dataTransfer.items.add(file);
      input.files = dataTransfer.files;
  
      // Trigger the onchange event to handle the file
      input.dispatchEvent(new Event("change"));
    }
  }
  