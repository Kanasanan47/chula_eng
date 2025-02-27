import tkinter as tk
import random

# Thai consonants and their names
thai_consonants = [
    ("ก", "gor gai"), ("\u0e02", "khor khai"), ("\u0e04", "khor kua"),
    ("\u0e06", "khor rakhang"), ("\u0e07", "ngor ngu"), ("\u0e08", "jor jaan"),
    ("\u0e0a", "chor chang"), ("\u0e0c", "chor ching"), ("\u0e0e", "chor choe"),
    ("\u0e10", "yor ying"), ("\u0e14", "dor dek"), ("\u0e16", "tor tao"),
    ("\u0e18", "thor than"), ("\u0e1a", "nor nen"), ("\u0e1c", "dor cha da"),
    ("\u0e1e", "por pla"), ("\u0e20", "for fan"), ("\u0e22", "yor yak"),
    ("\u0e24", "ror ruea"), ("\u0e26", "lor ling"), ("\u0e28", "sor sua"),
    ("\u0e2a", "sor sala"), ("\u0e2c", "sor rue si"), ("\u0e2e", "hor nok huk")
]

class FlashcardApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Thai Consonant Flashcards")
        self.root.geometry("400x300")
        
        self.card_frame = tk.Frame(root, width=400, height=300, bg="white")
        self.card_frame.pack(expand=True, fill="both")
        
        self.label = tk.Label(self.card_frame, text="", font=("Arial", 50), bg="white")
        self.label.pack(expand=True)
        
        self.card_frame.bind("<Button-1>", self.flip_card)
        self.new_card()
        
    def new_card(self):
        self.current_card = random.choice(thai_consonants)
        self.label.config(text=self.current_card[0], font=("Arial", 100), fg="black")
        self.is_flipped = False

    def flip_card(self, event):
        if self.is_flipped:
            self.new_card()
        else:
            self.label.config(text=self.current_card[1], font=("Arial", 30), fg="blue")
            self.is_flipped = True

if __name__ == "__main__":
    root = tk.Tk()
    app = FlashcardApp(root)
    root.mainloop()