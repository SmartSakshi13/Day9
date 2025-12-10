from robotics.motors import set_speed
from robotics.sensors import read_distance
from robotics.utils import log

log("Robot Starting...")
d = read_disatance()
log(f"Distance : {d}cm")
set_speed(20,10)
