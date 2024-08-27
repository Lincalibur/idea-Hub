import customtkinter as ctk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Create the main window
root = ctk.CTk()
root.geometry("600x400")

# Create a frame to hold the chart
chart_frame = ctk.CTkFrame(root)
chart_frame.pack(fill="both", expand=True, padx=20, pady=20)

# Create a Matplotlib figure
fig = Figure(figsize=(5, 4), dpi=100)
ax = fig.add_subplot(111)

# Sample data for the pie chart
labels = ['Category A', 'Category B', 'Category C', 'Category D']
sizes = [15, 30, 45, 10]  # Percentages
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99']

# Create the pie chart
ax.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)

# Equal aspect ratio ensures that pie is drawn as a circle
ax.axis('equal')

# Create a canvas to display the chart
canvas = FigureCanvasTkAgg(fig, master=chart_frame)
canvas.draw()
canvas.get_tk_widget().pack(fill="both", expand=True)

# Start the main loop
root.mainloop()
