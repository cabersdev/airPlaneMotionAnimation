import numpy as np

class Flight:
    def __init__(self, speed, altitude, t_end):
        '''
        Initializes a flight object with given parameters

        Parameters:
        - speed (float): Speed of the airplane in kilometers per hour.
        - altitude (float): Altitude of the airplane in kilometers. 
        - t_end (float): End time of the flight simulation in hours.
        '''

        self.speed = speed  # [km/h]
        self.altitude = altitude  # [km]
        self.t_end = t_end  # [hrs]
        self.t_start = 0  # [hrs]
        self.dt = 0.005  # time step
        self.t = np.arange(self.t_start, self.t_end, self.dt)  # time array
        self.d = speed * self.t
        self.altitude_array = np.ones(len(self.t)) * altitude