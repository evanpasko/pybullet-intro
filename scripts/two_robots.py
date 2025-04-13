import pybullet as p
import time
import pybullet_data

def main():
    physicsClient = p.connect(p.GUI)#or p.DIRECT for non-graphical version
    p.setAdditionalSearchPath(pybullet_data.getDataPath()) #optionally
    p.setGravity(0,0,-10)
    planeId = p.loadURDF("plane.urdf")
    startPos = [0,0,1]
    startOrientation = p.getQuaternionFromEuler([0,0,0])
    boxId = p.loadURDF("r2d2.urdf",startPos, startOrientation)

    # Instantiate second robot to check for collisions: 
    robot2_p0 = [0,0,2]
    robot2_r0 = p.getQuaternionFromEuler([0.5, 0.5, 0.5])
    r2_id = p.loadURDF("r2d2.urdf", robot2_p0, robot2_r0)

    #set the center of mass frame (loadURDF sets base link frame) startPos/Ornp.resetBasePositionAndOrientation(boxId, startPos, startOrientation)
    for i in range (10000):
        p.stepSimulation()
        time.sleep(1./240.)
    cubePos, cubeOrn = p.getBasePositionAndOrientation(boxId)
    print(cubePos,cubeOrn)
    p.disconnect()

if __name__ == "__main__":
    main()