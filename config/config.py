# Game Configuration
import json

def get_config():
  with open('config/config.json', 'r') as f:
    return json.load(f)


# Unpack our configurations
config = get_config()
goal_symbol = config["goal_symbol"]
money_symbol = config["money_symbol"]
explored_symbol = config["explored_symbol"]
wall_symbol = config["wall_symbol"]
loop_delay = config["loop_delay"]
unexplored_symbol = config["unexplored_symbol"]
width = config["window_width"]
height = config["window_height"]