#ifndef TRACKER_NODE_H
#define TRACKER_NODE_H
#include <k4a/k4a.hpp>
#include <k4abt.h>
#include <ros/ros.h>
#include <std_msgs/String.h>
#include <sensor_msgs/point_cloud2_iterator.h>

struct InputSettings
{
    k4a_depth_mode_t DepthCameraMode = K4A_DEPTH_MODE_WFOV_UNBINNED;
    k4abt_tracker_processing_mode_t processingMode = K4ABT_TRACKER_PROCESSING_MODE_GPU_CUDA;
    k4a_fps_t cameraFPS = K4A_FRAMES_PER_SECOND_15;
    k4a_color_resolution_t colorResolution = K4A_COLOR_RESOLUTION_720P;
};

class TrackerNode
{
public:
  ros::NodeHandle nh;
  ros::Publisher length_pub, pointcloud_pub;
  TrackerNode(ros::NodeHandle& _nh);
  void showInfo(InputSettings& inputSettings);
  k4a_result_t getPointCloud(const k4a::capture& capture, sensor_msgs::PointCloud2Ptr& point_cloud);
  k4a_result_t fillPointCloud(const k4a::image& pointcloud_image, sensor_msgs::PointCloud2Ptr& point_cloud);
private:
  uint16_t count_=0; 
};
#endif // TRACKER_NODE_H