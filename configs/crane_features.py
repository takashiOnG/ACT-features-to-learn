features = {
    "observation.state": {
        "dtype": "float32",
        "shape": (8,),
        "names": ["joint1", "joint2", "joint3", "joint4", "gripper", "ee_x", "ee_y", "ee_z"],
    },
    "observation.environment_state": {
        "dtype": "float32",
        "shape": (8,),
        "names": ["joint1", "joint2", "joint3", "joint4", "gripper", "ee_x", "ee_y", "ee_z"],
    },
    "action": {
        "dtype": "float32",
        "shape": (5,),
        "names": ["joint1", "joint2", "joint3", "joint4", "gripper"],
    },
}
# Below is used for the dataset conversion
robot_type = "crane_plus"
repo_id = "crane_plus_pekori_and_kururi20_EE2"
root = "/home/ubuntu/dataset/lerobot_dataset/crane_plus_pekori_and_kururi20_EE2"
task_name = "pekori_and_kururi20_EE2"
