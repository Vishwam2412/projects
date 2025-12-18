const quote_element = document.querySelector("#quote");
//const message_element = document.getElementById("message");

const quotes = [
  "This is 1st quote"
];

const get_random_quote = () => quotes[Math.floor(Math.random() * quotes.length)];

quote_element.innerText = get_random_quote();


