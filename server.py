from flask import Flask, request

# create new server
app = Flask(__name__)

next_id = 5
contacts = [
    {"id":"1", "name":"John", "phone":"253-546-492"},
    {"id":"2", "name":"Jane", "phone":"852-526-472"},
    {"id":"3", "name":"Tom", "phone":"852-896-457"},
    {"id":"4", "name":"Bob", "phone":"852-159-482"},
]

# list all contacts
@app.get("/contacts")
def list_contacts():
    return contacts

# list single contact
@app.get("/contacts/<id>")
def read_single_contact(id):
    for contact in contacts:
        if contact["id"] == id:
            return contact
        
    return "Contact does not exist."

# add a new contact
@app.post("/contacts")
def create_contact():
    global next_id

    new_contact = {
        "id": f'{next_id}',
        "name": request.json["name"],
        "phone": request.json["phone"]
    }

    contacts.append(new_contact)

    next_id += 1

    return new_contact

# update contacts
@app.put("/contacts/<id>")
def update_contact(id):
    for contact in contacts:
        if contact["id"] == id:
            contact["name"] = request.json["name"] if "name" in request.json else contact["name"]
            contact["phone"] = request.json["phone"] if "phone" in request.json else contact["phone"]
            return contact
    
    return "Contact not found"

# delete contact
@app.delete("/contacts/<id>")
def delete_contact(id):
    for contact in contacts:
        if contact["id"] == id:
            contacts.remove(contact)
            return contact
    
    return "No contact to delete"

if __name__ == "__main__":
    app.run(debug=True)