import simplegui

# define variables
time = 0
x = 0
y = 0
stop_boolean = True

# define helper hunction format(t)
def format(t):
    D = int(t) % 10
    C = int(t/10) % 10
    B = int(t/100) % 6
    A = int(t/600) % 600
    string = str(A) + ":" + str(B) + str(C) + "." + str(D)
    return string

# define tick function for timer
def tick():
    global time
    time += 1

# timer handlers
def start():
    global stop_boolean
    stop_boolean = False
    timer.start()

def stop():
    global stop_boolean, time, x, y
    if stop_boolean == False:
        if time % 10 == 0 and time != 0:
            x += 1
            y += 1
        elif time != 0:
            y += 1
    stop_boolean = True
    timer.stop()
    
def reset():
    global time, stop_boolean, x, y
    time = 0
    stop_boolean = True
    x = 0
    y = 0
    timer.stop()
       
# define draw handler
def draw(canvas):
    canvas.draw_text(str(format(time)), (5, 175), 92, 'white')
    canvas.draw_text(str(x) + "/" + str(y), (200, 50), 48, 'red')

# create frame
frame = simplegui.create_frame("Stop: Game", 300, 300)
frame.set_canvas_background('blue')

# register draw handler
frame.set_draw_handler(draw)

# add timer
timer = simplegui.create_timer(100, tick)

# add buttons
frame.add_button("Start", start, 200)
frame.add_button("Stop", stop, 200)
frame.add_button("Reset", reset, 200)

# start frame
frame.start()
