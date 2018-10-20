from tkinter import *
import math
import requests
import xmltodict

def station():
    Gebruiker_station = entry.get()
    auth_details = ('janpaulmoolen99@gmail.com', 'BL03juvmVIkzP65x1p8F4iTokVclbRUFv04Icuejr3GW45fGPLsnEA')
    api_url = 'http://webservices.ns.nl/ns-api-avt?station={}'.format(Gebruiker_station)
    response = requests.get(api_url, auth=auth_details)

    vertrekXML = xmltodict.parse(response.text)
    print('Dit zijn de vertrekkende treinen:')

    for vertrek in vertrekXML['ActueleVertrekTijden']['VertrekkendeTrein']:
        eindbestemming = vertrek['EindBestemming']

        vertrektijd = vertrek['VertrekTijd']  # 2016-09-27T18:36:00+0200
        vertrektijd = vertrektijd[11:16]  # 18:36
        vertrekspoor = vertrek['VertrekSpoor']
        treintype = vertrek['TreinSoort']
        if '#text' in vertrekspoor:
            print('Om ' + vertrektijd + ' vertrekt een trein naar ' + eindbestemming + ' en deze trein vertrekt vanaf spoor {0} en het is een {1}'.format(vertrekspoor[('#text')], treintype))
root = Tk()

label = Label(master=root,text='voer een station in voor de reisinformatie',height=2)
label.pack()

button = Button(master=root, text='reisinformatie ophalen', command=station)
button.pack(side=RIGHT, pady=5)

entry = Entry(master=root)
entry.pack(side=TOP, padx=20, pady=20)

root.mainloop()
