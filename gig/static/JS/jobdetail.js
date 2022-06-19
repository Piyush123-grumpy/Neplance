
let apply_btn = document.getElementById('apply-btn');
let popup = document.getElementById('popup');
let detailSec = document.getElementById('detail-sec');
let cancel_btn = document.getElementById('x');
let submit_btn = document.getElementById('submit-apply');
let applied_btn = document.getElementById('applied-btn');

apply_btn.addEventListener('click', togglePopup);
cancel_btn.addEventListener('click', togglePopup);


// Apply for job action listener.
$("#submit-apply").click(applyJob);

function togglePopup(){
    popup.classList.toggle("hide")
    detailSec.classList.toggle("blur")
}

function applyJob(){
    // CSRF token taken from DOM.
    csrftoken = document.querySelector('[name="csrfmiddlewaretoken"]').value;

    // XMLHttpRequest used for sending POST request.
    var req = new XMLHttpRequest();
    req.open("POST", '/gig/applyjson/', true);

    // Headers.
    req.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
    req.setRequestHeader("x-csrfToken", csrftoken);

    // Send data.
    let statement = 'user='+user+'&gig='+gig
    req.send(statement);

    // Recieve response.
    req.onload = ()=>{
        
        if(req.response == 6969){
            apply_btn.classList.add('hide')
            applied_btn.classList.remove('hide');
            togglePopup();
        }
    }
}