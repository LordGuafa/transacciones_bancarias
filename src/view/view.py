
class View:
    
    def show(self, text: str):
        print(text)

    def write(self) ->str:
        text = input()
        return text
    
    def write(self,text:str) ->int:
        number = int(input(text))
        return number
