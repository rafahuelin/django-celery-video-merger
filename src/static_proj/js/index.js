import '../scss/main.scss';

import 'bootstrap';
import Sortable from 'sortablejs';

document.addEventListener("DOMContentLoaded", function (event) {
  // Variables definition
  const csrftoken = document.getElementsByName("csrfmiddlewaretoken")[0].value;
  const displayArea = document.getElementById("videoList");
  const fileForm = document.getElementsByTagName('form')[0];
  const formUrl = document.getElementsByTagName("form")[0].action;
  const uploader = document.getElementById("id_file_field");
  let files;
  let sortedTitles = [];

  // Event listeners
  uploader.addEventListener("input", displayFileNames);
  fileForm.addEventListener("submit", sendFiles);

  // Functions
  function displayFileNames() {
    files = uploader.files;
    let fileNames = [];
    displayArea.innerHTML = '';

    // Create filenames array
    for (let i = 0; i < files.length; i++) {
      fileNames.push(files[i].name);
    }

    // Display filenames list
    fileNames.forEach(function (fileName) {
      displayArea.innerHTML += "<li class='list-group-item'>" + fileName + "</li>";
    });

  }

  // Sort frontend list
  Sortable.create(displayArea, {
    animation: 150
  });

  function createSortedTitles() {
    sortedTitles = [];
    const sortedList = document.getElementsByClassName('list-group-item');
    for (let i = 0; i < files.length; i++) {
      sortedTitles.push(sortedList[i].innerText);
    }
  }

  // Upload sorted multiple files
  async function sendFiles(e) {
    e.preventDefault();
    createSortedTitles();
    let formData = new FormData();
    formData.append('title', 'Videos to Merge');
    formData.append('csrfmiddlewaretoken', csrftoken);
    formData.append('sortedtitles', sortedTitles);
    sortedTitles.forEach(function (title) {
      for (let i = 0; i < files.length; i++) {
        if (title == files[i].name) {
          console.log(title, files[i].name);
          formData.append('file_field', files[i]);
        }
      }
    });

    const options = {
      method: 'POST',
      body: formData
    }

    try {
      const response = await fetch(formUrl, options);
      const result = await response.json();
      console.log('Success:', JSON.stringify(result));
    } catch (error) {
      console.log('Error', error);
    }
  }
});
