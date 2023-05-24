import matplotlib.pyplot as plt
from matplotlib import animation

from fileParser import parseArmCoors, parseWristAngles, parseClawState

armCoors = parseArmCoors("/home/ibrahim/simAll.txt")
wristCoors = parseWristAngles("/home/ibrahim/simAll.txt")
clawStateArr = parseClawState("/home/ibrahim/simAll.txt")
fig = plt.figure(figsize=(15, 12))
ax = fig.add_subplot(autoscale_on=False, xlim=(-4., 4.), ylim=(-2., 2.))
clawState = ax.text(0.02, 0.95, '', transform=ax.transAxes)
ax.set_aspect('equal')
ax.grid()
line, = ax.plot([], [], 'o-', lw=2)
chamberLine, = ax.plot([], [], 'o-', lw=2)
wristState = ax.text(0.02, 0.90, '', transform=ax.transAxes)


totalFrames = len(armCoors)


# poses
# pivot: (0,0)
# min arm length: .8
# max arm length: 1.8
# chamber close = (-.1, -1)
# chamber far = (-.6,-1)
def update(frame):
    # for each frame, update the data stored on each artist.
    p1 = [0, armCoors[frame][0]]
    p2 = [0, armCoors[frame][1]]

    chamberClose = [-.1, -.6]
    chamberFar = [-1, -1]
    line.set_data(p1, p2)
    chamberLine.set_data(chamberClose, chamberFar)
    clawState.set_text("Claw State: " +clawStateArr[frame])
    wristState.set_text("Wrist Angle: " + str(wristCoors[frame]/3.14*180))
    return line, chamberLine, wristState, clawState

    # def plotArm():


ani = animation.FuncAnimation(fig, update, totalFrames, interval=.02 * 1000, blit=True)
ani.save('arm.mp4')
plt.show()
