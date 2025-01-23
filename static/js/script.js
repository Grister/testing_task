document.querySelectorAll('.btn-reply').forEach((checkbox) => {
    checkbox.addEventListener('change', (e) => {
        const replyForm = checkbox.closest('.post__card').querySelector('.reply-form');
        if (e.target.checked) {
            replyForm.classList.add('visable');
        } else {
            replyForm.classList.remove('visable');
        }
    });
});