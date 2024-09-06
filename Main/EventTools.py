import numpy as np
import os

class EventTools():
    def __init__(self, path):
        if not (os.path.isfile(path) or os.path.isdir(path)):
            raise ValueError(f"The path {path} is not a valid file or directory.")
        self.path = path
        self.events_array = None
        self.events_window = None 
        self.eimg = None
        self.ewindow = None
        
    def read_events(self):
        '''Array with event, unpacked from bin-encode event data file.'''
        events = []
        
        with open(self.path, 'rb') as f:
            while True:
                data = f.read(5)
                if len(data) < 5:
                    break
                
                packed_data = int.from_bytes(data, byteorder='big')
                
                x = (packed_data >> 32) & 0xFF        
                y = (packed_data >> 24) & 0xFF        
                polarity = (packed_data >> 23) & 0x01 
                timestamp = packed_data & 0x7FFFFF    
                
                events.append((x, y, polarity, timestamp))
                
        self.events_array = np.array(events)

    
    def filter_window(self,start_time, end_time):
        '''Array with spatiotemporal events window'''
        self.events_window = self.events_array[(self.events_array[:, 3] >= start_time) & (self.events_array[:, 3] <= end_time)]

    def find_min_max_index(self, index, find_min=True):
        if find_min:
            return min(self.events_array, key=lambda event: event[index])[index]
        else:
            return max(self.events_array, key=lambda event: event[index])[index]
    
    def e2img(self,H ,W ,window = False):
        '''Return an array image according a criterium'''
        if window:
            self.ewindow = np.zeros((H, W), dtype=np.uint16)
            for x, y, _, polarity in self.events_window:
                if polarity == 1:
                    #print(1)
                    self.ewindow[y, x] += 1
                else:
                    #print(0)
                    self.ewindow[y, x] -= 1
      
            
        else:
            self.eimg = np.zeros((H, W), dtype=np.float64)
            for x, y, _, polarity in self.events_array:
                if polarity == 1:
                    self.eimg[y, x] += 1
                else:
                    self.eimg[y, x] -= 1
                    


        
    def reset(self):
        self.events_array = None
        self.events_window = None 
        self.eimg = None
        self.ewindow = None