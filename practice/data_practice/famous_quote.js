//THIS IS TO PRACTICE DOWNLOADING JSON FILES.


let quotes = [];

document.getElementById('quoteForm').addEventListener('submit', function(e) {
  e.preventDefault();

  // Retrieve the values from the form
  let nameInput = document.getElementById('name').value;
  let quoteInput = document.getElementById('quote').value;

  // Log the values to check if they are being retrieved correctly
  // console.log('Name:', nameInput);
  // console.log('Quote:', quoteInput);

  let newQuote = {
      name: nameInput,
      quote: quoteInput
  };
  // console.log(newQuote)




  // Retrieve existing quotes from local storage
  let quotes = JSON.parse(localStorage.getItem('quotes')) || [];

  // Log the existing quotes to check if they are being retrieved correctly
  // console.log('Existing quotes:', quotes);

  // Add the new quote to the array. NOTE: It is not pushing quotes from JSON.parse from above.
  quotes.push(newQuote);

  // Log the updated quotes array to check if the new quote is added correctly
  // console.log('Updated quotes:', quotes);

  // Save the updated quotes array back to local storage
  localStorage.setItem('quotes', JSON.stringify(quotes));


  // Clear the form after submitting
  document.getElementById('quoteForm').reset();
  displayQuotes();
});


// Make an empty array
// Inside the form's add.EventListener
// e.preventDefault() to prevent refresh during submission
// grab value from forms
// make the object to put the form values into
// make a quotes variable and bring back pre-existing stored JSON
// push quotes into empty array
// make setItem to save quotes with JSON.stringify


function displayQuotes() {
  let quotes = JSON.parse(localStorage.getItem('quotes')) || [];
  let quotesList = document.getElementById('quotesList');
  quotesList.innerHTML = '';

  for (let i = 0; i < quotes.length; i++) {
    let quote = quotes[i];
    let li = document.createElement('li');
    li.textContent = `${quote.name}: "${quote.quote}"`;
    quotesList.appendChild(li);
  }
}

/*
Explanation
HTML Update:

Ensure FileSaver.js is included in the <head> section of your HTML file.
JavaScript Update:

displayQuotes Function: Remains the same, displaying saved quotes from local storage.
Form Submission Event: Remains the same, handling the form submission, saving quotes to local storage, and updating the displayed list.
Save JSON Button Event:

Add an event listener for the "Save JSON" button.

Retrieve the quotes from local storage.

Convert the quotes array to a JSON string using JSON.stringify.

Create a Blob from the JSON string with the type set to "application/json".
Use FileSaver.js's saveAs function to prompt the user to download the JSON file, naming it quotes.json.

Test Your Implementation by downloading a file.
*/

// This is to download the JSON.
const saveJSON = document.querySelector('.saveJSON')
saveJSON.addEventListener('click', downloadJSON)

function downloadJSON() {
  let quotes = JSON.parse(localStorage.getItem('quotes')) || [];
  let quotesJSON = JSON.stringify(quotes, null, 2); // This line converts a JavaScript object or array (quotes) into a JSON string.
  let blob = new Blob([quotesJSON], { type: "application/json" }); //This line creates a Blob object representing the data in the JSON string format, with the specified MIME type.
  saveAs(blob, 'quotes.json') // downloads the file.
}


// Display quotes on page load
displayQuotes();
