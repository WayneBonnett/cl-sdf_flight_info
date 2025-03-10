#include the necessary libs
import pandas as pd
import matplotlib 
from matplotlib import pyplot as plt
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

class SdfFlightApp:
    def __init__(self, root):
        self.root = root
        self.root.title("SDF Flight Analysis")
        
        # Create buttons
        self.arrivals_btn = tk.Button(root, text="Show Arrivals", command=self.show_arrivals)
        self.arrivals_btn.pack(pady=10)
        
        self.departures_btn = tk.Button(root, text="Show Departures", command=self.show_departures)
        self.departures_btn.pack(pady=10)
        
        # Create a frame for the plot
        self.plot_frame = tk.Frame(root)
        self.plot_frame.pack(fill=tk.BOTH, expand=True)

    def show_arrivals(self):
        # Clear previous plot
        for widget in self.plot_frame.winfo_children():
            widget.destroy()
            
        #Load arrival data
        arrivals = pd.read_csv('./assets/arrivals.csv', usecols=['airline', 'arr_year', 'total_arrivals'])
        
        # Create figure and plot
        fig = Figure(figsize=(10, 6))
        ax = fig.add_subplot(111)
        
        arrivals['arr_year'] = arrivals['arr_year'].astype(int)
        arrivals.groupby(['arr_year', 'airline']).sum()['total_arrivals'].unstack().plot(kind='line', ax=ax)
        ax.set_xticks(arrivals['arr_year'].unique())
        ax.set_xlabel('Year')
        ax.set_ylabel('# of flights')
        ax.set_title('Total SDF arrivals by Year')
        
        # Embed plot in tkinter window
        canvas = FigureCanvasTkAgg(fig, master=self.plot_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    def show_departures(self):
        # Clear previous plot
        for widget in self.plot_frame.winfo_children():
            widget.destroy()
            
        #Load departure data
        departures = pd.read_csv('./assets/departures.csv', usecols=['airline', 'dep_year', 'total_departures'])
        
        # Create figure and plot
        fig = Figure(figsize=(10, 6))
        ax = fig.add_subplot(111)
        
        departures['dep_year'] = departures['dep_year'].astype(int)
        departures.groupby(['dep_year', 'airline']).sum()['total_departures'].unstack().plot(kind='line', ax=ax)
        ax.set_xticks(departures['dep_year'].unique())
        ax.set_xlabel('Year')
        ax.set_ylabel('Total flights')
        ax.set_title('Total SDF Departures by Year')
        
        # Embed plot in tkinter window
        canvas = FigureCanvasTkAgg(fig, master=self.plot_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

def main():
    root = tk.Tk()
    app = SdfFlightApp(root)
    root.geometry("800x600")
    root.mainloop()

if __name__ == "__main__":
    main()