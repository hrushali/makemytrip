from tkinter import Tk, Label, Entry, Button, StringVar, Scrollbar, Text, OptionMenu, END
from googletrans import Translator

class TranslationApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Language Translator")

        self.translator = Translator()
        self.language = {"bn": "Bangla", "en": "English", "ko": "Korean", "fr": "French",
                         "de": "German", "he": "Hebrew", "hi": "Hindi", "it": "Italian",
                         "ja": "Japanese", 'la': "Latin", "ms": "Malay", "ne": "Nepali",
                         "ru": "Russian", "ar": "Arabic", "zh": "Chinese", "es": "Spanish",
                         "mr": "Marathi"}  # Added Marathi

        self.allow = True

        # Language selection frame
        self.lang_frame = Label(master, text="Language:")
        self.lang_frame.grid(row=0, column=0, padx=10, pady=10)

        self.selected_lang = StringVar(master)
        self.selected_lang.set("English")  # Default language
        self.lang_dropdown = OptionMenu(master, self.selected_lang, *list(self.language.values()))
        self.lang_dropdown.grid(row=0, column=1, padx=10, pady=10)

        self.lang_button = Button(master, text="Submit", command=self.validate_language)
        self.lang_button.grid(row=0, column=2, padx=10, pady=10)

        # Text input and translation frame
        self.text_frame = Label(master, text="Enter Text:")
        self.text_frame.grid(row=1, column=0, padx=10, pady=10)

        self.text_entry = Entry(master)
        self.text_entry.grid(row=1, column=1, padx=10, pady=10)

        self.translate_button = Button(master, text="Translate", command=self.translate_text)
        self.translate_button.grid(row=1, column=2, padx=10, pady=10)

        self.clear_button = Button(master, text="Clear", command=self.clear_fields)
        self.clear_button.grid(row=1, column=3, padx=10, pady=10)

        # Output frame
        self.output_frame = Text(master, height=6, width=40, wrap='word')
        self.output_frame.grid(row=2, column=0, columnspan=4, padx=10, pady=10)

        self.scrollbar = Scrollbar(master, command=self.output_frame.yview)
        self.scrollbar.grid(row=2, column=4, sticky='nsew')

        self.output_frame['yscrollcommand'] = self.scrollbar.set

        # Exit button
        self.exit_button = Button(master, text="Exit", command=self.master.destroy)
        self.exit_button.grid(row=3, column=2, pady=10)

    def validate_language(self):
        selected_lang = self.selected_lang.get()
        if selected_lang.lower() == "options":
            self.output_frame.delete(1.0, END)
            self.output_frame.insert(END, "Code : Language\n")
            for code, language in self.language.items():
                self.output_frame.insert(END, f"{code} => {language}\n")
        else:
            self.allow = False
            self.output_frame.delete(1.0, END)
            self.output_frame.insert(END, f"You have selected {selected_lang}")

    def translate_text(self):
        if not self.allow:
            text_to_translate = self.text_entry.get()
            if text_to_translate.lower() == "close":
                self.output_frame.delete(1.0, END)
                self.output_frame.insert(END, "Have a nice day!")
                self.master.after(2000, self.master.destroy)
            else:
                try:
                    lang_code = [code for code, lang in self.language.items() if lang == self.selected_lang.get()][0]
                    translated = self.translator.translate(text_to_translate, dest=lang_code)
                    self.output_frame.delete(1.0, END)
                    self.output_frame.insert(END, f"{self.selected_lang.get()} translation: {translated.text}\n")
                    self.output_frame.insert(END, f"Pronunciation: {translated.pronunciation}\n")
                    self.output_frame.insert(END, f"Translated from: {self.language[translated.src]}\n")
                except Exception as e:
                    print(f"Error: {e}")
                    self.output_frame.delete(1.0, END)
                    self.output_frame.insert(END, f"Error: {e}")

    def clear_fields(self):
        self.text_entry.delete(0, END)
        self.output_frame.delete(1.0, END)
        self.allow = True

if __name__ == "__main__":
    root = Tk()
    app = TranslationApp(root)
    root.mainloop()
