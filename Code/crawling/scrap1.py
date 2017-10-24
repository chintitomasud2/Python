import requests

myheaders={'user-agent':'Iphone 7'}

url="http://www.uiu.ac.bd/"
#r=requests.get('http://httpbin.org/headers',headers=myheaders)
r=requests.get(url,headers=myheaders)

#..................Post..........................

#r=requests.post('http://httpbin.org/post',data={'name':'masud'})

print(r.text)

print("Status Code")
print('\t[-]'+str(r.status_code)+'\n')

print("Server Headers")
print("***************************************");

for x in r.headers:
    print("\t "+x+':'+r.headers[x])

print("*****************************************")

print("Content")
#print(r.text)
print("""""""""""""""""""""""""""""""""""""""""""")