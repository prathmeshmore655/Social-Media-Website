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
