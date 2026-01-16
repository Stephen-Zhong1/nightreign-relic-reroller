from tkinter import *
from tkinter import ttk
import ast
import pyautogui
import pydirectinput
import time
import os
from pynput import keyboard
from threading import Thread
from tkinter import filedialog

path = 'C:/Users/plush/OneDrive/Documents/code/nr_perk'
perkclass = {'Attributes': ['Vigor Up', 'Mind Up', 'Endurance Up','Maximum FP Increased for each Sorcerer\'s Rise unlocked','Max FP Up with 3+ Staves','Max FP Up with 3+ Seals','Poise Up'],
            'Offensive': ['Fire Attack Power Up','Magic Attack Power Up','Holy Attack Power Up','Lightning Attack Power Up','Physical Attack Up','Improved Critical Hits','Taking attacks improves attack power','Improved Initial Standard Attack','Improved Throwing Pot Damage','Guard Counter is given a boost based on current HP','Attack power up after defeating a Night Invader'],
            'Spells': ['Improved Crystalian Sorceries','Improved Carian Sword Sorceries','Improved Glintblade Sorceries','Improved Gravity Sorceries','Improved Invisibility Sorceries','Improved Stonedigger Sorceries','Improved Thorn Sorceries','Improved Bestial Incantations','Improved Dragon Cult Incantations','Improved Dragon Communion Incantations','Improved Frenzied Flame Incantations','Improved Fundamentalist Incantations','Improved Giant\'s Flame Incantations','Improved Godslayer Incantations'],
            'Character': ['Duchess Specific Perks','Executor Specific Perks','Guardian Specific Perks','Ironeye Specific Perks','Raider Specific Perks','Recluse Specific Perks','Revenant Specific Perks','Scholar Specific Perks','Undertaker Specific Perks','Wylder Specific Perks'],
            'Starting Weapon': ['Starting armament inflicts bleed','Starting armament inflicts frost','Starting armament inflicts poison','Starting armament deals holy damage','Starting armament deals magic damage','Change armament skill to Blood Blade','Change armament skill to Determination','Change armament skill to Endure','Change armament skill to Flaming Strike','Change armament skill to Glintblade Phalanx','Change armament skill to Gravitas','Change armament skill to Hoarfrost Stomp','Change armament skill to Poison Moth\'s Flight','Change armament skill to Poisonous Mist','Change armament skill to Rain of Arrows','Change armament skill to Seppuku','Change armament skill to Storm Stomp','Change armament sorcery to Magic Glintblade','Change armament sorcery to Magma Shot','Change armament sorcery to Night Shard','Change armament incantation to Beast Claw','Change armament incantation to Lightning Spear','Change armament incantation to O\'Flame','Change armament incantation to Wrath of Gold'],
            'Weapon Specific': ['Dormant Power Helps Discover Colossal Weapons','Dormant Power Helps Discover Curved Swords','Dormant Power Helps Discover Fists','Dormant Power Helps Discover Flails','Dormant Power Helps Discover Greatbows','Dormant Power Helps Discover Great Spears','Dormant Power Helps Discover Greatshields','Dormant Power Helps Discover Hammers','Dormant Power Helps Discover Reapers','Dormant Power Helps Discover Whips'],
            'Misc': ['Begin with Small Pouch','Begin with Starlight Shards','Begin with Stonesword Key','Begin with Wraith Calling Bell','Gain Ult Charge when Killing Enemies','Ultimate Auto Charge Up','Character Skill Cooldown Reduction','Partial HP Restoration on Post-Damage Attacks','Improved Stance-Breaking when Two Handing Weapon','Stamina Recovery upon Landing Attacks','Items Confer Effect to Allies','Improved Poise and Damage Negation when Knocked Back by Attack','Slowly restore HP for self and nearby allies when HP is low']
            }
depth_perkclass = {'Attributes': ['Increased HP','Increased FP','Increased Stamina','Reduced FP Consumption','Max HP Up when clearing Great Churches','Maximum FP Increased for each Sorcerer\'s Rise unlocked','Max FP Up with 3+ Staves','Max FP Up with 3+ Seals'],
                'Offensive': ['Improved Affinity Attack Power','Fire Attack Power Up','Magic Attack Power Up','Holy Attack Power Up','Lightning Attack Power Up','Physical Attack Up','Improved Critical Hits','Taking attacks improves attack power','Improved Initial Standard Attack','Improved Throwing Pot Damage','Guard Counter is given a boost based on current HP'],
                'Defensive': ['Affinity Damage Negation','Damage Negation at Low HP','Physical Damage Negation','Improved Poise and Damage Negation when Knocked Back by Attack'],
                'Spells': ['Improved Sorceries','Improved Incantations','Improved Crystalian Sorceries','Improved Carian Sword Sorceries','Improved Glintblade Sorceries','Improved Gravity Sorceries','Improved Invisibility Sorceries','Improved Stonedigger Sorceries','Improved Thorn Sorceries','Improved Bestial Incantations','Improved Dragon Cult Incantations','Improved Dragon Communion Incantations','Improved Frenzied Flame Incantations','Improved Fundamentalist Incantations','Improved Giant\'s Flame Incantations','Improved Godslayer Incantations'],
                'Character': ['Duchess Specific Perks','Executor Specific Perks','Guardian Specific Perks','Ironeye Specific Perks','Raider Specific Perks','Recluse Specific Perks','Revenant Specific Perks','Scholar Specific Perks','Undertaker Specific Perks','Wylder Specific Perks'],
                'Weapon Specific': ['Dormant Power Helps Discover Colossal Weapons','Dormant Power Helps Discover Curved Swords','Dormant Power Helps Discover Fists','Dormant Power Helps Discover Flails','Dormant Power Helps Discover Greatbows','Dormant Power Helps Discover Great Spears','Dormant Power Helps Discover Greatshields','Dormant Power Helps Discover Hammers','Dormant Power Helps Discover Reapers','Dormant Power Helps Discover Whips'],
                'Misc': ['Begin with Small Pouch','Gain Ult Charge when Killing Enemies','Partial HP Restoration on Post-Damage Attacks','Improved Stance-Breaking when Two Handing Weapon','Stamina Recovery upon Landing Attacks','Items Confer Effect to Allies','Slowly restore HP for self and nearby allies when HP is low']
                }
perk_ids = {'Affinity Damage Negation':'affinityneg', 
            'Max HP Up when clearing Churches':'churchhp', 
            'Dormant Power Helps Discover Fists':'dormantfist',
            'Increased HP':'hpup', 
            'Damage Negation at Low HP':'lowneg', 
            'Gain Ult Charge when Killing Enemies':'moreult', 
            'Physical Damage Negation':'physneg', 
            'Partial HP Restoration on Post-Damage Attacks':'postdamagerec',
            'Improved Affinity Attack Power': 'affinityatk',
            'Improved Crystalian Sorceries': 'crystalian',
            'Improved Dragon Cult Incantations': 'dragoncult',
            'Improved Dragon Communion Incantations': 'dragonheart',
            'Duchess Specific Perks': 'duchess',
            'Fire Attack Power Up': 'fireatk',
            'Increased FP': 'fpup',
            'Reduced FP Consumption': 'fpuse',
            'Improved Fundamentalist Incantations': 'fundamental',
            'Improved Giant\'s Flame Incantations': 'giantsflame',
            'Holy Attack Power Up': 'holyatk',
            'Improved Incantations': 'incantup',
            'Magic Attack Power Up': 'magicatk',
            'Physical Attack Up': 'physatk',
            'Revenant Specific Perks': 'rev',
            'Improved Sorceries': 'sorceryup',
            'Increased Stamina': 'stamup',
            'Improved Stonedigger Sorceries': 'stonedigger',
            'Undertaker Specific Perks': 'undertaker',
            'Lightning Attack Power Up': 'lightningatk',
            'Improved Stance-Breaking when Two Handing Weapon': '2hstance',
            'Items Confer Effect to Allies': 'allyitem',
            'Change armament skill to Hoarfrost Stomp': 'ashhoarfrost',
            'Improved Bestial Incantations': 'bestial',
            'Improved Carian Sword Sorceries': 'carianatk',
            'Character Skill Cooldown Reduction': 'skillcd',
            'Stamina Recovery upon Landing Attacks': 'stamatk',
            'Endurance Up': 'endurance',
            'Guardian Specific Perks': 'guardian',
            'Mind Up': 'mind',
            'Recluse Specific Perks': 'recluse',
            'Scholar Specific Perks': 'scholar',
            'Improved Throwing Pot Damage': 'potatk',
            'Change armament incantation to O\'Flame': 'startoflame',
            'Starting armament inflicts poison': 'startpoison',
            'Vigor Up': 'vigor', 
            'Wylder Specific Perks': 'wylder',
            'Maximum FP Increased for each Sorcerer\'s Rise unlocked': 'risefp',
            'Improved Critical Hits': 'critup',
            'Taking attacks improves attack power': 'dmgatk',
            'Improved Poise and Damage Negation when Knocked Back by Attack': 'dmgtanky',
            'Dormant Power Helps Discover Greatbows': 'dormantgreatbow',
            'Dormant Power Helps Discover Great Spears': 'dormantgspear',
            'Improved Frenzied Flame Incantations': 'frenzy',
            'Guard Counter is given a boost based on current HP': 'gchpboost',
            'Improved Glintblade Sorceries': 'glintblade',
            'Improved Godslayer Incantations': 'godslayer',
            'Improved Gravity Sorceries': 'gravity',
            'Improved Initial Standard Attack': 'initialatk',
            'Attack power up after defeating a Night Invader': 'invader',
            'Improved Invisibility Sorceries': 'invisible',
            'Slowly restore HP for self and nearby allies when HP is low': 'lowhpheal',
            'Poise Up': 'poiseup',
            'Change armament skill to Poison Moth\'s Flight': 'poisonmoth',
            'Change armament skill to Rain of Arrows': 'rainofarrow',
            'Starting armament inflicts bleed': 'startbleed',
            'Change armament incantation to Beast Claw': 'startclaw',
            'Change armament skill to Endure': 'startendure',
            'Starting armament inflicts frost': 'startfrost',
            'Change armament skill to Gravitas': 'gravitas',
            'Starting armament deals holy damage': 'startholy',
            'Starting armament deals magic damage': 'startmagic',
            'Change armament sorcery to Magma Shot': 'startmagma',
            'Begin with Small Pouch': 'startpouch',
            'Change armament skill to Seppuku': 'startseppuku',
            'Change armament sorcery to Night Shard': 'startshard',
            'Change armament skill to Storm Stomp': 'startstomp',
            'Begin with Wraith Calling Bell': 'startwraiths',
            'Change armament incantation to Wrath of Gold': 'startwrath',
            'Ultimate Auto Charge Up': 'ultauto',
            'Dormant Power Helps Discover Colossal Weapons': 'dormantcolossal',
            'Dormant Power Helps Discover Curved Swords': 'dormantcurveds',
            'Dormant Power Helps Discover Flails': 'dormantflail',
            'Dormant Power Helps Discover Greatshields': 'dormantgshield',
            'Dormant Power Helps Discover Hammers': 'dormanthammer',
            'Dormant Power Helps Discover Reapers': 'dormantreaper',
            'Dormant Power Helps Discover Whips': 'dormantwhip',
            'Max FP Up with 3+ Seals': 'fpseal',
            'Max FP Up with 3+ Staves': 'fpstaves',
            'Change armament skill to Blood Blade': 'startbloodblade',
            'Change armament skill to Determination': 'startdetermination',
            'Change armament skill to Flaming Strike': 'startflamingstrike',
            'Change armament sorcery to Magic Glintblade': 'startglintblade',
            'Change armament incantation to Lightning Spear': 'startlightspear',
            'Change armament skill to Glintblade Phalanx': 'startphalanx',
            'Change armament skill to Poisonous Mist': 'startpoisonmist',
            'Begin with Stonesword Key': 'startkey',
            'Begin with Starlight Shards': 'startstarlight',
            'Improved Thorn Sorceries': 'thorn',
            'Raider Specific Perks':'raider',
            'Ironeye Specific Perks':'ironeye',
            'Executor Specific Perks':'executor',
            '':'None'}
curse_ids = {'Reduced Damage Negation after Evading': 'dmgevasion',
             'Repeated Evasions Lower Damage Negation': 'dmgevasionspam',
             'Taking Damage Causes Blood Loss Buildup': 'dmgbleed',
             'Taking Damage causes Death Buildup': 'dmgdeath',
             'Taking Damage Causes Frost Buildup': 'dmgfrost',
             'Taking Damage causes Madness Buildup': 'dmgmadness',
             'Taking Damage causes Poison Buildup': 'dmgpoison',
             'Rot Buildup when below Max HP': 'maxhprot',
             'All Resistances Down': 'resistdown',
             'Lower Attack When Below Max HP': 'atkdownhp',
             'Near Death Reduces Max HP': 'deathhpdown',
             'Continuous HP Loss': 'hploss',
             'Reduced Faith and Strength': 'faistrdown',
             'Reduced Vigor and Arcane': 'hparcdown',
             'Reduced Intelligence and Dexterity': 'intdexdown',
             'Reduced Strength and Intelligence': 'strintdown',
             'Reduced Rune Acquisition': 'runedown',
             'Ultimate Art Charging Impaired': 'ultdown',
             'Reduced Flask HP Restoration': 'flaskdown'
             }

root = Tk()
root.title("Buwum's Nightreign Relic Reroller") # root window title and dimension
root.geometry('430x300') #Set geometry (widthxheight)
root.iconphoto(True, PhotoImage(file=path+'/icon.png'))

hotbar = Frame(root)
mainframe = Frame(root)

canvas=Canvas(mainframe)
scrollbar = Scrollbar(mainframe, orient="vertical", command=canvas.yview)
scrollable_frame = Frame(canvas)

scrollable_frame.bind("<Configure>",lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
canvas.create_window((10, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

hotbar.pack()
mainframe.pack(side="left", fill="both", expand=True)
canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

num_reroll = 0
relic_type = 'Normal'
relic_only3 = FALSE
relic_confirm = TRUE
def settings():
    new_window = Toplevel(root)
    new_window.title("Settings")
    new_window.geometry("360x140")

    global relic_only3, relic_confirm
    only3 = BooleanVar()
    confirm = BooleanVar()

    T = Text(new_window, height=1, width=5)
    T.grid(row=0, column=0, padx = (0,0), pady=(0,0)) 
    T.insert(END, num_reroll)
    Label(new_window, textvariable=StringVar(value = 'Number of Times to Reroll')).grid(padx=(0,0),pady=(0,0), row=0, column=1,sticky='w')  
    
    roll_type = ttk.Combobox(new_window, values=['Normal','Depth'], width=5)
    roll_type.set(relic_type)
    roll_type.grid(row=1, column=0,sticky='w',padx=(20), pady=(10,0))  
    Label(new_window, textvariable=StringVar(value = 'Type of Relic Roll')).grid(padx=(0,0),pady=(0,0), row=1, column=1,sticky='w')  

    only3_checkbox = Checkbutton(new_window, variable=only3, onvalue=1, offvalue=0, command=None)
    only3_checkbox.grid(row=2,column=0,padx=(50,0))
    if relic_only3:
        only3_checkbox.select()
    Label(new_window, textvariable=StringVar(value = 'Auto-delete Relics without 3 Perks')).grid(row=2, column=1,sticky='w')  

    confirm_checkbox = Checkbutton(new_window, variable=confirm, onvalue=1, offvalue=0, command=None)
    confirm_checkbox.grid(row=3,column=0,padx=(50,0))
    if relic_confirm:
        confirm_checkbox.select()
    Label(new_window, textvariable=StringVar(value = 'Confirmation Window when Rolling Valid Relic')).grid(row=3, column=1,sticky='w')  

    Button(new_window, text="Confirm", command= lambda:[setting_confirm(T, roll_type, only3, confirm), new_window.destroy()]).grid(row=100,column=0,columnspan=2)

def setting_confirm(text, roll_type, only3, confirm):
    global num_reroll, relic_type, relic_only3, relic_confirm
    num_reroll = int(text.get("1.0", "end-1c"))
    relic_type = roll_type.get()
    relic_only3 = only3.get()
    relic_confirm = confirm.get()

relics = []
depths = []
relic_effects = []
relic_curses = []
def create_relic(name, load, deep):
    frame = Frame(scrollable_frame, bg='lightgray', borderwidth=2, relief = 'ridge', padx = 10)
    frame.grid(row = len(relics), column = 0, pady = (10, 0))
    relics.append(frame)
    if not load:
        relic_effects.append(['', '', ''])
        relic_curses.append([''])

    deep_frame = Frame(frame, bg='lightgray', padx = 15)
    deep_frame.grid(row=0, column = 0, pady = (10, 0))
    Label(deep_frame, bg='lightgray', textvariable=StringVar(value = 'Depth')).grid(row=0, column=0)
    depth = BooleanVar()
    confirm_checkbox = Checkbutton(deep_frame, bg='lightgray', variable=depth, onvalue=1, offvalue=0, command=None)
    confirm_checkbox.grid(row=1,column=0,padx=(0,0))
    depths.append(depth)
    if deep:
        confirm_checkbox.select()

    T = Text(frame, height = 2, width = 15)
    T.grid(row = 0, column=1, padx = (0, 10), pady = (10, 10))
    T.insert(END, name)
    Button(frame, text="Edit Relic Roll", command=lambda:[relic_popup(depth.get(), frame)]).grid(row = 0, column=2)
    Button(frame, text="Delete Relic", command=lambda:[confirm_delete(frame)]).grid(row = 0, column=3, padx = (10, 10))



def relic_popup(depth, frame):
    children = frame.winfo_children()
    for item in children:
        if isinstance(item, Text):
            name = item.get("1.0", "end-1c")

    relic_window = Toplevel(root)
    relic_window.title("Edit Relic: " + str(name))
    relic_window.geometry("560x420")

    perk_frame = Frame(relic_window, highlightbackground="blue", highlightcolor="blue", highlightthickness=5)
    perk_frame.grid(row=0,column=0, padx=(10),pady=(10))
    Label(perk_frame, textvariable=StringVar(value = 'Select Relic Perks')).grid(padx=(10,0),pady=(10), row = 0, column = 0, columnspan = 2)

    T1 = Text(perk_frame, height = 5, width = 50)
    T2 = Text(perk_frame, height = 5, width = 50)
    T3 = Text(perk_frame, height = 5, width = 50)
    T1.insert(END, relic_effects[relics.index(frame)][0])
    T2.insert(END, relic_effects[relics.index(frame)][1])
    T3.insert(END, relic_effects[relics.index(frame)][2])
    T1.grid(row = 1, column = 0, padx=(10, 10), pady = (0, 0))
    T2.grid(row = 2, column = 0, padx=(10, 10), pady = (10, 0))
    T3.grid(row = 3, column = 0, padx=(10, 10), pady = (10, 10))
    T1['state'] = DISABLED
    T2['state'] = DISABLED
    T3['state'] = DISABLED

    if depth:
        relic_window.geometry("560x570")
        curse_frame = Frame(relic_window, highlightbackground="red", highlightcolor="red", highlightthickness=5)
        curse_frame.grid(row=1,column=0, padx=(10))
        Label(curse_frame, textvariable=StringVar(value = 'Exclude Relic Curses')).grid(padx=(10,0),pady=(10), row = 0, column = 0, columnspan = 2)

        T4 = Text(curse_frame, height = 5, width = 50)
        T4.insert(END, relic_curses[relics.index(frame)])
        T4.grid(row = 1, column = 0, padx=(10, 10), pady = (0, 10))
        T4['state'] = DISABLED
        Button(curse_frame, text="Edit Relic Curses", command=lambda:[list_popup(T4, FALSE, True)]).grid(row=1, column=1, pady=(0, 0),padx = (0, 10))

        Button(perk_frame, text="Edit Relic Effects", command=lambda:[list_popup(T1, TRUE, True)]).grid(row=1, column=1, pady=(0, 0),padx = (0, 10))
        Button(perk_frame, text="Edit Relic Effects", command=lambda:[list_popup(T2, TRUE, True)]).grid(row=2, column=1, pady=(10, 0),padx = (0, 10))  
        Button(perk_frame, text="Edit Relic Effects", command=lambda:[list_popup(T3, TRUE, True)]).grid(row=3, column=1, pady=(10, 0),padx = (0, 10))

        Button(relic_window, text="Confirm", command= lambda:[save_perks(frame, perk_frame, T4), relic_window.destroy()]).grid(pady = (20, 0))
    else:
        Button(perk_frame, text="Edit Relic Effects", command=lambda:[list_popup(T1, TRUE, False)]).grid(row=1, column=1, pady=(0, 0),padx = (0, 10))
        Button(perk_frame, text="Edit Relic Effects", command=lambda:[list_popup(T2, TRUE, False)]).grid(row=2, column=1, pady=(10, 0),padx = (0, 10))  
        Button(perk_frame, text="Edit Relic Effects", command=lambda:[list_popup(T3, TRUE, False)]).grid(row=3, column=1, pady=(10, 0),padx = (0, 10))

        Button(relic_window, text="Confirm", command= lambda:[save_perks(frame, perk_frame, None), relic_window.destroy()]).grid(pady = (20, 0))


def save_perks(frame, window1, curses):
    perks = []
    children = window1.winfo_children()
    for item in children:
        if isinstance(item, Text):
            perks.append(item.get("1.0", "end-1c"))

    relic_effects[relics.index(frame)] = perks
    relic_curses[relics.index(frame)] = ['']
    try:
        if(curses.get("1.0", "end-1c") != ''):
            relic_curses[relics.index(frame)] = curses.get("1.0", "end-1c")
    except:
        pass
        


def list_popup(selected_box, perks, depth):
    new_window = Toplevel(root)
    #new_window.geometry("250x300")

    boxes = []
    if perks:
        new_window.title("Select Perks")
        new_window.geometry("450x300")

        notebook = ttk.Notebook(new_window)
        notebook.pack(pady=10, expand=True, fill='both')
        if depth:
            for perk_class in depth_perkclass.keys():
                frame = ttk.Frame(notebook)#, width=300, height=200)
                frame.pack(fill='both', expand=True)

                listbox = Listbox(frame, exportselection=False, selectmode=MULTIPLE) # Set exportselection=False
                for item in depth_perkclass[perk_class]:
                    listbox.insert(END, item)
                listbox.pack(pady=10, padx=10, fill='both', expand=True)
                boxes.append(listbox)
                
                notebook.add(frame, text=perk_class)
        else:
            for perk_class in perkclass.keys():
                frame = ttk.Frame(notebook)#, width=300, height=200)
                frame.pack(fill='both', expand=True)

                listbox = Listbox(frame, exportselection=False, selectmode=MULTIPLE) # Set exportselection=False
                for item in perkclass[perk_class]:
                    listbox.insert(END, item)
                listbox.pack(pady=10, padx=10, fill='both', expand=True)
                boxes.append(listbox)
                
                notebook.add(frame, text=perk_class)
    else:
        new_window.title("Exclude Curses")
        new_window.geometry("250x300")

        perk_listbox = Listbox(new_window, selectmode=MULTIPLE)
        perk_listbox.pack(pady=10, fill=BOTH, expand=True)
        for item in curse_ids.keys():
            perk_listbox.insert(END,item)
        
        boxes.append(perk_listbox)

    # Optional: Add a button to the new window to close it
    close_button = Button(new_window, text="Confirm", command=lambda:[new_perks(selected_box, boxes), new_window.destroy()])
    close_button.pack(pady=5)


def confirm_delete(frame):
    new_window = Toplevel(root)
    new_window.title("Confirmation")
    new_window.geometry("280x80")

    Label(new_window, textvariable=StringVar(value = 'Are you sure you want to delete your relic?')).grid(padx=(30,0),pady=(0,10), row = 0, column = 0, columnspan = 2)
    Button(new_window, text="Yes", command=lambda:[delete_relic(frame), new_window.destroy()], width=10).grid(row=1, column=0, padx=(30,0))
    Button(new_window, text="No", command=lambda:[new_window.destroy()], width=10).grid(row=1, column=1, padx=(15,0))

    

def delete_relic(frame):
    del relic_effects[relics.index(frame)]
    del relic_curses[relics.index(frame)]
    del depths[relics.index(frame)]
    del relics[relics.index(frame)]
    frame.destroy()


def new_perks(selected_box, boxes):
    selected_box['state'] = NORMAL
    selected_box.delete("1.0",END) 

    for box in boxes:
        perk_values = [box.get(idx) for idx in box.curselection()]
        for perk in perk_values:
            selected_box.insert(END, perk + '\n')

    selected_box['state'] = DISABLED #stop people from typing in it


def get_pos(img):
    img_path = os.path.join(path, img)
    try:
        x, y = pyautogui.center(pyautogui.locateOnScreen(img_path, confidence = 0.9))
        return x, y
    except pyautogui.ImageNotFoundException:
        return -1, -1
    
def perk_exist(perk):
    img_path = os.path.join(path, perk + '.png')
    try:
        pyautogui.center(pyautogui.locateOnScreen(img_path, confidence = 0.95))
        return True
    except pyautogui.ImageNotFoundException:
        return False


def click(x, y, **kwargs):
    reps = 1
    if kwargs != {}:
        reps = kwargs['reps']

    for z in range(reps):
        pydirectinput.moveTo(x, y)
        pydirectinput.mouseDown()
        time.sleep(0.1)
        pydirectinput.mouseUp()

interrupt = False
def start_rolls():
    time.sleep(1)
    global interrupt, relic_type, relic_confirm
    looking_depth = False
    if relic_type == 'Depth':
        looking_depth = True
    
    relic_posX, relic_posY = get_pos('relic.png')
    if looking_depth:
        relic_posX, relic_posY = get_pos('deeprelic.png')

    x=0
    while(x < num_reroll and not interrupt): 
        click(relic_posX, relic_posY)
        if x == 0:
            scroll_posX, scroll_posY = get_pos('scroll.png')
        click(scroll_posX, scroll_posY)
        pydirectinput.press('f')
        pyautogui.moveTo(520, 300) # move mouse to 520 300 = pos of relic 1
        pydirectinput.press('f') #rush relic buying
        
        for a in range(10):
            if relic_only3 and perk_exist('perknone'):
                pydirectinput.press('3') #user wants 3 perks but a perk is missing
                continue
            for relic_id in range(len(relic_effects)):
                if looking_depth != depths[relic_id].get(): #escape loop (stop looking at current relic) if depths does not match
                        if interrupt:
                            pyautogui.confirm('Relic Rerolling Interrupted')
                            interrupt = False
                            return
                        break
                
                valid_effects = 0
                total_effects = 0
                taken_effect = []
                for effect_list in relic_effects[relic_id]:
                    total_effects += 1
                    effects = effect_list.split('\n')
                    for effect in effects:
                        if(effects[0] != ''):
                            if(effect != 'None'):
                                if(effect not in taken_effect):
                                    if perk_exist(perk_ids[effect]): #one of the listed perks exists
                                        valid_effects += 1
                                        taken_effect.append(effect)
                                        break
                        else:
                            valid_effects += 1
                    
                    if(valid_effects != total_effects):
                        break

                if(valid_effects == 3): #check for curses
                    try:
                        curses = relic_curses[relic_id].split('\n')
                        for curse in curses:
                            if(curse != ''):
                                try:
                                    if perk_exist(curse_ids[curse]): #one of the listed curses exists
                                        pyautogui.confirm('relic ruined by curse')
                                        valid_effects -= 100
                                        break
                                except:
                                    pass
                    except:
                        pass

                if(valid_effects == 3): #this is so inelegant
                    posX, posY = pyautogui.position()
                    if relic_confirm:
                        pyautogui.confirm('Valid relic exists')
                        time.sleep(0.5)
                        pyautogui.moveTo(posX, posY)
                    print('lets go')
                    pyautogui.moveRel(175, 0)
                    valid_effects = 0
                    break
                else:
                    pydirectinput.press('3') #delete relic if it doesnt have enough perks

            if interrupt:
                pyautogui.confirm('Relic Rerolling Interrupted')
                interrupt = False
                return
            
        pydirectinput.press('f') #leave relic screen
            

        x+=1

    pyautogui.confirm('Relic Rerolling Finished')
    interrupt = False



def on_press(key):
    global interrupt
    try:
        if key.char == 'p': # Check if the pressed key is 'p'
            print('p key pressed. Stopping program...')
            interrupt = True
            time.sleep(1)
    except AttributeError:
        pass

def save_relics():
    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text files", "*.txt"), ("All files", "*.*")],
        title="Save your Relic Setup"
    )

    global num_reroll, relic_type, relic_confirm
    relic_names = []
    for relic in relics:
        children = relic.winfo_children()
        for item in children:
            if isinstance(item, Text):
                relic_names.append(item.get("1.0", "end-1c"))

    relic_depths = []
    for box in depths:
        relic_depths.append(box.get())
    
    # Check if a file path was selected (user didn't cancel)
    if file_path:
        try:
            # Your data to save
            file_content = '|'.join(relic_names)+'\n' + '|'.join(str(v) for v in relic_effects)+'\n' + '|'.join(str([v]) for v in relic_curses)+'\n'+  '|'.join(str([v]) for v in relic_depths)+'\n'+  str(num_reroll) +'\n'+ relic_type +'\n'+ str(relic_only3) +'\n'+ str(relic_confirm)
            
            # Open the file in write mode ('w') and save the content
            with open(file_path, 'w') as file:
                file.write(file_content)
            print(f"File saved successfully to: {file_path}")
        except Exception as e:
            print(e)


def load_relics():
    file_path = filedialog.askopenfilename(
        title="Select a file",
        filetypes=(("Text files", "*.txt"), ("All files", "*.*"))
    )

    if file_path:
        f = open(file_path)
        saved = f.read().split('\n')
        f.close()

        for i in range(len(saved[0].split('|'))):
            create_relic(saved[0].split('|')[i], True, ast.literal_eval(saved[3].split('|')[i].replace('[','').replace(']','')))

        global relic_effects, relic_curses
        for x in range(len(saved[1].split('|'))):
            relic_effects.append(ast.literal_eval(saved[1].split('|')[x]))
            relic_curses.append(ast.literal_eval(saved[2].split('|')[x])[0])

        global num_reroll, relic_type, relic_only3, relic_confirm
        num_reroll = int(saved[4])
        relic_type = saved[5]
        relic_only3 = ast.literal_eval(saved[6])
        relic_confirm = ast.literal_eval(saved[7])


aboutme = StringVar(value = 'Contact me here: https://discord.gg/eHFgbgkBVh.\n\nHey! I\'m Buwum and this is my Nightreign Relic Reroller tool. Over my hundreds of hours in this game mostly playing Depth 5 I\'ve accumulated millions of murk but never really got around to spending it since it took so long. I built this tool for myself to make this easier, and now I\'m sharing with the rest of the community.\n\nSay Hi if you encounter me ingame (Buwum) and good luck rerolling!')
def about():
    about_window = Toplevel(root)
    about_window.title("About Me")
    about_window.geometry("360x175")

    Label(about_window, textvariable=aboutme,wraplength="320").pack(fill='both')



Button(hotbar, text="Settings", command=settings).pack(side = 'left', pady = (0, 10))
Button(hotbar, text="New Relic Preset", command=lambda:[create_relic('New Relic', False, False)]).pack(side = 'left', pady = (0, 10))
Button(hotbar, text="Save Setup", command=save_relics).pack(side = 'left', pady = (0, 10))
Button(hotbar, text="Load Setup", command=load_relics).pack(side = 'left', pady = (0, 10))
Button(hotbar, text="Start Rolls", command=start_rolls).pack(side = 'left', pady = (0, 10))
Button(hotbar, text="More Info", command=about).pack(side = 'left', pady = (0, 10))


listener = keyboard.Listener(on_press=on_press)
listener.start()
loop_thread = Thread(target=root.mainloop(), daemon=True)
