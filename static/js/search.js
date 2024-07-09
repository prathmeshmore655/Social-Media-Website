function view_edit_profile(){

    var block = document.getElementById('view_block');

    block.style.display = 'block';

    

}

function closeDiv() {
    var div = document.getElementById('view_block');

    div.style.display = 'none';
}


function openDiv(){

    var div = document.getElementById('post_popup');

    div.style.display = 'block'
}

function closePost(){

    var div = document.getElementById('post_popup');

    div.style.display = 'none'
}



const reels = document.querySelectorAll('.reel');


  reels.forEach((reel) => {

    const observer = new IntersectionObserver((entries) => {

      if (entries[0].isIntersecting) {

        reel.play();

      } else {

        reel.pause();

      }

    }, { threshold: 1.0 });


    observer.observe(reel);

  });