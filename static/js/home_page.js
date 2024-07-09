    function open_comments_box(event) {
        var postId = event.target.dataset.postId;
        var commentBlock = document.getElementById('comment_block_' + postId);
        commentBlock.style.display = 'block';

        fetch_comments(postId);
    }

    function close_comments_box(postId) {
        document.getElementById('comment_block_' + postId).style.display = 'none';
    }



    function fetch_comments(postId) {
        fetch(`/get_comments/${postId}/`)
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                return response.json();
            })
            .then(data => {
                var commentsSection = document.getElementById(`comments_${postId}`);
                commentsSection.innerHTML = '';
    
                let commentsHTML = '';
                data.comments.forEach(comment => {
                    commentsHTML += `
                        <div class="comment">

                            <p style="display: flex;justify-content: left;width: 100%;">
                            ${comment.by_commented} :
                            </p>


                            <p style="font-size:small">${comment.comments}</p>
                            <hr>
                        </div>
                    `;
                });
    
                commentsSection.innerHTML = commentsHTML;
            })
            .catch(error => {
                console.error('Error fetching comments:', error);
                var commentsSection = document.getElementById(`comments_${postId}`);
                commentsSection.innerHTML = '<p style="color: red;">Failed to load comments. Please try again later.</p>';
            });
    }
    


    function view_edit_profile() {
        var block = document.getElementById('view_block');
        block.style.display = 'block';
    }

    function closeDiv() {
        var div = document.getElementById('view_block');
        div.style.display = 'none';
    }

    function openDiv() {
        var div = document.getElementById('post_popup');
        div.style.display = 'block';
    }

    function closePost() {
        var div = document.getElementById('post_popup');
        div.style.display = 'none';
    }

    function add_comments(postId) {
        const commentPost = document.getElementById(`comment_post_${postId}`);
        commentPost.style.display = 'block';
    }

    function view_followers() {
        var div = document.getElementById('view_followers');
        div.style.display = 'block';
    }

    function view_followers_close() {
        var div = document.getElementById('view_followers');
        div.style.display = 'none';
    }



    function view_following(){

        var div = document.getElementById('view_following');

        div.style.display = 'block';
    }

    function view_following_close(){

        var div = document.getElementById('view_following');
        div.style.display = 'none';

    }