function redirectToHome(){
    window.location.href = '/';
}
function renderPlanner(){
    window.location.href = '/planner';
}

document.addEventListener("DOMContentLoaded", function () {
    const button = document.getElementById("signInButton");
    if (button) {
        button.addEventListener("click", function () {
            window.location.href = "/auth/signup";
        });
    }
});

document.addEventListener("DOMContentLoaded", function () {
    const button = document.getElementById("recommenderLink");
    if (button) {
        button.addEventListener("click", function () {
            window.location.href = "/recommender";
        });
    }
});