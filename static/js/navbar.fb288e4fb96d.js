let nav = document.querySelector('#navbar');

// Add scroll event listner to the window.
window.addEventListener('scroll', ()=>{
    // Add transistion duration to navbar
    nav.style.transitionDuration = '0.3s';
    // If scroll on top of the page.
    if(window.scrollY!=0){
        nav.style.backgroundColor = '#0065AD'; 
    }
    // If scroll on top of the page.
    else{
        
        nav.style.backgroundColor = '#243A73';
    }
})