from argparse import ArgumentParser
import random

class MelodyWriter():
    def __init__(self):
        self.header = "\\version \"2.20.0\"\n{\n"
        self.footer = "\n}\n"
        self.notes = ["b","c'","d'","e'","f'","g'","a'"]
        self.stable = [1,3,5]
        self.strong = True
        self.position = 1
        self.filename = "out.txt"

    def printnote(self,s,x,stbl):
        self.file.write(f"{x}8 ")
        if (s and not stbl):
            print("!!! error")

    def generate_variants(self):
        v = [*self.stable, self.position + 1,self.position + 1,self.position + 1, self.position - 1,self.position - 1,self.position - 1]
        return v

    def write(self, number):
        self.file = open(self.filename, "w")
        self.file.write(self.header)
        random.seed()
        for i in range(0,number):
            self.printnote(self.strong, self.notes[self.position], self.position in self.stable)
            variants = []
            if (self.position in self.stable):
                if (self.strong):
                    variants = self.generate_variants()
                else:
                    variants = self.stable
            else:
                if (self.position > 0 and ((self.position - 1) in self.stable)):
                    variants.append(self.position - 1)
                if (self.position < 6 and ((self.position + 1) in self.stable)):
                    variants.append(self.position + 1)
            
            self.position = random.choice(variants)
            
            self.strong = not self.strong
        self.file.write(self.footer)
        self.file.close()

def main():
    parser = ArgumentParser()
    parser.add_argument("-s", "--scale", dest="scale", default="b c' d' e' f' g' a'")
    parser.add_argument("-l", "--length", dest="len", default=100)
    parser.add_argument("-o", "--output", dest="len", default="out.txt")
    args = parser.parse_args()
    writer = MelodyWriter()
    writer.notes = args.scale.split(" ")
    writer.notes = args.scale.split(" ")

    writer.write(100)
    return 1

if __name__ == "__main__":
    main()
