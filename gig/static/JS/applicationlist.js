// Reject buttons
let rejectBtns = document.getElementsByClassName('btn-reject')
var rejArr = [].slice.call(rejectBtns);
rejArr.forEach(element => {
    let app = element.dataset.app
    let status = element.dataset.status
    element.addEventListener('click', ()=>{
        updateApp(app, status);
        // console.log('id'+ app)

    })
});

// Hire Buttons
let hireBtns = document.getElementsByClassName('btn-hire')
var hireArr = [].slice.call(hireBtns);
hireArr.forEach(element => {
    let app = element.dataset.app
    let status = element.dataset.status
    element.addEventListener('click', ()=>{
        updateApp(app, status);
    })
});

function updateApp(app, status){
    // CSRF token taken from DOM.
    csrftoken = document.querySelector('[name="csrfmiddlewaretoken"]').value;

    // XMLHttpRequest used for sending POST request.
    var req = new XMLHttpRequest();
    req.open("POST", '/gig/updateApplication/', true);

    // Headers.
    req.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
    req.setRequestHeader("x-csrfToken", csrftoken);

    // Send data.
    let statement = 'application='+app+'&status='+status
    req.send(statement);

    // Recieve response.
    req.onload = ()=>{
        console.log('response:::::::'+req.response);
        window.location.reload();

    };
}