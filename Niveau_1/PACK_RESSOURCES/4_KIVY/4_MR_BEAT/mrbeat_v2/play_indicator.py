from kivy.metrics import dp
from kivy.properties import NumericProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.togglebutton import ToggleButton


class PlayIndicatorButton(ToggleButton):
    pass


class PlayIndicatorWidget(BoxLayout):
    nb_steps = 0
    buttons = []
    left_align = NumericProperty(0)

    def set_current_step_index(self, index):
        if index >= len(self.buttons):
            return
        for i in range(0, len(self.buttons)):
            button = self.buttons[i]
            if i == index:
                button.state = "down"
            else:
                button.state = "normal"

    def set_nb_steps(self, nb_steps):
        if not nb_steps == self.nb_steps:
            # Reconstruire notre layout -> mettre les boutons
            self.buttons = []
            self.clear_widgets()

            dummy_button = Button()
            dummy_button.size_hint_x = None
            dummy_button.width = self.left_align
            dummy_button.disabled = True
            self.add_widget(dummy_button)

            for i in range(0, nb_steps):
                button = PlayIndicatorButton()
                button.disabled = True
                button.background_color = (0.5, 0.5, 1.0, 1.0)
                button.background_disabled_down = ''
                #if i == 0:
                #    button.state = "down"
                self.buttons.append(button)
                self.add_widget(button)

            self.nb_steps = nb_steps

