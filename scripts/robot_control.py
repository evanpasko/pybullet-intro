import pybullet as p
import time
import pybullet_data
from typing import Iterable

from pybullet_intro.utils import JointCommands


def main():
    """
    Core simulation function - instantiate and step pybullet sim with simple plane and R2-D2 bot
    for testing basic PyBullet capabilities
    """
    physicsClient = p.connect(p.GUI)  # or p.DIRECT for non-graphical version
    p.setAdditionalSearchPath(pybullet_data.getDataPath())  # optionally
    p.setGravity(0, 0, -10)

    # Change timestep to work on my slow macbook
    p.setTimeStep(1 / 60.0)

    planeId = p.loadURDF("plane.urdf")
    startPos = [0, 0, 1]
    startOrientation = p.getQuaternionFromEuler([0, 0, 0])

    # set the center of mass frame (loadURDF sets base link frame) startPos/Ornp.resetBasePositionAndOrientation(boxId, startPos, startOrientation)
    boxId = p.loadURDF("r2d2.urdf", startPos, startOrientation)

    targetVel = 100
    maxForce = 500

    # Command right wheels
    JointCommands.command_velocity(boxId, [2, 3], [50, 50])

    # Command left wheels
    JointCommands.command_velocity(boxId, [6, 7], [50, 50])

    for i in range(10000):
        p.stepSimulation()
        time.sleep(1.0 / 60.0)

    cubePos, cubeOrn = p.getBasePositionAndOrientation(boxId)
    print(cubePos, cubeOrn)
    p.disconnect()


if __name__ == "__main__":
    main()
