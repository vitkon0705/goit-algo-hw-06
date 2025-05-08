from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    pass

class Phone(Field):
    def __init__(self, value: str):
        if Phone.is_number_correct(value):
            super().__init__(value)

    @staticmethod
    def is_number_correct(value: str):
        if len(value) != 10 or not value.isdigit():
            raise ValueError(
                f"Number {value} is wrong! Phone number must contain only digits and only ten ones")
        return True


class Record:
    def __init__(self, name_str: str):
        self.name = Name(name_str)
        self.phones = []

    def __str__(self):
        phone_numbers_str = []
        for phone_obj in self.phones:
            phone_numbers_str.append(phone_obj.value)
        return f"Contact name: {self.name.value}, phones: {', '.join(phone_numbers_str)}"

    def add_phone(self, phone_str: str):
        self.phones.append(Phone(phone_str))

    def find_phone(self, phone_str: str):
        for phone_obj in self.phones:
            if phone_obj.value == phone_str:
                return phone_obj
        return None

    def remove_phone(self, phone_str: str):
        found_phone_obj = self.find_phone(phone_str)
        self.phones.remove(found_phone_obj)

    def edit_phone(self, phone_old_str: str, phone_new_str: str):
        if Phone.is_number_correct(phone_old_str) and Phone.is_number_correct(phone_new_str):
            if not self.find_phone(phone_old_str):
                raise ValueError(
                    f"Phone number {phone_old_str} is not in the list!")
            else:
                self.remove_phone(phone_old_str)
                self.add_phone(phone_new_str)

class AddressBook(UserDict):
    def __str__(self):
        content = ""
        for value in self.data.values():
            content += f"{value};\n"
        return content.strip()

    def add_record(self, record: Record):
        self.data[record.name.value] = record

    def find(self, name_str: str):
        if name_str in self.data:
            return self.data[name_str]
        return None

    def delete(self, name_str: str):
        if name_str in self.data:
            del self.data[name_str]

book = AddressBook()
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")
book.add_record(john_record)

jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

found_record = book.find("John")
#print(found_record)
#book.delete("John")
#print(book)
#found_phone = found_record.find_phone("1234567890")
#found_record.remove_phone("1234567890")
#print(f"{found_record.name}: {found_phone}")
found_record.edit_phone("1234567890", "1234567899")
print(book)