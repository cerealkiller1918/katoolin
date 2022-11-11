#!/usr/bin/python

import os,sys, traceback,time


if os.getuid() != 0:
	print ("Sorry. This script requires sudo privledges")
	sys.exit()
def main():
	try:
		titlePrint()
		time.sleep(1)
		start()
	except KeyboardInterrupt:
		leave()
	except Exception:
		traceback.print_exc(file=sys.stdout)
	sys.exit(0)

def titlePrint():

	print ('''

 $$\   $$\             $$\                         $$\ $$\           
 $$ | $$  |            $$ |                        $$ |\__|          
 $$ |$$  /  $$$$$$\  $$$$$$\    $$$$$$\   $$$$$$\  $$ |$$\ $$$$$$$\  
 $$$$$  /   \____$$\ \_$$  _|  $$  __$$\ $$  __$$\ $$ |$$ |$$  __$$\ 
 $$  $$<    $$$$$$$ |  \033[1;36mKali linux tools installer\033[1;m |$$ |$$ |$$ |  $$ |
 \033[1;36m$$ |\$$\  $$  __$$ |  $$ |$$\ $$ |  $$ |$$ |  $$ |$$ |$$ |$$ |  $$ |
 $$ | \$$\ \$$$$$$$ |  \$$$$  |\$$$$$$  |\$$$$$$  |$$ |$$ |$$ |  $$ |
 \__|  \__| \_______|   \____/  \______/  \______/ \__|\__|\__|  \__| V2.0 \033[1;m


 \033[1;32m+ -- -- +=[ Author: LionSec | Homepage: www.neodrix.com\033[1;m
 \033[1;32m+ -- -- +=[ 331 Tools \033[1;m


\033[1;91m[W] Before updating your system , please remove all Kali-linux repositories to avoid any kind of problem .\033[1;m
	''')

def classicMenuPrint():
	print (''' 
ClassicMenu Indicator is a notification area applet (application indicator) for the top panel of Ubuntu's Unity desktop environment.

It provides a simple way to get a classic GNOME-style application menu for those who prefer this over the Unity dash menu.

Like the classic GNOME menu, it includes Wine games and applications if you have those installed.

For more information , please visit : http://www.florian-diesch.de/software/classicmenu-indicator/

''')

def start():
	mainMenu()
	categories()

def helpPrint():
	print (''' 
	****************** +Commands+ ******************

	\033[1;32mback\033[1;m 	\033[1;33mGo back\033[1;m

	\033[1;32mgohome\033[1;m	\033[1;33mGo to the main menu\033[1;m
	\033[1;32mexit\033[1;m		\033[1;33Exit the app\033[1;m
	

	''')

def allCategoriesPrint():
	print ('''
\033[1;36m**************************** All Categories *****************************\033[1;m

1) Information Gathering			8) Exploitation Tools
2) Vulnerability Analysis			9) Forensics Tools
3) Wireless Attacks				10) Stress Testing
4) Web Applications				11) Password Attacks
5) Sniffing & Spoofing				12) Reverse Engineering
6) Maintaining Access				13) Hardware Hacking
7) Reporting Tools 				14) Extra
									
0) All

	''')
	print ("\033[1;32mSelect a category or press (0) to install all Kali linux tools .\n\033[1;m")


def mainMenu():
	while True:
		print ('''1) Add Kali repositories & Update\n2) View Categories\n3) Install classicmenu indicator\n4) Install Kali menu\n5) Help\n''')

		match input("\033[1;36mkat > \033[1;m"):
			case "1":
				break	
				add_and_remove_kali()
			case "2":
				break
				categories()
				
			case "3":
				classicMenuPrint()
				repo = input("\033[1;32mDo you want to install classicmenu indicator ? [y/n]> \033[1;m")
				if repo == "y":
					cmd1 = os.system("add-apt-repository ppa:diesch/testing && apt update")
					cmd = os.system("sudo apt install classicmenu-indicator")

			case "4"	:
				repo = input("\033[1;32mDo you want to install Kali menu ? [y/n]> \033[1;m")
				if repo == "y":
					cmd1 = os.system("apt install kali-menu")

			case "5":
				helpPrint()
			case "exit":
				leave()
			case _:
				wrongChoice()


def add_and_remove_kali():
	while True:
		print ('''1) Add kali linux repositories\n2) Update\n3) Remove all kali linux repositories\n4) View the contents of sources.list file\n''')
						 
		match input("\033[1;32mWhat do you want to do ?> \033[1;m"):
			case "1":
				# Adds the Kali linux repo 
				cmd1 = os.system("apt-key adv --keyserver keyserver.ubuntu.com --recv-keys ED444FF07D8D0BF6")
				cmd2 = os.system("echo '# Kali linux repositories | Added by Katoolin\ndeb http://http.kali.org/kali kali-rolling main contrib non-free' >> /etc/apt/sources.list")


			case "2":
				# Updates the repos
				cmd3 = os.system("apt update")
			case "3":
				# TODO 
				infile = "/etc/apt/sources.list"
				outfile = "/etc/apt/sources.list"

				delete_list = ["# Kali linux repositories | Added by Katoolin\n", "deb http://http.kali.org/kali kali-rolling main contrib non-free\n"]
				fin = open(infile)
				os.remove("/etc/apt/sources.list")
				fout = open(outfile, "w+")
				for line in fin:
					for word in delete_list:
						line = line.replace(word, "")
					fout.write(line)
				fin.close()
				fout.close()
				print ("\033[1;31m\nAll kali linux repositories have been deleted !\n\033[1;m")
			case "back":
				break
				start()
			case "gohome":
				break
				start()
			case "4":
				file = open('/etc/apt/sources.list', 'r')

				print (file.read())

			case _:
				wrongChoice() 	

def installAllPackages():
	cmd = os.system("apt -f install acccheck ace-voip amap automater braa casefile cdpsnarf cisco-torch cookie-cadger copy-router-config dmitry dnmap dnsenum dnsmap dnsrecon dnstracer dnswalk dotdotpwn enum4linux enumiax exploitdb fierce firewalk fragroute fragrouter ghost-phisher golismero goofile lbd maltego-teeth masscan metagoofil miranda nmap p0f parsero recon-ng set smtp-user-enum snmpcheck sslcaudit sslsplit sslstrip sslyze thc-ipv6 theharvester tlssled twofi urlcrazy wireshark wol-e xplico ismtp intrace hping3 bbqsql bed cisco-auditing-tool cisco-global-exploiter cisco-ocs cisco-torch copy-router-config doona dotdotpwn greenbone-security-assistant hexorbase jsql lynis nmap ohrwurm openvas-cli openvas-manager openvas-scanner oscanner powerfuzzer sfuzz sidguesser siparmyknife sqlmap sqlninja sqlsus thc-ipv6 tnscmd10g unix-privesc-check yersinia aircrack-ng asleap bluelog blueranger bluesnarfer bully cowpatty crackle eapmd5pass fern-wifi-cracker ghost-phisher giskismet gqrx kalibrate-rtl killerbee kismet mdk3 mfcuk mfoc mfterm multimon-ng pixiewps reaver redfang spooftooph wifi-honey wifitap wifite apache-users arachni bbqsql blindelephant burpsuite cutycapt davtest deblaze dirb dirbuster fimap funkload grabber jboss-autopwn joomscan jsql maltego-teeth padbuster paros parsero plecost powerfuzzer proxystrike recon-ng skipfish sqlmap sqlninja sqlsus ua-tester uniscan vega w3af webscarab websploit wfuzz wpscan xsser zaproxy burpsuite dnschef fiked hamster-sidejack hexinject iaxflood inviteflood ismtp mitmproxy ohrwurm protos-sip rebind responder rtpbreak rtpinsertsound rtpmixsound sctpscan siparmyknife sipp sipvicious sniffjoke sslsplit sslstrip thc-ipv6 voiphopper webscarab wifi-honey wireshark xspy yersinia zaproxy cryptcat cymothoa dbd dns2tcp http-tunnel httptunnel intersect nishang polenum powersploit pwnat ridenum sbd u3-pwn webshells weevely casefile cutycapt dos2unix dradis keepnote magictree metagoofil nipper-ng pipal armitage backdoor-factory cisco-auditing-tool cisco-global-exploiter cisco-ocs cisco-torch crackle jboss-autopwn linux-exploit-suggester maltego-teeth set shellnoob sqlmap thc-ipv6 yersinia beef-xss binwalk bulk-extractor chntpw cuckoo dc3dd ddrescue dumpzilla extundelete foremost galleta guymager iphone-backup-analyzer p0f pdf-parser pdfid pdgmail peepdf volatility xplico dhcpig funkload iaxflood inviteflood ipv6-toolkit mdk3 reaver rtpflood slowhttptest t50 termineter thc-ipv6 thc-ssl-dos acccheck burpsuite cewl chntpw cisco-auditing-tool cmospwd creddump crunch findmyhash gpp-decrypt hash-identifier hexorbase john johnny keimpx maltego-teeth maskprocessor multiforcer ncrack oclgausscrack pack patator polenum rainbowcrack rcracki-mt rsmangler statsprocessor thc-pptp-bruter truecrack webscarab wordlists zaproxy apktool dex2jar python-distorm3 edb-debugger jad javasnoop jd ollydbg smali valgrind yara android-sdk apktool arduino dex2jar sakis3g smali && wget http://www.morningstarsecurity.com/downloads/bing-ip2hosts-0.4.tar.gz && tar -xzvf bing-ip2hosts-0.4.tar.gz && cp bing-ip2hosts-0.4/bing-ip2hosts /usr/local/bin/")	

def printInfoGathering()
	print ('''
\033[1;36m=+[ Information Gathering\033[1;m

 1) acccheck					30) lbd
 2) ace-voip					31) Maltego Teeth
 3) Amap					32) masscan
 4) Automater					33) Metagoofil
 5) bing-ip2hosts				34) Miranda
 6) braa					35) Nmap
 7) CaseFile					36) ntop
 8) CDPSnarf					37) p0f
 9) cisco-torch					38) Parsero
10) Cookie Cadger				39) Recon-ng
11) copy-router-config				40) SET
12) DMitry					41) smtp-user-enum
13) dnmap					42) snmpcheck
14) dnsenum					43) sslcaudit
15) dnsmap					44) SSLsplit
16) DNSRecon					45) sslstrip
17) dnstracer					46) SSLyze
18) dnswalk					47) THC-IPV6
19) DotDotPwn					48) theHarvester
20) enum4linux					49) TLSSLed
21) enumIAX					50) twofi
22) exploitdb					51) URLCrazy
23) Fierce					52) Wireshark
24) Firewalk					53) WOL-E
25) fragroute					54) Xplico
26) fragrouter					55) iSMTP
27) Ghost Phisher				56) InTrace
28) GoLismero					57) hping3
29) goofile

0) Install all Information Gathering tools
				 ''')

def informationGathering():
	while True:
		printInfoGathering()
		print ("\033[1;32mInsert the number of the tool to install it .\n\033[1;m")
		match input("\033[1;36mkat > \033[1;m"):
			case "1":
				cmd = os.system("apt install acccheck")
			case "2":
				cmd = os.system("apt install ace-voip")
			case "3":
				cmd = os.system("apt install amap")
			case "4":
				cmd = os.system("apt install automater")
			case "5":
				cmd = os.system("wget http://www.morningstarsecurity.com/downloads/bing-ip2hosts-0.4.tar.gz && tar -xzvf bing-ip2hosts-0.4.tar.gz && cp bing-ip2hosts-0.4/bing-ip2hosts /usr/local/bin/")
			case "6":
				cmd = os.system("apt install braa")
			case "7":
				cmd = os.system("apt install casefile")
			case "8":
				cmd = os.system("apt install cdpsnarf")
			case "9":
				cmd = os.system("apt install cisco-torch")
			case "10":
				cmd = os.system("apt install cookie-cadger")
			case "11":
				cmd = os.system("apt install copy-router-config")
			case "12":
				cmd = os.system("apt install dmitry")
			case "13":
				cmd = os.system("apt install dnmap")
			case "14":
				cmd = os.system("apt install dnsenum")
			case "15":
				cmd = os.system("apt install dnsmap")
			case "16":
				cmd = os.system("apt install dnsrecon")
			case "17":
				cmd = os.system("apt install dnstracer")
			case "18":
				cmd = os.system("apt install dnswalk")
			case "19":
				cmd = os.system("apt install dotdotpwn")
			case "20":
				cmd = os.system("apt install enum4linux")
			case "21":
				cmd = os.system("apt install enumiax")
			case "22":
				cmd = os.system("apt install exploitdb")
			case "23":
				cmd = os.system("apt install fierce")
			case "24":
				cmd = os.system("apt install firewalk")
			case "25":
				cmd = os.system("apt install fragroute")
			case "26":
				cmd = os.system("apt install fragrouter")
			case "27":
				cmd = os.system("apt install ghost-phisher")
			case "28":
				cmd = os.system("apt install golismero")
			case "29":
				cmd = os.system("apt install goofile")
			case "30":
				cmd = os.system("apt install lbd")
			case "31":
				cmd = os.system("apt install maltego-teeth")
			case "32":
				cmd = os.system("apt install masscan")
			case "33":
				cmd = os.system("apt install metagoofil")
			case "34":
				cmd = os.system("apt install miranda")
			case "35":
				cmd = os.system("apt install nmap")
			case "36":
				print ('ntop is unavailable')
			case "37":
				cmd = os.system("apt install p0f")
			case "38":
				cmd = os.system("apt install parsero")
			case "39":
				cmd = os.system("apt install recon-ng")
			case "40":
				cmd = os.system("apt install set")
			case "41":
				cmd = os.system("apt install smtp-user-enum")
			case "42":
				cmd = os.system("apt install snmpcheck")
			case "43":
				cmd = os.system("apt install sslcaudit")
			case "44":
				cmd = os.system("apt install sslsplit")
			case "45":
				cmd = os.system("apt install sslstrip")
			case "46":
				cmd = os.system("apt install sslyze")
			case "47":
				cmd = os.system("apt install thc-ipv6")
			case "48":
				cmd = os.system("apt install theharvester")
			case "49":
				cmd = os.system("apt install tlssled")
			case "50":
				cmd = os.system("apt install twofi")
			case "51":
				cmd = os.system("apt install urlcrazy")
			case "52":
				cmd = os.system("apt install wireshark")
			case "53":
				cmd = os.system("apt install wol-e")
			case "54":
				cmd = os.system("apt install xplico")
			case "55":
				cmd = os.system("apt install ismtp")
			case "56":
				cmd = os.system("apt install intrace")
			case "57":
				cmd = os.system("apt install hping3")
			case "back":
				break
				categories()
			case "gohome":
				break
				start()	
			case "0":
				cmd = os.system("apt install -y acccheck ace-voip amap automater braa casefile cdpsnarf cisco-torch cookie-cadger copy-router-config dmitry dnmap dnsenum dnsmap dnsrecon dnstracer dnswalk dotdotpwn enum4linux enumiax exploitdb fierce firewalk fragroute fragrouter ghost-phisher golismero goofile lbd maltego-teeth masscan metagoofil miranda nmap p0f parsero recon-ng set smtp-user-enum snmpcheck sslcaudit sslsplit sslstrip sslyze thc-ipv6 theharvester tlssled twofi urlcrazy wireshark wol-e xplico ismtp intrace hping3 && wget http://www.morningstarsecurity.com/downloads/bing-ip2hosts-0.4.tar.gz && tar -xzvf bing-ip2hosts-0.4.tar.gz && cp bing-ip2hosts-0.4/bing-ip2hosts /usr/local/bin/")				
			case _:
				wrongChoice()

def printVulnerabilityAnalysis():
	print ('''
\033[1;36m=+[ Vulnerability Analysis\033[1;m

 1) BBQSQL				18) Nmap
 2) BED					19)ohrwurm
 3) cisco-auditing-tool			20) openvas-administrator
 4) cisco-global-exploiter		21) openvas-cli
 5) cisco-ocs				22) openvas-manager
 6) cisco-torch				23) openvas-scanner
 7) copy-router-config			24) Oscanner
 8) commix				25) Powerfuzzer
 9) DBPwAudit				26) sfuzz
10) DoonaDot				27) SidGuesser
11) DotPwn				28) SIPArmyKnife
12) Greenbone Security Assistant 	29) sqlmap
13) GSD					30) Sqlninja
14) HexorBase				31) sqlsus
15) Inguma				32) THC-IPV6
16) jSQL				33) tnscmd10g
17) Lynis				34) unix-privesc-check
					35) Yersinia

0) Install all Vulnerability Analysis tools
				 
						''')
	print ("\033[1;32mInsert the number of the tool to install it .\n\033[1;m")

def vulnerabilityAnalysis():
	while True:
		match input("\033[1;36mkat > \033[1;m"):
			case "1":
				cmd = os.system("apt install bbqsql")

			case "2":
				cmd = os.system("apt install bed")

			case "3":
				cmd = os.system("apt install cisco-auditing-tool")
			case "4":
				cmd = os.system("apt install cisco-global-exploiter")
			case "5":
				cmd = os.system("apt install cisco-ocs")
			case "6":
				cmd = os.system("apt install cisco-torch")
			case "7":
				cmd = os.system("apt install copy-router-config")
			case "8":
				cmd = os.system("apt install git && git clone https://github.com/stasinopoulos/commix.git commix && cd commix && python ./commix.py --install")
			case "9":
				cmd = os.system("echo 'download page : http://www.cqure.net/wp/tools/database/dbpwaudit/'")
			case "10":
				cmd = os.system("apt install doona")
			case "11":
				cmd = os.system("apt install dotdotpwn")
			case "12":
				cmd = os.system("apt install greenbone-security-assistant")
			case "13":
				cmd = os.system("apt install git && git clone git://git.kali.org/packages/gsd.git")
			case "14":
				cmd = os.system("apt install hexorbase")
			case "15":
				print ("Please download inguma from : http://inguma.sourceforge.net")
			case "16":
				cmd = os.system("apt install jsql")
			case "17":
				cmd = os.system("apt install lynis")
			case "18":
				cmd = os.system("apt install nmap")
			case "19":
				cmd = os.system("apt install ohrwurm")
			case "20":
				cmd = os.system("apt install openvas-administrator")
			case "21":
				cmd = os.system("apt install openvas-cli")
			case "22":
				cmd = os.system("apt install openvas-manager")
			case "23":
				cmd = os.system("apt install openvas-scanner")
			case "24":
				cmd = os.system("apt install oscanner")
			case "25":
				cmd = os.system("apt install powerfuzzer")
			case "26":
				cmd = os.system("apt install sfuzz")
			case "27":
				cmd = os.system("apt install sidguesser")
			case "28":
				cmd = os.system("apt install siparmyknife")
			case "29":
				cmd = os.system("apt install sqlmap")
			case "30":
				cmd = os.system("apt install sqlninja")
			case "31":
				cmd = os.system("apt install sqlsus")
			case "32":
				cmd = os.system("apt install thc-ipv6")
			case "33":
				cmd = os.system("apt install tnscmd10g")
			case "34":
				cmd = os.system("apt install unix-privesc-check")
			case "35":
				cmd = os.system("apt install yersinia")
			case "back":
				break
				categories()
			case "gohome":
				break
				start()						
			case "0":
				cmd = os.system("apt install -y bbqsql bed cisco-auditing-tool cisco-global-exploiter cisco-ocs cisco-torch copy-router-config doona dotdotpwn greenbone-security-assistant hexorbase jsql lynis nmap ohrwurm openvas-cli openvas-manager openvas-scanner oscanner powerfuzzer sfuzz sidguesser siparmyknife sqlmap sqlninja sqlsus thc-ipv6 tnscmd10g unix-privesc-check yersinia")						
			case _:
				wrongChoice()

def printPasswordAttacks():
	print ('''
\033[1;36m=+[ Password Attacks\033[1;m

 1) acccheck				19) Maskprocessor
 2) Burp Suite				20) multiforcer
 3) CeWL				21) Ncrack
 4) chntpw				22) oclgausscrack
 5) cisco-auditing-tool			23) PACK
 6) CmosPwd				24) patator
 7) creddump				25) phrasendrescher
 8) crunch				26) polenum
 9) DBPwAudit				27) RainbowCrack
10) findmyhash				28) rcracki-mt
11) gpp-decrypt				29) RSMangler
12) hash-identifier			30) SQLdict
13) HexorBase				31) Statsprocessor
14) THC-Hydra				32) THC-pptp-bruter
15) John the Ripper			33) TrueCrack
16) Johnny				34) WebScarab 
17) keimpx				35) wordlists 
18) Maltego Teeth			36) zaproxy 

0) Install all Password Attacks tools
				 
						''')
	print ("\033[1;32mInsert the number of the tool to install it .\n\033[1;m")


def passwordAttacks():
	while True:
		printPasswordAttacks()
		match input("\033[1;36mkat > \033[1;m"):
			case "1":
				cmd = os.system("apt install acccheck")
			case "2":
				cmd = os.system("apt install burpsuite")
			case "3":
				cmd = os.system("apt install cewl")
			case "4":
				cmd = os.system("apt install chntpw")
			case "5":
				cmd = os.system("apt install cisco-auditing-tool")
			case "6":
				cmd = os.system("apt install cmospwd")
			case "7":
				cmd = os.system("apt install creddump")
			case "8":
				cmd = os.system("apt install crunch")
			case "9":
				cmd = os.system("apt install git && git clone git://git.kali.org/packages/dbpwaudit.git")
			case "10":
				cmd = os.system("apt install findmyhash")
			case "11":
				cmd = os.system("apt install gpp-decrypt")
			case "12":
				cmd = os.system("apt install hash-identifier")
			case "13":
				cmd = os.system("apt install hexorbase")
			case "14":
				cmd = os.system("echo 'please visit : https://www.thc.org/thc-hydra/' ")
			case "15":
				cmd = os.system("apt install john")
			case "16":
				cmd = os.system("apt install johnny")
			case "17":
				cmd = os.system("apt install keimpx")
			case "18":
				cmd = os.system("apt install maltego-teeth")
			case "19":
				cmd = os.system("apt install maskprocessor")
			case "20":
				cmd = os.system("apt install multiforcer")
			case "21":
				cmd = os.system("apt install ncrack")
			case "22":
				cmd = os.system("apt install oclgausscrack")
			case "23":
				cmd = os.system("apt install pack")
			case "24":
				cmd = os.system("apt install patator")
			case "25":
				cmd = os.system("echo 'please visit : http://www.leidecker.info/projects/phrasendrescher/index.shtml' ")
			case "26":
				cmd = os.system("apt install polenum")
			case "27":
				cmd = os.system("apt install rainbowcrack")
			case "28":
				cmd = os.system("apt install rcracki-mt")
			case "29":
				cmd = os.system("apt install rsmangler")
			case "30":
				print ("Sqldict is unavailable")
			case "31":
				cmd = os.system("apt install statsprocessor")
			case "32":
				cmd = os.system("apt install thc-pptp-bruter")
			case "33":
				cmd = os.system("apt install truecrack")
			case "34":
				cmd = os.system("apt install webscarab")
			case "35":
				cmd = os.system("apt install wordlists")
			case "36":
				cmd = os.system("apt install zaproxy")
			case "back":
				break
				categories()
			case "gohome":
				break
				start()   
			case "0":
				cmd = os.system("apt install -y acccheck burpsuite cewl chntpw cisco-auditing-tool cmospwd creddump crunch findmyhash gpp-decrypt hash-identifier hexorbase john johnny keimpx maltego-teeth maskprocessor multiforcer ncrack oclgausscrack pack patator polenum rainbowcrack rcracki-mt rsmangler statsprocessor thc-pptp-bruter truecrack webscarab wordlists zaproxy")
			case _:
				wrongChoice()
def printWirelessAttacks():
	print ('''
		\033[1;36m=+[ Wireless Attacks\033[1;m

 1) Aircrack-ng				17) kalibrate-rtl
 2) Asleap				18) KillerBee
 3) Bluelog				19) Kismet
 4) BlueMaho				20) mdk3
 5) Bluepot				21) mfcuk
 6) BlueRanger				22) mfoc
 7) Bluesnarfer				23) mfterm
 8) Bully				24) Multimon-NG
 9) coWPAtty				25) PixieWPS
10) crackle				26) Reaver
11) eapmd5pass				27) redfang
12) Fern Wifi Cracker			28) RTLSDR Scanner
13) Ghost Phisher			29) Spooftooph
14) GISKismet				30) Wifi Honey				31) Wifitap
16) gr-scan				32) Wifite 

0) Install all Wireless Attacks tools
				 
	''')
	print ("\033[1;32mInsert the number of the tool to install it .\n\033[1;m")

def wirelessAttacks():
	while True:
		printWirelessAttacks()
		match input("\033[1;36mkat > \033[1;m"):
			case"1":
				cmd = os.system("apt install aircrack-ng")
			case "2":
				cmd = os.system("apt install asleap")
			case "3":
				cmd = os.system("apt install bluelog")
			case "4":
				cmd = os.system("apt install git && git clone git://git.kali.org/packages/bluemaho.git")
			case "5":
				cmd = os.system("apt install git && git clone git://git.kali.org/packages/bluepot.git")
			case "6":
				cmd = os.system("apt install blueranger")
			case "7":
				cmd = os.system("apt install bluesnarfer")
			case "8":
				cmd = os.system("apt install bully")
			case "9":
				cmd = os.system("apt install cowpatty")
			case "10":
				cmd = os.system("apt install crackle")
			case "11":
				cmd = os.system("apt install eapmd5pass")
			case "12":
				cmd = os.system("apt install fern-wifi-cracker")
			case "13":
				cmd = os.system("apt install ghost-phisher")
			case "14":
				cmd = os.system("apt install giskismet")
			case "16":
				cmd = os.system("apt install git && git clone git://git.kali.org/packages/gr-scan.git")
			case "17":
				cmd = os.system("apt install kalibrate-rtl")
			case "18":
				cmd = os.system("apt install killerbee")
			case "19":
				cmd = os.system("apt install kismet")
			case "20":
				cmd = os.system("apt install mdk3")
			case "21":
				cmd = os.system("apt install mfcuk")
			case "22":
				cmd = os.system("apt install mfoc")
			case "23":
				cmd = os.system("apt install mfterm")
			case "24":
				cmd = os.system("apt install multimon-ng")
			case "25":
				cmd = os.system("apt install pixiewps")
			case "26":
				cmd = os.system("apt install reaver")
			case "27":
				cmd = os.system("apt install redfang")
			case "28":
				cmd = os.system("apt install rtlsdr-scanner")
			case "29":
				cmd = os.system("apt install spooftooph")
			case "30":
				cmd = os.system("apt install wifi-honey")
			case "31":
				cmd = os.system("apt install wifitap")
			case "32":
				cmd = os.system("apt install wifite")
			case "0":
				cmd = os.system("apt install -y aircrack-ng asleap bluelog blueranger bluesnarfer bully cowpatty crackle eapmd5pass fern-wifi-cracker ghost-phisher giskismet gqrx kalibrate-rtl killerbee kismet mdk3 mfcuk mfoc mfterm multimon-ng pixiewps reaver redfang spooftooph wifi-honey wifitap wifite")
			case "back":
				break
				categories()
			case "gohome":
				break
				start()						
			case _:
				wrongChoice()
def printWebApps():
	print ('''
\033[1;36m=+[ Web Applications\033[1;m

 1) apache-users			21) Parsero
 2) Arachni				22) plecost
 3) BBQSQL				23) Powerfuzzer
 4) BlindElephant			24) ProxyStrike
 5) Burp Suite				25) Recon-ng
 6) commix				26) Skipfish
 7) CutyCapt				27) sqlmap
 8) DAVTest				28) Sqlninja
 9) deblaze				29) sqlsus
10) DIRB				30) ua-tester
11) DirBuster				31) Uniscan
12) fimap				32) Vega
13) FunkLoad				33) w3af
14) Grabber				34) WebScarab
15) jboss-autopwn			35) Webshag
16) joomscan				36) WebSlayer
17) jSQL				37) WebSploit
18) Maltego Teeth			38) Wfuzz
19) PadBuster				39) WPScan
20) Paros				40) XSSer
					41) zaproxy

0) Install all Web Applications tools
				 
	''')
	print ("\033[1;32mInsert the number of the tool to install it .\n\033[1;m")

	
def webApps():
	while True:
		printWebApps()					
		match input("\033[1;36mkat > \033[1;m"):
			case "1":
				cmd = os.system("apt install apache-users")
			case "2":
				cmd = os.system("apt install arachni")
			case "3":
				cmd = os.system("apt install bbqsql")
			case "4":
				cmd = os.system("apt install blindelephant")
			case "5":
				cmd = os.system("apt install burpsuite")
			case "6":
				cmd = os.system("apt install cutycapt")
			case "7":
				cmd = os.system("apt install git && git clone https://github.com/stasinopoulos/commix.git commix && cd commix && python ./commix.py --install")
			case "8":
				cmd = os.system("apt install davtest")
			case "9":
				cmd = os.system("apt install deblaze")
			case "10":
				cmd = os.system("apt install dirb")
			case "11":
				cmd = os.system("apt install dirbuster")
			case "12":
				cmd = os.system("apt install fimap")
			case "13":
				cmd = os.system("apt install funkload")
			case "14":
				cmd = os.system("apt install grabber")
			case "15":
				cmd = os.system("apt install jboss-autopwn")
			case "16":
				cmd = os.system("apt install joomscan")
			case "17":
				cmd = os.system("apt install jsql")
			case "18":
				cmd = os.system("apt install maltego-teeth")
			case "19":
				cmd = os.system("apt install padbuster")
			case "20":
				cmd = os.system("apt install paros")
			case "21":
				cmd = os.system("apt install parsero")
			case "22":
				cmd = os.system("apt install plecost")
			case "23":
				cmd = os.system("apt install powerfuzzer")
			case "24":
				cmd = os.system("apt install proxystrike")
			case "25":
				cmd = os.system("apt install recon-ng")
			case "26":
				cmd = os.system("apt install skipfish")
			case "27":
				cmd = os.system("apt install sqlmap")
			case "28":
				cmd = os.system("apt install sqlninja")
			case "29":
				cmd = os.system("apt install sqlsus")
			case "30":
				cmd = os.system("apt install ua-tester")
			case "31":
				cmd = os.system("apt install uniscan")
			case "32":
				cmd = os.system("apt install vega")
			case "33":
				cmd = os.system("apt install w3af")
			case "34":
				cmd = os.system("apt install webscarab")
			case "35":
				print ("Webshag is unavailable")
			case "36":
				cmd = os.system("apt install git && git clone git://git.kali.org/packages/webslayer.git")
			case "37":
				cmd = os.system("apt install websploit")
			case "38":
				cmd = os.system("apt install wfuzz")
			case "39":
				cmd = os.system("apt install wpscan")
			case "40":
				cmd = os.system("apt install xsser")
			case "41":
				cmd = os.system("apt install zaproxy")										
			case "back":
				break
				categories()
			case "gohome":
				break
				start()	
			case "0":
				cmd = os.system("apt install -y apache-users arachni bbqsql blindelephant burpsuite cutycapt davtest deblaze dirb dirbuster fimap funkload grabber jboss-autopwn joomscan jsql maltego-teeth padbuster paros parsero plecost powerfuzzer proxystrike recon-ng skipfish sqlmap sqlninja sqlsus ua-tester uniscan vega w3af webscarab websploit wfuzz wpscan xsser zaproxy")												
			case _:
				wrongChoice()
def printSniffinfSpoofing():
	print ('''
\033[1;36m=+[ Sniffing & Spoofing\033[1;m

 1) Burp Suite				17) rtpmixsound
 2) DNSChef				18) sctpscan
 3) fiked				19) SIPArmyKnife
 4) hamster-sidejack			20) SIPp
 5) HexInject				21) SIPVicious
 6) iaxflood				22) SniffJoke
 7) inviteflood				23) SSLsplit
 8) iSMTP				24) sslstrip
 9) isr-evilgrade			25) THC-IPV6
10) mitmproxy				26) VoIPHopper
11) ohrwurm				27) WebScarab
12) protos-sip				28) Wifi Honey
13) rebind				29) Wireshark
14) responder				30) xspy
15) rtpbreak				31) Yersinia
16) rtpinsertsound			32) zaproxy 

0) Install all Sniffing & Spoofing tools
				 
						''')
	print ("\033[1;32mInsert the number of the tool to install it .\n\033[1;m")

def sniffinfSpoofing():
	while True:
		printSniffinfSpoofing()
		match input("\033[1;36mkat > \033[1;m"):
			case "1":
				cmd = os.system("apt install burpsuite -y")

			case "2":
				cmd = os.system("apt install dnschef -y")

			case "3":
				cmd = os.system("apt install fiked -y")
			case "4":
				cmd = os.system("apt install hamster-sidejack -y")
			case "5":
				cmd = os.system("apt install hexinject -y")
			case "6":
				cmd = os.system("apt install iaxflood -y")
			case "7":
				cmd = os.system("apt install inviteflood -y")
			case "8":
				cmd = os.system("apt install ismtp -y")
			case "9":
				cmd = os.system("apt install git -y && git clone git://git.kali.org/packages/isr-evilgrade.git")
			case "10":
				cmd = os.system("apt install mitmproxy -y")
			case "11":
				cmd = os.system("apt install ohrwurm -y")
			case "12":
				cmd = os.system("apt install protos-sip -y")
			case "13":
				cmd = os.system("apt install rebind -y")
			case "14":
				cmd = os.system("apt install responder -y")
			case "15":
				cmd = os.system("apt install rtpbreak -y")
			case "16":
				cmd = os.system("apt install rtpinsertsound -y")
			case "17":
				cmd = os.system("apt install rtpmixsound -y")
			case "18":
				cmd = os.system("apt install sctpscan -y")
			case "19":
				cmd = os.system("apt install siparmyknife -y")
			case "20":
				cmd = os.system("apt install sipp -y")
			case "21":
				cmd = os.system("apt install sipvicious -y")
			case "22":
				cmd = os.system("apt install sniffjoke -y")
			case "23":
				cmd = os.system("apt install sslsplit -y")
			case "24":
				cmd = os.system("apt install sslstrip -y")
			case "25":
				cmd = os.system("apt install thc-ipv6 -y")
			case "26":
				cmd = os.system("apt install voiphopper -y")
			case "27":
				cmd = os.system("apt install webscarab -y")
			case "28":
				cmd = os.system("apt install wifi-honey -y")
			case "29":
				cmd = os.system("apt install wireshark -y")
			case "30":
				cmd = os.system("apt install xspy -y")
			case "31":
				cmd = os.system("apt install yersinia -y")
			case "32":
				cmd = os.system("apt install zaproxy -y")
			case "back":
				break
				categories()
			case "gohome":
				break
				start()
			case "0":
				cmd = os.system("apt install -y burpsuite dnschef fiked hamster-sidejack hexinject iaxflood inviteflood ismtp mitmproxy ohrwurm protos-sip rebind responder rtpbreak rtpinsertsound rtpmixsound sctpscan siparmyknife sipp sipvicious sniffjoke sslsplit sslstrip thc-ipv6 voiphopper webscarab wifi-honey wireshark xspy yersinia zaproxy")  
			case _:
				wrongChoice()

def printMaintainingAccess():
		print ('''
	\033[1;36m=+[ Maintaining Access\033[1;m

	 1) CryptCat
	 2) Cymothoa
	 3) dbd
	 4) dns2tcp
	 5) http-tunnel	
	 6) HTTPTunnel
	 7) Intersect
	 8) Nishang
	 9) polenum
	10) PowerSploit
	11) pwnat
	12) RidEnum
	13) sbd
	14) U3-Pwn
	15) Webshells
	16) Weevely

	0) Install all Maintaining Access tools
					 
		''')
		print ("\033[1;32mInsert the number of the tool to install it .\n\033[1;m")

def maintainingAccess():
	while True
		printMaintainingAccess()
		match input("\033[1;36mkat > \033[1;m"):
			case "1":
				cmd = os.system("apt install cryptcat")
			case "2":
				cmd = os.system("apt install cymothoa")
			case "3":
				cmd = os.system("apt install dbd")
			case "4":
				cmd = os.system("apt install dns2tcp")
			case "5":
				cmd = os.system("apt install http-tunnel")
			case "6":
				cmd = os.system("apt install httptunnel")
			case "7":
				cmd = os.system("apt install intersect")
			case "8":
				cmd = os.system("apt install nishang")
			case "9":
				cmd = os.system("apt install polenum")
			case "10":
				cmd = os.system("apt install powersploit")
			case "11":
				cmd = os.system("apt install pwnat")
			case "12":
				cmd = os.system("apt install ridenum")
			case "13":
				cmd = os.system("apt install sbd")
			case "14":
				cmd = os.system("apt install u3-pwn")
			case "15":
				cmd = os.system("apt install webshells")
			case "16":
				cmd = os.system("apt install weevely")
			case "back":
				break
				categories()
			case "gohome":
				break
				start()   
			case "0":
				cmd = os.system("apt install -y cryptcat cymothoa dbd dns2tcp http-tunnel httptunnel intersect nishang polenum powersploit pwnat ridenum sbd u3-pwn webshells weevely")
			case _:
				wrongChoice()
def printReportingTools():
	print ('''
\033[1;36m=+[ Reporting Tools\033[1;m

1) CaseFile
2) CutyCapt
3) dos2unix
4) Dradis
5) KeepNote	
6) MagicTree
7) Metagoofil
8) Nipper-ng
9) pipal

0) Install all Reporting Tools		 
		''')
	print ("\033[1;32mInsert the number of the tool to install it .\n\033[1;m")

def reportingTools():
	
	while True:
		printReportingTools()
		match input("\033[1;36mkat > \033[1;m"):
			case "1":
				cmd = os.system("apt install casefile")
			case "2":
				cmd = os.system("apt install cutycapt")
			case "3":
				cmd = os.system("apt install dos2unix")
			case "4":
				cmd = os.system("apt install dradis")
			case "5":
				cmd = os.system("apt install keepnote")
			case "6":
				cmd = os.system("apt install magictree")
			case "7":
				cmd = os.system("apt install metagoofil")
			case "8":
				cmd = os.system("apt install nipper-ng")
			case "9":
				cmd = os.system("apt install pipal")
			case "back":
				break
				categories()
			case "gohome":
				break
				start()   
			case "0":
				cmd = os.system("apt install -y casefile cutycapt dos2unix dradis keepnote magictree metagoofil nipper-ng pipal")  
			case _:
				wrongChoice()
def printExpolitationTool():
	print ('''
\033[1;36m=+[ Exploitation Tools\033[1;m

 1) Armitage
 2) Backdoor Factory
 3) BeEF
 4) cisco-auditing-tool
 5) cisco-global-exploiter	
 6) cisco-ocs
 7) cisco-torch
 8) commix
 9) crackle
10) jboss-autopwn
11) Linux Exploit Suggester
12) Maltego Teeth
13) SET
14) ShellNoob
15) sqlmap
16) THC-IPV6
17) Yersinia

0) Install all Exploitation Tools
				 
	''')
	print ("\033[1;32mInsert the number of the tool to install it .\n\033[1;m")

def exploitationTool():
	while True:
		printExpolitationTool()
		match input("\033[1;36mkat > \033[1;m"):
			case "1":
				cmd = os.system("apt install armitage")
			case "2":
				cmd = os.system("apt install backdoor-factory")
			case "3":
				cmd = os.system("apt install beef-xss")
			case "4":
				cmd = os.system("apt install cisco-auditing-tool")
			case "5":
				cmd = os.system("apt install cisco-global-exploiter")
			case "6":
				cmd = os.system("apt install cisco-ocs")
			case "7":
				cmd = os.system("apt install cisco-torch")
			case "8":
				cmd = os.system("apt install git && git clone https://github.com/stasinopoulos/commix.git commix && cd commix && python ./commix.py --install")
			case "9":
				cmd = os.system("apt install crackle")
			case "10":
				cmd = os.system("apt install jboss-autopwn")
			case "11":
				cmd = os.system("apt install linux-exploit-suggester")
			case "12":
				cmd = os.system("apt install maltego-teeth")
			case "13":
				cmd = os.system("apt install set")
			case "14":
				cmd = os.system("apt install shellnoob")
			case "15":
				cmd = os.system("apt install sqlmap")
			case "16":
				cmd = os.system("apt install thc-ipv6")
			case "17":
				cmd = os.system("apt install yersinia")
			case "back":
				break
				categories()
			case "gohome":
				break
				start()   
			case "0":
				cmd = os.system("apt install -y armitage backdoor-factory cisco-auditing-tool cisco-global-exploiter cisco-ocs cisco-torch crackle jboss-autopwn linux-exploit-suggester maltego-teeth set shellnoob sqlmap thc-ipv6 yersinia beef-xss")  						
			case _:
				wrongChoice()

def printForensicsTools():
	print ('''
\033[1;36m=+[ Forensics Tools\033[1;m

 1) Binwalk				11) extundelete
 2) bulk-extractor			12) Foremost
 3) Capstone				13) Galleta
 4) chntpw				14) Guymager
 5) Cuckoo				15) iPhone Backup Analyzer
 6) dc3dd				16) p0f
 7) ddrescue				17) pdf-parser
 8) DFF					18) pdfid
 9) diStorm3				19) pdgmail
10) Dumpzilla				20) peepdf
					21) RegRipper
					22) Volatility
					23) Xplico

0) Install all Forensics Tools
				 
	''')
	print ("\033[1;32mInsert the number of the tool to install it .\n\033[1;m")

def forensicsTools():
	while True:
		printExpolitationTool()
		match input("\033[1;36mkat > \033[1;m"):
			case "1":
				cmd = os.system("apt install binwalk")
			case "2":
				cmd = os.system("apt install bulk-extractor")
			case "3":
				cmd = os.system("apt install git && git clone git://git.kali.org/packages/capstone.git")
			case "4":
				cmd = os.system("apt install chntpw")
			case "5":
				cmd = os.system("apt install cuckoo")
			case "6":
				cmd = os.system("apt install dc3dd")
			case "7":
				cmd = os.system("apt install ddrescue")
			case "8":
				print ('dff is unavailable')
			case "9":
				cmd = os.system("apt install git && git clone git://git.kali.org/packages/distorm3.git")
			case "10":
				cmd = os.system("apt install dumpzilla")
			case "11":
				cmd = os.system("apt install extundelete")
			case "12":
				cmd = os.system("apt install foremost")
			case "13":
				cmd = os.system("apt install galleta")
			case "14":
				cmd = os.system("apt install guymager")
			case "15":
				cmd = os.system("apt install iphone-backup-analyzer")
			case "16":
				cmd = os.system("apt install p0f")
			case "17":
				cmd = os.system("apt install pdf-parser")
			case "18":
				cmd = os.system("apt install pdfid")
			case "19":
				cmd = os.system("apt install pdgmail")
			case "20":
				cmd = os.system("apt install peepdf")
			case "21":
				print ("Regripper is unavailable")
			case "22":
				cmd = os.system("apt install volatility")
			case "23":
				cmd = os.system("apt install xplico")
			case "back":
				break
				categories()
			case "gohome":
				break
				start()   
			case "0":
				cmd = os.system("apt install -y binwalk bulk-extractor chntpw cuckoo dc3dd ddrescue dumpzilla extundelete foremost galleta guymager iphone-backup-analyzer p0f pdf-parser pdfid pdgmail peepdf volatility xplico")						
			case _:
				wrongChoice()
def printStressTest():
	print ('''
\033[1;36m=+[ Stress Testing\033[1;m

 1) DHCPig
 2) FunkLoad
 3) iaxflood
 4) Inundator
 5) inviteflood	
 6) ipv6-toolkit
 7) mdk3
 8) Reaver
 9) rtpflood
10) SlowHTTPTest
11) t50
12) Termineter
13) THC-IPV6
14) THC-SSL-DOS 		

0) Install all Stress Testing tools
				 
						''')
	print ("\033[1;32mInsert the number of the tool to install it .\n\033[1;m")



def stressTest():
	while True:
		printStressTest()
		match input("\033[1;36mkat > \033[1;m"):
			case  "1":
				cmd = os.system("apt install dhcpig")
			case "2":
				cmd = os.system("apt install funkload")
			case "3":
				cmd = os.system("apt install iaxflood")
			case "4":
				cmd = os.system("apt install git && git clone git://git.kali.org/packages/inundator.git")
			case "5":
				cmd = os.system("apt install inviteflood")
			case "6":
				cmd = os.system("apt install ipv6-toolkit")
			case "7":
				cmd = os.system("apt install mdk3")
			case "8":
				cmd = os.system("apt install reaver")
			case "9":
				cmd = os.system("apt install rtpflood")
			case "10":
				cmd = os.system("apt install slowhttptest")
			case "11":
				cmd = os.system("apt install t50")
			case "12":
				cmd = os.system("apt install termineter")
			case "13":
				cmd = os.system("apt install thc-ipv6")
			case "14":
				cmd = os.system("apt install thc-ssl-dos ")    				             										
			case "back":
				break
				categories()
			case "gohome":
				break
				start()   
			case "0":
				cmd = os.system("apt install -y dhcpig funkload iaxflood inviteflood ipv6-toolkit mdk3 reaver rtpflood slowhttptest t50 termineter thc-ipv6 thc-ssl-dos")
			case _:
				wrongChoice()

def printReverseEngineering():
	print ('''
\033[1;36m=+[ Reverse Engineering\033[1;m

 1) apktool
 2) dex2jar
 3) diStorm3
 4) edb-debugger
 5) jad	
 6) javasnoop
 7) JD-GUI
 8) OllyDbg
 9) smali
10) Valgrind
11) YARA

0) Install all Reverse Engineering tools
				 
	''')
	print ("\033[1;32mInsert the number of the tool to install it .\n\033[1;m")

def reverseEngineering():
	while True:
		printReverseEngineering()
	
		match input("\033[1;36mkat > \033[1;m"):
			case  "1":
				cmd = os.system("apt install apktool")
			case "2":
				cmd = os.system("apt install dex2jar")
			case "3":
				cmd = os.system("apt install python-diStorm3")
			case "4":
				cmd = os.system("apt install edb-debugger")
			case "5":
				cmd = os.system("apt install jad")
			case "6":
				cmd = os.system("apt install javasnoop")
			case "7":
				cmd = os.system("apt install JD")
			case "8":
				cmd = os.system("apt install OllyDbg")
			case "9":
				cmd = os.system("apt install smali")
			case "10":
				cmd = os.system("apt install Valgrind")
			case "11":
				cmd = os.system("apt install YARA")
			case "back":
				break
				categories()
			case "gohome":
				break
				start()   
			case "0":
				cmd = os.system("apt install -y apktool dex2jar python-diStorm3 edb-debugger jad javasnoop JD OllyDbg smali Valgrind YARA")
			case _:
				wrongChoice()

def printHardwareHacking():
	print ('''
\033[1;36m=+[ Hardware Hacking\033[1;m

 1) android-sdk
 2) apktool
 3) Arduino
 4) dex2jar
 5) Sakis3G	
 6) smali

0) Install all Hardware Hacking tools
				 
	''')
	print ("\033[1;32mInsert the number of the tool to install it .\n\033[1;m")

def hardwareHacking():
	while True:
		printHardwareHacking()
		match input("\033[1;36mkat > \033[1;m"):
			case  "1":
				cmd = os.system("apt install android-sdk")
			case "2":
				cmd = os.system("apt install apktool")
			case "3":
				cmd = os.system("apt install arduino")
			case "4":
				cmd = os.system("apt install dex2jar")
			case "5":
				cmd = os.system("apt install sakis3g")
			case "6":
				cmd = os.system("apt install smali")
			case "back":
				break
				categories()
			case "gohome":
				break
				start()   
			case "0":
				cmd = os.system("apt install -y android-sdk apktool arduino dex2jar sakis3g smali")
			case _:
				wrongChoice()

def extra():
	while True:
		print ('''
\033[1;36m=+[ Extra\033[1;m

1) Wifresti
2) Squid3
	''')
		print ("\033[1;32mInsert the number of the tool to install it .\n\033[1;m")
		match input("\033[1;36mkat > \033[1;m"):
			case  "1":
				cmd = os.system("git clone https://github.com/LionSec/wifresti.git && cp wifresti/wifresti.py /usr/bin/wifresti && chmod +x /usr/bin/wifresti && wifresti")
				print (" ")
			case "2":
				cmd = os.system("apt install squid3")
				print (" ")
			case "back":
				break
				categories()
			case "gohome":
				break
				start()
			case _:
				wrongChoice()

def categories():
	while True:
		allCategoriesPrint()

		match input("\033[1;36mkat > \033[1;m"):
			case "back":
				break
				start()
			case "gohome":
				break
				start()
			case "0":
				installAllPackages()
			case "1":
				informationGathering()
			case "2":
				vulnerabilityAnalysis()
			case "3":
				wirelessAttacks()
			case "4":
				webApps()
			case "5":
				sniffinfSpoofing()
			case "6":
				maintainingAccess()
			case "7":
				reportingTools()
			case "8":
				exploitationTool()
			case "9":
				forensicsToools()
			case "10":
				stressTest()
			case "11":
				passwordAttacks()
			case "12" :
				reverseEngineering()
			case "13" :
				hardwareHacking()
			case "14" :
				extra()
			case _:
				wrongChoice()

def wrongChoice():
	cmd = os.system("clear")
	cmd = os.system('spd-say "Sorry, that was an invalid command"')
	print ("\n\033[1;31mSorry, that was an invalid command!\033[1;m\n")
	time.sleep(2) 
def leave():
	cmd = os.system('spd-say "Goodbye"')
	print ("Shutdown requested...Goodbye...")
	time.sleep(2)
	sys.exit()


if __name__ == "__main__":
    main()
