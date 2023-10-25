const replyButtons = document.querySelectorAll('.reply-button');
const replySections = document.querySelectorAll('.reply-section');
const textInputs = document.querySelectorAll('.text-input');

replyButtons.forEach((button, index) => {
    button.addEventListener('click', (e) => {
        e.stopPropagation(); // Prevent click on the reply button from propagating to the document
        if (replySections[index].style.display === 'block') {
            replySections[index].style.display = 'none';
        } else {
            replySections.forEach(section => section.style.display = 'none');
            replySections[index].style.display = 'block';
            textInputs[index].focus();
        }
    });
});

// Close all reply sections when clicking anywhere on the page
document.addEventListener('click', () => {
    replySections.forEach(section => section.style.display = 'none');
});