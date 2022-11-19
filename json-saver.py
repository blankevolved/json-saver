import json
import os


def save_to_file(filepath, key, val):
    ## check if save.json dosent exist, if it dosent create it.
    if os.path.exists(filepath) == False:
        with open(filepath, 'w+') as json_file:
            json_file.write('{}')
            json_file.close()
    
    ## load the json file with the json module and store it in loaded_json
    with open(filepath, 'r') as json_file:
        loaded_json = json.load(json_file)
        json_file.close()
    
    ## write to the save file
    with open(filepath, 'w+') as json_file:
        loaded_json[key] = val

        json_file.seek(0)
        json.dump(loaded_json, json_file, indent=4)
        json_file.truncate()

        json_file.close()

def load_from_file(filepath):
    ## check if save.json exists
    if os.path.exists(filepath) == True:
        with open(filepath, 'r') as json_file:
            ## load file as a json
            loaded_json = json.load(json_file)
            json_file.close()
            ## return data
            return loaded_json
