import os

class NewMenu:
    def __init__(self,file=None,parent_menu="default"):
        self.file = file
        self.parent_menu = parent_menu
        self.attributes = {
            "title":"Example Title",
            "desc":"Example Description",
            "options":{}
                           }

    def set_title(self,new_title):
        self.attributes["title"] = str(new_title)

    def add_command(self,text,function,*args):
        self.attributes["options"][text] = [function]
        self.attributes["options"][text].extend(args)

    def display(self,choice):
        if "all" in choice:
            print(self.attributes["title"])
            print(self.attributes["desc"])
            counter = 0
            for i in self.attributes["options"]:
                counter += 1
                print(str(counter) + " - " + str(i))
        else:
            if "title" in choice:
                print(self.attributes["title"])

            if "desc" in choice:
                print(self.attributes["desc"])

            if "options" in choice:
                counter = 0
                for i in self.attributes["options"]:
                    counter += 1
                    print(str(counter) + " - " + str(i))

    def await_input(self):
        user_input = int(input("> "))
        for i in range(len(self.attributes["options"])):
            if (i+1) == int(user_input) and (self.attributes["options"][list(self.attributes["options"])[i]][0] != "expression"):
                self.attributes["options"][list(self.attributes["options"])[i]][0](self.attributes["options"][list(self.attributes["options"])[i]][1:][0])
                break
            if self.attributes["options"][list(self.attributes["options"])[i]][0] == "expression":
                exec(self.attributes["options"][list(self.attributes["options"])[i]][1])

    def show(self):
        self.display(["title","options"])
        self.await_input()

    def loop(self,condition=1):
        while condition:
            self.display(["title","options"])
            self.await_input()
            os.system("pause")
            os.system("cls")


    

menu = NewMenu()
menu.set_title("Example New Title")
menu.add_command("Do the command that prints \"Hello World\"",print,"Hello World")
menu.add_command("Do the command that print list",print,["hello",123])
menu.add_command("Set variable x to 5","statement","x=5")
menu.add_command("Print variable x","expression","print(x)")
menu.loop()
