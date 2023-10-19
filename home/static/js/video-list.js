document.addEventListener("DOMContentLoaded", function () {
    const chapters = document.querySelectorAll('.chapter');

    chapters.forEach(chapter => {
        chapter.addEventListener('click', () => {
            chapter.classList.toggle('active');
        });
    });
});