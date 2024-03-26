document.addEventListener('DOMContentLoaded', function() {
    var bookModal = document.getElementById('bookModal');
    var addBookBtn = document.getElementById('add-books-btn');
    var closeModals = document.getElementsByClassName('close-modal');
    addBookBtn.onclick = function() {
        bookModal.style.display = 'block';
    }

    var bookInstanceModal = document.getElementById('bookInstanceModal');
    var addBookInstanceBtn = document.getElementById('add-book-instance-btn');
    
    addBookInstanceBtn.onclick = function() {
        bookInstanceModal.style.display = 'block';
    }

    for (var i = 0; i < closeModals.length; i++) {
        closeModals[i].onclick = function() {
            bookInstanceModal.style.display = 'none';
            bookModal.style.display = 'none';
        };
    }

    window.onclick = function(event) {
        if (event.target == bookInstanceModal) {
            bookInstanceModal.style.display = 'none';
        }
        else if(event.target == bookModal){
            bookModal.style.display = 'none';
        }
    }
});
