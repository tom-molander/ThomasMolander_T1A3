import csv
from functions import add_contact
from colored import fg, attr, bg


test_file_name = "test_contacts_library.csv"


def test_add(monkeypatch):
   original_length = 0
   with open(test_file_name) as f:
       reader = csv.reader(f)
       original_length = sum(1 for row in reader)
   monkeypatch.setattr('builtins.input', lambda _: "Test Add Contact")
   add_contact(test_file_name)
   with open(test_file_name) as f:
       reader = csv.reader(f)
       new_length = sum(1 for row in reader)
   print(original_length)
   print(new_length)
   assert new_length == original_length + 1