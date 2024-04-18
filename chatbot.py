import os
import google.generativeai as genai
import tkinter as tk

def chatbot():      
       os.environ['GOOGLE_API_KEY'] = "AIzaSyAfufeHXLwIYhg160GQJkINHM-s5ee-JbU"
       genai.configure(api_key=os.environ['GOOGLE_API_KEY'])
       
       model = genai.GenerativeModel('gemini-pro')
       
       def generate_response(query):
           response = model.generate_content(query)
           return response.text
       
       
       # Create the main GUI window
       root = tk.Tk()
       root.title("A.I. ChatBot ")
       root.geometry("720x720") 
        
       # Set the window size
       
       # Add an input field for the user's query
       query_label = tk.Label(root, text="Enter your query:")
       query_label.pack(pady=10)
       
       query_entry = tk.Entry(root, width=50)
       query_entry.pack()
       
       # Create a button to trigger response generation
       def handle_generate_button_click():
           query = query_entry.get()
           if query:  # Check if the query is not empty
               generated_text = generate_response(query)  # Call the generate_response function
               response_label.config(text=f"Response: {generated_text}")  # Update the response label
           else:
               response_label.config(text="Please enter a query.")
       
       generate_button = tk.Button(root, text="Generate Response", command=handle_generate_button_click)
       generate_button.pack(pady=10)
       
       # Add a label to display the generated response
       response_label = tk.Label(root, text="")
       response_label.pack()
       
       # Start the main event loop
       root.mainloop()

chatbot()