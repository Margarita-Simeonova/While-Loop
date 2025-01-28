def old_library(searched_book):
    books_counter = 0
    present_book = input()

    while not present_book == "No More Books":
        if present_book == searched_book:
            return f"You checked {books_counter} books and found it."

        books_counter += 1
        present_book = input()

    return f"The book you search is not here!\nYou checked {books_counter} books."


searched_book_arg = input()
result = old_library(searched_book_arg)
print(result)
