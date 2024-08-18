from bin2np import *
from np2img import *
from Plot3D import *
from img2canny import *
import os
import numpy as np
import os
import plotly.graph_objects as go



car = read_events("/home/fbn/EventsTools/Main/bins/car.bin")
chair = read_events("/home/fbn/EventsTools/Main/bins/chair.bin")
helicopter = read_events("/home/fbn/EventsTools/Main/bins/Helicopter.bin")
umbrella = read_events("//home/fbn/EventsTools/Main/bins/umbrella.bin")



def imageinator(array ,name ,T_milliseconds, destiny_save, subfolder_name, canny_=False):
    """
    Create a subfolder in destiny and save N images from event array 
    with T_millisecond windows time between images.
    """

    min_x_y_p_t = [0,0,0,0]
    max_x_y_p_t = [0,0,0,0]
    for i in range(0,4):
        min_x_y_p_t[i] = find_min_max(array, i, find_min=True)
        max_x_y_p_t[i] = find_min_max(array, i, find_min=False)

    i = min_x_y_p_t[3]
    name_number = 0
    ext = ".jpg"

    path_subfolder = os.path.join(destiny_save, subfolder_name)
    if not os.path.exists(path_subfolder):
        os.makedirs(path_subfolder)

    while i < max_x_y_p_t[3]:
        image = np2img_windows_np(array, max_x_y_p_t[0]+1, max_x_y_p_t[1]+1, T_milliseconds, start_time = i)
        _, image = cv2.threshold(image, 1, 255, cv2.THRESH_BINARY)
        if canny_:
            image = GaussianBlur_(image)
            image = median_(image)
            
            
            image = GaussianBlur_(image)
            #_, image = cv2.threshold(image, 30, 255, cv2.THRESH_BINARY)
            #image = eroded_(image)
            #image = dilated_(image)
            #image = canny(image)
        name_file = name+"_"+str(name_number)+ext 
        print(name_file)  
        name_number+=1
        
        path_img = os.path.join(path_subfolder, name_file)
        cv2.imwrite(path_img, image)
        print(f"Img save in: {path_img}")
        
        if(i+T_milliseconds > max_x_y_p_t[3]):
            i+=max_x_y_p_t[3] - i
        else:
            i+=T_milliseconds
        print(i, max_x_y_p_t[3])


imageinator(helicopter,"Helicopter", 5000, "/home/fbn/EventsTools/Main/images", "Helicopter", True)
imageinator(chair,"Chair", 5000, "/home/fbn/EventsTools/Main/images", "Chair", True)
imageinator(car,"car", 5000, "/home/fbn/EventsTools/Main/images", "car", True)
imageinator(umbrella,"umbrella", 5000, "/home/fbn/EventsTools/Main/images", "umbrella", True)

