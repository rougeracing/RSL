from appJar import gui
import socket


# Extract the IP addresses using regular expressions


def send_content(btn):
    # Get the selected options from the app
    ip_address = app.getOptionBox("IP Address")

    # Send the content based on the selected type
    if btn == "Update Drivers":
        data = "UPD"
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip_address, 12345))
        s.sendall(data.encode())
        s.close()
    if btn == "Restart":
        # Send a link
        data = "RST"
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip_address, 12345))
        s.sendall(data.encode())
        s.close()
    if btn == "Custom Shaders Patch":
        data = "CSP"
    if btn == "Open Sigma":
        data = "SIG"
    if btn == "Test":
        data = "TET"
    if btn == "Shut Down":
        data = "SHT"


app = gui()
app.addLabelEntry("Message")
app.addButton("Restart", send_content)
app.addButton("Shut Down", send_content)
app.addButton("Update Drivers", send_content)
app.addOptionBox("IP Address",["192.168.1.56","192.168.1.12"])
app.go()