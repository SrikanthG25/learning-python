import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
'''

#label
class chat(App):
    def click(self,instance,value):
        print("to click")
    def build(self):
        l= Label(text = "[color=#E90CEC][i]Welcome[/i][/color] to our [color=#0CECDF][b]python[/b][/color] [ref=application]Application[/ref]",font_size="50sp",markup=True)
        l.bind(on_ref_press = self.click) #to take action of button
        return l 
k=chat()
k.run()

'''
#button 
class welcome(App):
    def build(self):
        return Button()
if __name__ == "__main__":
    welcome().run()