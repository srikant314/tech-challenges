import requests
import json

url = 'http://169.254.169.254/latest/'

def convert_mdata_to_json():
    mdata = fetch_mdata()
    mdata_json = json.dumps(mdata, indent=4, sort_keys=True)
    return mdata_json

def fetch_mdata():
    first_entry = ["meta-data/"]
    output_data = flatten_data(url, first_entry)
    return output_data


def flatten_data(url, array):
    output = {}
    for item in array:
        changed_url = url + item
        request = requests.get(changed_url)
        request_text = request.text
        if item[-1] == "/":
            list_data = request.text.splitlines()
            output[item[:-1]] = flatten_data(changed_url, list_data)
        elif is_json(request_text):
            output[item] = json.loads(request_text)
        else:
            output[item] = request_text
    return output

def is_json(mdata_json):
    try:
        json.loads(mdata_json)
    except ValueError:
        return False
    return True

if __name__ == '__main__':
    print(convert_mdata_to_json())
