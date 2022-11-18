import rclpy
from rclpy.node import Node

from sensor_msgs.msg import Joy
#from std_msgs.msg import UInt8MultiArray
from std_msgs.msg import UInt16

class DrivetrainSubscriber(Node):
	
	def __init__(self):
		super().__init__('drivetrain_subscriber')
		self.subscription = self.create_subscription(
			Joy,
			'joy',
			self.listener_callback,
			10)
		self.subscription
		#self.publisher = self.create_publisher(UInt8MultiArray, 'motor_control', 10)
		self.publisher = self.create_publisher(UInt16, 'motor_control', 10)
		self.max_speed_val = 180
		self.middle_speed_val = 90	
	def listener_callback(self, msg):
		#print("Forward back:", msg.axes[1]) # forward back axis
		#print("Left right:", msg.axes[0]) # left right axis
		self.left_speed = 0
		self.right_speed = 0
		self.left_speed = msg.axes[1] - msg.axes[0]
		self.right_speed = msg.axes[1] + msg.axes[0]
		if self.left_speed > 1:
			self.left_speed = 1
		elif self.left_speed < -1:
			self.left_speed = -1
		if self.right_speed > 1:
			self.right_speed = 1
		elif self.right_speed < -1:
			self.right_speed = -1
		self.left_speed = (self.left_speed + 1) * self.middle_speed_val
		self.right_speed = (self.right_speed + 1) * self.middle_speed_val 
		print("Left speed:", self.left_speed)
		print("Right speed:", self.right_speed)
		print("test")
		self.msg_to_send = UInt16() #MultiArray()
		print("Another test")
		self.msg_to_send.data = int(self.left_speed) | (int(self.right_speed) << 8)#, int(self.right_speed)]
		
		print(self.msg_to_send)
		self.publisher.publish(self.msg_to_send)

		#print(msg)
		
def main(args=None):
	rclpy.init(args=args)
	
	dt = DrivetrainSubscriber()
	
	rclpy.spin(dt)
	
	dt.destroy_node()
	rclpy.shutdown()

if __name__ == '__main__':
    main()
