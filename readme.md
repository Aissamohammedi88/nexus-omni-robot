<div align="center">

# 🦾 NEXUS OMNI-ROBOT

### *The 20% Open-Source Core. Built on the shoulders of giants.*

[![Status](https://img.shields.io/badge/STATUS-ACTIVE_R%26D-00ff88?style=for-the-badge)](#)
[![License](https://img.shields.io/badge/LICENSE-NEXUS--OPEN--3.0-00e5ff?style=for-the-badge)](#)
[![Hardware](https://img.shields.io/badge/HARDWARE-Open_Source-ff00c8?style=for-the-badge)](#)
[![Software](https://img.shields.io/badge/SOFTWARE-Sovereign-purple?style=for-the-badge)](#)

</div>

---

## 📖 The 20% Exposure

The **Nexus Omni-Robot** is a next-generation humanoid platform. We are exposing **20% of our proprietary architecture** to the open-source community to accelerate research, foster collaboration, and establish a new standard for sovereign robotics.

This repository contains:
1.  **The Core Perception Stack** (Vision & Spatial Awareness).
2.  **The Kinematic Solver** (Inverse Kinematics for 32 Degrees of Freedom).
3.  **The Swarm Router** (How the robot delegates tasks to local and cloud AI agents).

The remaining 80% (proprietary actuator control, energy management, and the Nexus Quantum Core) remains closed-source.

---

## 🧠 Architecture: Inspired by the Best

We did not reinvent the wheel. We synthesized the best ideas from the most advanced programs in the world.

| Component | Inspiration | Our Implementation |
| :--- | :--- | :--- |
| **Perception** | **Google Appolo** (Autonomous Driving) | We adapted Appolo's sensor fusion algorithms for a 360° LiDAR/Camera array, allowing the robot to navigate dynamic human environments safely. |
| **Actuation** | **Tesla Optimus** (Humanoid) | We adopted the "end-to-end neural network" approach for motor control, bypassing traditional PID controllers for smoother, more human-like movement. |
| **Cognition** | **Nexus Omega** (Our Engine) | The robot uses our proprietary OMEGA protocol to route complex tasks to local LLMs (for privacy) or cloud APIs (for heavy computation). |

---

## ⚙️ Hardware Specifications

<div align="center">

| Spec | Value |
| :--- | :--- |
| **Degrees of Freedom** | 32 (Human-like dexterity) |
| **Actuators** | Custom Brushless DC (Torque: 120 Nm) |
| **Compute** | Dual NVIDIA Jetson Orin (One for Vision, One for Motion) |
| **Sensors** | 1x 360° LiDAR, 4x Depth Cameras, 2x Force-Torque Sensors |
| **Power** | 48V Solid-State Battery (8 hours runtime) |
| **Weight** | 65 kg |

</div>

---

## 🚀 The 20% Open-Source Core (What is in this repo?)

This repository is not a toy. It contains the critical code that allows the robot to *see* and *move*.

### 1. `perception/` (The Eyes)
- `lidar_fusion.py`: Fuses raw LiDAR point clouds with RGB camera feeds.
- `obstacle_avoidance.py`: Real-time path planning using A* and RRT*.

### 2. `kinematics/` (The Muscles)
- `ik_solver.py`: Inverse Kinematics solver for the 32-DOF arm and leg joints.
- `gait_generator.py`: Dynamic walking algorithm (Zero Moment Point).

### 3. `cognition/` (The Brain Interface)
- `omega_router.py`: The interface to the Nexus OMEGA Swarm. It decides if a command is processed locally (for speed) or sent to the cloud (for complex reasoning).

---

## 🛠️ Installation & Simulation

You don't need the physical robot to test our code. We provide a complete simulation environment.

### Prerequisites
- Python 3.10+
- ROS 2 (Humble Hawksbill)
- Gazebo Sim

### Quick Start

```bash
# 1. Clone the repository
git clone https://github.com/Aissamohammedi88/nexus-omni-robot.git
cd nexus-omni-robot

# 2. Install dependencies
pip install -r requirements.txt
🔒 License & Contribution

This project is licensed under NEXUS-OPEN 3.0.

    You can use, modify, and distribute the 20% core.

    You must attribute the original work to Aissa Mohammedi (DGK).

    You cannot patent derived works.

We are looking for contributors in:

    Computer Vision (SLAM, Object Detection)

    Reinforcement Learning (for gait optimization)

    Embedded Systems (for actuator control)

<div align="center">

Aissa Mohammedi (DGK)
Founder, Nexus Ecosystem

    "A robot is not a product. It is a physical manifestation of software. And software must be free."

</div> ```
# 3. Launch the simulation
# This will open a Gazebo window with the robot in a virtual environment
ros2 launch nexus_robot simulation.launch.py
