from flask import Flask,jsonify

Entries = []

app = Flask(__name__)

@app.route('/mydiary/api/v1/entries',methods = ['GET'])
def get_items():
    response = jsonify({'All Entries':Entries})
    return response




    
if __name__ == "__main__":
    app.run(debug=True)    