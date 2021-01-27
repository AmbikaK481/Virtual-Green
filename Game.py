class Game:
    def_init_(form,gameState)

    def form():
        form.name = database.ref('getForm')
        form.greeting.show = str(input("Hello"))
        form.age = int(input(age))
        gameState = int(input(0))


    def getState():
        MyVar_gameStateRef = database.ref('gameState')
        MyVar_gameStateRef.on("value",(data))
        gameState = data.value()

    def update(gameState):
        database.ref('/').update
        gameState = state
    
