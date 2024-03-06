import picamera
import time

# Create an object to represent the camera
with picamera.PiCamera() as camera:
    # Set the resolution of the image (optional)
    camera.resolution = (1024, 768)
    
    # Wait for the automatic gain control to settle
    time.sleep(2)
    
    # Now fix the values
    camera.shutter_speed = camera.exposure_speed
    camera.exposure_mode = 'off'
    g = camera.awb_gains
    camera.awb_mode = 'off'
    camera.awb_gains = g
    
    # Finally, take a picture and save it
    camera.capture('/home/pi/Desktop/image.jpg')

print("Image has been captured and saved.")
