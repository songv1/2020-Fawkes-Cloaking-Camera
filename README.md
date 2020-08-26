# Fawkes Cloaking Camera
This program uses the desktop webcam to take a picture. It then cloaks the picture using Fawkes so that the subject in the picture may avoid identification by facial recognition software.

# Motivation
The idea to create a cloaking camera using the latest cutting-edge cloaking mechanism began when I was enrolled in my summer Linear Algebra class. For my final project, I chose to research the application of Linear Algebra in facial recognition algorithms. Naturally, I came across the seminal paper written by Turk et al. (1991), but of course facial recognition algorithms have improved drastically since then. I was astounded at how ubiquitous facial recognition software has become-- from mass surveillance on the streets to bots scraping the internet for social media posts, it seems that privacy/anonymity has become a relic of the past. This is highly troubling considering that not all facial recognition software has been used for ethical purposes. 

Fortunately, people have created cloaking mechanisms to guard against these breaches of privacy. After a few days of Wikipedia tunneling and Google searching, I learned about the Fawkes cloaking mechanism by SandLab. SandLab claims that Fawkes can defeat even the most powerful AI facial recognition software, such as those used by Clearview.ai, Microsoft, Amazon, and Face++. My immediate reaction was, "Wow, wouldn't it be great if we could have a camera that did this?"

Read on... 

# Features
As of now, there doesn't seem to be such a camera-- at least not one that used Fawkes. So I decided to create one. The code SandLab released uses the command line to process a directory of images, but I think it would be more user-friendly, convenient and accessible if Fawkes was automatically invoked at the press of a button right after a picture is taken. It saves time and energy that way. 

# Creation Process
1. My goal was to create a Fawkes Cloaking Camera, so I needed two things:
	* A GUI program for the camera. I used one created by Martin Fitzpatrick, found [here](https://www.learnpyqt.com/examples/photobooth-webcam/). 
	* The Fawkes code provided by SandLab, found [here](https://github.com/Shawn-Shan/fawkes).
2. Install dependencies listed below.
3. Brainstorming. The goal is to link these two programs. I wrote some informal pseudocode to see how I'd go about implementing Fawkes in the camera. 
	* What camera function should I modify? -> The one that takes and saves the picture. 
	* How do I modify it? After saving the file, I need to reload the file and apply Fawkes to it. 
	* Define a new function that uses Fawkes.
		* Within the new function, define a Fawkes object. 
		* Use Fawkes.methods
	* To find out what Fawkes.methods to call, refer to Fawkes code and select the appropriate method. Make note of necessary parameters. 	
4. Coding and debugging. 
	* Write some code.
	* Read error message and fix code accordingly, one error at a time.
5. Done! This sure was a learning experience. 
	* Something I learned from this project is that the computer takes time to save a file, so you can't call subsequent code immediately if it depends on the creation of a file. You have to time.sleep() first to make sure you're dealing with an existing object. 
	* Another thing I learned was how ot pass the correct arguments into the complicated class constructor of Fawkes. 
	* Lastly, using print() not only helps for debugging, but it's also a good way to prototype when you don't have the full function completed yet. 

# Dependencies
You must pip install fawkes, tensorflow, and PyQT5 before running this program.

# How to use?
1. Download code. 
2. Install dependencies.
3. In FawkesCloakingCamera.py, set self.save_path = "Location of the folder containing FawkesCloakingCamera.py"
4. Run in command line using command: python FawkesCloakingCamera.py
5. A webcam window pops up. Click the camera icon to take a picture. 
6. Your photo is stored in the folder called "Fawkes" containing this project. Wait a while, and the program will automatically cloak the image for you. The cloaked image will be saved in the same location under a different name. 
7. Compare the two images! Do you notice any differences? 

# Next steps for this project
In the future, I hope to streamline this program by moving cloaked images to a different folder and deleting the uncloaked original. This is because the Fawkes code will cloak all images it finds in the specified directory, which can make the program very slow if you have a lot of images. 

Also, SandLabs estimates that Fawkes takes 40s per face per image. Hopefully they will release an updated algorithm that runs faster. 

# Credits
I would like to thank...
* SandLabs for creating Fawkes. 
* Martin Fitzpatrick for creating the NSAViewer desktop Photobooth. 

# License
Due to the current licensing of Fawkes provided by SandLabs, I request that you do not redistribute or modify this project. 


