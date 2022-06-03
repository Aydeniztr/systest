import platform,socket,re,uuid,logging,os,sys

linux_logo = r'''
        _nnnn_
        dGGGGMMb
       @p~qp~~qMb
       M|@||@) M|
       @,----.JM|
      JS^\__/  qKL
     dZP        qKRb
    dZP          qKKb
   fZP            SMMb
   HZM            MMMM
   FqM            MMMM
 __| ".        |\dS"qML
 |    `.       | `' \Zq
_)      \.___.,|     .'
\____   )MMMMMP|   .'
     `-'       `--'
'''

windows_logo = r'''
        ,.=:!!t3Z3z.,                  
       :tt:::tt333EE3 
       Et:::ztt33EEEL @Ee.,      ..,    
      ;tt:::tt333EE7 ;EEEEEEttttt33#    
     :Et:::zt333EEQ. $EEEEEttttt33QL    
     it::::tt333EEF @EEEEEEttttt33F    
    ;3=*^```"*4EEV :EEEEEEttttt33@.    
    ,.=::::!t=., ` @EEEEEEtttz33QF      
   ;::::::::zt33)   "4EEEtttji3P*      
  :t::::::::tt33.:Z3z..  `` ,..g.       
  i::::::::zt33F AEEEtttt::::ztF
 ;:::::::::t33V ;EEEttttt::::t3
 E::::::::zt33L @EEEtttt::::z3F
{3=*^```"*4E3) ;EEEtttt:::::tZ`
             ` :EEEEtttt::::z7
                 "VEzjt:;;z>*`
'''
def getSystemInfo(): 
  try:
    print(windows_logo if os.name == 'nt' else linux_logo)
    print('\n')
    print('platform:'+ platform.system())
    print('platform-release:'+ platform.release()) 
    print('platform-version:'+ platform.version())
    print('architecture:'+ platform.machine()) 
    print('hostname:'+ socket.gethostname()) 
    print('ip-address:'+ socket.gethostbyname(socket.gethostname())) 
    print('mac-address:'+':'.join(re.findall('..', '%012x' % uuid.getnode())))
    print('processor:'+ platform.processor())
    print('\n'+'='*40+' advanced info '+'='*40+'\n')
    
    for item in os.environ:
      print(item + " : " + os.environ[item])
    print('\n')
  except Exception as e: logging.exception(e)

getSystemInfo()

author = '''
systest:shows advanced system info

maded by Ahmet Yigit AYDENIZ
*****************************
'''
print(author)

try:
	input('\nctrl+c or press enter key to exit\n')
except:
	exit()
