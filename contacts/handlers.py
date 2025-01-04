from .record import Record

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Enter a name and a valid phone number (10 digits)."
        except KeyError:
            return "Contact not found."
        except IndexError:
            return "Enter user name."
        except Exception as e:
            return f"Error: {e}"
    return inner

@input_error
def add_contact(args, book):
    name, phone = args
    record = book.find(name)
    
    if record is None:
        record = Record(name)
        book.add_record(record)
    record.add_phone(phone)
    return "Contact added."

@input_error
def change_contact(args, book):
    name, old_phone, new_phone = args
    record = book.find(name)
    if record is None:
        raise KeyError
    
    record.edit_phone(old_phone, new_phone)
    return "Contact updated."

@input_error
def show_phone(args, book):
    name = args[0]
    record = book.find(name)
    if record is None:
        raise KeyError
    return record

@input_error
def show_all(book):
    if not book.data:
        return "No contacts saved."
    return "\n".join(str(record) for record in book.data.values())

@input_error
def remove_phone(args, book):
    name, phone = args
    record = book.find(name)
    if record is None:
        raise KeyError
    record.remove_phone(phone)
    return "Phone removed."

@input_error
def delete_contact(args, book):
    name = args[0]
    if book.find(name) is None:
        raise KeyError
    book.delete(name)
    return "Contact deleted."
