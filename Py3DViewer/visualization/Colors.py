import numpy as np


class colors:
    
    teal = np.array([1, 212, 180],dtype=np.float) / 255
    black = np.array([0, 0, 0],dtype=np.float) / 255
    orange = np.array([255, 165, 0], dtype=np.float) / 255
    blue = np.array([0, 0, 255], dtype=np.float) / 255
    red = np.array([255, 0, 0], dtype=np.float) / 255
    green = np.array([0, 255, 0], dtype=np.float) / 255
    white = np.array([255, 255, 255], dtype=np.float) / 255
    purple = np.array([255, 0, 255], dtype=np.float) / 255
    
    
    def hex2rgb(hex_color):
        return [int(hex_color[1:3],16)/255,int(hex_color[3:5],16)/255,int(hex_color[5:],16)/255]

    def rgb2hex(rgb_color):
        r = format(int(rgb_color[0]*255), 'x')
        g = format(int(rgb_color[1]*255), 'x')
        b = format(int(rgb_color[2]*255), 'x')
        
        if len(r) == 1:
            r = '0'+r
        if len(g) == 1:
            g = '0'+g
        if len(b) == 1:
            b = '0'+b
        return f"#{r}{g}{b}"
    
    
    def random_color(return_hex = False):
        
        r = np.random.randint(256) / 255.0
        g = np.random.randint(256) / 255.0 
        b = np.random.randint(256) / 255.0
        
        color = np.array([r,g,b], dtype=np.float)
        
        if return_hex:
            
            return colors.rgb2hex(color)
        
        return color