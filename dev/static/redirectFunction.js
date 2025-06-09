function redirectToHome(){
    window.location.href = '/';
}
function renderPlanner(){
    window.location.href = '/planner';
}

document.addEventListener("DOMContentLoaded", function () {
    const button = document.getElementById("signInButton");
    console.log("Found the sign in button");
    if (button) {
        button.addEventListener("click", function () {
            window.location.href = "/auth/signup";
        });
    }
});