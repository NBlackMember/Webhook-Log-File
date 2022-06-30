from dhooks import Webhook, Embed
import time
import psutil
import socket

#Ganti Data Kalian Disini
hook = Webhook("Paste Webhook Kalian Disini Kontol")
filedata = 'Filenya ditulis disini Memek'


def readfile():
    with open(filedata, "r") as t:
        read = t.readlines()
    return read

def sendembed():
    embed = Embed(color=0x5CDBF0)
    embed.set_author(name='Bot And System Info')
    embed.add_field(name=str(wibu), value='=========================================================', inline='false')
    embed.add_field(name='CPU', value=str(cpu), inline='true')
    embed.add_field(name='MEMORY', value=str(ram), inline='true')
    embed.add_field(name='IP', value=str(ip), inline='false')
    embed.set_footer(text='By Nitroz#8329') #lu ganti ini gw heck luwh
    hook.send(embed=embed)

hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)
before = readfile()
while True:
    cpu1 = psutil.cpu_percent(interval=1)
    ram1 = psutil.virtual_memory().percent
    percent = '%'
    cpu = str(cpu1) + percent
    ram = str(ram1) + percent
    after = readfile()
    if before != after:
        for line in after:
            if line not in before:
                with open(filedata, "r") as tzy:
                    for wibu in tzy:
                        pass
                for kelas in range(1):
                    print(wibu)
                    try:
                        sendembed()
                    except Exception: 
                        pass
        before = after