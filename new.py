from tkinter import* 
from tkinter import messagebox
window = Tk()
window.title("CSI POLYTECHNIC COLLEGE")
def show_option(option):
    messagebox.showinfo("Selected Option", f"You selected: {option}")
menubar = Menu(window)
window.config(menu=menubar)
home_menu = Menu(menubar, tearoff=0)
courses_menu = Menu(menubar, tearoff=0)
eligibility_menu = Menu(menubar, tearoff=0)
features_menu = Menu(menubar, tearoff=0)
infrastructure_menu = Menu(menubar, tearoff=0)
placements_menu = Menu(menubar, tearoff=0)
staff_menu = Menu(menubar, tearoff=0)
contact_menu = Menu(menubar, tearoff=0)
home_menu.add_command(label="Home", command=lambda: show_option("Home"))
courses_menu.add_command(label="Courses", command=lambda: show_option("Courses"))
eligibility_menu.add_command(label="Eligibility", command=lambda: show_option("Eligibility"))
features_menu.add_command(label="Features", command=lambda: show_option("Features"))
infrastructure_menu.add_command(label="Infrastructure", command=lambda: show_option("Infrastructure"))
placements_menu.add_command(label="Placements", command=lambda: show_option("Placements"))
staff_menu.add_command(label="Staff Detail", command=lambda: show_option("Staff Detail"))
contact_menu.add_command(label="Contact Detail", command=lambda: show_option("Contact Detail"))
menubar.add_cascade(label="Home", menu=home_menu)
menubar.add_cascade(label="Courses", menu=courses_menu)
menubar.add_cascade(label="Eligibility", menu=eligibility_menu)
menubar.add_cascade(label="Features", menu=features_menu)
menubar.add_cascade(label="Infrastructure", menu=infrastructure_menu)
menubar.add_cascade(label="Placements", menu=placements_menu)
menubar.add_cascade(label="Staff", menu=staff_menu)
menubar.add_cascade(label="Contact", menu=contact_menu)
window.mainloop()