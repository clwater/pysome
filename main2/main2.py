import requests
import re
import hashlib


def getNextUrl(text):
    # print text
    next = re.findall('right.*?</p>' , text)
    next = next[0]
    next = next.replace(' ' , '')
    # print 'next:  ' + next
    nexturl = re.findall('href=.*?>' , next)
    nexturl = nexturl[0]
    nexturl = nexturl.replace('href="' , '')
    nexturl = nexturl.replace('">' , '')
    return nexturl


def saveImg(text , name = '/2017/09/27'):
    # print text
    if "<p><img" in text:
        print 'p'
        imageurl = re.findall('<p><img.*?</p>' , text)
        imageurl = imageurl[0]
        print imageurl
        imageurl = imageurl.replace(' ' , '')
        if 'imgalt' in imageurl:
            imageurl = imageurl.replace('<p><imgalt=""src="' , '')
        else:
            imageurl = imageurl.replace('<p><imgsrc="', '')
        imageurl = imageurl.replace('"/></p>' , '')
        print  'imageurl: ' + imageurl
    elif '<h3><img' in text:
        print 'h3'
        imageurl = re.findall('<h3><img.*?</h3>', text)
        imageurl = imageurl[0]
        imageurl = imageurl.replace(' ', '')
        imageurl = imageurl.replace('<h3><imgalt=""src="', '')
        imageurl = imageurl.replace('"/></h3>', '')
        print  'imageurl: ' + imageurl
    elif '<h2><img' in text:
        print 'h2'
        imageurl = re.findall('<h2><img.*?</h2>', text)
        imageurl = imageurl[0]
        imageurl = imageurl.replace(' ', '')
        imageurl = imageurl.replace('<h2><imgalt=""src="', '')
        imageurl = imageurl.replace('"/></h2>', '')
        print  'imageurl: ' + imageurl
    elif '<h1><img' in text:
        print 'h1'
        imageurl = re.findall('<h1><img.*?</h1>', text)
        imageurl = imageurl[0]
        print imageurl
        imageurl = re.findall('http.*?jpg' , imageurl)
        imageurl = imageurl[0]

        print  'imageurl:  '  + imageurl
    elif '<h1 style="margin:' in text:
        try:
            print 'other11'
            imageurl = re.findall('<h1 style=".*?</h1>', text)
            imageurl = imageurl[0]
            imageurl = imageurl.replace(' ', '')
            imageurl = re.findall('<imgsrc=".*?.jpg' , imageurl)
            imageurl = imageurl[0]


            imageurl = imageurl.replace('<imgsrc="', '')
            print  'imageurl:  ' + imageurl
        except Exception:
            print 'other11'
            imageurl = re.findall('<h1 style=".*?</h1>', text)
            imageurl = imageurl[1]
            imageurl = imageurl.replace(' ', '')
            imageurl = re.findall('<imgsrc=".*?.jpg', imageurl)
            imageurl = imageurl[0]

            imageurl = imageurl.replace('<imgsrc="', '')
            print  'imageurl:  ' + imageurl
    # print 'name:' + name

    imageurl = re.findall('http.*?jpg' ,imageurl)
    imageurl = imageurl[0]
    print 'new imageurl:' + imageurl
    imagename = name.replace('/' , '')
    imagename =  imagename + '.jpg'
    # print imagename



    filename = 'images/' + imagename
    try:
        r = requests.get(imageurl)
        with open(filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024):
                f.write(chunk)
    except :
        print(str (imagename) + 'Exception: ' + Exception.message)



def getText(nexturl = ''):
    weburl = 'http://gank.io' + nexturl
    print weburl
    text = requests.get(weburl).text

    text = text.replace('\t' , '')
    text = text.replace('\r' , '')
    text = text.replace('\n' , '')
    # text.replace(' ' , '')


    try:
        saveImg(text , nexturl)
    except:
        pass


    nexturl = getNextUrl(text)
    print nexturl
    getText(nexturl)





getText('/2017/05/22')
# getText('/2015/08/14')