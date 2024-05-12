var likeButton = document.querySelector("#like");
var dislikeButton = document.querySelector("#dislike");
var postId = likeButton.getAttribute("data-post-id");

likeButton.addEventListener("click", function () {
    var csrftoken = getCookie('csrftoken');

    fetch(`/like/${postId}`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": csrftoken
        },
    })
        .then(response => response.json())
        .then(result => {
            console.log(result);
            document.querySelector("#lc").innerHTML = "&hearts; " + result.likes;
        });
});

dislikeButton.addEventListener("click", function () {
    var csrftoken = getCookie('csrftoken');

    fetch(`/dislike/${postId}`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": csrftoken
        },
    })
        .then(response => response.json())
        .then(result => {
            console.log(result);
            document.querySelector("#lc").innerHTML = "&hearts; " + result.likes;
        });
});

// Function to get CSRF token from cookie
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}