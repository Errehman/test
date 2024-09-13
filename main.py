from faker import Faker
fake = Faker()
data_list = []
for _ in range(10):
    fake_data = {
        'name': fake.name(),
        'address': fake.address(),
        'text': fake.text()
    }
    data_list.append(fake_data)
for index, data in enumerate(data_list, start=1):
    print(f"Entry {index}:")
    print(f"Name: {data['name']}")
    print(f"Address: {data['address']}")
    print(f"Text: {data['text']}\n")