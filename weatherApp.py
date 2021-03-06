import requests
from tkinter import *

from PIL import ImageTk,Image






class Weather: 
    def __init__(self):
        
        
        self.root=Tk()
        self.root.title("Weather App")
        self.root.minsize(200,200)
        self.img1 = ImageTk.PhotoImage(Image.open('clear.png'))
        self.img2 = ImageTk.PhotoImage(Image.open('fog.png'))
        self.img3 = ImageTk.PhotoImage(Image.open('cloudy.png'))
        self.img4 = ImageTk.PhotoImage(Image.open('cloudy_s_sunny.png'))
        self.img5 = ImageTk.PhotoImage(Image.open('cloudy-scattered-showers.png'))
        Label(self.root, text="Enter Your City:").grid(row=1, column=0)
        self.userInput=Entry(self.root)
        self.userInput.grid(row=1, column=1)
        Button(self.root, text="Get Weather", bg='yellow',fg='black', bd='2', relief='solid', highlightbackground='red', command=self.weather).grid(row=2, columnspan=2)
        self.root.mainloop()
    def weather(self):
        self.api="https://api.openweathermap.org/data/2.5/weather?appid=39dacc08673eb5e0eb92027f0965a763&q=" #Test_API:0c42f7f6b53b244c78a418f4f181282a
        self.url=self.api+self.userInput.get()
        self.result=requests.get(self.url).json()
        self.temp=self.result['main']['temp']-273
        i=Label(self.root,fg='brown', text="Temp:(degC)").grid(row=3, column=0)
        j=Label(self.root, text=self.temp).grid(row=3, column=1)
        self.temp1=self.result['main']['pressure']/760
        i=Label(self.root,fg='brown', text="Pressure:(atm)").grid(row=4, column=0)
        j=Label(self.root, text=self.temp1).grid(row=4, column=1)
        self.temp2=self.result['main']['humidity']
        i=Label(self.root,fg='brown', text="Humidity:").grid(row=5, column=0)
        j=Label(self.root, text=self.temp2).grid(row=5, column=1)
        self.temp3=self.result['weather'][0]['main']
        i=Label(self.root,fg='brown', text="Weather Type:").grid(row=6, column=0)
        j=Label(self.root, text=self.temp3).grid(row=6, column=1)
        self.temp4=self.result['weather'][0]['description']
        i=Label(self.root,fg='brown', text="Overall Weather:").grid(row=7, column=0)
        j=Label(self.root, text=self.temp4).grid(row=7, column=1)
        self.temp5=self.result['main']['temp_min']-273
        i=Label(self.root,fg='brown', text="Min Temp:(degC)").grid(row=8, column=0)
        j=Label(self.root, text=self.temp5).grid(row=8, column=1)
        self.temp6=self.result['main']['temp_max']-273
        i=Label(self.root,fg='brown', text="Max Temp:(degC)").grid(row=9, column=0)
        j=Label(self.root, text=self.temp6).grid(row=9, column=1)
        self.temp7=self.result['visibility']
        i=Label(self.root,fg='brown', text="Visibility:").grid(row=10, column=0)
        j=Label(self.root, text=self.temp7).grid(row=10, column=1)
        self.temp8=self.result['wind']['speed']
        i=Label(self.root,fg='brown', text="Wind Speed:").grid(row=11, column=0)
        j=Label(self.root, text=self.temp8).grid(row=11, column=1)
        self.city=self.result['name']
        Button(self.root, text="Weather Type of"+"\t"+self.city, bg='green',fg='white', bd='2', relief='ridge', highlightbackground='red').grid(row=12, columnspan=2)
        if self.temp3=='Smoke':
            
            panel = Label(self.root,bg='skyblue',image=self.img2)
            

        elif self.temp3=='Clouds':

            panel = Label(self.root,bg='skyblue',image=self.img3)

        elif self.temp3=='Haze':

            panel = Label(self.root,bg='skyblue',image=self.img4)

        elif self.temp3=='Clear':

            panel = Label(self.root,bg='skyblue',image=self.img1)
            
            
        else:
            
            panel = Label(self.root,bg='skyblue',image=self.img5)
        panel.grid(row=14, columnspan=2)
        
        
            
        
        

        

    
            
        
        
obj=Weather()

        


