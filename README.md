# MapAnnot

... is a tool to annotate results of an Entity Linking process, based on Flask and Folium libraries

The following instructions will consecutively :
- import the dependancies
- generate the map HTML file from the inputs
- run the app.py script to start the Flask server

```python
pip install folium flask ;
python map_with_annotation.py ;
python app.py
```

## Inputs
The input is a list of tags coming from your Entity Linking pipeline, as JSON (here produced during experiment `test_france`):
```python
[
    {
      "experiment_id": 'test_france', # identifier of the experiment that produced that tag
      "related_to": '1/1066/Afrique', # hash of the mention
      "rank": 0,
      "pred_id": "Q3390498",
      "pred_coords": [48.8458, 2.37243],
      "acc@10": False,
    },
    ...
]
```

## OUtputs
The annotations, along with the hash value and the state of each checkbox (correct, wrong, abberant), are sent to the Flask server upon form submission. The server saves the collected data in a JSON file (annotations.json) in the following format:
```json
{
   "8/252/HAMIZ-MUTAGARA": # hash of the mention
      {  
         "annotation": "Q818608", # annotation text provided by the user
         "correct": null, # 1st tickbox option
         "wrong": "True", # 2nd 
         "abberant": null, # 3rd
         "note": "micro" # note provided by the user
      }
}
```
**TODO**
- [X] inserting `def retrieve_info(QID)` collecting label and description from WD
- [X] display top 10 suggestions at the end
- [ ] `def retrieve_info(QID)` from SOLR 
- [ ] add metadatas to annotation file : as input of app.py ? 



![Alt text](images/example.png)