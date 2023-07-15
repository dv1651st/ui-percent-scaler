import tkinter as tk
from Python_undeveloped_version.scaler_engine import calculate_values

root = tk.Tk()
root.geometry('400x400')

digit_labels = []  # List to hold the digit label widgets
def on_slider_move(_val):
    # Get the current slider values
    skew = slider.get()
    element_count = int(slider1.get())
    spread = slider2.get()

    slider.config(to=element_count)

    # Call calculate_values and print the results
    myLabels = calculate_values(skew, element_count, spread)

    # Also call update_labels
    update_labels(myLabels, element_count, skew)

def update_labels(myLabels,element_count, skew):


    # Remove all current digit labels
    for label in digit_labels:
        label.destroy()
    digit_labels.clear()

    # Create new labels
    for i in range(element_count):
        text_value = str(myLabels[i])

        label_color = "red" if i+1 == skew else "black"
        
        new_label = tk.Label(digits_frame, text=text_value, font=("Arial", 20), fg=label_color)
        new_label.pack(side='left', padx=18)  # Add padding
        digit_labels.append(new_label)

# Create a slider from 1 to 100
slider = tk.Scale(root, from_=1, to=20, orient=tk.HORIZONTAL, command=on_slider_move,resolution=1)
slider.set(0)  # Set initial value

# Label for the main slider
label_main = tk.Label(root, text="Skew")
label_main.pack(side=tk.BOTTOM)
slider.pack(side=tk.BOTTOM, fill=tk.X, padx=10)

# Create a frame to hold the two new sliders
frame = tk.Frame(root)
frame.pack(side=tk.BOTTOM, pady=10)

# Create two new sliders
slider1 = tk.Scale(frame, from_=1, to=20, length=180, resolution=1, orient=tk.HORIZONTAL, command=on_slider_move)  # Set range to 1-20 and snap to integer values
slider1.set(3)
slider2 = tk.Scale(frame, from_=1, to=100, length=180, orient=tk.HORIZONTAL, command=on_slider_move)

# Labels for the smaller sliders
label1 = tk.Label(frame, text="Element Count")
label2 = tk.Label(frame, text="Spread")
label1.grid(row=0, column=0, padx=5)
label2.grid(row=0, column=1, padx=5)

# Grid the sliders side by side in the frame
slider1.grid(row=1, column=0, padx=5)
slider2.grid(row=1, column=1, padx=5)

# Create a frame to hold the digit labels
digits_frame = tk.Frame(root)
digits_frame.pack(fill=tk.X, pady=10)

# Create empty labels as spacers
top_spacer = tk.Label(root, height=10)
top_spacer.pack()
side_spacer = tk.Label(root, width=20)
side_spacer.pack(side=tk.LEFT)




root.mainloop()