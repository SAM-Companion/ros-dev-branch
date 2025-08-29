from mult_interfaces.srv import MultTwoInts

import rclpy
from rclpy.node import Node


class MinimalClientAsync(Node):

    def __init__(self):
        super().__init__('minimal_client_async')
        self.cli = self.create_client(MultTwoInts, 'mult_two_ints')
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')
        self.req = MultTwoInts.Request()

    def send_request(self, a, b):
        self.req.a = a
        self.req.b = b
        return self.cli.call_async(self.req)


def main():
    rclpy.init()

    minimal_client = MinimalClientAsync()
    flag = True
    while flag:
        i, j = map(int, input("Input two integers:\n> ").strip().split())
        future = minimal_client.send_request(i, j)
        rclpy.spin_until_future_complete(minimal_client, future)
        response = future.result()
        minimal_client.get_logger().info(
            'Response: %d * %d = %d\n' %
            (i, j, response.prod))
        if int(response.prod) == 6:
            flag = False 
        
        continue 

    minimal_client.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()


