import numpy as np 

class Flight:
    def __init__(self, speed, altitude, t_end):
        '''
        '''
        self.speed = speed #[km/h]
        self.altitude = altitude #[km]
        self.t_end = duration #[hrs]
        self.t_start = 0 #[hrs]
        self.dt = 0.005
        self.t = np.arrange(self.t_start, self.t_end, self.dt)


    def adjust_speed(self):
        pass

    def adjust_altitude(self):
        pass



