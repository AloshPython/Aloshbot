import requests,time
from user_agent import generate_user_agent
user_agent=generate_user_agent()
import random
from bs4 import BeautifulSoup



while True:	
	def make_email_fake():
		response=requests.get('https://10minutemail.net/address.api.php')
		cook= response.json()['mail_get_mail'],response.cookies['PHPSESSID']
		email=response.json()['mail_get_mail']
		cookies=cook[0]+':'+cook[1]
		open("session.txt","w+").write(str(cookies)+'\n')
		return (email) 
		
	
	def get_code():
	    
	    try:
		    sessionn = open("session.txt", "r").readline().split('\n')[0]
		    gg=sessionn.split(":")[1]    
		    response = requests.get("https://10minutemail.net/address.api.php",cookies={"PHPSESSID":gg})
		    k =response.json()['mail_list'][0]['subject']
		    code=k.split(" is")[0]      
		    return code
	    except:
	    	return  k
	    	
	    	
	
	    	
	
	
	prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
	kk=prox.split()
	co=random.choices(kk)
	
	
	
	client_id='ZSRYOQABAAFuIBvDe0OhhJi7jqYu'
	email=make_email_fake()
	print("Done Get Email : "+email)
	print('\n')
	print('Done Get Proxy: '+str(co[0]))
	print('\n')
	name='alosh'
	user=email.split('@')[0]
	pas='ali@0968241@'
	
	proxy={'http': 'socks4://'+co[0]}
	Session=requests.Session()
	
	csrf=Session.get('https://www.instagram.com/api/v1/web/accounts/fb_profile/?hl=ar',proxies=proxy).cookies['csrftoken']
	
	
	
	Session.headers.update({'x-csrftoken':str(csrf),
	'content-type': 'application/x-www-form-urlencoded',
	'accept': '*/*',
	'user-agent': str(user_agent)})
	cookie=(requests.get('https://www.instagram.com/api/v1/web/accounts/fb_profile/?hl=en').cookies.get_dict())
	Session.cookies.update(cookie)
	
	
	req_1=Session.post(
	'https://www.instagram.com/api/v1/web/accounts/web_create_ajax/attempt/',
	
	data='enc_password='+'#PWD_INSTAGRAM_BROWSER:0:9775445428:'+str(pas)+'&email='+email+'&first_name='+name+'&username='+user+'&client_id='+str(client_id)+'&seamless_login_enabled=1&opt_into_one_tap=false',proxies=proxy).text
	print(req_1)
	print('\n\n')
	
	req_2=Session.post('https://www.instagram.com/api/v1/web/consent/check_age_eligibility/',data='day=26&month=8&year=2006',proxies=proxy).text
	
	print(req_2)
	print('\n\n')
	
	
	req_3=Session.post('https://www.instagram.com/api/v1/accounts/send_verify_email/',data='device_id='+str(client_id)+'&email='+email,proxies=proxy).text
	print(req_3)
	print('\n\n')
	time.sleep(20)
	if 'Hi, Welcome to 10 Minute Mail' == get_code():	
		
			time.sleep(1)
			code=(get_code())
			
	
	else:
		#print(get_code())
		code=get_code()
		
	print(code)
	
	
	req_4=Session.post('https://www.instagram.com/api/v1/accounts/check_confirmation_code/',data='code='+code+'&device_id='+str(client_id)+'&email='+email,proxies=proxy)
	
	print(req_4.json())
	print('\n\n')
	code_con=req_4.json()['signup_code']
	
	req_5=Session.post('https://www.instagram.com/api/v1/web/accounts/web_create_ajax/',
	data={
	'enc_password':'#PWD_INSTAGRAM_BROWSER:0:9775445428:'+str(pas),
	
	'day':'26',
	
	'email':email,
	
	'first_name':name,
	
	'month':'8',
	
	'username':user,
	
	'year':'2006',
	
	'client_id':client_id,
	
	'seamless_login_enabled':'1',
	
	'tos_version':'row',
	
	'force_sign_up_code':code_con
	
	},proxies=proxy,)
	print(req_5.text)

	#user='horo_3'
	try:
	        URL = "https://www.instagram.com/{}/"
	        r = requests.get(URL.format(user))
	        s = BeautifulSoup(r.text, "html.parser")
	        meta = s.find("meta", property ="og:description")
	    
	        done=(meta.attrs['content'])
	            
	        print("Info: "+done)
	        if 'Posts' in done:
	            F = '\033[2;32m' #اخضر
	            print(F+f' Done Create | Response : '+user)
	except:print("Ban, Acc")
	print('°'*40)
	print('\n\n\n\n\n\n')     
	
