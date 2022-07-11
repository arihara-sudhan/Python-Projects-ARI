from tkinter import *
from pytube import YouTube

class ARI_DOWNLOADS:
	def __init__(self):
		self.ari = Tk()
		bg=PhotoImage(file="IMGS/bg.png")
		self.w = bg.width()
		self.h = bg.height()
		self.ari.geometry("%dx%d" % (self.w, self.h))
		Label(self.ari,image=bg).pack()
		self.ari.resizable(0,0)
		self.ari.title('YouTube Video Downloader')
		self.widgets()
		self.ari.mainloop()
	def widgets(self):
		self.link = StringVar()
		Entry(self.ari,textvariable=self.link,font='arial 30 bold',width=20).place(x=self.w//2-220, y=self.h//2+180)
		print(str(self.link.get()))
		Button(self.ari,text="GET VIDEO",font='arial 20 bold',bg='red',fg='white',command=self.download).place(x=self.w//2-90, y=self.h//2+250)

	def download(self):
		url = YouTube(str(self.link.get()))
		vid = url.streams.first()
		vid.download()
		Label(self.ari,text='Downloaded',bg='red',fg='white').place(x=600,y=550)
ARI_DOWNLOADS()