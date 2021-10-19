import requests
from time import sleep

print('''
------------------------------------------
		Dictionary web  👣
		+ The developer : Salman - IYoPJ +
		
		insta : IYoPJJ € 

------------------------------------------
''')




dictionary = open('dicn.txt', 'r')
url = input('URL ---> ')
for x in dictionary:
	r=requests.get(url + '/' + x.rstrip('/n'))
	if r.status_code == 200:
		print(url + '/' + x + '[----------------Good-----------------]')
		
	else:
		print(url + '/'+ x +  '[----------------Not-------------------]')
		
		
		
ff = open('Good.txt', 'w')
ff.write(r)
ff.cloce()
		

