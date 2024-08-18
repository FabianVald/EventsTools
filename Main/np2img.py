import numpy as np
import matplotlib.pyplot as plt
from bin2np import read_events

def np2img_(events, width, height):
    image = np.zeros((height, width), dtype=np.uint8)
    
    for x, y, _, polarity in events:
        image[y, x] = polarity  #Sobrevive la ultima polaridad
    
    return image

def filter_events_by_time(events, start_time, end_time):
    return events[(events[:, 3] >= start_time) & (events[:, 3] <= end_time)]



def np2img_windows_np(array, width, height, T_milliseconds,start_time):
    events = array 

    T_microseconds = T_milliseconds# milisegundos a microsegundos

    #setear tiempos relativos o absolutos.
    end_time = start_time + T_microseconds

    filtered_events = filter_events_by_time(events, start_time, end_time)
    image = np2img_(filtered_events, width, height)

    return image
