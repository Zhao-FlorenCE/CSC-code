import requests
import json

key1 = '?key=ff483156213750afe2229dc8f75bc9a4'
key2 = '?key=ff483156213750afe2229dc8f75bc9a4&num=10'

def main():
    print('Daily News:')
    resp1 = requests.get('http://api.tianapi.com/bulletin/index' \
                         + key1)
    data_model1 = json.loads(resp1.text)
    i = 1
    for news in data_model1['newslist']:
        print('%d.%s (%s)' % (i, news['title'], news['mtime']))
        i += 1
        print('  ', news['digest'])
    print()
    print('Scientific Sailing:')
    resp2 = requests.get('http://api.tianapi.com/sicprobe/index' \
                         + key2)
    data_model2 = json.loads(resp2.text)
    j = 1
    for news in data_model2['newslist']:
        print('%d.%s (%s)' % (i, news['title'], news['ctime']))
        j += 1
        print('  ', news['description'])
        print('(source: %s, url: %s)' % \
             (news['source'], news['url']))


if __name__ == '__main__':
    main()