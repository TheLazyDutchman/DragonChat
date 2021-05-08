import tkinter as tk
import tkinter.ttk as ttk

class ScrollableFrame(ttk.Frame):
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        self.canvas = tk.Canvas(self, *args, **kwargs)
        scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = ttk.Frame(self.canvas, *args, **kwargs)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )

        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

        self.canvas.configure(yscrollcommand=scrollbar.set)

        self.canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        self.objAmount = 0

        self.canvas.bind("<MouseWheel>", self.mouse_wheel) # Windows mouse wheel event
        self.canvas.bind("<Button-4>", self.mouse_wheel) # Linux mouse wheel event (Up)
        self.canvas.bind("<Button-5>", self.mouse_wheel) # Linux mouse wheel event (Down)

        self.scrollable_frame.bind("<MouseWheel>", self.mouse_wheel) # Windows mouse wheel event
        self.scrollable_frame.bind("<Button-4>", self.mouse_wheel) # Linux mouse wheel event (Up)
        self.scrollable_frame.bind("<Button-5>", self.mouse_wheel) # Linux mouse wheel event (Down)

    def mouse_wheel(self, event):
        """ Mouse wheel as scroll bar """
        direction = 0
        # respond to Linux or Windows wheel event
        if event.num == 5 or event.delta == -120:
            direction = 1
        if event.num == 4 or event.delta == 120:
            direction = -1
        self.canvas.yview_scroll(direction, "units")

    def clearFrame(self):
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()

        self.objAmount = 0
        self.canvas.yview_moveto(0.0)

    def bindObj(self, obj, indentLevel = 0):
        obj.grid(row=self.objAmount, column = 0, columnspan = 8, sticky="NW")
        self.objAmount += 1

        obj.bind("<MouseWheel>", self.mouse_wheel) # Windows mouse wheel event
        obj.bind("<Button-4>", self.mouse_wheel) # Linux mouse wheel event (Up)
        obj.bind("<Button-5>", self.mouse_wheel) # Linux mouse wheel event (Down)

        return obj

    def bind(self, obj):
        obj.bind("<MouseWheel>", self.mouse_wheel) # Windows mouse wheel event
        obj.bind("<Button-4>", self.mouse_wheel) # Linux mouse wheel event (Up)
        obj.bind("<Button-5>", self.mouse_wheel) # Linux mouse wheel event (Down)
