greenPlayer = input("greenPlayer")
Canvas = input(Canvas)
backgroundImg = input("GreenTime")
StepActivity = input("StepActivity")

def preload(): 
    audio = mp.AudioFileClip("happybirthday.mp3")
    img = Image.open('C:\Users\To_vi\OneDrive\Desktop\Python Work\Energy_Conversation_Ambika_VIIIC\s1.jpg')

def setup():
    createCanvas(500,500)
    greenPlayer = createSprite(200,430,40,80)
    activity = input("New Activity")
    activity = input("getActivity")
    activity = int(input(0))

    game = input("New Game")
    game = input("getGameState")
    game = int(input(0))


def draw():
    backgroundImg = Image.open("GreenTime.jpg")

if StepActivity < 5:
    print("The StepActivity is less than 5 ")
elif StepActivity == 8:
    print("StepActivity is equal to 8")
else:
    print("StepActivity started")

