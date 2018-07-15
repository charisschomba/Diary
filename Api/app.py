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
 
if __name__ == "__main__":
    app.run(debug=True)    