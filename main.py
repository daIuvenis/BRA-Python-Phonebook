# {("first_name", "last_name"): ("phone_number", "sity", "state")  }
phonebook = {}


class Phonebook:
    def __init__(self):
        self.phonebook = {}

    def add_entry(self, first_name, last_name, phone_number, city, state):  # Nazar
        if not all([first_name, last_name, phone_number, city, state]):
            raise ValueError("All fields are required")

        first_name = first_name.strip()
        last_name = last_name.strip()
        phone_number = phone_number.strip()
        city = city.strip()
        state = state.strip()

        key = (first_name, last_name)

        if key in self.phonebook:
            raise ValueError(f"Entry for {first_name} {last_name} already exists")

        self.phonebook[key] = (phone_number, city, state)
        return True

    def search_by_first_name(self):  # Артем Ніколаєв
        print("Search by first name - stub")

    def search_by_last_name(self, l_name):  # Андрій
        if not l_name or not l_name.strip():
            return []
        results = []

        l_name = l_name.strip()

        for (first_name, last_name), (phone_number, city, state) in self.phonebook.items():
            if last_name.lower() == l_name.lower():
                results.append((first_name, last_name, phone_number, city, state))

        return results

    def search_by_full_name(self):  # Віталіна
        print("Search by full name - stub")

    def search_by_phone_number(self):  # Михайло
        print("Search by telephone number - stub")

    def search_by_city_or_state(self):  # Ростислав
        print("Search by city or state - stub")

    def delete_by_phone_number(self):  # Дмитро
        print("Delete a record by telephone number - stub")

    def update_by_phone_number(self, phone_number, new_person):  # Юлія
        print("Update a record by telephone number - stub")

    def exit_program(self):
        print("Exiting program.")
        return False

    def application_loop(self):
        is_working = True
        while is_working:
            print("""\nPhonebook Menu:
    1) Add new entries 
    2) Search by first name 
    3) Search by last name 
    4) Search by full name
    5) Search by telephone number
    6) Search by city or state
    7) Delete a record for a given telephone number
    8) Update a record for a given telephone number
    9) Exit the program""")
            try:
                choice = int(input('Your choice: '))
            except ValueError:
                print("Please enter a valid number from 1 to 9.")
                continue

            match choice:
                case 1:
                    self.add_entry()
                case 2:
                    self.search_by_first_name()
                case 3:
                    self.search_by_last_name()
                case 4:
                    self.search_by_full_name()
                case 5:
                    self.search_by_phone_number()
                case 6:
                    self.search_by_city_or_state()
                case 7:
                    self.delete_by_phone_number()
                case 8:
                    self.update_by_phone_number()
                case 9:
                    is_working = self.exit_program()
                case _:
                    print("Invalid choice. Please select a number from 1 to 9.")


def main():
    phone_book = Phonebook()
    print(phone_book.search_by_last_name("last_name"))


main()
