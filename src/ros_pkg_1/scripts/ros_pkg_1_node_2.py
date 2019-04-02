#!/usr/bin/env python
# coding=utf-8


# 接口的提供

import rospy
from ros_pkg_1.msg import UserInfo, UserInfos, KeyValue
from ros_pkg_1.srv import AddTwoInts, AddTwoIntsResponse, GetKeyValues, GetKeyValuesResponse
from std_msgs.msg import String, Header

ros_pkg_1_node_2_log_prefix = 'ros_pkg_1_node_2'


def add_two_ints(request):
    re = request.a + request.b
    rospy.loginfo('%s add ints, a=%s, b=%s, return=%s', ros_pkg_1_node_2_log_prefix, request.a, request.b, re)
    return AddTwoIntsResponse(re)


def get_key_values(request):
    keys = request.keys
    rospy.loginfo('%s get key_values, keys=%s', ros_pkg_1_node_2_log_prefix, str(keys))
    arr = []
    for item in keys:
        arr.append(KeyValue(key=item, value=item + '-value'))
    return GetKeyValuesResponse(key_values=arr)


def server():
    rospy.init_node(ros_pkg_1_node_2_log_prefix)
    rospy.Service(ros_pkg_1_node_2_log_prefix + '/add_two_ints', AddTwoInts, add_two_ints)
    rospy.Service(ros_pkg_1_node_2_log_prefix + '/get_key_values', GetKeyValues, get_key_values)
    rospy.loginfo("%s Ready!", ros_pkg_1_node_2_log_prefix)
    rospy.spin()


if __name__ == '__main__':
    server()
