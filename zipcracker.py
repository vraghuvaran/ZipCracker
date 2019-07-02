import zipfile
import optparse
import threading
import os
import sys
import subprocess


R = '\033[31m' # red
G = '\033[32m' # green
C = '\033[36m' # cyan
W = '\033[0;47m'  # white Background
B = '\033[94m' #blue
BOLD = '\033[1m' 
ENDC = '\033[0m'
M='\033[35m' #magenta 



version='1.0'
c=False

def test(z,x):
    
   global c   

   try:
      z.extractall(pwd=x)
      print('[+] '+BOLD+B+'passwd found : '+M+x+ENDC)
      c=True
   except:
      pass


def banner():

   os.system('clear')
   
   print '############################################################################################'
   print '#     __ __        __        __ __   ___                 ___ __         __ __   __         #'
   print '#          /   |  |  \      /       |   \      /\       /        |  /  |       |   \       #'
   print '#         /    |  |   |    |        |    |    /  \     |         | /   |       |    |      #'
   print '#        /     |  |__/     |        |___/    /__ _\    |         |/    |__ __  |__ /       #'
   print '#       /      |  |        |        | \     /      \   |         |\    |       | \         #'
   print '#      /       |  |        |        |  \   /        \  |         | \   |       |  \        #'
   print '#     /__ __   |  |         \__ __  |   \ /          \  \___ __  |  \  |__ __  |   \       #'
   print '#                                                                                          #'         
   print '############################################################################################'

   print ('\n' + G + '[>]' + C + ' Created By : ' + BOLD+ 'raghuvaran_guptha'+ENDC)
   print (G + '[>]' + C + ' Version    : ' + BOLD+ version +ENDC+ '\n')

def main():

   banner()
   parser=optparse.OptionParser(usage=" %prog [options] -f <filename> -d <dictionay file>",version="%prog 1.0")
   parser.add_option('-f','--file',dest='zfile',help='specify the zipfile')
   parser.add_option('-d','--dict',dest='zdict',help='specify the dictionary')
   (values,keys)=parser.parse_args()
   zfile=values.zfile
   zdict=values.zdict
   if (zfile==None) | (zdict==None):
       #os.system('python '+sys.argv[0]+' -h')   --->Not recommended to use
       subprocess.call('python '+sys.argv[0]+' -h',shell=True)  #It's recommended to use
       exit(0)
   else:
       f=open(zdict,'r')
       z=zipfile.ZipFile(zfile)
       for x in f.readlines():
           if c==False:
              x=x.strip('\n')
              t=threading.Thread(target=test,args=(z,x))
              t.start()
       t.join() 
       if c==False:
           print '[-] '+R+'Password Not Found' 
  
if __name__=='__main__':
   main()