// Check if Website has been loaded, then call function for API Call

window.addEventListener("DOMContentLoaded", (event)=> {
   
    reviseCount();
   
})


// The URL of the AWS API GATE
let AWS_API_GATEWAY_URL = 'https://w0os4gqp84.execute-api.us-east-1.amazonaws.com/getCount';

/*----------API Call----------*/
async function reviseCount() {
    let response = await fetch(AWS_API_GATEWAY_URL);
    let data = await response.json();
    document.getElementById("counter").innerText = data.body.pageViews;
  }