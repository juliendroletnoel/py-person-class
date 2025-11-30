class Person(object):

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

        Person.people[name] = self


def create_person_list(people: list) -> list:

    persons = []

    for person in people:
        if person["name"] not in Person.people:
            new_person = Person(person["name"], person["age"])

            if person.get("wife") and person["wife"] in Person.people:
                new_person.wife = Person.people[person["wife"]]

            elif person.get("husband") and person["husband"] in Person.people:
                new_person.husband = Person.people[person["husband"]]

            persons.append(new_person)
            
    return persons