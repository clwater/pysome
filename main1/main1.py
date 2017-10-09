import requests


with open('date', 'r') as f:
    items = f.read()

items = items.split(',')

for item in items:
    print item
    imagesrc = 'http://www.gstatic.com/prettyearth/assets/full/' + item + '.jpg'
    filename = 'images/' + item + ".jpg"
    try:
        r = requests.get(imagesrc)
        with open(filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024):
                f.write(chunk)
    except Exception:
        print(filename + 'Exception: ' + Exception.message)
