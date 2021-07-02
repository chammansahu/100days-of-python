persons=[
    {
        "name": "chaman sahu",
        "age": 29,
        "hobbis": ["coding", "listenig song", "cycling", "playing game", "fucking"],
        "email":{"gmail": "chammansahu@gmail.com", "outlook": "chammansahu@outlook.com"}
    },
    {
        "name": "Laxmi Dhiwar",
        "age": 25,
        "hobbis": ["coding", "listenig song", "cycling", "playing game", "fucking"],
        "email":{"gmail": "Laxmidhiwar@gmail.com", "outlook": "laxmidhiwar@outlook.com"}
    },
    {
        "name": "john doe",
        "age": 24,
        "hobbis": ["coding", "listenig song", "cycling", "playing game", "fucking"],
        "email":{"gmail": "johndoe@gmail.com", "outlook": "johndoe@outlook.com"}
    }
];


name=input("Enter Name")
age=input("Enter Age")

newPerson={
    "name":name,
    "age":age,
    "hobbis": ["coding", "listenig song", "cycling", "playing game", "fucking"],
    "email": {"gmail": "chammansahu@gmail.com", "outlook": "chammansahu@outlook.com"}
}

persons.append(newPerson)

print(persons)
