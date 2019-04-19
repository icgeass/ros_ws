#! /usr/bin/env python
# coding=utf-8

import roslib

import rospy
import actionlib
import threading

import time

from ros_pkg_1.msg import DoDishesAction, DoDishesGoal

ros_pkg_1_node_4_log_prefix = 'ros_pkg_1_node_4'


def wait_finished(client):
    finished = client.wait_for_result(rospy.Duration.from_sec(1.0))
    while not finished:
        rospy.loginfo('%s waiting completed...', ros_pkg_1_node_4_log_prefix)
        time.sleep(1)
        finished = client.wait_for_result(rospy.Duration.from_sec(1.0))
    rospy.loginfo('%s actionlib execute completed!, state=%s, result=%s', ros_pkg_1_node_4_log_prefix, client.get_state(), client.get_result())


# TODO
def feedback_cb(feedback):
    rospy.loginfo('%s feedback_cb: data=%s', ros_pkg_1_node_4_log_prefix, feedback)


def active_cb():
    rospy.loginfo('%s active_cb', ros_pkg_1_node_4_log_prefix)


def done_cb(param1, param2):
    rospy.loginfo('%s done_cb, param1=%s, param2=%s', ros_pkg_1_node_4_log_prefix, param1, param2)


if __name__ == '__main__':
    rospy.init_node('do_dishes_client')
    client = actionlib.SimpleActionClient('do_dishes', DoDishesAction)
    client.wait_for_server()

    goal = DoDishesGoal(dishwasher_id=11)
    # Fill in the goal here
    client.send_goal(goal, done_cb=done_cb, active_cb=active_cb, feedback_cb=feedback_cb)

    threading.Thread(target=wait_finished, args=(client,)).start()
    # wait_finished(client)

    rospy.loginfo('%s Ready!', ros_pkg_1_node_4_log_prefix)
    rospy.spin()
