from flight.flight import Flight
from animation.animation import Animation

if __name__ == "__main__":
    # Example usage:
    speed = 800  # km/h
    altitude = 2  # km
    t_end = 2  # hrs

    # Create a Flight object
    flight = Flight(speed, altitude, t_end)

    # Create Animation object
    animation_obj = Animation(flight)
