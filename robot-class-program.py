class DriveBot:
  def __init__(self, motor_speed = 0, direction = 0, sensor_range = 0):
    self.motor_speed = motor_speed
    self.direction = direction
    self.sensor_range = sensor_range

  def control_bot(self, new_speed, new_direction):
    self.motor_speed = new_speed
    self.direction = new_direction

  def adjust_sensor(self, new_sensor_range):
    self.sensor_range = new_sensor_range


#MAKE ROBOT 1

robot_1 = DriveBot(5, 90, 10)

print(robot_1.motor_speed)    #outputs 5
print(robot_1.direction)       #outputs 90
print(robot_1.sensor_range)     #outputs 10



robot_1.control_bot(10, 180)        #changes speed to 10mph and direction by 180 degrees
robot_1.adjust_sensor(20)	    #changes sensor to 20ft

print(robot_1.motor_speed)    #outputs 10
print(robot_1.direction)       #outputs 180
print(robot_1.sensor_range)     #outputs 20


#MAKE ROBOT 2

robot_2 = DriveBot(35, 75, 25)
print(robot_2.motor_speed)   #35
print(robot_2.direction)     #75
print(robot_2.sensor_range)    #25
