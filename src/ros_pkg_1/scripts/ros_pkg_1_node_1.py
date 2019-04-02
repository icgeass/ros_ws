#!/usr/bin/env python
# coding=utf-8


# 消息的接收

import rospy
from ros_pkg_1.msg import UserInfo, UserInfos
from std_msgs.msg import String, Header

ros_pkg_1_node_1_log_prefix = 'ros_pkg_1_node_1'


def on_messgae_1(request):
    rospy.loginfo('%s 收到原生消息: %s', ros_pkg_1_node_1_log_prefix, request.data)


def on_messgae_2(request):
    rospy.loginfo('%s 收到自定义消息: first_name=%s, last_name=%s, age=%s, score=%s', ros_pkg_1_node_1_log_prefix,
                  request.first_name, request.last_name, request.age, request.score)


def on_messgae_3(request):
    header = request.header
    user_infos = request.user_infos
    lines = ''
    for item in user_infos:
        rospy.loginfo('user_info.first_name=%s', item.first_name)
        lines = lines + str(item) + '\n------\n'
    rospy.loginfo('%s 收到嵌套消息: header.seq=%s, header.frame_id=%s, header.stamp=%s, id=%s, user_infos=%s',
                  ros_pkg_1_node_1_log_prefix,
                  header.seq, header.frame_id, header.stamp, request.id, lines)


def listener():
    rospy.init_node(ros_pkg_1_node_1_log_prefix)
    rospy.Subscriber("ros_pkg_1_node_1_msg_1", String, on_messgae_1)
    rospy.Subscriber("ros_pkg_1_node_1_msg_2", UserInfo, on_messgae_2)
    rospy.Subscriber("ros_pkg_1_node_1_msg_3", UserInfos, on_messgae_3)
    rospy.loginfo("%s Ready!", ros_pkg_1_node_1_log_prefix)
    rospy.spin()


if __name__ == '__main__':
    listener()
