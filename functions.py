import re
import requests

def get_apikey_devenv():
    my_id = ''
    key_token = ''
    try:
        with open('./../OMDbAPIKey.txt') as f:
            for item in re.finditer("(\w*)\n?", f.read()):
                if my_id == '':
                    my_id = item.group(1)
                elif key_token == '':
                    key_token = item.group(1)
        f.close()
        return my_id, key_token
    except:
        pass

def request_movie(my_id, key_token, search):
    try:
        url = "http://www.omdbapi.com/?i=" + my_id + "&apikey=" + key_token + "&s=" + search
        response = requests.get(url)
        response.raise_for_status()
        result = response.json()['Search'][0]['Title']

        return result
    except requests.exceptions.HTTPError as error:
        print(error)
        print('Possible error; get a valid API KEY in https://www.omdbapi.com/apikey.aspx')
