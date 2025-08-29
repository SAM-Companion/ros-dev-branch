import rclpy
from rclpy.node import Node

from mult_interfaces.srv import MultTwoInts

class MinimalService(Node):

    def __init__(self):
        super().__init__('minimal_service')
        self.srv = self.create_service(MultTwoInts, 'mult_two_ints', self.mult_two_ints_callback)
        self.get_logger().info('Additive service node setup complete.\n----------------\n')


    def mult_two_ints_callback(self, request, response):
        response.prod = request.a * request.b
        self.get_logger().info('Incoming request\na: %d b: %d\n' % (request.a, request.b))

        return response


def main():
    rclpy.init()

    minimal_service = MinimalService()

    rclpy.spin(minimal_service)

    rclpy.shutdown()


if __name__ == '__main__':
    main()


