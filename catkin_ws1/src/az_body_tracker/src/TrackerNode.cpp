#include "TrackerNode.h"
#include <std_msgs/Float32.h>

TrackerNode::TrackerNode(ros::NodeHandle& _nh)
{
	nh=_nh;
	length_pub = nh.advertise<std_msgs::Float32>("length",1000);
	// pointcloud_pub = nh.advertise<sensor_msgs::PointCloud2>("depth_pcl",1);
	// set queue size 10 
}

void TrackerNode::showInfo(InputSettings& inputSettings){
	if(inputSettings.DepthCameraMode == K4A_DEPTH_MODE_NFOV_UNBINNED) {
		ROS_INFO("Depth Mode : NFOV_UNBINNED");
		ROS_INFO("Depth Resolution : 640 x 576");
		ROS_INFO("Camera FPS : 30");}
		// RCLCPP_INFO(this->get_logger(), "K4A depth_mode : NFOV_UNBINNED");
		// RCLCPP_INFO(this->get_logger(), "K4A camera_FPS : 30");}
	else if (inputSettings.DepthCameraMode == K4A_DEPTH_MODE_WFOV_2X2BINNED){
		ROS_INFO("Depth Mode : WFOV_2X2BINNED");
		ROS_INFO("Depth Resolution : 512 x 512");
		ROS_INFO("Camera FPS : 30");}

		// RCLCPP_INFO(this->get_logger(), "K4A depth_mode : WFOV_2X2BINNED");
		// RCLCPP_INFO(this->get_logger(), "K4A camera_FPS : 30");}
	else if(inputSettings.DepthCameraMode == K4A_DEPTH_MODE_WFOV_UNBINNED){
		ROS_INFO("Depth Mode : WFOV_UNBINNED");
		ROS_INFO("Depth Resolution : 1024 x 1024");
		ROS_INFO("Camera FPS : 15");}
		// RCLCPP_INFO(this->get_logger(), "K4A depth_mode : WFOV_UNBINNED");
		// RCLCPP_INFO(this->get_logger(), "K4A camera_FPS : 15");}
	else ROS_INFO("failed to read DepthMode.");
}

// k4a_result_t TrackerNode::getPointCloud(const k4a::capture& capture, sensor_msgs::PointCloud2Ptr& point_cloud)
// {
//   k4a::image k4a_depth_frame = capture.get_depth_image();

//   if (!k4a_depth_frame)
//   {
//     ROS_ERROR("Cannot render point cloud: no depth frame");
//     return K4A_RESULT_FAILED;
//   }

//   point_cloud->header.frame_id = calibration_data_.tf_prefix_ + calibration_data_.depth_camera_frame_;
//   point_cloud->header.stamp = timestampToROS(k4a_depth_frame.get_device_timestamp());

//   // Tranform depth image to point cloud
//   calibration_data_.k4a_transformation_.depth_image_to_point_cloud(k4a_depth_frame, K4A_CALIBRATION_TYPE_DEPTH,
//                                                                    &calibration_data_.point_cloud_image_);

//   return fillPointCloud(calibration_data_.point_cloud_image_, point_cloud);
// }

// k4a_result_t TrackerNode::fillPointCloud(const k4a::image& pointcloud_image, sensor_msgs::PointCloud2Ptr& point_cloud)
// {
//   point_cloud->height = pointcloud_image.get_height_pixels();
//   point_cloud->width = pointcloud_image.get_width_pixels();
//   point_cloud->is_dense = false;
//   point_cloud->is_bigendian = false;

//   const size_t point_count = pointcloud_image.get_height_pixels() * pointcloud_image.get_width_pixels();

//   sensor_msgs::PointCloud2Modifier pcd_modifier(*point_cloud);
//   pcd_modifier.setPointCloud2FieldsByString(1, "xyz");

//   sensor_msgs::PointCloud2Iterator<float> iter_x(*point_cloud, "x");
//   sensor_msgs::PointCloud2Iterator<float> iter_y(*point_cloud, "y");
//   sensor_msgs::PointCloud2Iterator<float> iter_z(*point_cloud, "z");

//   pcd_modifier.resize(point_count);

//   const int16_t* point_cloud_buffer = reinterpret_cast<const int16_t*>(pointcloud_image.get_buffer());

//   for (size_t i = 0; i < point_count; i++, ++iter_x, ++iter_y, ++iter_z)
//   {
//     float z = static_cast<float>(point_cloud_buffer[3 * i + 2]);

//     if (z <= 0.0f)
//     {
//       *iter_x = *iter_y = *iter_z = std::numeric_limits<float>::quiet_NaN();
//     }
//     else
//     {
//       constexpr float kMillimeterToMeter = 1.0 / 1000.0f;
//       *iter_x = kMillimeterToMeter * static_cast<float>(point_cloud_buffer[3 * i + 0]);
//       *iter_y = kMillimeterToMeter * static_cast<float>(point_cloud_buffer[3 * i + 1]);
//       *iter_z = kMillimeterToMeter * z;
//     }
//   }

//   return K4A_RESULT_SUCCEEDED;
// }

	// k4a_result_t startTracker();
	// k4a_result_t startImu();

	// void stopTracker();
	// void stopImu();

	// // Get camera calibration information for the depth camera
	// void getDepthCameraInfo(sensor_msgs::msg::CameraInfo& camera_info);

	// void getRgbCameraInfo(sensor_msgs::msg::CameraInfo& camera_info);

	// k4a_result_t getDepthFrame(const k4a::capture& capture, std::shared_ptr<sensor_msgs::msg::Image>& depth_frame, bool rectified);

	// k4a_result_t getPointCloud(const k4a::capture& capture, std::shared_ptr<sensor_msgs::msg::PointCloud2>& point_cloud);

	// k4a_result_t getRgbPointCloudInRgbFrame(const k4a::capture& capture, std::shared_ptr<sensor_msgs::msg::PointCloud2>& point_cloud);
	// k4a_result_t getRgbPointCloudInDepthFrame(const k4a::capture& capture, std::shared_ptr<sensor_msgs::msg::PointCloud2>& point_cloud);

