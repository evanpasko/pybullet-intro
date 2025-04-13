import pybullet as p
import time
import pybullet_data
from typing import Iterable

def command_velocity(uid: int, j: Iterable[int], v: Iterable[float]) -> None: 
    '''
    Command each joint in the list with its corresponding velocity.

    :param uid: unique ID of the robot loaded into the sim via LoadURDF or similar
    :param j: list of joints you wish to command (note: not all joints are mobile, refer to URDF
    to be certain which joints are not static).
    :param v: velocities with which you want to command each joint of corresponding index
    '''
    if len(j) != len(v):
        raise Exception("joint and velocity lists are of unequal length")

    maxForce = 500
    for i in range(len(v)):
        p.setJointMotorControl2(bodyUniqueId=uid, 
            jointIndex=j[i], 
            controlMode=p.VELOCITY_CONTROL,
            targetVelocity = v[i],
            force = maxForce)       

    return None


def main():
    '''
    Core simulation function - instantiate and step pybullet sim with simple plane and R2-D2 bot
    for testing basic PyBullet capabilities
    '''
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
    print(type(boxId))
    print(p.getJointInfo(boxId, 0))

    targetVel = 100
    maxForce = 500

    # Command right wheels
    command_velocity(boxId, [2, 3], [50, 50])

    # Command left wheels
    command_velocity(boxId, [6, 7], [50, 50])

    for i in range(10000):
        p.stepSimulation()

        time.sleep(1.0 / 60.0)
    cubePos, cubeOrn = p.getBasePositionAndOrientation(boxId)
    print(cubePos, cubeOrn)
    p.disconnect()


if __name__ == "__main__":
    main()
