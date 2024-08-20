from flask import Flask, request
import json
import sys

app = Flask(__name__)

# Ensure the annotation_id is provided as a command-line argument
if len(sys.argv) < 2:
    print("Usage: python app.py <annotation_id>")
    sys.exit(1)

# Annotation campaign identifier
annotation_id = sys.argv[1]

@app.route('/save_annotation', methods=['POST'])
def save_annotation():
    annotation = request.form['annotation']
    hash_value = request.form['hash']
    note = request.form['note']
    #choice = request.form['choice']
    correct = 'True' if 'correct' in request.form else None
    wrong = 'True' if 'wrong' in request.form else None
    abberant = 'abberant' if 'abberant' in request.form else None
    
    data = {
        'annotation': annotation,
        'correct': correct,
        'wrong': wrong,
        'abberant': abberant,
        'note': note,
        'annotation_id': annotation_id
    }
    # first check if the file JSONL exists
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