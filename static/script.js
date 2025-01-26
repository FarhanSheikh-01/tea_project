const dropZone = document.getElementById('dropZone');
  const dropZoneText = document.getElementById('dropZoneText');
  const imageInput = document.getElementById('imageInput');
  const imagePreview = document.getElementById('imagePreview');
  const previewContainer = document.getElementById('previewContainer');
  const resultText = document.getElementById('resultText');

  // Click on drop zone to trigger file input
  dropZone.addEventListener('click', () => {
    imageInput.click();
  });

  // Drag-and-drop functionality
  dropZone.addEventListener('dragover', (e) => {
    e.preventDefault();
    dropZone.style.borderColor = 'blue';
  });

  dropZone.addEventListener('dragleave', () => {
    dropZone.style.borderColor = 'black';
  });

  dropZone.addEventListener('drop', (e) => {
    e.preventDefault();
    dropZone.style.borderColor = 'black';
    const file = e.dataTransfer.files[0];
    if (file && file.type.startsWith('image/')) {
      handleFileUpload(file);
    } else {
      alert('Please upload a valid image file.');
    }
  });

  // Handle file input change
  imageInput.addEventListener('change', (e) => {
    const file = e.target.files[0];
    if (file) {
      handleFileUpload(file);
    }
  });

  // Handle file upload and preview
  function handleFileUpload(file) {
    const reader = new FileReader();
    reader.onload = (e) => {
      imagePreview.src = e.target.result;
      previewContainer.style.display = 'block';
      dropZone.style.display = 'none';
      sendForPrediction(file);
    };
    reader.readAsDataURL(file);
  }

  // Send image to server for prediction
  async function sendForPrediction(file) {
    const formData = new FormData();
    formData.append('image', file);

    resultText.textContent = 'Processing...';

    try {
      const response = await fetch('/predict', { method: 'POST', body: formData });
      const data = await response.json();
      resultText.textContent = `Prediction: ${data.prediction}`;
    } catch (error) {
      resultText.textContent = 'Error in prediction. Please try again.';
    }
  }