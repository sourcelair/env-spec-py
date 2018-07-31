const myRequest = new Request('/api/render/', {method: 'GET'});

fetch(myRequest).then(function(response) {
  response.text().then(function(text) {
    poemDisplay.textContent = text;
  });
});