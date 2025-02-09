import random
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from kivy.core.window import Window

# Set the background color
Window.clearcolor = (0, 0, 1, 1)  # Light grey

# Character attributes
size = ['<3', '3-5', '5-8', '8-11', '11-13']
thickness = ['Flat', 'Small', 'Medium', 'Big', 'Gigantic']
height = ['Almost Pedo', 'Shorty', 'Medium', 'Tall', 'Very Tall']
skin = ['Black', 'White', 'Skin', 'Brown']
hair = ['Black', 'White', 'Red', 'Blue', 'Green', 'Brown', 'Blonde', 'Yellow', 'Orange', 'Violet', 'Purple', 'Pink', 'Grey', 'Crimson', 'Burgundy']
emo = ['Eager', 'Vulnerable', 'Resenting', 'Embarras', 'Apathic', 'Empathic', 'Nostalgic', 'Jealous', 'Joyful', 'Hopeful', 'Lonely', 'Prideful', 'Shameless', 'Angry', 'Confused', 'Afraid']
Nature = ['Boisterous', 'Cold', 'Sick', 'Loving', 'Silent', 'Royal Complex', 'Idiot', 'God Complex', 'Cool', 'Sadistic', 'Teasing', 'Fool', 'Passionate', 'Gloomy', 'Submissive']
fear = ['None', 'Heights', 'Confinement', 'Dark', 'Society', 'Spider', 'Snakes', 'Blood', 'Dentist', 'Insects', 'Flying', 'Vegetables', 'Clown', 'Being Alone', 'No fear']
skill = ['Leadership', 'Combat', 'Stealth', 'Negotiation', 'Marksman', 'Survival', 'Problem Solving', 'Cooking', 'Artistry', 'Athletic', 'Diplomacy', 'Engineering', 'Linguistics', 'Tracking', 'Charisma']
motivate = ['Revenge', 'None', 'Power', 'Wealth', 'Love', 'Justice', 'Survival', 'Fame', 'Legacy', 'Knowledge', 'Friendship', 'Nothing', 'Adventure', 'Redemption', 'Creation']
hobby = ['Painting', 'Photography', 'Gardening', 'Cooking', 'Reading', 'Travelling', 'Music', 'Fitness', 'Games', 'Dance', 'Sports', 'Hiking', 'Crafting', 'Collecting', 'Wine Tasting']
job = ['Swordsman', 'Mage', 'Archer', 'Knight', 'Home Maker', 'NEET', 'Teacher', 'Stripper', 'Singer', 'Dancer', 'Waitress', 'Maid', 'Noble', 'Chef', 'Doctor']
world = ['Pokemon', 'One Piece', 'Normal', 'JJK', 'OPM', 'Rent-A-Girlfriend', 'Naruto', 'Bleach', 'Chainsaw Man', 'Dragon Ball', 'Konosuba', 'Wind Breaker', 'AOT', 'KNY', 'Food Wars', 'Gintama']

class CharacterApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        self.label = Label(text='Is the character a boy or a girl?', color=(0, 0, 0, 1), font_size=24)
        self.input = TextInput(hint_text='Enter "boy" or "girl"', multiline=False, font_size=18)
        layout.add_widget(self.label)
        layout.add_widget(self.input)
        
        # Add a submit button
        btn = Button(text='Submit', size_hint=(1, 0.5), font_size=18, background_color=(0.3, 0.5, 0.8, 1))
        btn.bind(on_press=self.submit_gender)
        layout.add_widget(btn)
        return layout

    def submit_gender(self, instance):
        gender = self.input.text.lower()
        if gender not in ['boy', 'girl']:
            self.show_popup('Please enter "boy" or "girl".')
        else:
            self.label.text = 'Generate a Character!'
            self.input.parent.remove_widget(self.input)
            instance.text = 'Generate'
            instance.unbind(on_press=self.submit_gender)
            instance.bind(on_press=self.generate_character)
            self.gender = gender

    def show_popup(self, message):
        popup_content = BoxLayout(orientation='vertical', padding=10, spacing=10)
        popup_content.add_widget(Label(text=message, color=(0, 0, 0, 1), font_size=20))
        close_btn = Button(text='Close', size_hint=(1, 0.5), font_size=18, background_color=(0.3, 0.5, 0.8, 1))
        popup_content.add_widget(close_btn)
        popup = Popup(title='Error', content=popup_content, size_hint=(None, None), size=(400, 200))
        close_btn.bind(on_press=popup.dismiss)
        popup.open()

    def generate_character(self, instance):
        if self.gender == 'boy':
            character = {
                'Size': random.choice(size),
                'Height': random.choice(height),
                'Skin': random.choice(skin),
                'Hair': random.choice(hair),
                'Emotion': random.choice(emo),
                'Nature': random.choice(Nature),
                'Fear': random.choice(fear),
                'Skill': random.choice(skill),
                'Motivation': random.choice(motivate),
                'Hobby': random.choice(hobby),
                'Job': random.choice(job),
                'World': random.choice(world),
            }
        else:
            character = {
                'Thickness': random.choice(thickness),
                'Height': random.choice(height),
                'Skin': random.choice(skin),
                'Hair': random.choice(hair),
                'Emotion': random.choice(emo),
                'Nature': random.choice(Nature),
                'Fear': random.choice(fear),
                'Skill': random.choice(skill),
                'Motivation': random.choice(motivate),
                'Hobby': random.choice(hobby),
                'Job': random.choice(job),
                'World': random.choice(world),
            }
        
        # Display the character attributes in a nicely formatted string
        character_str = '\n'.join([f'{key}: {value}' for key, value in character.items()])
        self.label.text = character_str

if __name__ == '__main__':
    CharacterApp().run()
