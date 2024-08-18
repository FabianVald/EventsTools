import numpy as np

def read_events(path):
    events = []
    with open(path, 'rb') as f:
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
    
    return np.array(events)

def find_min_max(array, index, find_min=True):
    if find_min:
        return min(array, key=lambda evento: evento[index])[index]
    else:
        return max(array, key=lambda evento: evento[index])[index]
