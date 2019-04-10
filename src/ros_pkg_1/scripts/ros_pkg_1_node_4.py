#! /usr/bin/env python
# coding=utf-8

import roslib

import rospy
import actionlib
import threading

import time

from ros_pkg_1.msg import DoDishesAction, DoDishesGoal

ros_pkg_1_node_4_log_prefix = 'ros_pkg_1_node_4'


# TODO
def feedback(resp):
    rospy.loginfo('%s feedback: data=%s', ros_pkg_1_node_4_log_prefix, resp.data)


def wait_finished(client):
    finished = client.wait_for_result(rospy.Duration.from_sec(1.0))
    while not finished:
        rospy.loginfo('%s waiting completed...', ros_pkg_1_node_4_log_prefix)
        time.sleep(1)
        finished = client.wait_for_result(rospy.Duration.from_sec(1.0))
    rospy.loginfo('%s actionlib execute completed!', ros_pkg_1_node_4_log_prefix)


if __name__ == '__main__':
    rospy.init_node('do_dishes_client')
    client = actionlib.SimpleActionClient('do_dishes', DoDishesAction)
    client.wait_for_server()

    goal = DoDishesGoal()
    # Fill in the goal here
    client.send_goal(goal, feedback_cb=feedback)

    threading.Thread(target=wait_finished, args=(client,)).start()
    # wait_finished(client)

    rospy.loginfo('%s Ready!', ros_pkg_1_node_4_log_prefix)
    rospy.spin()
