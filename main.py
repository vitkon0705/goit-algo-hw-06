from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, value: str):
        super().__init__(value)
        if len(str(self.value)) < 1 or not self.value[0].isupper():
            raise ValueError(
                f"Name {value} is wrong! Name must contain at least 2 symbols and start with big letter")

class Phone(Field):
    def __init__(self, value: str):
        super().__init__(value)
        if len(self.value) != 10 or not self.value.isdigit():
            raise ValueError(
                f"Number {value} is wrong! Phone number must contain only digits and only 10")

class Record:
    def __init__(self, name_str: str):
        try:
            name = Name(name_str)
            if name:
                self.name = name
                self.phones = []
        except ValueError as e:
            print(e)

    def __str__(self):
        phone_numbers = []
        for phone in self.phones:
            phone_numbers.append(phone.value)
        return f"Contact name: {self.name.value}, phones: {', '.join(phone_numbers)}"

    def add_phone(self, phone_str: str):
        try:
            new_phone = Phone(phone_str)
            if new_phone and len(self.phones) == 0:
                self.phones.append(new_phone)
            elif new_phone:
                phones_str = []
                for phone_obj in self.phones:
                    phones_str.append(phone_obj.value)
                if phone_str in phones_str:
                    return
                else:
                    self.phones.append(new_phone)
        except ValueError as e:
            print(e)

    def find_phone(self, phone_str: str):
        phone_obj = Phone(phone_str)
        for elem in self.phones:
            if elem.value == phone_str:
                return phone_obj
        return None

    def remove_phone(self, phone_str: str):
        phone_obj = Phone(phone_str)
        if phone_obj:
            for elem in self.phones:
                if elem.value == phone_str:
                    self.phones.remove(elem)

    def edit_phone(self, phone_old_str: str, phone_new_str: str):
        phone_old_obj = Phone(phone_old_str)
        phone_new_obj = Phone(phone_new_str)
        if phone_old_obj and phone_new_obj:
            for elem in self.phones:
                if elem.value == phone_old_str:
                    index = self.phones.index(elem)
                    self.phones.remove(elem)
                    self.phones.insert(index, phone_new_obj)

class PhonesBook(UserDict):
    def __str__(self):
        content = ""
        for value in self.data.values():
            content += f"{value};\n"
        return content.strip()

    def add_record(self, record: Record):
        self.data[record.name.value] = record

    def find_record(self, name_str: str):
        if name_str in self.data:
            return self.data[name_str]
        return None

    def delete_record(self, name_str: str):
        if name_str in self.data:
            del self.data[name_str]

phones_book = PhonesBook()
john_record = Record("John")
#print(john_record)
john_record.add_phone("1234567890")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")
john_record.add_phone("5555555555")
john_record.add_phone("1234567890")
#print(john_record)
phones_book.add_record(john_record)

jane_record = Record("Jane")
jane_record.add_phone("9876543210")
phones_book.add_record(jane_record)
#print(address_book)

found_record = phones_book.find_record("John")
#print(found_record)
#address_book.delete_record("John")
#print(address_book)
found_phone = found_record.find_phone("1234567890")
#found_record.remove_phone("1234567890")
#print(f"{found_record.name}: {found_phone}")
found_record.edit_phone("1234567898", "1234567899")
print(phones_book)