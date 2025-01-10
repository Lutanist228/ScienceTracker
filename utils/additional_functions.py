import json
from typing import Optional, Union

def json_reader(path: str):
    '''Чтение json-файла и возврат значения'''
    with open(path, 'r', encoding="utf-8") as j_file:
        return json.load(j_file)

def retrieve_urole(inputted_information: Union[str, list], json_doc: dict) -> str:
    found_user = False
    iter_num = 0
    roles = list(json_doc.keys())
    
    while found_user is False:
        urole = roles[iter_num]
        
        for user in json_doc[urole]:
            if inputted_information in user.values():
                found_user = True
                break 
       
        iter_num += 1
       
    if found_user == True:     
        return urole
    else: 
        return None
    
