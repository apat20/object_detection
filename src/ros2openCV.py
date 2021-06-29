#!/usr/bin/env python
## Subscriber node for subscribing to the Image topic published by the Intel Realsense D415 Camera.
# By: Aditya Patankar


import rospy
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import sys

#Initialize a bridge object of class CvBridge
bridge = CvBridge()

#Callback funtion for the subscriber node
def image_callback(ros_image):
    global bridge
    try:
        cv2_image = bridge.imgmsg_to_cv2(ros_image, "bgr8")
    except CvBridgeError as error:
        print(error)
    cv2.imshow("Image: ", cv2_image)
    cv2.imwrite("/home/aditya/catkin_ws/src/object_detection/src/Saved_Images/"+"object_scene"+".jpg",cv2_image)
    cv2.waitKey(3)

#Subscriber node
def image_converter_node(args):
    rospy.init_node('image_converter', anonymous=True)
    image_sub = rospy.Subscriber("/camera/color/image_raw", Image, image_callback)
    try:
        rospy.spin()
    except KeyboardInterrupt:
        print("Shutting down")
    cv2.destroyAllWindows()

if __name__ == '__main__':
    image_converter_node(sys.argv)
