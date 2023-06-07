import customtkinter as tk
from PIL import ImageGrab, ImageTk


class NewWindow(tk.CTkToplevel):
    def __init__(self,x,y,result):
        super().__init__()
        self.result = result
        self.screen_X = int(x.get())
        self.screen_Y = int(y.get())
        self.screen_res = None
        self.withdraw()
        self.attributes('-fullscreen', True)

        self.canvas = tk.CTkCanvas(self)
        self.canvas.pack(fill="both", expand=True)

        image = ImageGrab.grab()
        self.image = ImageTk.PhotoImage(image)
        self.photo = self.canvas.create_image(0, 0, image=self.image, anchor="nw")

        self.x, self.y = 0, 0
        self.rect, self.start_x, self.start_y, self.curX, self.curY = None, None, None, None, None
        self.deiconify()

        self.canvas.tag_bind(self.photo, "<ButtonPress-1>", self.on_button_press)
        self.canvas.tag_bind(self.photo, "<B1-Motion>", self.on_move_press)
        self.canvas.tag_bind(self.photo, "<ButtonRelease-1>", self.on_button_release)

    def on_button_press(self, event):
        self.start_x = event.x
        self.start_y = event.y
        self.rect = self.canvas.create_rectangle(self.x, self.y, 1, 1, outline='green')

    def on_move_press(self, event):
        self.curX, self.curY = (event.x, event.y)
        self.canvas.coords(self.rect, self.start_x, self.start_y, self.curX, self.curY)

    def on_button_release(self, event):
        volume = self.compute_volume()
        screen_volume = self.screen_X * self.screen_Y
        print(f"Square pixels: {volume} ")
        print(f"Your screen resolution: {self.screen_X} x {self.screen_Y}")
        print(f"Display square pixels: {screen_volume}")
        percent = abs(volume/screen_volume*100)
        result_txt = f"You chosen: {percent:.2f}% of screen"
        print(result_txt)
        self.result.configure(text=result_txt)
        self.destroy()
    def compute_volume(self):
        w = self.start_x - self.curX
        h = self.start_y - self.curY
        return w * h
