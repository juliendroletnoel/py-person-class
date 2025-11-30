class Person(object):

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

        Person.people[name] = self


def create_person_list(people: list) -> list:

    persons = [Person(person["name"], person["age"]) for person in people]

    for person in people:
        if person.get("wife") and person["wife"] in Person.people:
            husband = Person.people[person["name"]]
            wife = person["wife"]
            husband.wife = Person.people[wife]

        elif person.get("husband") and person["husband"] in Person.people:
            wife = Person.people[person["name"]]
            husband = person["husband"]
            wife.husband = Person.people[husband]

    return persons
