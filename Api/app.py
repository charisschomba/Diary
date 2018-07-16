from datetime import datetime
from flask import Flask
from flask import jsonify
from flask import request

Entries = []

app = Flask(__name__)

@app.route('/mydiary/api/v1/entries', methods=['GET'])
def get_all_entries():
    """
    Method: GET
    Get all entries
    URL path: mydiary/api/v1/entries/
    """
    response = jsonify({'All Entries':Entries})
    return response

@app.route('/mydiary/api/v1/entries', methods=['POST'])
def create_entry():
    """
    Method: POST
    Create an Entry
    URL path: mydiary/api/v1/entries/
    """
    request_data = request.get_json()
    if len(Entries) == 0:
        id_ = 1
    else:
        id_ = Entries[-1]['id'] + 1  
    if request_data['title'] == '' or request_data['content'] == '':
        return jsonify({'Message':'title or content cannot be empty'}), 400
    else:
        try:    
            new_entry = {
                'id': id_,
                'date':datetime.now().strftime("%d-%m-%Y"),
                'title':request_data['title'],
                'content':request_data['content']
            }
            Entries.append(new_entry)
        except:
            return jsonify({'Message':'An error occured while processing your request'}), 500
    return (jsonify(new_entry)), 201
 
@app.route("/mydiary/api/v1/entries/<int:entryId>",methods=['GET'])
def get_entry_by_id(entryId):
    """
    Method: GET
    Fetches a single entry by it's Id
    URL path: mydiary/api/v1/entries/<int:entryId>
    """
    for entry in Entries:
        if entry['id'] == entryId:
            return jsonify(entry),200
    return jsonify({'Message':"Entry requested does not exist"}), 404  

@app.route("/mydiary/api/v1/entries/<int:entryId>",methods=['PUT'])
def modify_entry_by_id(entryId):
    """
    Method: PUT
    Modifies an entry by it's Id
    URL path: mydiary/api/v1/entries/<int:entryId>
    """
    entry = next(filter(lambda x: x['id'] == entryId, Entries), None)
    if entry is None:
        return jsonify({'message':"Entry does not exixt"}), 404
    else:
        request_data = request.get_json()
        entry.update(request_data)
    return jsonify(entry),200

if __name__ == "__main__":
    app.run(debug=True)    