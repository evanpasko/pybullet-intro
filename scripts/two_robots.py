import pybullet as p
import time
import pybullet_data


def main():
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

    # Instantiate second robot to check for collisions:
    robot2_p0 = [0, 0, 2]
    robot2_r0 = p.getQuaternionFromEuler([0.5, 0.5, 0.5])
    r2_id = p.loadURDF("r2d2.urdf", robot2_p0, robot2_r0)

    # Let some time go by and then update model transforms
    for i in range(40):
        p.stepSimulation()
        time.sleep(1.0 / 60.0)

    robot2_p1 = [1, 1, 0]
    robot2_r1 = p.getQuaternionFromEuler([0, 0, 0])
    p.resetBasePositionAndOrientation(r2_id, robot2_p1, robot2_r1)

    for i in range(10000):
        p.stepSimulation()
        time.sleep(1.0 / 60.0)
    cubePos, cubeOrn = p.getBasePositionAndOrientation(boxId)
    print(cubePos, cubeOrn)
    p.disconnect()


if __name__ == "__main__":
    main()
