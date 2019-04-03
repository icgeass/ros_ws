#!/usr/bin/env python
# coding=utf-8


# 服务调用和消息发送

import rospy
from ros_pkg_1.msg import *
from ros_pkg_1.srv import *

from std_srvs.srv import Trigger, TriggerResponse
from std_msgs.msg import String, Header
from ros_pkg_1_node_2 import ros_pkg_1_node_2_log_prefix

ros_pkg_1_node_3_log_prefix = 'ros_pkg_1_node_3'

ros_pkg_1_node_3_pub = None
ros_pkg_1_node_3_service_proxy = None


def service_call_and_msg_publish(request):
    re = TriggerResponse(success=False, message='msg')
    try:
        rospy.loginfo('%s request=%s', ros_pkg_1_node_3_log_prefix, str(request))

        global ros_pkg_1_node_3_service_proxy, ros_pkg_1_node_3_pub

        # 调服务
        result1 = ros_pkg_1_node_3_service_proxy(GetKeyValuesRequest(keys=['key1', 'key2']))
        rospy.loginfo('%s service result: %s', ros_pkg_1_node_3_log_prefix, result1.key_values[0].value)

        # 发消息
        user_infos = UserInfos(header=Header(seq=101, stamp=rospy.get_rostime(), frame_id='frame_id-1'), id=1,
                               user_infos=[UserInfo(first_name='f1'), UserInfo(first_name='f2')])

        ros_pkg_1_node_3_pub.publish(user_infos)
        rospy.loginfo('%s publish msg success, msg=%s', ros_pkg_1_node_3_log_prefix, str(user_infos))

        re.success = True
    except Exception as e:
        re.message = e.message
        rospy.logerr('%s service_call_and_msg_publish Exception=%s', ros_pkg_1_node_3_log_prefix, e.message)
    return re


def server():
    rospy.init_node(ros_pkg_1_node_3_log_prefix)

    global ros_pkg_1_node_3_service_proxy, ros_pkg_1_node_3_pub
    # 服务代理
    ros_pkg_1_node_3_service_proxy = rospy.ServiceProxy(ros_pkg_1_node_2_log_prefix + '/get_key_values', GetKeyValues)
    # 消息发送
    ros_pkg_1_node_3_pub = rospy.Publisher('ros_pkg_1_node_1_msg_3', UserInfos, queue_size=1)

    rospy.Service(ros_pkg_1_node_3_log_prefix + '/service_call_and_msg_publish', Trigger, service_call_and_msg_publish)
    rospy.loginfo("%s Ready!", ros_pkg_1_node_3_log_prefix)
    rospy.spin()


if __name__ == '__main__':
    server()
