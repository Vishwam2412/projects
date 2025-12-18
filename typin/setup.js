alert("JS loaded");

const quote_element = document.querySelector("#quote");
const message_element = document.querySelector("#message");
const input_part = document.querySelector("#input");

const quotes = [
  "This is 1st quote",
  "Random quote 2nd"
];

const get_random_quote = () => quotes[Math.floor(Math.random() * quotes.length)];
quote_element.innerText = "Yhsaj";

let start = 0;
let words = [];
let quote = "";
let index = 0;

const startWith = () => {
  start = Date.now();
  quote = get_random_quote();
  quote_element.innerText = quote;
  words = quote.split(" ");
  index = 0 ; 
  input_part.disabled = false;
input_part.value = "";
message_element.innerText = "";

}


const logic = () => {
  input_part.addEventListener('input', (ip)=>{
      const inp = ip.target.value;
      //word = words[index];
//      for(int i = 0 ; i<inp.length ; ++i){
        const word = words[index];
        //if(word == inp && index == words.length-1){
        // const fin = (Date.now() - start) /1000;
      // message_element.innerText = `Suceeded in ${fin}.`
        //}
        if(inp.endsWith(' ')){
           const match = inp.trim();
        
        if(word != match){
          message_element.innerText = "MisMatch---------------";
        }else{
          ++index;
          ip.target.value="";
          message_element.innerText="";
          if (index === words.length) {
          const fin = ((Date.now() - start) / 1000).toFixed(2);
          message_element.innerText = `Succeeded in ${fin} seconds ✅`;
          input_part.disabled = true;
        }
        }
        }
      

  })
}

startWith();
logic();


