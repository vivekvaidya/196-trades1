from tkinter import *
from tkinter import ttk
    
root = Tk()
root.title("make money")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

firstSpot = StringVar()
secondSpot = StringVar()
thirdSpot = StringVar()
fourthSpot = StringVar()
fifthSpot = StringVar()
sixthSpot = StringVar()
seventhSpot = StringVar()
eighthSpot = StringVar()
ninthSpot = StringVar()
tenthSpot = StringVar()
eleventhSpot = StringVar()

money1_entry = ttk.Entry(mainframe, width=7, textvariable=firstSpot)
money1_entry.grid(column=2, row=1, sticky=(W, E))

money2_entry = ttk.Entry(mainframe, width=7, textvariable=secondSpot)
money2_entry.grid(column=2, row=2, sticky=(W, E))

money3_entry = ttk.Entry(mainframe, width=7, textvariable=thirdSpot)
money3_entry.grid(column=2, row=3, sticky=(W, E))

money4_entry = ttk.Entry(mainframe, width=7, textvariable=fourthSpot)
money4_entry.grid(column=2, row=4, sticky=(W, E))

money5_entry = ttk.Entry(mainframe, width=7, textvariable=fifthSpot)
money5_entry.grid(column=2, row=5, sticky=(W, E))

ttk.Label(mainframe, text = "\t").grid(column=1, row=1, sticky=W)

ttk.Label(mainframe, text="$10.05").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="$10.04").grid(column=3, row=2, sticky=W)
ttk.Label(mainframe, text="$10.03").grid(column=3, row=3, sticky=W)
ttk.Label(mainframe, text="$10.02").grid(column=3, row=4, sticky=W)
ttk.Label(mainframe, text="$10.01").grid(column=3, row=5, sticky=W)

money6_entry = ttk.Entry(mainframe, width=7, textvariable=sixthSpot)
money6_entry.grid(column=3, row=6, sticky=(W, E))

money7_entry = ttk.Entry(mainframe, width=7, textvariable=seventhSpot)
money7_entry.grid(column=3, row=7, sticky=(W, E))

money8_entry = ttk.Entry(mainframe, width=7, textvariable=eighthSpot)
money8_entry.grid(column=3, row=8, sticky=(W, E))

money9_entry = ttk.Entry(mainframe, width=7, textvariable=ninthSpot)
money9_entry.grid(column=3, row=9, sticky=(W, E))

money10_entry = ttk.Entry(mainframe, width=7, textvariable=tenthSpot)
money10_entry.grid(column=3, row=10, sticky=(W, E))

money11_entry = ttk.Entry(mainframe, width=7, textvariable=eleventhSpot)
money11_entry.grid(column=3, row=11, sticky=(W, E))

ttk.Label(mainframe, text = "\t").grid(column=1, row=1, sticky=W)

ttk.Label(mainframe, text="$10.00").grid(column=2, row=6, sticky=W)
ttk.Label(mainframe, text="$9.99").grid(column=2, row=7, sticky=W)
ttk.Label(mainframe, text="$9.98").grid(column=2, row=8, sticky=W)
ttk.Label(mainframe, text="$9.97").grid(column=2, row=9, sticky=W)
ttk.Label(mainframe, text="$9.96").grid(column=2, row=10, sticky=W)
ttk.Label(mainframe, text="$9.95").grid(column=2, row=11, sticky=W)

ttk.Button(mainframe, text="make money").grid(column=4, row=11, sticky=W)

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

money1_entry.focus()
#root.bind('<Return>', calculate)

root.mainloop()
