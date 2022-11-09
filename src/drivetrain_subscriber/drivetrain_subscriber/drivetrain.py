import rclpy
from rclpy.node import Node

from sensor_msgs.msg import Joy

class DrivetrainSubscriber(Node):
	def __init__(self):
		super().__init__('drivetrain_subscriber')
		self.subscription = self.create_subscription(
			Joy,
			'joy',
			self.listener_callback,
			10)
		self.subscription
	def listener_callback(self, msg):
		print("Forward back:", msg.axes[1]) # forward back axis
		print("Left right:", msg.axes[0]) # left right axis
		
		#print(msg)
		
def main(args=None):
	rclpy.init(args=args)
	
	dt = DrivetrainSubscriber()
	
	rclpy.spin(dt)
	
	dt.destroy_node()
	rclpy.shutdown()

if __name__ == '__main__':
    main()
