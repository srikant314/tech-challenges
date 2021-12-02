from fetch_mdata import fetch_mdata

def fetch_key(key):
    mdata = fetch_mdata()
    return list(get_extract(key, mdata))


def get_extract(key, var):
    if hasattr(var, 'items'):
        for k, v in var.items():
            if k == key:
                yield v
            if isinstance(v, dict):
                for result in get_extract(key, v):
                    yield result
            elif isinstance(v, list):
                for d in v:
                    for result in get_extract(key, d):
                        yield result

if __name__ == '__main__':
    key = input("Please enter the key for which value needs to be extracted\n")
    print(fetch_key(key))
