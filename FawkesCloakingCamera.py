from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtPrintSupport import *
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import *

import os
import sys
import time

'''
Before running this program, make sure to pip install PyQt5, fawkes,
and tensorflow.
'''
import fawkes
import glob
import functools

class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.available_cameras = QCameraInfo.availableCameras()
        if not self.available_cameras:
            pass #quit

        self.status = QStatusBar()
        self.setStatusBar(self.status)

        #Save files in the Fawkes folder, where you find this program.
        self.save_path = "Location of Fawkes folder containing this file."

        self.viewfinder = QCameraViewfinder()
        self.viewfinder.show()
        self.setCentralWidget(self.viewfinder)

        # Set the default camera.
        self.select_camera(0)

        # Setup tools
        camera_toolbar = QToolBar("Camera")
        camera_toolbar.setIconSize(QSize(14, 14))
        self.addToolBar(camera_toolbar)

        #Camera
        photo_action = QAction(QIcon(os.path.join('images', 'camera-black.png')), "Take photo...", self)
        photo_action.setStatusTip("Take photo of current view")
        photo_action.triggered.connect(self.take_photo)
        camera_toolbar.addAction(photo_action)

        camera_selector = QComboBox()
        camera_selector.addItems([c.description() for c in self.available_cameras])
        camera_selector.currentIndexChanged.connect( self.select_camera )

        camera_toolbar.addWidget(camera_selector)


        self.setWindowTitle("Fawkes Cloaking Camera")
        self.show()

    def select_camera(self, i):
        """
        Detects if you've selected the camera button.
        """
        self.camera = QCamera(self.available_cameras[i])
        self.camera.setViewfinder(self.viewfinder)
        self.camera.setCaptureMode(QCamera.CaptureStillImage)
        self.camera.error.connect(lambda: self.alert(self.camera.errorString()))
        self.camera.start()

        self.capture = QCameraImageCapture(self.camera)
        self.capture.error.connect(lambda i, e, s: self.alert(s))
        self.capture.imageCaptured.connect(lambda d, i: self.status.showMessage("Image %04d captured" % self.save_seq))

        self.current_camera_name = self.available_cameras[i].description()
        self.save_seq = 0
        
    def take_photo(self):
        """
        Tells the computer's camera to take a photo and then calls fawkes_filter() to cloak the image.
        """
        timestamp = time.strftime("%d-%b-%Y-%H_%M_%S")

        image_name = "%s-%04d-%s.jpg" % (
            self.current_camera_name,
            self.save_seq,
            timestamp
        )
        
        self.capture.capture(image_name)
        
        #You need to sleep because files take time to process/create.
        while not os.path.exists(image_name):
            time.sleep(0.1)

        print("\nDone sleeping.")
        
        self.fawkes_filter(image_name)
        
        self.save_seq += 1
    
    def fawkes_filter(self, image_name):
        """
        Takes an image and cloakes it using Fawkes.
        """
        
        print("THIS IS THE IMAGE NAME: " + image_name)
        
        #For the Fawkes class constructor.
        image_paths = glob.glob(os.path.join(self.save_path, "*"))
        image_paths = [path for path in image_paths if "_cloaked" not in path.split("/")[-1]]
        protector = fawkes.Fawkes("high_extract", '0', 1)
        
        print([self.save_path])
        protector.run_protection(image_paths)
        
        '''
        Possible next steps:
        1) Move cloaked file into new directory.
        2) Delete old uncloaked file.
        '''
        print("Congragulations! Your face(s) have been Fawkesed.")
        

    def alert(self, s):
        """
        Handle errors coming from QCamera dn QCameraImageCapture by displaying alerts.
        """
        err = QErrorMessage(self)
        err.showMessage(s)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setApplicationName("Fawkes Cloaking Camera")

    window = MainWindow()
    app.exec_()
