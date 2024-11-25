document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("studentForm");
    form.addEventListener("submit", (event) => {
        if (!form.checkValidity()) {
            event.preventDefault();
            event.stopPropagation();
        }
        form.classList.add("was-validated");
    });
});
