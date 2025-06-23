import tkinter as tk
from tkinter import font
from tkcalendar import DateEntry
from tkinter import filedialog
import save_article

# Initialize the main window
window = tk.Tk()
window.title("BeanPyPacker")
window.geometry("600x400")
window.minsize(width=600, height=650)

# Fonts
InstructionsFont = font.Font(family="Comic Sans", size=12)
NoteFont = font.Font(family="Comic Sans", size=10)

def validate_input(new_value):
    if new_value.isdigit(1,2,3,4,5) or new_value == "":
        return True
    return False

# Instructions Label
Instructions = tk.Label(text="Voici le portail officiel pour les articles du site web du journal etudiant", font=InstructionsFont, wraplength=400)
Instructions.grid(row=0, column=0, columnspan=2, padx=10, pady=5)

# Title Entry
Titre = tk.Label(text="Mettez le titre", font=InstructionsFont)
Titre.grid(row=1, column=0, padx=10, pady=5, sticky='w')
TitleEntry = tk.Entry()
TitleEntry.grid(row=1, column=1, padx=10, pady=5, sticky='e')

# Description Entry
Description = tk.Label(text="Mettez une brève description", font=InstructionsFont)
Description.grid(row=2, column=0, padx=10, pady=5, sticky='w')
DescriptionEntry = tk.Entry()
DescriptionEntry.grid(row=2, column=1, padx=10, pady=5, sticky='e')

# Article Content Entry
ArticleContenu = tk.Label(text="Mettez le contenu de l'article", font=InstructionsFont)
ArticleContenu.grid(row=3, column=0, padx=10, pady=5, sticky='W')
ArticleContenuTip = tk.Label(text="Vous pouvez mettre du contenu HTML!", fg="grey", font=NoteFont, wraplength=400)
ArticleContenuTip.grid(row=4, column=0, columnspan=2, padx=10, pady=5)
ArticleContentInput = tk.Text(height=10, width=8)  # Set height and width
ArticleContentInput.grid(row=3, column=1, columnspan=1, padx=10, pady=5, sticky='EW')

# Program Selection
Programe = tk.Label(text="Selectionez votre programme", font=InstructionsFont)
Programe.grid(row=6, column=0, padx=10, pady=5, sticky='w')

program_selectione_option = tk.StringVar()
program_selectione_option.set("Choisissez votre programme")
programes_options = ["PEI", "Exploraction", "Classe Specialisés", "Classes d'acceuil", "Groupes TSA"]

dropdown = tk.OptionMenu(window, program_selectione_option, *programes_options)
dropdown.grid(row=6, column=1, padx=10, pady=5)

# Journalist Name Entry
journaliste_name = tk.Label(text="Mettez votre nom", font=InstructionsFont)
journaliste_name.grid(row=7, column=0, padx=10, pady=5, sticky='w')
journaliste_name_entry = tk.Entry()
journaliste_name_entry.grid(row=7, column=1, padx=10, pady=5, sticky='e')

# Publication Date Entry
date_publication_tip = tk.Label(text="Mettez la date de publication", font=InstructionsFont)
date_publication_tip.grid(row=8, column=0, padx=10, pady=5, sticky='w')
date_publication = DateEntry(window)
date_publication.grid(row=8, column=1, padx=10, pady=5, sticky='e')

img_upload_tip = tk.Label(text="Choisisez votre image", font=InstructionsFont)
img_upload_tip.grid(row=9, column=0, padx=10, pady=5, sticky='w')
img_url = ""  # Initialize img_url globally

def upload_file():
    global img_url  # Declare img_url as global
    file_types = [("Image Files", "*.jpg;*.png")]
    file_name = filedialog.askopenfilename(filetypes=file_types)
    if file_name:
        img_url = file_name  # Assign the selected file path to the global variable

upload_button = tk.Button(window, text="Telechargement", command=upload_file)
upload_button.grid(row=9, column=1, padx=10, pady=5, sticky='e')
alt_text = tk.Label(text="Mettez le texte alternatif pour votre image", font=InstructionsFont)
alt_text.grid(row=11, column=0, padx=10, pady=5, sticky='w')
alt_text_entry = tk.Entry()
alt_text_entry.grid(row=11, column=1, padx=10, pady=5, sticky='e')

niveau_scolaire = tk.Label(text="Niveau scolaire", font=InstructionsFont)
niveau_scolaire.grid(row=12, column=0, padx=10, pady=5, sticky='w')
vcmd = window.register(validate_input)
niveau_entry = tk.Entry(window, validate="key", validatecommand=(vcmd, '%P'))
niveau_entry.grid(row=12, column=1, padx=10, pady=5, sticky='e')

def on_submit():
    title = TitleEntry.get()
    description = DescriptionEntry.get()
    content = ArticleContentInput.get("1.0", tk.END)
    name = journaliste_name_entry.get()
    program = program_selectione_option.get()
    level = niveau_entry.get()
    image = img_url
    date = date_publication.get()
    image_alt = alt_text_entry.get()

    save_article.save_article(title, description, content, name, program, level, image, date, image_alt)

submit_button = tk.Button(window, text="Valider", command=on_submit)
submit_button.grid(row=13, column=0, padx=10, pady=5, sticky='w')

window.mainloop()
