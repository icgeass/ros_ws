#!/usr/bin/env python
# coding=utf-8

import rospy
from ros_pkg_1.msg import UserInfo
from std_msgs.msg import String

ros_pkg_1_node_1_log_prefix = 'ros_pkg_1_node_1'


def on_messgae_1(request):
    rospy.loginfo('%s 收到原生消息: %s', ros_pkg_1_node_1_log_prefix, request.data)


def on_messgae_2(request):
    rospy.loginfo('%s 收到自定义消息: first_name=%s, last_name=%s, age=%s, score=%s', ros_pkg_1_node_1_log_prefix,
                  request.first_name, request.last_name, request.age, request.score)


def listener():
    rospy.init_node(ros_pkg_1_node_1_log_prefix)
    rospy.Subscriber("ros_pkg_1_node_1_msg_1", String, on_messgae_1)
    rospy.Subscriber("ros_pkg_1_node_1_msg_2", UserInfo, on_messgae_2)
    rospy.loginfo("%s Ready!", ros_pkg_1_node_1_log_prefix)
    rospy.spin()


if __name__ == '__main__':
    listener()
