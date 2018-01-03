import time ;
import webbrowser ;

times = 3;

breaktimes = 0 ;

print ("program is start !" + time.ctime());

while(breaktimes < times):
    time.sleep(5);
    webbrowser.open("https://www.youtube.com/watch?v=lqQNWs-w0n8");
    breaktimes = breaktimes + 1;

