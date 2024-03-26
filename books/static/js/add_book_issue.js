document.addEventListener('DOMContentLoaded', function() {
    var modal = document.getElementById('issueModal');
    var btn = document.getElementById('add-issue-btn');
    var closeModals = document.getElementsByClassName('close-modal');
    btn.onclick = function() {
        modal.style.display = 'block';
    }

    for (var i = 0; i < closeModals.length; i++) {
        closeModals[i].onclick = function() {
            modal.style.display = 'none';
        };
    }

    window.onclick = function(event) {
        if (event.target == modal) {
            modal.style.display = 'none';
        }
    }
});
$(document).ready(function() {
    $('.selector').select2({
        width: '100%'
    });
    
});
