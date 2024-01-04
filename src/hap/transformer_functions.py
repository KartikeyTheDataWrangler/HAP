import pandas as pd


def get_pulsepressure(pressure):
    pressure_list = pressure.split(sep='/')
    pp = int(pressure_list[0]) - int(pressure_list[1])
    pp_ = 0
    
    
    if pp<40:
        pp_ = 'low'
       
      
    elif pp>=40 and pp<=80:
        pp_ = 'normal'
        
    
    elif pp>80 and pp<=120:
        pp_ = 'high'
         
    else:
        pp_ = 'extremely high'
    
    
    return pp_

