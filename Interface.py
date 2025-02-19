import tkinter as tk
from tkinter import filedialog

class Interface: 
    file_path = None

    def __init__(self, download_service=None):
        self.download_service = download_service
        
        self.root = tk.Tk()
        self.root.title("Youtube Downloader")
        self.link_var=tk.StringVar()
        self.youtube_link_label = tk.Label(self.root, text = 'Youtube Link', font=('calibre',10, 'bold'))
        
        self.link = tk.Entry(self.root,textvariable = self.link_var, font=('calibre',10,'normal'))
        
        self.youtube_link_label.grid(row=0,column=1)
        self.link.grid(row=0,column=2)

        self.select_button = tk.Button(self.root, 
                   text="Select Folder", 
                   command=self.get_file_folder,
                   activebackground="blue", 
                   activeforeground="white",
                   anchor="center",
                   bd=3,
                   bg="lightgray",
                   cursor="hand2",
                   disabledforeground="gray",
                   fg="black",
                   font=("Arial", 12),
                   height=2,
                   highlightbackground="black",
                   highlightcolor="green",
                   highlightthickness=2,
                   justify="center",
                   overrelief="raised",
                   padx=2,
                   pady=2,
                   width=15,
                   wraplength=100)

        self.download_button = tk.Button(self.root, 
                   text="Download", 
                   command=self.download,
                   activebackground="blue", 
                   activeforeground="white",
                   anchor="center",
                   bd=3,
                   bg="lightgray",
                   cursor="hand2",
                   disabledforeground="gray",
                   fg="black",
                   font=("Arial", 12),
                   height=2,
                   highlightbackground="black",
                   highlightcolor="green",
                   highlightthickness=2,
                   justify="center",
                   overrelief="raised",
                   padx=2,
                   pady=2,
                   width=15,
                   wraplength=100)
        
        self.select_button.grid(row=3, column=0)
        self.download_button.grid(row=3, column=1)
        self.root.mainloop()
    
    def get_file_folder(self):
        self.file_path = filedialog.askdirectory()

    def download(self):
        if not self.file_path:
            print('You should select the destination folder...')
            return
        
        if self.youtube_link_label and self.link:
            self.download_service.download_video_as_mp3(self.link.get())
