# Project Name :Diabetic Retinopathy Detection   

# Problem statement :    
Diabetic Retinopathy is a disease with an increasing prevalence and the main cause of blindness among working-age population. The risk of severe vision loss can be significantly reduced by timely diagnosis and treatment. Systematic screening for DR has been identified as a cost-effective way to save health services resources. Automatic retinal image analysis is emerging as an important screening tool for early DR detection, which can reduce the workload associated to manual grading as well as save diagnosis costs and time. Many research efforts in the last years have been devoted to developing automated tools to help in the detection and evaluation of DR lesions.
We are interested in automating this predition using deep learning models.

# Dataset : [Kaggle Diabetic Retinopathy dataset](https://www.kaggle.com/c/aptos2019-blindness-detection/data)      

# Solution :   
  
Deep learning looks promising because already various types of image classification tasks has been performed by various CNN's so, we can rely on DL pretrained models or we can modify some layers if we wish to :)    
A GUI based system has been made using Tkinter and I used heidiSQL to maintain and store a list of predictions with their patient id and name (which is very risky , the reason we will get to it some time later).   
I also used Twilio API to Make SMS connectivity to patients possible in case they are not contactable or accesible (in that case we can also use mail).       

# Summary of Technologies used in this project :       
| Dev Env. | Framework/ library/ languages |
| ------------- | ------------- |
| Backend development  | PyTorch (Deep learning framework) |
| Frontend development | Tkinter (Python GUI toolkit) |
| Database connectivity | HeidiSQL (MySQL server) |
| Programming Languages | Python, SQL |
| API | Twilio cloud API|      

# Data visualization :     
Input data (raw) is like this -     
![visual1](images/visual1.JPG)
   

# Visualization of complete system :    
![visual](images/vid.gif)    


# Getting started :       
[Click Here](https://github.com/suraj038/Diabetic_Retinopathy_Detection/blob/master/GettingStarted.md) to get started locally on your system.

## Some snaps :     
![images/gui1.png](images/gui1.png)
![images/gui2.png](images/gui2.png)
![images/gui3.png](images/gui3.png)
![images/gui4.JPG](images/gui4.JPG)
![images/sms.JPG](images/sms.JPG)       

 
 # Future Prospect :    
 * My next goal is to develop this into WebApp (probably using some light weight model as resnet models are heavy).   
 * Next goal will be using encryption techniques to achieve not only high accuracy but also high level of privacy in terms of differentially private basis and use technqiues such as Federated learning and Secure Multi party computation for privacy preserving deep learning classification.
 Acheiving a level of privacy is also very important task in medical datasets so that there can be factor of trust established between different stakeholders using the system.   
 * Some ideas for concurrency control has to be implemented properly using some kind of locks defined in MySQL so that multiple users can use the system at the same time when deployed on web.
 (Otherwise, locally you can run the executable file multiple times to open and run the GUI and it works fine).      
 
# Navigating the project :  
* [Check out the training code here](https://github.com/suraj038/Diabetic_Retinopathy_Detection/blob/master/training.ipynb)  
* [Check out testing done on unseen image](https://github.com/suraj038/Diabetic_Retinopathy_Detection/blob/master/Single_test_inference.ipynb)    
* [Check out the executable file (for running GUI)](https://github.com/suraj038/Diabetic_Retinopathy_Detection/blob/master/blindness.py)    
* [check out the model executable file (for loading to get inference locally)](https://github.com/suraj038/Diabetic_Retinopathy_Detection/blob/master/model.py)    
* [check out the Twilio API executable file (to get SMS for inference)](https://github.com/suraj038/Diabetic_Retinopathy_Detection/blob/master/send_sms.py)
* [for getting pre-trained weights for this model, check out getting started section here](https://github.com/suraj038/Diabetic_Retinopathy_Detection/blob/master/GettingStarted.md)       

[Note : The training files in this repo is only shown after final training as it took around more than 100 epochs to reach 97% accuracy and a lot of compute power and time.]     


⭐️ this Project if you liked it !
