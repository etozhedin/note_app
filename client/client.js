const url = 'http://127.0.0.1:8000/api/token/';
const data = {
  username: 'etozhedin',
  password: '1234'
};

fetch(url, {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json'
  },
  body: JSON.stringify(data)
})
  .then(response => response.json())
  .then(data => console.log(data)); 
  