import time,subprocess,webbrowser
timeleft = int(input('enter you countdown: '))
while timeleft > 0:
    print(timeleft, end=' \n')
    time.sleep(1)
    timeleft = timeleft -1

subprocess.Popen(['start', 'alarm.wav'], shell = True)
