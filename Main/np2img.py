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

filename = ''
events = read_events(filename) 

width = 240
height = 100

T_milliseconds = 33
T_microseconds = T_milliseconds * 1000  # milisegundos a microsegundos

#setear tiempos relativos o absolutos.
start_time = 0
end_time = T_microseconds

filtered_events = filter_events_by_time(events, start_time, end_time)
image = np2img_(filtered_events, width, height)

plt.imshow(image, cmap='gray', origin='upper')
plt.colorbar()  
plt.title(f'Imagen de Eventos ({T_milliseconds} ms)')
plt.show()
