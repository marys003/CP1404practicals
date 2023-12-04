from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.properties import StringProperty

NEW_COLOUR = (1, 0, 0, 1)  # RGBA for red
ALTERNATIVE_COLOUR = (1, 0, 1, 1)  # RGBA for magenta


class DynamicLabelsApp(App):
    """Main program - Kivy app to demo dynamic label creation."""
    status_text = StringProperty()

    def __init__(self, **kwargs):
        """Construct main app."""
        super().__init__(**kwargs)
        # basic data (model) example - list of names
        self.names = ["Bob Brown", "Cat Cyan", "Oren Ochre"]

    def build(self):
        """Build the Kivy GUI."""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_labels()
        return self.root

    def create_labels(self):
        """Create labels from data and add them to the GUI."""
        for name in self.names:
            # create a label for each data entry, specifying the text
            temp_label = Label(text=name)
            temp_label.bind(on_touch_down=self.touch_label)
            # set the label's background colour
            temp_label.background_color = NEW_COLOUR
            # add the label to the "labels_box" layout widget
            self.root.ids.labels_box.add_widget(temp_label)

    def touch_label(self, instance, touch):
        """Handle touching labels."""
        if instance.collide_point(*touch.pos):
            # change the label's background colour
            instance.background_color = ALTERNATIVE_COLOUR
            # update status text
            self.status_text = f"Touched label: {instance.text}"

    def clear_all(self):
        """Clear all widgets that are children of the "labels_box" layout widget."""
        self.root.ids.labels_box.clear_widgets()


DynamicLabelsApp().run()
