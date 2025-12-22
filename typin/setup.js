//alert("JS loaded");

const start_button = document.querySelector("#st_button");
const quote_element = document.querySelector("#quote");
const message_element = document.querySelector("#message");
const input_part = document.querySelector("#input");

const quotes = [
  "This is 1st quote",
  "Random quote 2nd"
];

const get_random_quote = () => quotes[Math.floor(Math.random() * quotes.length)];

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
  input_part.focus();
  input_part.value = "";
  message_element.innerText = "";
}

//
//const logic = () => {
  //input_part.addEventListener('input', (ip)=>{
      //const inp = ip.target.value;
      ////word = words[index];
////      for(int i = 0 ; i<inp.length ; ++i){
        //const word = words[index];
        ////if(word == inp && index == words.length-1){
        //// const fin = (Date.now() - start) /1000;
      //// message_element.innerText = `Suceeded in ${fin}.`
        ////}
        //if(inp.endsWith(' ')){
           //const match = inp.trim();
        //
        //if(word != match){
          //message_element.innerText = "MisMatch---------------";
        //}else{
          //++index;
          //ip.target.value="";
          //message_element.innerText="";
          //if (index === words.length) {
          //const fin = ((Date.now() - start) / 1000).toFixed(2);
          //message_element.innerText = `Succeeded in ${fin} seconds ✅`;
          //input_part.disabled = true;
        //}
        //}
        //}
      //
//
  //})
//}
//


const logic = ()=>{
  const currentWord = words[index];
  const typedValue = input_part.value;
  if(currentWord===typedValue.trim() && index === words.length-1){
      const finish_time = ((Date.now() - start)/1000).toFixed(2);
      message_element.innerText = `Completed test in ${finish_time}.`;
      input_part.disabled = true;
    return;
  }
  else if(typedValue.endsWith(" ") && typedValue.trim()===currentWord){
      //const match = typedValue.trim();
      //if(match!=word){
        //console.log('MisMatch---------------');
      //}else{
        ++index;
        input_part.value = "";
      //}
  }
  else if(currentWord.startsWith(typedValue)){
      input_part.classList.remove("error");
      //for(int i = 0 ; i<match.length ; ++i){
        //if(match[i]!=currentWord[i]){
        //console.log('MisMatch---------------');
        //}
      //}
      
  }else{
    input_part.classList.add("error");
    message_element.innerText = "MisMatch---------------";
  }
 }

start_button.addEventListener('click',startWith);
input_part.addEventListener('input',logic);

//startWith();
//logic();


