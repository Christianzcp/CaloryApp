
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class MainScreen(BoxLayout):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(orientation='vertical', **kwargs)
        
        self.add_widget(Label(text="Desayuno 🍳", font_size='20sp'))
        self.add_widget(Label(text="Almuerzo 🍝", font_size='20sp'))
        self.add_widget(Label(text="Cena 🍲", font_size='20sp'))
        self.add_widget(Label(text="Aperitivos 🍪", font_size='20sp'))

        camera_button = Button(text="📷 Tomar/Seleccionar Foto", font_size='18sp', size_hint=(1, 0.2))
        camera_button.bind(on_press=self.open_camera)
        self.add_widget(camera_button)

    def open_camera(self, instance):
        print("Abrir cámara o galería (lógica por implementar).")

class CaloryApp(App):
    def build(self):
        return MainScreen()

if __name__ == "__main__":
    CaloryApp().run()
