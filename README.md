# PyBullet Shenanigans

This repository is entirely for me to gain experience with the PyBullet dynamics/kinematics engine for use in Robotics and AI applications.

While I primarily work in ROS/Gazebo, I think it's important to understand the capabilities of PyBullet along with the other leading simulations in edge-AI research (Isaac and MuJoCo). 

## Tutorial

### Setup the project

This project uses [uv](https://github.com/astral-sh/uv), a rust-based python project manager. If you'd like to take advantage of the uv interface, follow the instructions for installation. 

1. Clone the repository and setup your python environment
```bash
git clone git@github.com:evanpasko/pybullet-intro.git
cd pybullet-intro
uv sync
source .venv/bin/activate
```
Now you should have a python virtual environment with all of our project dependencies. 

If you don't want to use uv - you can install the dependencies with 

```bash
pip3 install -e .
```

### Hello Pybullet World

To run the introductory pybullet world, make sure you have your virtual environment activated or the dependencies installed in your base python environment. 

```bash
cd scripts
python3 hello-pybullet.py
```

Now, an interactive simulation window should pop up, which you can interact with through the GUI. 

Simply closing the simulation window, or pressing `ctrl+c` in the terminal window will shutdown the process. you can also wait for it to timeout. 


### Experimenting with PyBullet