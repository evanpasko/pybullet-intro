import pybullet as p
import time
import pybullet_data
from typing import Iterable

class JointCommands:
    '''
    Collection of useful tools for commanding joints in pybullet
    '''

    @staticmethod
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