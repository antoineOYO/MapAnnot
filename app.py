from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/save_annotation', methods=['POST'])
def save_annotation():
    annotation = request.form['text']
    hash_value = request.form['hash']
    correct = 'True' if 'correct' in request.form else None
    wrong = 'False' if 'wrong' in request.form else None
    abberant = 'abberant' if 'abberant' in request.form else None
    
    data = {
        'annotation': annotation,
        'correct': correct,
        'wrong': wrong,
        'abberant': abberant
    }
    # first check if the file exists
    try:
        with open('annotations.json', 'r') as f:
            previous_annotations = json.load(f)
            if previous_annotations.get(hash_value) is None:
                previous_annotations[hash_value] = data
            else :   
                previous_annotations[hash_value].update(data)
            with open('annotations.json', 'w') as f:
                json.dump(previous_annotations, f, indent=3)
    except FileNotFoundError:
        # create the file if it doesn't exist
        previous_annotations = {hash_value: data}
        with open('annotations.json', 'w') as f:
            json.dump(previous_annotations, f, indent=3)
    return 'Annotation sauvegardée !'

if __name__ == '__main__':
    app.run(debug=True)
