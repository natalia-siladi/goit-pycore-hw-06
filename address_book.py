import re  
from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    def __init__(self, value):
        if not self.validate(value):
            raise ValueError("Ім'я повинно містити лише літери.")
        super().__init__(value)

    @staticmethod  
    def validate(value):
        return value.isalpha()


class Phone(Field):
    def __init__(self, value):
        if self.validate_phone(value):
            super().__init__(value)
        else:
            raise ValueError("Номер телефону має містити 10 цифр.")

    @staticmethod  
    def validate_phone(value):
        pattern = r'^\d{10}$'
        return bool(re.match(pattern, value))


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone_number):
        new_phone = Phone(phone_number)
        self.phones.append(new_phone)

    def remove_phone(self, phone_number):
        for phone in self.phones:
            if phone.value == phone_number:
                self.phones.remove(phone)
                return  
        print(f"Номер {phone_number} не знайдено.")

    def edit_phone(self, old_number, new_number):
        for phone in self.phones:
            if phone.value == old_number:
                phone.value = new_number  
                return  
        print(f"Номер {old_number} не знайдено.")

    def find_phone(self, phone_number):
        for phone in self.phones:
            if phone.value == phone_number:
                return f"Номер {phone_number} знайдено."
        return f"Номер {phone_number} не знайдено."

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record  
        print(f"Запис додано: {record.name.value} - {record}")

    def find(self, name):
        if name in self.data:
            return self.data[name]  # Return the Record object  
        else:
            return None  # Return None if not found

    def delete(self, name):
        if name in self.data:
            del self.data[name]
            print(f"Запис видалено: {name}")
        else:
            print("Запис не знайдено.")


# Main execution block  
if __name__ == "__main__":
    # Створення нової адресної книги  
    book = AddressBook()

    # Створення запису для John  
    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")

    # Додавання запису John до адресної книги  
    book.add_record(john_record)

    # Створення та додавання нового запису для Jane  
    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)

    # Виведення всіх записів у книзі  
    for name, record in book.data.items():
        print(record)

    # Знаходження та редагування телефону для John  
    john = book.find("John")
    if john:  # Check if john record exists  
        john.edit_phone("1234567890", "1112223333")
        print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

        # Пошук конкретного телефону у записі John  
        found_phone = john.find_phone("5555555555")
        print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

    # Видалення запису Jane  
    book.delete("Jane")