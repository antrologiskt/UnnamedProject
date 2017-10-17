from guizero import App, Text, TextBox, PushButton, Slider
# for picture import Picture, use gif format, displayed as stills
# add picture to same folder as script

app = App(title='Hello world')

# welcome text. 1st arg assigns it to app
text1 = Text(app, text='This is Batman', size=45, font='Times New Roman')

# textbox widget
my_name = TextBox(app, width=25)

# get function; from textbox widget [set() for new value)
def say_my_name():
    text1.set(my_name.get())

# add pushbutton that receives input from say_my_name
update_text = PushButton(app, command=say_my_name, text='Display my name')

# text resize function
def change_text_size(slider_value):
    text1.font_size(slider_value)

#text size slider widget
text_size = Slider(app, command=change_text_size, start=10, end=80)


# starts event loop. no code after this executes
app.display()
