


const queryString = window.location.search;
const urlParams = new URLSearchParams(queryString);


if (urlParams.get('min')){
    document.getElementById('mobile-min-input').value=urlParams.get('min');
    document.getElementById('min-input').value=urlParams.get('min');
}

if (urlParams.get('max')){
    document.getElementById('mobile-max-input').value=urlParams.get('max');
    document.getElementById('max-input').value=urlParams.get('max');
}

if (urlParams.get('tag')){
    document.getElementById('mobile-tag').value=urlParams.get('tag');
    document.getElementById('tag').value=urlParams.get('tag');
}

if (urlParams.get('category')){
    document.getElementById(urlParams.get('category')+'-input').checked = true;
    document.getElementById('mobile-'+urlParams.get('category')+'-input').checked = true;
}

if (urlParams.get('country')){
    document.getElementById('country').value = urlParams.get('country');
    document.getElementById('mobile-country').value = urlParams.get('country');
}


// Desktop Event Listeners.
search_btn = document.getElementById('btn-search')
search_btn.addEventListener('click',()=>{
    // alert('yes queen')
    url = new URL('/search', window.location.origin)
    // url = new URL('http://127.0.0.1:8000/search')
    if(document.getElementById('tag').value){
        url.searchParams.set('tag', document.getElementById('tag').value);
    }
    if(document.getElementById('min-input').value){
        url.searchParams.set('min', document.getElementById('min-input').value);
    }
    if(document.getElementById('max-input').value){
        url.searchParams.set('max', document.getElementById('max-input').value);
    }

    if (document.getElementById('country').value!=''){
        url.searchParams.set('country', document.getElementById('country').value);
    }

    // categories.
    let categories = document.getElementsByName('category');
    categories.forEach(i=>{
        if(i.checked){
            url.searchParams.set('category', i.value)
        }
    })
    // alert(url)
    window.location.replace(url)
})

// Mobile Event Listeners.
search_btn = document.getElementById('mobile-btn-search')
search_btn.addEventListener('click',()=>{
    url = new URL('/search', window.location.origin)
    // url = new URL('http://127.0.0.1:8000/search')
    if(document.getElementById('mobile-tag').value){
        url.searchParams.set('tag', document.getElementById('mobile-tag').value);
    }
    if(document.getElementById('mobile-min-input').value){
        url.searchParams.set('min', document.getElementById('mobile-min-input').value);
    }
    if(document.getElementById('mobile-max-input').value){
        url.searchParams.set('max', document.getElementById('mobile-max-input').value);
    }

    if (document.getElementById('mobile-country').value != ''){
        url.searchParams.set('country', document.getElementById('mobile-country').value);
    }

    // categories.
    let categories = document.getElementsByName('mobile-category');
    categories.forEach(i=>{
        if(i.checked){
            url.searchParams.set('category', i.value)
        }
    })


    // alert(url)
    window.location.replace(url)
})