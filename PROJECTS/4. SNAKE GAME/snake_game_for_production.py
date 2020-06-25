#THE BEST CLASSIC SNAKE GAME
#Santiago Garcia Arango
#This file is for production with py-installer, otherwise look at the other one
#----------------------------------------------------------------------------------

from random import randint
import sys
import os
import tkinter as tk
from PIL import Image, ImageTk

#Some constants for the implementation of the code...
current_folder = os.path.dirname( __file__ ) #Current folder obtained with "os" library
MOVE_INCREMENT = 20 #Constant to move this amount of pixels the snake
MOVE_SPEED = 75 #Constant to update the speed in which the snake "moves"(updates)

#Main class for the control of the snake
#Remark: When we inherit "tk.Canvas", we obtain the mehods of the default...
#...Canvas class [canvas = tk.Canvas() ] in our Snake class
class Snake( tk.Canvas ):
    def __init__(self):
        #We pass some properties to Canvas from the inheritance properties
        super().__init__( width=600, height=620, background="black", highlightthickness=0)

        #Default snake positions when beggining (note that each body-part is 20x20)
        self.snake_positions = [(100,100), (80,100), (60,100)]

        #Default food position when beggining
        self.food_position = self.set_new_food_position()

        #Default score and direction at the begginging
        self.score = 0
        self.direction = "Right"
        

        #We bind the functionalities of the keyboard presses (UP,DOWN,LEFT,RIGHT)
        #bind_all:"<Key>" let us react to event of keypress...
        #self.on_key_press: is called after the event of a keypress (and change direction of Snake)
        self.bind_all("<Key>", self.on_key_press)


        #We call the methods for the canvas snake creation
        self.load_images()
        self.create_objects()


        #Now we call once the method for performing the movement "infinitely" until crash
        #This method allows us to call a method after X amount of time
        #Remark: we pass the function name (but without parenthesis, so it works properly)        
        self.after(MOVE_SPEED, self.perform_actions)

        self.active_game = True #Variable to know if an active game is being played, or is over

    def load_images(self):
        #We place this code in try-except if the images are not found (and tell us)
        try:
            #=================================================================
            #THIS IS HOW WE ADD THE IMAGES FOR PRODUCTION (WITH PY-INSTALLER)
            bundle_dir = getattr(sys, "_MEIPASS", os.path.abspath( os.path.dirname(__file__) ) )
            print(bundle_dir)
            path_to_snake = os.path.join(bundle_dir, "imgs", "snake.png")
            self.snake_body_image = Image.open( path_to_snake )
            self.snake_body = ImageTk.PhotoImage(self.snake_body_image)

            path_to_food = os.path.join(bundle_dir, "imgs", "food.png")
            self.food_image = Image.open( path_to_food)
            self.food = ImageTk.PhotoImage(self.food_image)

            path_to_rick = os.path.join(bundle_dir, "imgs", "rick.png")
            self.rick_image = Image.open( path_to_rick)
            self.rick = ImageTk.PhotoImage(self.rick_image)

        except IOError as error:
            print( error )
            root.destroy()


    #Allows us to create and "place" the snake's body correctly
    def create_objects(self):
        #We create the text associated with the current score of the game
        self.create_text( 
            45, 
            13, 
            text="Score: {}".format(self.score), 
            tag="score",
            fill="#FFF",
            font=("TkDefaultFont", 14)
            )
        
        #Display my name at the top right
        self.create_text( 
            400, 
            13, 
            text="Santiago Garcia Arango, June 2020", 
            fill="#FFFF33",
            font=("TkDefaultFont", 14)
            )

        #We got through the list of tuples that define the snake's body
        for x_position, y_position in self.snake_positions:
            #We call a method inherited from the "tk.Canvas" that places the images
            #Note: the tag "snake" will help us keep track of the current images and change them...
            #... later when we need to move the snake (easy way to "remove" them strategically)
            self.create_image(x_position, y_position, image=self.snake_body, tag="snake")

        #Now we create the corresponding image for the food, based on "food_position tuple"
        self.create_image(self.food_position[0], self.food_position[1], image=self.food, tag="food")
        
        #We create the rectangle that gives the "boundaries" of the endpoints of the game
        self.create_rectangle( 7, 27, 593, 613, outline="#B8AEAB")


    #Main method to allows us to create the illusion of "moving" the snake
    def move_snake(self):
        #We obtain the current info of the position of the head os snake
        head_x_position, head_y_position = self.snake_positions[0]

        #Depending on the last keyboard pressed by the user, we "move" the snake in that way
        if self.direction == "Up":
            new_head_position = (head_x_position, head_y_position - MOVE_INCREMENT)
        elif self.direction == "Down":
            new_head_position = (head_x_position, head_y_position + MOVE_INCREMENT)
        elif self.direction == "Left":
            new_head_position = (head_x_position - MOVE_INCREMENT, head_y_position)
        elif self.direction == "Right":
            new_head_position = (head_x_position + MOVE_INCREMENT, head_y_position)


        #The goal is to "move" the snake, so the best way to do it, is by adding the new position...
        #... where the head is going, chopping the last element and then combining these two.
        #so we add the position of the new head and the old snake positions without the last element
        self.snake_positions = [new_head_position] + self.snake_positions[:-1]

        #After the new "self.snake_positions" are established, we must "update" the corresponding...
        #...canvas that are determined by these positions of the snake (this isn't automatic)
        #self.find_withtag(): help us find all elements with "snake" tag
        #Also, there are as many elements with tag "snake", as the snake_position (they match)
        #zip: lets us create a tuple that "intertwines" both of them (element by element)
        for segment, position in zip(self.find_withtag("snake"), self.snake_positions):
            #Canvas method to change coordinates of "segment" to the respective position given
            self.coords(segment, position)


    #Method to actually do the actions of the snake movement every determined time
    def perform_actions(self):
        #First, we check that the snake did not crash(so we call and check our method "check_collision()")
        if self.check_collision():
            #Method for showing final game message
            self.end_game()
            #When the snake crashes, the other part of this method wont execute (game stops)
            return()
        
        #If the snake did not crash, we keep the program running
        self.check_food_collision()
        self.move_snake()

        #This method allows us to call a method after X amount of time 
        #Remark: we pass the function name (but without parenthesis, so it works properly)
        self.after( MOVE_SPEED, self.perform_actions )


    #Method that allows us to stop the game, when a collision happens
    def check_collision(self):
        #We obtain the current info of the position of the head os snake
        head_x_position, head_y_position = self.snake_positions[0]

        #If head reaches X_limits or Y_limits or another current snake position of the snake body
        #to check colission with snake body, we see if head is in other snake_position
        if( 
            head_x_position in (0,600) or 
            head_y_position in (20,620) or 
            (head_x_position, head_y_position) in self.snake_positions[1:] 
            ):
            #If one of this conditions happens (crash), we return true in this method
            return( True )

    def on_key_press(self, event):
        #The new direction is set by the "event" of the key_press
        new_direction = event.keysym

        #The way to restart the game
        if (new_direction=="space" and not self.active_game):
            self.reset_game()


        #We must limit the keyboard presses to avoid "A,"B","5",etc..
        all_directions = ("Up", "Down", "Left", "Right")

        #We check that is a possible direction
        if new_direction in all_directions:
            #An interesting case, is that we DON'T want the user to change direction in the opposite...
            #...way from where he is heading (this is impossible), so we prevent this case
            if (new_direction =="Up" and self.direction=="Down"):
                return()
            if (new_direction =="Down" and self.direction=="Up"):
                return()
            if (new_direction =="Left" and self.direction=="Right"):
                return()
            if (new_direction =="Right" and self.direction=="Left"):
                return()
            
            #If the user did not press the opposite directions, then, the new direction is valid
            self.direction = new_direction

    #Method to check if the food is eaten by the snake
    def check_food_collision(self):
        #The food is eaten when the head_position matches with the food possition
        if self.snake_positions[0] == self.food_position:
            self.score += 1
            #We add to the snake, the last possition of itself (last item)
            self.snake_positions.append( self.snake_positions[-1] )

            #We create the image right at this point (for the last item added)
            self.create_image(
                self.snake_positions[-1][0], 
                self.snake_positions[-1][1],
                image=self.snake_body,
                tag="snake"
            )

            #We change the position of the food to a new one (see method)
            self.food_position = self.set_new_food_position()
            self.coords( self.find_withtag("food"), self.food_position )

            #We update the last score, to the new one.
            #First, we obtain the item with the tag "score" and keep it in "score_to_change"
            score_to_change = self.find_withtag("score")
            #We update the existing element of the score to the current score value
            self.itemconfigure( score_to_change, text="Score: {}".format(self.score), tag="score" )

    #Method to find a new position for the new food after the snakes eat one food
    def set_new_food_position(self):
        while True:
            #We generate random food locations between available screen sizes
            new_x_position = randint(1,29) * MOVE_INCREMENT
            new_y_position = randint(3,30) * MOVE_INCREMENT
            new_food_position = (new_x_position, new_y_position)
            
            #We check that the new food location is not inside the current snake_positions...
            #...otherwise, this would generate a food inside the current snake bode (error)
            if new_food_position not in self.snake_positions:
                return(new_food_position)

    #Method for when the user crashes and fails
    def end_game(self):
        self.active_game = False

        #This Canvas inherited function allows us to delete everything from it
        self.delete(tk.ALL)

        #Now we show the text at the end of the game to show score
        self.create_text( 
            self.winfo_width()/2, #Obtain half of the window-size in width
            30,
            text="Press <space> to restart", 
            fill="#FFFF33",
            font=("TkDefaultFont", 16)
            )

        #Now we show the text at the end of the game to show score
        self.create_text( 
            self.winfo_width()/2, #Obtain half of the window-size in width
            self.winfo_height()/4, #Obtain 1/4 of the window-size in height
            text="THANK YOU FOR PLAYING\nTHE BEST SNAKE GAME\nYour score is: {}".format(self.score), 
            fill="#FFF",
            font=("TkDefaultFont", 20)
            )
        
        self.create_image(
            self.winfo_width()/2, #Obtain half of the window-size in width
            self.winfo_height()*2/3, #Obtain 1/3 of the window-size in height
            image=self.rick,
            tag="snake"
        )

    def reset_game(self):
        self.active_game = True

        #This Canvas inherited function allows us to delete everything from it
        self.delete(tk.ALL)

        #Default snake positions when beggining (note that each body-part is 20x20)
        self.snake_positions = [(100,100), (80,100), (60,100)]

        #Default food position when beggining
        self.food_position = self.set_new_food_position()

        #Default score and direction at the begginging
        self.score = 0
        self.direction = "Right"
        

        #We bind the functionalities of the keyboard presses (UP,DOWN,LEFT,RIGHT)
        #bind_all:"<Key>" let us react to event of keypress...
        #self.on_key_press: is called after the event of a keypress (and change direction of Snake)
        self.bind_all("<Key>", self.on_key_press)


        #We call the methods for the canvas snake creation
        self.load_images()
        self.create_objects()


        #Now we call once the method for performing the movement "infinitely" until crash
        #This method allows us to call a method after X amount of time
        #Remark: we pass the function name (but without parenthesis, so it works properly)        
        self.after(MOVE_SPEED, self.perform_actions)



#FOR PRODUCTION, is better to add this try-except at the executing of the window
try:
    root = tk.Tk()
    root.title("SNAKE GAME:  Santiago Garcia Arango")
    root.resizable(False, False)

    #We create the main Snake Canvas with the class at the top... (then we pack it in tkinter root)
    game = Snake()
    game.pack()

    #Execute main window created with tkinter
    root.mainloop()

except:
    #This is how we look for the problem, if something happened in the executable in production (with py-installer)
    import traceback
    traceback.print_exc()
    input("Press Enter to end...")