# from kivy.app import App
# from kivy import animation
# from kivy.uix.label import Label
# from kivy.uix.image import Image
# class MainApp(App):
# 	def build(self):
# 		label = Label(text = "Hello from Kivy ",size_hint=(.5 , .5) , pos_hint={'center_x': 0.5 , 'center_y':0.5} )
# 		imag = Image(source="C:\\Users\\Kavitha\\Desktop\\zeus.png",size_hint=(1, 1) , pos_hint={'center_x': 0.5 , 'center_y':0.5})
# 		return imag
# 		return label
# if __name__ == '__main__':
# 	app = MainApp()
# 	app.run()
import kivy
import random
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.app import App
from matplotlib import pyplot as plt
from kivy.uix.image import Image

red  = [1,0,0,1]
green  = [0,1,0,1]
blue = [0, 0 ,1 ,1 ]
purple= [1, 0 , 1,1]

class HBoxLayout(App):
	def build(self):
		title = "Name"
		layout = BoxLayout(padding = 10)
		colors = [red , green , blue , purple]
		for i in range(5):
			btn = Button(text = 'Button #%s '%str(i+1) , background_color = random.choice(colors))

			layout.add_widget(btn)
		
		return layout	

		def on_press_button(self, instance):
			print("You pressed the button!")

if __name__=='__main__':
	app = HBoxLayout()
	app.run()


