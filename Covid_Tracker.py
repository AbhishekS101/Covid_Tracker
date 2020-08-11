from tkinter import *


from covid import Covid
import re

global exp
exp = ""


def reg(s):
    z = 0
    sol = re.findall(r"[Id:]([0-9]{2,})[Name]", s)
    for i in sol:
        z = i
    # return 'The country selelected is '+s.rsplit(':', 1)[1]+' with Id is: '+z
    return z


def cov(s):
    co = Covid()
    lst=[]
    case = co.get_status_by_country_id(s)
    global exp
    exp = ""
    for p in case:
        if p == 'id':
            exp = str(case[p])
            textid.set(exp)
            exp = ""
        if p =='country':
            exp = str(case[p])
            textc.set(exp)
            exp = ""
        if p == 'confirmed':
            exp = str(case[p])
            textcon.set(exp)
            exp = " "
        if p == 'active':
            exp = str(case[p])
            textact.set(exp)
            exp = ""
        if p == 'recovered':
            exp = str(case[p])
            textreco.set(exp)
            exp = ""
        if p == 'deaths':
            exp = str(case[p])
            textdet.set(exp)
            exp = ""


OptionList = []
with open('new_lst.txt', 'r') as file:
    for i in file:
        OptionList.append(i)


app = Tk()

app.title("Covid Tracker")
app.geometry('250x400')

variable = StringVar(app)
variable.set(OptionList[0])

opt = OptionMenu(app, variable, *OptionList)
opt.config(font=('Helvetica', 12))
opt.grid(row=0,column=0,sticky='ew',padx=40)

global textid
textid = StringVar()
global textc
textc = StringVar()
global textdet
textdet = StringVar()
global textact
textact = StringVar()
global textcon
textcon = StringVar()
global textreco
textreco = StringVar()

labelTest = Label(text="", font=('Helvetica', 12), fg='red')
labelTest.grid(row=1,column=0,sticky='ew',columnspan=10)

labelid = Label(text="ID", font=('Helvetica', 12), fg='black')
labelid.grid(row=2,column=0,sticky='ew')

IDENTRY = Entry(app, textvariable=textid,justify='center')
IDENTRY.grid(row=3,column=0,sticky='ew')

labelc = Label(text="Country", font=('Helvetica', 12), fg='black')
labelc.grid(row=4,column=0,sticky='ew')
cENTRY = Entry(app, textvariable=textc,justify='center')
cENTRY.grid(row=5,column=0,sticky='ew')

labelcon = Label(text="Confirmed Cases", font=('Helvetica', 12), fg='black')
labelcon.grid(row=6,column=0,sticky='ew')
conENTRY = Entry(app, textvariable=textcon,justify='center')
conENTRY.grid(row=7,column=0,sticky='ew')

labelact = Label(text="Active Cases", font=('Helvetica', 12), fg='black')
labelact.grid(row=8,column=0,sticky='ew')
act = Entry(app, textvariable=textact,justify='center')
act.grid(row=9,column=0,sticky='ew')

rec = Label(text="Recovered", font=('Helvetica', 12), fg='black')
rec.grid(row=10,column=0,sticky='ew')
reco = Entry(app, textvariable=textreco,justify='center')
reco.grid(row=11,column=0,sticky='ew')

deth = Label(text="Deaths", font=('Helvetica', 12), fg='black')
deth.grid(row=12,column=0,sticky='ew')
det = Entry(app, textvariable=textdet,justify='center')
det.grid(row=13,column=0,sticky='ew')


def callback(*args):
    s = reg(variable.get())
    cov(int(s))

variable.trace("w", callback)

app.mainloop()


