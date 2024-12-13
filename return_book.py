import json

def load_books():
    try:
        with open("lend_books.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_books(lend_book_data):
    with open("lend_books.json", "w") as file:
        json.dump(lend_book_data, file, indent=4)

def return_book(all_books):
    lend_book_data = load_books()
    book_title = input("Enter the title of the book to return: ")
    borrower_name = input("Enter the borrower's name: ")

    for record in lend_book_data:
        if record["book_title"].lower() == book_title.lower() and record["borrower_name"].lower() == borrower_name.lower():
            lend_book_data.remove(record)
            
            for book in all_books:
                if book["title"].lower() == book_title.lower():
                    book["quantity"] += 1
                    break

            save_books(lend_book_data)
            print(f"Book '{book_title}' returned successfully by {borrower_name}.")
            return all_books

    print("No matching lending record found.")
    return all_books


