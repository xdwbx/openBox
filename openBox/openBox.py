from python_imagesearch.imagesearch import imagesearch_loop
import pyautogui
import time
opened = 2755

while True:
    start = imagesearch_loop("./start.png", 1, 0.5)
    print("position : ", start[0], start[1])
    pyautogui.click(x=start[0], y=start[1])
    time.sleep(1)
    open = imagesearch_loop("./open.png", 1)
    print("position : ", open[0], open[1])
    pyautogui.click(x=open[0], y=open[1])
    time.sleep(2)
    box = imagesearch_loop("./box.png", 1)
    print("position : ", box[0], box[1])
    pyautogui.click(x=box[0], y=box[1])
    time.sleep(4)
    openall = imagesearch_loop("./openall.png", 1, 0.5)
    print("position : ", openall[0], openall[1])
    pyautogui.click(x=openall[0], y=openall[1])
    time.sleep(1)
    ok = imagesearch_loop("./ok.png", 1, 0.5)
    print("position : ", ok[0], ok[1])
    pyautogui.click(x=ok[0], y=ok[1])
    opened = opened + 1
    print ("opened: " + str(opened))




