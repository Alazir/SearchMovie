import functions as func
from kivy.app import App
from kivy.uix.gridlayout import GridLayout

my_id, key_token = func.get_apikey_devenv()

class MainLayout(GridLayout):
    pass

class SearchMovie(App):
    #pass
    def on_button_click(self):
        self.root.ids.result.text = func.request_movie(my_id, key_token, self.root.ids.input.text)

if __name__ == "__main__":
    SearchMovie().run()