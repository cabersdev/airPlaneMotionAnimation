import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib.animation as animation
from flight.flight import Flight

class Animation:
    def __init__(self, flight):
        self.flight = flight
        
        # Initialize animation parameters
        self.frame_amount = len(flight.t)
        self.dt = flight.dt
        self.x = flight.d
        self.y = flight.altitude_array
        self.speed_x = flight.speed

        # Create the figure and subplots
        self.fig = plt.figure(figsize=(16, 9), dpi=120, facecolor=(0.8, 0.8, 0.8))
        self.gs = gridspec.GridSpec(2, 2)
        self.setup_plots()

    def setup_plots(self):
        # Subplot 1
        self.ax0 = self.fig.add_subplot(self.gs[0, :], facecolor=(0.9, 0.9, 0.9))
        self.plane_trajectory, = self.ax0.plot([], [], 'r:o', linewidth=2)
        self.ax0.set_xlim(min(self.x), max(self.x))
        self.ax0.set_ylim(0, max(self.y) * 1.1)  # Adjust y-limit to show the entire trajectory
        self.ax0.set_xlabel('Distance (km)')
        self.ax0.set_ylabel('Altitude (km)')

        # Subplot 2
        self.ax2 = self.fig.add_subplot(self.gs[1, 0], facecolor=(0.9, 0.9, 0.9))
        self.x_dist, = self.ax2.plot([], [], '-b', linewidth=3, label='X=800*t')
        self.ax2.set_xlim(min(self.x), max(self.x))
        self.ax2.set_ylim(0, max(self.y) * 1.1)  # Adjust y-limit to show the entire trajectory
        self.ax2.set_xlabel('Time (hrs)')
        self.ax2.set_ylabel('Distance (km)')

        # Subplot 3
        self.ax4 = self.fig.add_subplot(self.gs[1, 1], facecolor=(0.9, 0.9, 0.9))
        self.speed, = self.ax4.plot([], [], '-b', linewidth=3, label='ΔX/Δt = 800')
        self.ax4.set_xlim(min(self.x), max(self.x))
        self.ax4.set_ylim(0, self.speed_x * 1.1)  # Adjust y-limit to show the entire speed range
        self.ax4.set_xlabel('Time (hrs)')
        self.ax4.set_ylabel('Speed (km/h)')

        # Initialize the animation
        self.plane_ani = animation.FuncAnimation(self.fig, self.update_plot,
                                                  frames=self.frame_amount, interval=20,
                                                  repeat=True, blit=True)

        # Display the animation
        plt.show()

    def update_plot(self, num):
        # Update plot elements
        self.plane_trajectory.set_data(self.x[:num], self.y[:num])
        self.x_dist.set_data(self.flight.t[:num], self.x[:num])
        self.speed.set_data(self.flight.t[:num], [self.speed_x] * num)  # Constant speed for all time

        # Return the updated plot elements as a sequence of Artist objects
        return self.plane_trajectory, self.x_dist, self.speed