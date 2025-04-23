import rclpy
from rclpy.node import Node
from geometry_msgs.msg import TransformStamped
from tf2_ros import TransformBroadcaster


class DynamicTransformPublisher(Node):
    def __init__(self):
        super().__init__('dynamic_tf_publisher')
        self.br = TransformBroadcaster(self)
        self.timer = self.create_timer(1, self.publish_transform)  # 1 Hz

    def publish_transform(self):
        t = TransformStamped()

        t.header.stamp = self.get_clock().now().to_msg()
        t.header.frame_id = 'link_head_tilt'
        t.child_frame_id = 'camera_color_optical_frame'

        t.transform.translation.x = 0.031591
        t.transform.translation.y = -0.0119208
        t.transform.translation.z = 0.0807607

        t.transform.rotation.x = -0.489168
        t.transform.rotation.y = 0.51206
        t.transform.rotation.z = -0.507018
        t.transform.rotation.w = 0.491368

        self.br.sendTransform(t)


def main():
    rclpy.init()
    node = DynamicTransformPublisher()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == '__main__':
    main()