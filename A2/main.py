"""
Name:TongWenlin
Date:27/07/2020
Brief Project Description:A booking system, include interact function
GitHub URL:https://github.com/JCUS-CP1404/assignment-2-travel-tracker-JCU-Wenlin
"""
# Create your main program in this file, using the TravelTrackerApp class

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button


class BoxLayoutDemo(App):

    def build(self):
        """Add the window, put main function"""
        # put the window
        self.title = "TravelTrackerApp"
        self.root = Builder.load_file('app.kv')
        li = []
        li.append('Lima, Peru, 3, n'.split(','))
        li.append('Auckland, new Zealand, 1, v'.split(','))
        li.append('Rome, Italy, 12, n'.split(','))
        # put the list
        for i in range(len(li)):
            a = li[i]
            entrie = Button(
                id=str(i),
                text="{0} in {1}, priority {2}".format(a[0], a[1], a[2]),
                background_color=[69, 139, 116])
            self.root.ids.entries.add_widget(entrie)
        return self.root


if __name__ == '__main__':
    BoxLayoutDemo().run()
