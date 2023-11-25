# Characters are defined here

init python:
    class Actor:
        def __init__(self, character, name):
            self.character = character
            self.name = name


define joe = Actor(Character("Joe", color = "#300FCB"), "Joe")
define lizzy = Actor(Character("Lizzy", color = "#D6134C"), "Lizzy")    
define thokk = Actor(Character("Thokk", color = "#DC1AA3"), "Thokk")  
define griffon = Actor(Character("Griffon", color = "#AA7F3D"), "Griffon")      
define d = Actor(Character("Dearia", color = "#1EBEEF"), "Dearia")


define cedric = Actor(Character("Cedric", color = "#650E55", image="cedric"), "Cedric")

