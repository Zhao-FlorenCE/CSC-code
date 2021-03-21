import requests
import json
import datetime

key1 = '?key=ff483156213750afe2229dc8f75bc9a4'
key2 = '?key=ff483156213750afe2229dc8f75bc9a4&num=10'

def main():
    time = str(datetime.date.today())
    text = open('C:/Users/FlorenCE/Desktop/News py/' \
                + time + '.txt', 'w', encoding='utf-8')
    text.write('Daily News:' + '\n')
    resp1 = requests.get('http://api.tianapi.com/bulletin/index' \
                         + key1)
    data_model1 = json.loads(resp1.text)
    i = 1
    for news in data_model1['newslist']:
        text.write(str(i) + '.' + news['title'] + ' (' + \
                   news['mtime'] + ')\n')
        text.write('  ' + news['digest'] + '\n' + '\n')
        i += 1
    text.write('\n' + 'Scientific Sailing:' + '\n')
    resp2 = requests.get('http://api.tianapi.com/sicprobe/index' \
                         + key2)
    data_model2 = json.loads(resp2.text)
    j = 1
    for news in data_model2['newslist']:
        text.write(str(j) + '.' + news['title'] + ' (' + \
                   news['ctime'] + ')\n')
        text.write('  ' + news['description'] + '\n')
        text.write('Source: ' + news['source'] + '\n')
        text.write('Url: ' + news['url'] + '\n' + '\n')
        j += 1
    text.close()

if __name__ == '__main__':
    main()