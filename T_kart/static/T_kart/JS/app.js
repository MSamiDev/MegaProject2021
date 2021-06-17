
const menu = document.querySelector('.nav-list');
const menuBtn = document.querySelector('#check');
menuBtn.addEventListener('change', function(e){
    if(menuBtn.checked){
        menu.style.display = "block";
    }else{
        menu.style.display = "none";
    }
});