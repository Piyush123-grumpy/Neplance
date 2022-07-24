// Reject buttons
let rejectBtns = document.getElementsByClassName('btn-reject')
var rejArr = [].slice.call(rejectBtns);

let currentApplication = null;
let currentAmount = null;
let currentUser = null;

rejArr.forEach(element => {
    let app = element.dataset.app
    let status = element.dataset.status
    element.addEventListener('click', ()=>{
        updateApp(app, status);
        // console.log('id'+ app)
        console.log()

    })
});
// Hire Buttons
let hireBtns = document.getElementsByClassName('btn-hire')
var hireArr = [].slice.call(hireBtns);
hireArr.forEach(element => {
    let app = element.dataset.app;
    let status = element.dataset.status;
    let username = element.dataset.user;
    let amount = element.dataset.amount;
    element.addEventListener('click', ()=>{
        // updateApp(app, status);
        currentApplication = app;
        currentAmount = amount;
        currentUser = username;
        let popup = document.getElementById('popup');
        popup.style.transition = "500ms";
        popup.style.transform = "translate(-50%, -50%)";

        // Update hire message.
        document.getElementById('hire-message').innerHTML = "Are you sure you want to hire " + username + '?';

    })
});

document.getElementById('x').addEventListener('click', ()=>{
    let popup = document.getElementById('popup');
    popup.style.transition = "500ms";
    popup.style.transform = "translate(-50%, -500%)";
})






// Khalti
var config = {
    // replace the publicKey with yours
    "publicKey": "test_public_key_126703ef5476440c8ae6c68da6f938d8",
    "productIdentity": toString(currentApplication),
    "productName": toString(currentUser),
    "productUrl": "http://gameofthrones.wikia.com/wiki/Dragons",
    "paymentPreference": [
        "KHALTI",
        "CONNECT_IPS",
        ],
    "eventHandler": {
        onSuccess (payload) {
            // hit merchant api for initiating verfication
            console.log(payload);
            csrftoken = document.querySelector('[name="csrfmiddlewaretoken"]').value;

            // Send token and amount data to khalti url.
            var req = new XMLHttpRequest();
            req.open("POST", '/khalti/verifypayment/', true);
        
            // Headers.
            req.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
            req.setRequestHeader("x-csrfToken", csrftoken);
            // Send data.
            let statement = 'token=' + payload.token + '&amount=' + currentAmount;
            req.send(statement);
            req.onload = ()=>{
                response = JSON.parse(req.response)
                if(response.status == true){
                    updateApp(currentApplication, "Hired")
                    .then(window.location.reload());
                }
            }
        },
        onError (error) {
            console.log(error);
        },
        onClose () {
            console.log('widget is closing');
        }
    }
};

var checkout = new KhaltiCheckout(config);
var btn = document.getElementById("payment-button");
btn.onclick = function () {
    // minimum transaction amount must be 10, i.e 1000 in paisa.
    checkout.show({amount: currentAmount});
}


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
        window.location.reload();

    };
}

var verify_btns = document.getElementsByClassName('btn-verify-completed');
var verArr = [].slice.call(verify_btns);
verArr.forEach(element=>{
    element.addEventListener('click', ()=>{
        updateApp(element.dataset.app, "Completed");
    })
})