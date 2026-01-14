import pytest
from scripts.db_handler import DBHandler

def test_verify_initial_book_in_db():
    db = DBHandler()

    book_title = "The Lean Startup"
    result = db.get_book_by_title(book_title)

    assert result is not None, f"The book '{book_title} was not found in the DB"
    assert result["author"] == "Eric Ries", "The author does not match"

    print(f"\n Verification successful : The book '{result['title']}'by {result['author']} was found")

    db.close()