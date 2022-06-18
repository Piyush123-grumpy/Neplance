

let apply_btn = document.getElementById('apply-btn');
let popup = document.getElementById('popup');
let detailSec = document.getElementById('detail-sec');
let cancel_btn = document.getElementById('x');
let submit_btn = document.getElementById('submit-apply');

apply_btn.addEventListener('click', togglePopup);
cancel_btn.addEventListener('click', togglePopup);


// Apply for job action listener.
// submit_btn.addEventListener('click', applyJob);


// At Global Scope


// Inside the function.
// document.querySelector('#submit-apply').addEventListener('click', testajax);
$("#submit-apply").click(applyJob);



function togglePopup(){
    popup.classList.toggle("hide")
    detailSec.classList.toggle("blur")
}


async function applyJob(){
    // console.log('clicked')
    csrftoken = document.querySelector('[name="csrfmiddlewaretoken"]').value;
    console.log(csrftoken);
  try{
  await fetch('http://127.0.0.1:8000/gig/applyjson/',
  {
    method:"POST",
    mode: 'cors',
    headers: {
      'X-CSRFToken': csrftoken,
      'Content-Type': 'application/json',
      'Accept': 'application/json'
    },
    body: JSON.stringify({"user":2, "gig":3}),
    // data: {user:2, gig:3},
    },
  )
  .then(response => response.json())
  .then(data => console.log(data));
  }
  catch(ex){
    console.log(ex);
  }
}