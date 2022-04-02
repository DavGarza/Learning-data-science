DATA = [
    {
        "name": "miles",
        "age": 34,
        "gender": "male",
        "country": "peru",
        "profession": "Lawyer",
        "height": 170,
    },
    {
        "name": "martha",
        "age": 49,
        "gender": "female",
        "country": "canada",
        "profession": "Medic",
        "height": 169,
    },
    {
        "name": "lorena",
        "age": 25,
        "gender": "female",
        "country": "usa",
        "profession": "engeneer",
        "height": 166,
    },
    {
        "name": "michael",
        "age": 65,
        "gender": "male",
        "country": "canada",
        "profession": "lawyer",
        "height": 188,
    },
    {
        "name": "mary",
        "age": 18,
        "gender": "female",
        "country": "usa",
        "profession": "medic",
        "height": 177,
    }
]

def main():

    # a high order function using map that tells you if the person is a female
    male_or_female = list(map(lambda i: i ["gender"] == "female", DATA))
    print(male_or_female)

    # a high order function using filter and map to show the name of the person younger than 40
    young = list(filter(lambda i: i["age"] < 40, DATA))
    young = list(map(lambda i: i["name"], young))
    print(young)

    # prints the name of the persons older than 18
    adults = [i ["name"] for i in DATA if i ["age"] > 17]
    print(adults)

if __name__ == "__main__":
    main()