var searchBtn = document.querySelector('#SearchBtn');
searchBtn.addEventListener('click', getData);

var giglist = document.querySelector('#gig-list');
// giglist.innerHTML = {context.categories}
// console.log({{context}})

function getData(){
    // API url.    
    let url = 'http://127.0.0.1:8000/gig/filtersearch/';
    // User entered advance search data.
    let category = document.getElementById('categories').value;
    let min_input = parseInt(document.getElementById('min-pay').value);
    let max_input = parseInt(document.getElementById('max-pay').value);
    // If min input is not an integer.
    if (isNaN(min_input)){
        min_input = -9999;
    }
    if (isNaN(max_input)){
        max_input = -9999;
    }
    
    // Get the actual maximum and minimum values in the given input.
    // For validation purpose.

    url += category + '/' + min_input + '/' + max_input;
    console.log(url);
    fetch(url)
        .then(response=>response.json()
        .then(data=>{
            console.log(data);
            data.forEach(element => {
                    document.write(element.title + '<br>');
            });
        })
    )
}

