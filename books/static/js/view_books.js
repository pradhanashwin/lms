function search_books() {
    var input, view;
    input = document.getElementById('books_search_input').value.toLowerCase();
    view = document.getElementById("book_searched");
    view.replaceChildren("");

    if (input !== "") {
        // Send an AJAX request to the backend to search for books
        var xhr = new XMLHttpRequest();
        xhr.onreadystatechange = function () {
            if (xhr.readyState == XMLHttpRequest.DONE) {
                if (xhr.status == 200) {
                    // Parse the JSON response
                    var books = JSON.parse(xhr.responseText);
                    if (books.length > 0) {
                        for (var i = 0; i < books.length; i++) {
                            debugger
                            var book_title = document.createTextNode(books[i].book_title + '-' + books[i].author);
                            var link = document.createElement("a");
                            link.setAttribute("href", "/view_book_record/" + books[i].id);

                            var list_added = document.createElement("li");
                            list_added.appendChild(book_title);
                            link.appendChild(list_added);
                            view.appendChild(link);
                            view.style.display = "block";
                        }
                    } else {
                        view.innerHTML = "No results found.";
                        view.style.display = "block";
                    }
                } else {
                    console.error('Failed to fetch data.');
                }
            }
        };

        xhr.open('GET', '/search_books/?query=' + encodeURIComponent(input), true);
        xhr.send();
    } else {
        view.style.display = "none";
    }
}