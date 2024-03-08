import subprocess
import datetime
import os

folder_path = "/app/output"
def capture_image(folder_path):
    # Ensure the folder exists
    os.makedirs(folder_path, exist_ok=True)
    
    # Get the current time for a unique image filename
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"image_{timestamp}.jpg"
    
    # Specify the full path for the image
    full_path = os.path.join(folder_path, filename)
    
    # Capture an image using libcamera-still and save it in the specified folder
    command = f"libcamera-still -o {full_path}"
    subprocess.run(command, shell=True, check=True)

if __name__ == "__main__":
    # Call capture_image with the desired folder path
    i=1
    while(i>0):
        capture_image(folder_path)
        i+=1

