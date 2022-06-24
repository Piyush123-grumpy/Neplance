



// Reject buttons
let rejectBtns = document.getElementsByClassName('btn-reject')
var rejArr = [].slice.call(rejectBtns);

// Khalti
var config = {
    // replace the publicKey with yours
    "publicKey": "test_public_key_126703ef5476440c8ae6c68da6f938d8",
    "productIdentity": "123456789",
    "productName": "test",
    "productUrl": "http://gameofthrones.wikia.com/wiki/Dragons",
    "paymentPreference": [
        "KHALTI",
        "EBANKING",
        "MOBILE_BANKING",
        "CONNECT_IPS",
        "SCT",
        ],
    "eventHandler": {
        onSuccess (payload) {
            // hit merchant api for initiating verfication
            console.log(payload);
            console.log('token'+payload.token)
            csrftoken = document.querySelector('[name="csrfmiddlewaretoken"]').value;

            var req = new XMLHttpRequest();
            req.open("POST", '/khalti/verifypayment/', true);
        
            // Headers.
            req.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
            req.setRequestHeader("x-csrfToken", csrftoken);
            // Send data.
            let statement = 'token=' + payload.token + '&amount=1000'
            req.send(statement);
            req.onload = ()=>{
                console.log('response:::::::::::    '+req.response);
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
    checkout.show({amount: 1000});
}

// Update Status
rejArr.forEach(element => {
    let app = element.dataset.app
    let status = element.dataset.status
    element.addEventListener('click', ()=>{
        updateApp(app, status);
        // console.log('id'+ app)

    })
});


document.getElementById('btn-test').addEventListener('click', ()=>{
    // CSRF token taken from DOM.
    csrftoken = document.querySelector('[name="csrfmiddlewaretoken"]').value;
    // XMLHttpRequest used for sending POST request.
    var req = new XMLHttpRequest();
    req.open("POST", '/khalti/verifypayment/', true);
    req.setRequestHeader("x-csrfToken", csrftoken);

    // Headers.
    req.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");

    // Send data.
    let statement = 'token=QUao9cqFzxPgvWJNi9aKac&amount=150'
    req.send(statement);

    // Recieve response.
    req.onload = ()=>{
        console.log('response:::::::'+req.response);
        // window.location.reload();

    };
})

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