import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage
from tkinter import messagebox
from tkinter import filedialog
from keras.models import load_model
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.applications.vgg16 import preprocess_input
from keras.applications.vgg16 import decode_predictions
from keras.applications.vgg16 import VGG16
import numpy as np
 
from keras.models import model_from_json
from PIL import ImageTk, Image

import os

# Create the main application window
app = tk.Tk()
app.title("ColoDetect")
app.geometry("800x600")


# Create a tab control to manage tabs
tab_control = ttk.Notebook(app)


# Create the "Survey" tab
survey_tab = ttk.Frame(tab_control) 
tab_control.add(survey_tab, text="Survey")


#Cancer prediciton model
model = load_model('colon_cancer_model8.h5')

#model = model_from_json("colon_cancer_model_macos.json")

# Function to calculate risk
def calculate_risk():
   try:
       age = int(age_entry.get())
       family_history = family_var.get()
       personal_history = personal_var.get()
       dietary_habits = dietary_var.get()
       physical_activity = physical_activity_var.get()
       obesity = obesity_var.get()
       smoking = smoking_var.get()
       alcohol_consumption = alcohol_var.get()
       ibd = ibd_var.get()
       type_2_diabetes = diabetes_var.get()
       genetic_factors = genetic_var.get()
       screening_history = screening_var.get()


       # Calculate risk score based on user responses
       risk_score = 0


       if age > 50:
           risk_score += 20


       if family_history == "yes":
           risk_score += 10


       if personal_history == "yes":
           risk_score += 10


       if dietary_habits == "unhealthy":
           risk_score += 10


       if physical_activity == "rarely":
           risk_score += 10


       if obesity == "yes":
           risk_score += 10


       if smoking == "yes":
           risk_score += 10


       if alcohol_consumption == "high":
           risk_score += 10


       if ibd == "yes":
           risk_score += 10


       if type_2_diabetes == "yes":
           risk_score += 10


       if genetic_factors == "yes":
           risk_score += 10


       if screening_history == "no":
           risk_score += 10


       # Calculate the risk percentage
       risk_percentage = min(100, risk_score)  # Cap the risk at 100%


       result_label.config(
           text=f"Based on your responses, your estimated risk of colorectal cancer is approximately {risk_percentage}%.")
   except ValueError:
       messagebox.showerror("Error", "Please enter valid numeric values.")




# Create input fields and labels for questions
age_label = tk.Label(survey_tab, text="What is your current age?")
age_label.grid(row=0, column=0, padx=10, pady=5)
age_entry = tk.Entry(survey_tab)
age_entry.grid(row=0, column=1, padx=10, pady=5)


family_label = tk.Label(survey_tab, text="Do you have a family history of colorectal cancer or colorectal polyps?")
family_label.grid(row=1, column=0, padx=10, pady=5)
family_var = tk.StringVar()
family_var.set("yes")  # Default value
family_yes_radio = tk.Radiobutton(survey_tab, text="Yes", variable=family_var, value="yes")
family_no_radio = tk.Radiobutton(survey_tab, text="No", variable=family_var, value="no")
family_yes_radio.grid(row=1, column=1, padx=10, pady=5)
family_no_radio.grid(row=1, column=2, padx=10, pady=5)


personal_label = tk.Label(survey_tab, text="Have you previously been diagnosed with colorectal cancer or polyps?")
personal_label.grid(row=2, column=0, padx=10, pady=5)
personal_var = tk.StringVar()
personal_var.set("yes")  # Default value
personal_yes_radio = tk.Radiobutton(survey_tab, text="Yes", variable=personal_var, value="yes")
personal_no_radio = tk.Radiobutton(survey_tab, text="No", variable=personal_var, value="no")
personal_yes_radio.grid(row=2, column=1, padx=10, pady=5)
personal_no_radio.grid(row=2, column=2, padx=10, pady=5)


dietary_label = tk.Label(survey_tab,
                        text="Do you have a diet high in red and processed meats, and low in fruits, vegetables, "
                             "and fiber?")
dietary_label.grid(row=3, column=0, padx=10, pady=5)
dietary_var = tk.StringVar()
dietary_var.set("unhealthy")  # Default value
dietary_unhealthy_radio = tk.Radiobutton(survey_tab, text="Unhealthy", variable=dietary_var, value="unhealthy")
dietary_healthy_radio = tk.Radiobutton(survey_tab, text="Healthy", variable=dietary_var, value="healthy")
dietary_unhealthy_radio.grid(row=3, column=1, padx=10, pady=5)
dietary_healthy_radio.grid(row=3, column=2, padx=10, pady=5)


physical_activity_label = tk.Label(survey_tab, text="How often do you engage in physical activity and exercise?")
physical_activity_label.grid(row=4, column=0, padx=10, pady=5)
physical_activity_var = tk.StringVar()
physical_activity_var.set("rarely")  # Default value
physical_activity_rarely_radio = tk.Radiobutton(survey_tab, text="Rarely", variable=physical_activity_var,
                                               value="rarely")
physical_activity_regularly_radio = tk.Radiobutton(survey_tab, text="Regularly", variable=physical_activity_var,
                                                  value="regularly")
physical_activity_rarely_radio.grid(row=4, column=1, padx=10, pady=5)
physical_activity_regularly_radio.grid(row=4, column=2, padx=10, pady=5)


obesity_label = tk.Label(survey_tab, text="Are you currently overweight or obese?")
obesity_label.grid(row=5, column=0, padx=10, pady=5)
obesity_var = tk.StringVar()
obesity_var.set("yes")  # Default value
obesity_yes_radio = tk.Radiobutton(survey_tab, text="Yes", variable=obesity_var, value="yes")
obesity_no_radio = tk.Radiobutton(survey_tab, text="No", variable=obesity_var, value="no")
obesity_yes_radio.grid(row=5, column=1, padx=10, pady=5)
obesity_no_radio.grid(row=5, column=2, padx=10, pady=5)


smoking_label = tk.Label(survey_tab, text="Do you smoke or have a history of smoking?")
smoking_label.grid(row=6, column=0, padx=10, pady=5)
smoking_var = tk.StringVar()
smoking_var.set("yes")  # Default value
smoking_yes_radio = tk.Radiobutton(survey_tab, text="Yes", variable=smoking_var, value="yes")
smoking_no_radio = tk.Radiobutton(survey_tab, text="No", variable=smoking_var, value="no")
smoking_yes_radio.grid(row=6, column=1, padx=10, pady=5)
smoking_no_radio.grid(row=6, column=2, padx=10, pady=5)


alcohol_label = tk.Label(survey_tab, text="How much alcohol do you consume regularly?")
alcohol_label.grid(row=7, column=0, padx=10, pady=5)
alcohol_var = tk.StringVar()
alcohol_var.set("high")  # Default value
alcohol_high_radio = tk.Radiobutton(survey_tab, text="High", variable=alcohol_var, value="high")
alcohol_moderate_radio = tk.Radiobutton(survey_tab, text="Moderate", variable=alcohol_var, value="moderate")
alcohol_low_radio = tk.Radiobutton(survey_tab, text="Low", variable=alcohol_var, value="low")
alcohol_high_radio.grid(row=7, column=1, padx=10, pady=5)
alcohol_moderate_radio.grid(row=7, column=2, padx=10, pady=5)
alcohol_low_radio.grid(row=7, column=3, padx=10, pady=5)


ibd_label = tk.Label(survey_tab,
                    text="Do you have a history of inflammatory bowel diseases, such as Crohn's disease or "
                         "ulcerative colitis?")
ibd_label.grid(row=8, column=0, padx=10, pady=5)
ibd_var = tk.StringVar()
ibd_var.set("yes")  # Default value
ibd_yes_radio = tk.Radiobutton(survey_tab, text="Yes", variable=ibd_var, value="yes")
ibd_no_radio = tk.Radiobutton(survey_tab, text="No", variable=ibd_var, value="no")
ibd_yes_radio.grid(row=8, column=1, padx=10, pady=5)
ibd_no_radio.grid(row=8, column=2, padx=10, pady=5)


diabetes_label = tk.Label(survey_tab, text="Are you living with type 2 diabetes?")
diabetes_label.grid(row=9, column=0, padx=10, pady=5)
diabetes_var = tk.StringVar()
diabetes_var.set("yes")  # Default value
diabetes_yes_radio = tk.Radiobutton(survey_tab, text="Yes", variable=diabetes_var, value="yes")
diabetes_no_radio = tk.Radiobutton(survey_tab, text="No", variable=diabetes_var, value="no")
diabetes_yes_radio.grid(row=9, column=1, padx=10, pady=5)
diabetes_no_radio.grid(row=9, column=2, padx=10, pady=5)


genetic_label = tk.Label(survey_tab,
                        text="Have you been tested for genetic conditions like Lynch syndrome or familial "
                             "adenomatous polyposis (FAP)?")
genetic_label.grid(row=10, column=0, padx=10, pady=5)
genetic_var = tk.StringVar()
genetic_var.set("yes")  # Default value
genetic_yes_radio = tk.Radiobutton(survey_tab, text="Yes", variable=genetic_var, value="yes")
genetic_no_radio = tk.Radiobutton(survey_tab, text="No", variable=genetic_var, value="no")
genetic_yes_radio.grid(row=10, column=1, padx=10, pady=5)
genetic_no_radio.grid(row=10, column=2, padx=10, pady=5)


screening_label = tk.Label(survey_tab,
                          text="Have you undergone regular screenings for colorectal cancer, such as colonoscopy or "
                               "stool-based tests?")
screening_label.grid(row=11, column=0, padx=10, pady=5)
screening_var = tk.StringVar()
screening_var.set("no")  # Default value
screening_yes_radio = tk.Radiobutton(survey_tab, text="Yes", variable=screening_var, value="yes")
screening_no_radio = tk.Radiobutton(survey_tab, text="No", variable=screening_var, value="no")
screening_yes_radio.grid(row=11, column=1, padx=10, pady=5)
screening_no_radio.grid(row=11, column=2, padx=10, pady=5)


# Create a button to calculate risk
calculate_button = tk.Button(survey_tab, text="Calculate Risk", command=calculate_risk)
calculate_button.grid(row=12, column=0, columnspan=3, padx=10, pady=10)


# Create a label to display the risk result
result_label = tk.Label(survey_tab, text="", font=("Arial", 12))
result_label.grid(row=13, column=0, columnspan=3, padx=10, pady=10)


# Load colorectal cancer-related images
colorectal_cancer_image = PhotoImage(file="")  # Provide the path to your colorectal cancer image


# Create a label for the colorectal cancer image
colorectal_cancer_image_label = tk.Label(survey_tab, image=colorectal_cancer_image)
colorectal_cancer_image_label.grid(row=0, column=3, rowspan=14, padx=10, pady=10)


# Create the "Imaging" tab
imaging_tab = ttk.Frame(tab_control)
tab_control.add(imaging_tab, text="Imaging")




# Function to start the machine learning model (stub for now)
def start_machine_learning_model():
   filename = filedialog.askopenfilename(initialdir= os.path.abspath(os.curdir), 
                                         title = "Select an Image", 
                                         filetypes = [("JPG files", "*.jpg")])
   try:
    if os.path.exists(filename):
        img = Image.open(filename)
        img.resize((200, 200))
        img = ImageTk.PhotoImage(img)
        panel.configure(image=img)
        panel.image = img
        colon_image = load_img(filename, target_size=(224, 224))
        colon_image = np.array(colon_image)
        colon_image = colon_image / 255.0
        colon_image = colon_image.reshape(1, 224, 224, 3)
        prediction = model.predict(colon_image)
        prediction = 1.0 - prediction[0][0]
        prediction *= 100.0
        prediction = round(prediction, 3)
        label_container.config(text="Results:")
        predictions_text.delete(1.0, tk.END)
        predictions_text.insert(tk.END, f'Based on the imported image, there is a {prediction} % chance this patient has Colorectal Cancer.')
   except Exception as e:
    pass




# Create a button to start the machine learning model
start_model_button = tk.Button(imaging_tab, text="Import Colonoscopy Image:", command=start_machine_learning_model)
start_model_button.pack(pady=10)


# Create a canvas for rendering the webcam feed
#canvas = tk.Canvas(imaging_tab, width=200, height=200)
#canvas.pack()

initial_image = Image.open("white.jpg")
initial_image.resize((200, 200))
pic = ImageTk.PhotoImage(initial_image)
panel = tk.Label(imaging_tab, image=pic, width=200, height=200)
panel.pack()
#image_on_canvas = canvas.create_image(0, 0, anchor='nw', image=pic)



# Create a label container for displaying the model predictions
label_container = tk.Label(imaging_tab, text="")
label_container.pack()


# Use a Text widget to display the model predictions
predictions_text = tk.Text(imaging_tab, wrap=tk.WORD, width=40, height=5)
predictions_text.pack(pady=10)


# Add the tab control to the main application
tab_control.pack(expand=1, fill="both")


# Create the "About" tab
about_tab = ttk.Frame(tab_control)
tab_control.add(about_tab, text="About")


# Styling for the About tab
about_style = ttk.Style()
about_style.configure('About.TLabel', font=('Arial', 14))
about_style.configure('About.TFrame', background='lightblue')


# About tab content
about_frame = ttk.Frame(about_tab, style='About.TFrame')
about_frame.pack(fill='both', expand=True)


about_text = ("\n"
             "ColoDetect v1.0\n"
             "\n"
             "Creator: N/A\n"
             "\n"
             "Description:\n"
             "\n"
             "ColoDetect is an application designed to make the process of colorectal health assessment more "
             "accessible. It helps individuals assess their risk of colorectal cancer by providing a user-friendly "
             "survey that takes various risk factors into account.\n"
             "The application aims to raise awareness and promote early detection of colorectal cancer, ultimately "
             "contributing to better colorectal health outcomes.\n")
about_label = ttk.Label(about_frame, text=about_text, style='About.TLabel')
about_label.pack(padx=20, pady=20)
app.mainloop()
