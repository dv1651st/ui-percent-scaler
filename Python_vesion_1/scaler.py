import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import numpy as np  

def generate_y(m,element_count):
    for i in range(1, element_count+1):
        yield m*(i-(element_count/2))+1

def convertToPercentages(x,mySum):
    result = round((x/(mySum))*100, 2)
    if result == -0.0:
        return 0.0
    else:
        return round((x/(mySum))*100, 2)

def generateValues(mySum, myList):
    mySum = sum(myList)
    return list(map(lambda x: convertToPercentages(x, mySum), myList))

def draw_graph(m_norm):

    ax.clear()

    # Create a slider for the m value
    x_center, y_center = element_count/2, 1
    start_x, start_y = 1, 0
    end_x, end_y = element_count, 0

    to_limit = (start_y-y_center)/(start_x-x_center)
    from_limit = (end_y-y_center)/(end_x-x_center)
    m = m_norm * (to_limit - from_limit) + from_limit
    x_center = element_count/2
    to_limit = (0-1)/(1-x_center)
    y = to_limit*element_count + (-to_limit*1)
    totalSum = element_count/2 * (to_limit*element_count - to_limit)
    yLimit = y/totalSum*100

    # Generate yticks from 0 to yLimit in steps of 5
    yticks = np.arange(0, yLimit, 5)

    # Add yLimit to the ticks if it is not already there
    if yLimit - yticks[-1] < 1.75:
        print("element count: {element_count}")
        yticks = np.delete(yticks, -1)
        yticks = np.append(yticks, yLimit)
    else:
        yticks = np.append(yticks, yLimit)

    # Set yticks
    ax.set_yticks(yticks)

    # Set the y limit to yLimit
    ax.set_ylim([0, yLimit])

    myYs = list(generate_y(m, element_count))
    mySum = sum(myYs)
    values = generateValues(mySum,myYs)

    labels = [f'{value}%' for value in values]

    indices = range(1, element_count + 1)

    ax.bar(indices, values)

    ax.axline(((x_center+.5), yLimit/2), slope=m/mySum*100, color='red')

    ax.set_xticks(indices)
    ax.set_xticklabels(labels)

    canvas.draw()

def update_slider(val):
    m = float(val)
    draw_graph(m)

def update_element_slider(val):
    global element_count
    element_count = int(val)

    draw_graph(slider.get())

def get_element_count():
    return slider_element_count.get()

# Creating tkinter window
window = tk.Tk()
window.title("Bar Graph GUI")

# Creating a new Figure and an Axes which is a subplot in figure
figure = Figure(figsize=(15,5))
ax = figure.add_subplot(111)

# Creating tkinter Canvas containing the Matplotlib figure
canvas = FigureCanvasTkAgg(figure, master=window)

slider_element_count = tk.Scale(window, from_=3, to=20, resolution=1, length=500, orient='horizontal', command=update_element_slider)
slider_element_count.set(6)

element_count = get_element_count()

slider = tk.Scale(window, from_=0, to=1, resolution=.0001, length=500, orient='horizontal', command=update_slider, showvalue=0)
slider.set(.05)

canvas.get_tk_widget().pack()
slider.pack()
slider_element_count.pack()

draw_graph(4)

window.mainloop()

