from datetime import datetime
from flask import Flask
from flask import jsonify
from flask import request

Entries = []

app = Flask(__name__)

@app.route('/mydiary/api/v1/entries',methods = ['GET'])
def get_items():
    response = jsonify({'All Entries':Entries})
    return response
# This function creates a new entry in the diary
@app.route('/mydiary/api/v1/entries',methods = ['POST'])
def create_entry():
    request_data = request.get_json()
    if len(Entries) == 0:
        id = 1
    else:
        id = Entries[-1]['id'] + 1  
    new_entry = {
    'id': id,
    'date':datetime.now().strftime ("%d-%m-%Y"),
    'title':request_data['title'],
    'content':request_data['content']
    }

    Entries.append(new_entry)
    return (jsonify(new_entry)),201


    
if __name__ == "__main__":
    app.run(debug=True)    