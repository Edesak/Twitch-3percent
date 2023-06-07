from DragAndMark import NewWindow
import customtkinter as tk
from PIL import Image


def load_image():
    # Open a file dialog to select an image
    file_path = tk.filedialog.askopenfilename()

    # Check if a file was selected
    if file_path:
        # Open the image using PIL
        image = Image.open(file_path)

        # Get the resolution of the image
        width, height = image.size
        #print()
        #print((width*height)/(int(resolution_x.get())*int(resolution_y.get())))
        # Display the resolution
        percantage = (width*height)/(int(resolution_x.get())*int(resolution_y.get()))*100
        result.configure(text=f"This image will take: {percantage:.2f}% of screen")
def validate_input(self, new_value):
    if new_value.isdigit() or new_value == "":
        return True
    else:
        return False


root = tk.CTk()
validate_numeric = (root.register(validate_input), "%P")

resolution_x = tk.CTkLabel(root, text="Resolution X:")
resolution_x.grid(row=1, column=0, pady=10)
resolution_x = tk.CTkLabel(root, text="Resolution Y:")
resolution_x.grid(row=2, column=0, pady=10)

upload_button = tk.CTkButton(root, text="Messure", command=lambda: NewWindow(resolution_x, resolution_y,result))
upload_button.grid(row=0, column=1, padx=10)

resolution_x = tk.CTkEntry(root, validatecommand=validate_numeric)
resolution_x.grid(row=1, column=1, pady=10, padx=10)
resolution_x.insert(0,"1920")

resolution_y = tk.CTkEntry(root, validatecommand=validate_numeric)
resolution_y.grid(row=2, column=1, pady=10, padx=10)
resolution_y.insert(0,"1080")

load_button = tk.CTkButton(root, text="Load Image", command=load_image)
load_button.grid(row=0,column=2,padx=10)

result = tk.CTkLabel(root, text="There is no mesurement for now.")
result.grid(row=3, column=1, pady=10)
result = tk.CTkLabel(root, text="For image the computation is based on resolution of image. \n In case that you change it in OBS is not handled")
result.grid(row=4, column=1, pady=10)




root.geometry("600x300")
root.resizable(False, False)
root.mainloop()
