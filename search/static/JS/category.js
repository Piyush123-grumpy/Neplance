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

tags = "/search/";
let categories = document.getElementsByClassName('input-category');

search_btn = document.getElementById('btn-search')
search_btn.addEventListener('click',()=>{
    if (document.getElementById('tag').value){
        tags += '?tag='+document.getElementById('tag').value+'&'
    }
    if (document.getElementById('min-input').value){
        tags += '?min='+document.getElementById('min-input').value+'&'
    }
    if (document.getElementById('max-input').value){
        tags += '?max='+document.getElementById('max-input').value+'&'
    }
    // categories
    var categories = document.getElementsByName('category')
    for(let i=0; i<categories.length; i++){
        if(categories[i].checked){
            tags += '?category='+categories[i].value+'&'
        }
    }
    var mobile_categories = document.getElementsByName('mobile-category')
    for(let i=0; i<mobile_categories.length; i++){
        if(mobile_categories[i].checked){
            tags += '?category='+mobile_categories[i].value+'&'
        }
    }
    
    window.location.replace(tags)
    // alert(rag)
})