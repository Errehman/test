from flask import Flask, jsonify
from faker import Faker
fake = Faker()
app = Flask(__name__)

@app.route("/fakedata", methods=['GET'])
def fakedata():
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

    return jsonify(data_list)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)