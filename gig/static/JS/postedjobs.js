console.log()
let del_btns = document.getElementsByClassName('del-btn');
var arr = [].slice.call(del_btns);
let current = -9999;
arr.forEach(element => {
    element.addEventListener('click', ()=>{
        let div = document.getElementById('popup')
        div.style.transition = "500ms";
        div.style.transform = "translate(-50%, -50%)";
        div.style.display = null;
        current = element.dataset.id;
    });
    // document.getElementById('cfm-delete').addEventListener('click', ()=>{removeGig(id)})
});
document.getElementById('cfm-delete').addEventListener('click', removeGig)


function removeGig(){
    let gig = current
    // CSRF token taken from DOM.
    csrftoken = document.querySelector('[name="csrfmiddlewaretoken"]').value;

    // XMLHttpRequest used for sending POST request.
    var req = new XMLHttpRequest();
    req.open("POST", '/gig/removeGig/', true);

    // Headers.
    req.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
    req.setRequestHeader("x-csrfToken", csrftoken);

    // Send data.
    let statement = 'gig='+gig
    req.send(statement);

    // Recieve response.
    req.onload = ()=>{
        console.log('current', current)
        console.log(req.response);
        if(req.response == 69){
            console.log(req.response);
            window.location.reload();
        }
    };
        
}


document.getElementById('x').addEventListener('click', ()=>{
    let div = document.getElementById('popup');
    div.style.transition = "500ms";
    div.style.transform = "translate(-50%, -500%)";
})
