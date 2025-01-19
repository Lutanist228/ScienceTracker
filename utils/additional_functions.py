import json
from typing import Optional, Union
from dotenv import load_dotenv
import os

load_dotenv()

def json_reader(path: str):
    '''Чтение json-файла и возврат значения'''
    with open(path, 'r', encoding="utf-8") as j_file:
        return json.load(j_file)

def json_writer(j_dict: dict, path: str):
    '''Запись json-файла'''
    with open(path, 'w', encoding="utf-8") as j_file:
        return json.dump(j_dict, j_file, indent=4)

def retrieve_udata(inputted_information: Union[str, list], json_doc: dict) -> str:
    found_user = False
    iter_num = 0
    roles = list(json_doc.keys())
    
    while found_user is False:
        try:
            urole = roles[iter_num]
        except IndexError:
            break
        
        for user in json_doc[urole]:
            if inputted_information in user.values():
                found_user = True
                break 
    
        iter_num += 1
    
    if found_user == True:     
        return urole, user
    else: 
        return None, None

def set_json_value(json_doc: dict, key_value: str, **kwargs): 
    for role in json_doc:
        for user in json_doc[role]:
            if key_value in user.values():
                for key, value in kwargs.items():
                    user[key] = str(value)
                    
    json_writer(j_dict=json_doc, path=os.environ.get("USERS_PATH"))
    
    


    
