import requests

strr = "ev`kvi KvˆQ m®Zvb ZzjÅ।cÊRvˆ`i mzL-`z:L wbR ˆPvˆL ˆ`Lvi RbÅ Q`Ä ˆeˆk Nzˆi "
url = ''
data = {"inputFont":"Lekhoni","outputFont":"UTF-8","inputText": strr}

r = requests.post(
    url, 
    json=data, 
)

result = r.json()
text = result.get('outputText')
print(text)

with open('output.txt', 'w') as f:
    f.write(text)
