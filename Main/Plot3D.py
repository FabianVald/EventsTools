from bin2np import read_events
import numpy as np
import os
import plotly.graph_objects as go


filename = ''
events = read_events(filename) 

X = events[:, 0]
Y = events[:, 1]
polarity = events[:, 2]
colors = np.where(polarity == 0, 'black', 'blue')
timestamp = events[:, 3]


fig = go.Figure(
    [
        go.Scatter3d(x=X, 
                     y=Y,
                     z=timestamp, mode='markers',
        marker=dict(size=1, color = colors))
    ]
)
fig.update_layout(scene=dict(        
                    xaxis_title='X Axis',
                    yaxis_title='Y Axis',
                    zaxis_title='Timestamp',
                    xaxis=dict(showgrid=False, showbackground=False, showticklabels=False, visible=False),
                    yaxis=dict(showgrid=False, showbackground=False, showticklabels=False, visible=False),
                    zaxis=dict(showgrid=False, showbackground=False, showticklabels=False, visible=False)
                    ),    
                  title='3D Event Plot'
                )


fig.update_layout(scene_camera=dict(
    eye=dict(x=1, y=1.3, z=1)
))

fig.show()