class MadLibsGenerator:
    def Noun(self):
        self.noun=input("Enter a Noun : ")
        print("I am " + self.noun)

if __name__ == "__main__":
    app = MadLibsGenerator()
    print(app.Noun())
