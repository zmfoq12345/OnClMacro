from datetime import datetime
import pyperclip, pyautogui
import time

s = input("출석 체크 해야 할 시간 입력\nex)10시 10분 부터 3교시 동안 =>10 10 3\n오후는 13~\n").split(" ")
hours = [ int(s[0]) + x for x in range(0, int(s[2]))]
mins = int(s[1])
cnt = len(hours)

print(hours)

while cnt>0:
    now = datetime.now() 
    nhour = now.hour
    nmin = now.minute
    print(nhour, nmin)

    if (nmin == mins and (nhour in hours)):
        print("CHECK after 3sec")
        time.sleep(3)
        pyperclip.copy("출석합니다.")
        pyautogui.hotkey("ctrl", "v")
        pyautogui.press('enter')
        cnt -= 1
        print("success!")
        time.sleep(57) 
    time.sleep(60)