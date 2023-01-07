import socket
import webbrowser
from appJar import gui

def receive_message():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("0.0.0.0", 12345))
    s.listen(1)
    print("socket created")
    conn, addr = s.accept()
    print(f"Connection from {addr}")
    # Receive and decode the message
    data = conn.recv(1024).decode()
    print(f"Received: {data}")
    # Call the appropriate function based on the message received
    if data == "Open Link 1":
        open_link_1()
    elif data == "Open Link 2":
        open_link_2()
    # Close the socket
    conn.close()
    receive_message()

def open_link_1():
    webbrowser.open("https://www.example.com/link1")

def open_link_2():
    webbrowser.open("https://www.example.com/link2")

app = gui("Listener")
print("App Running")
print("No Server Running Yet")

app.addLabel("Server Manager")
app.addLabel("Message", "---")

app.startFrame("IP INFO")
app.addLabel("Your IP", "Your IP: 192.168.0.121", 1, 2)
app.addLabel("Host IP", "Host IP: 192.168.0.79", 2, 2)
app.addIcon
