from turtle import Turtle, pen, setworldcoordinates

MOVE_DISTANCE = 20
STARTING_POSITION = [(0,0),(-20,0),(-40,0)]

UP = 90
DOWN  = 270
LEFT = 180
RIGHT = 0


class Snake:
    
    def __init__(self):
        self.segment =[]
        self.create_snake() 
        self.head = self.segment[0]
        # This is how we declare the method.
    
    def create_snake(self):
        for i in STARTING_POSITION:
            self.add_segment(i)

            # pen = Turtle ("square")
            # pen.color("white")
            # pen.penup()
            # pen.goto(i)
            # self.segment.append(pen)

    def add_segment(self, i):
        pen = Turtle ("square")
        pen.color("white")
        pen.penup()
        pen.goto(i)
        self.segment.append(pen)


    def extend(self):
        # add a new segment to the snake
        self.add_segment(self.segment[-1].position())


    def move(self):
        for seg_num in range(len(self.segment)-1 , 0 , -1):
            new_x = self.segment[seg_num -1].xcor()
            new_y = self.segment[seg_num -1].ycor()
            self.segment[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading()!= DOWN:
            self.head.setheading(UP)
    
    def down(self):
        if self.head.heading()!= UP:
            self.head.setheading(DOWN)  
        
    def left(self):
        if self.head.heading()!= RIGHT:
            self.head.setheading(LEFT)
    
    def right(self):
        if self.head.heading()!= LEFT:
            self.head.setheading(RIGHT)

#  Class Inheritance

