import socket
import webbrowser
import pyautogui
from appJar import gui

def receive_message():
    # Create a socket and listen for incoming connections
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("0.0.0.0", 12345))
    s.listen(1)

    # Accept a connection
    conn, addr = s.accept()
    print(f"Connection from {addr}")
    # Receive and decode the message
    data = conn.recv(1024).decode()
    print(f"Received: {data}")
    if data == "UPD":
        webbrowser.open_new_tab("https://us.download.nvidia.com/Windows/528.02/528.02-desktop-win10-win11-64bit-international-dch-whql.exe")
    if data == "CSP":
        pyautogui.hotkey('win')
        pyautogui.sleep(1)
        pyautogui.typewrite('content manager')
        pyautogui.press('enter')
    elif data == "RST":
        print("Ressetting PC")
        pyautogui.hotkey('win')
        pyautogui.sleep(4) 
        pyautogui.typewrite('restart pc')
    
    if data == "SIG":
        pyautogui.hotkey('win')
        pyautogui.sleep(1)
        pyautogui.typewrite('sigma simulation')
        pyautogui.press('enter')
    if data == "TET":
        webbrowser.Mozilla.open("https://www.youtube.com/watch?v=0JcM8jLAfdo")
    
    # Open a message window with the received message
    app = gui("Message")
    app.infoBox("Message Received", f"From{addr}")
    conn.close()
    receive_message()

    
# Create a loop to continuously listen for incoming connections
while True:
    receive_message()