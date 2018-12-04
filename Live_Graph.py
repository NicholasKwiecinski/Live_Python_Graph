import serial # import Serial Library
import numpy  # Import numpy
import matplotlib.pyplot as plt #import matplotlib library
from drawnow import *

arduinoData = serial.Serial('COM4', 9600)
accx_log = []
plt.ion() #Tell matplotlib you want interactive mode to plot live data
arduinoData.flush()
cnt=0
#
#                   # or as much is in the buffer
# style.use('fivethirtyeight')
# fig = plt.figure()
# ax1 = fig.add_subplot(1,1,1)
# plt.ylim((-6, 6))

# print("connected to: " + ser.portstr)
# time_log = []

#
# def animate(i):
#     line = ser.readline().decode("ascii")
#     data = line.strip('\n').strip('\r').split(",")
#     time_log.append(time.time())
#     accx_log.append(data[0])
#     if (accx_log.__len__() == 100):
#         accx_log.pop(0)
#         time_log.pop(0)
#     ax1.clear()
#     ax1.plot(time_log, accx_log)
#
#
#
# ani = animation.FuncAnimation(fig, animate, interval=5)
# plt.show()


def makeFig():  # Create a function that makes our desired plot
    plt.ylim(-10, 10)  # Set y min and max values
    plt.title('My Live Streaming Sensor Data')  # Plot the title
    plt.grid(True)  # Turn the grid on
    plt.ylabel('m/s^2')  # Set ylabels
    plt.plot(accx_log, label='Acceleration X')  # plot the temperature
   # plt.legend(loc='upper left')  # plot the legend
   # plt2 = plt.twinx()  # Create a second y axis
   # plt.ylim(93450, 93525)  # Set limits of second y axis- adjust to readings you are getting
  #  plt2.plot(pressure, 'b^-', label='Pressure (Pa)')  # plot pressure data
   # plt2.set_ylabel('Pressrue (Pa)')  # label second y axis
  #  plt2.ticklabel_format(useOffset=False)  # Force matplotlib to NOT autoscale y axis
  #  plt2.legend(loc='upper right')  # plot the legend


while True:  # While loop that loops forever
    # while (arduinoData.inWaiting() == 0):  # Wait here until there is data
    #     pass  # do nothing
    arduinoString = arduinoData.readline()  # read the line of text from the serial port
    dataArray = arduinoString.decode("ascii").split(',')  # Split it into an array called dataArray
    acc_x = float(dataArray[0])
    accx_log.append(acc_x)
    drawnow(makeFig)  # Call drawnow to update our live graph
    plt.pause(.000001)  # Pause Briefly. Important to keep drawnow from crashing
    cnt = cnt + 1
    if (cnt > 50):  # If you have 50 or more points, delete the first one from the array
        accx_log.pop(0)  # This allows us to just see the last 50 data points
