// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from gazebo_map_creator_interface:srv/MapRequest.idl
// generated code does not contain a copyright notice

#ifndef GAZEBO_MAP_CREATOR_INTERFACE__SRV__DETAIL__MAP_REQUEST__BUILDER_HPP_
#define GAZEBO_MAP_CREATOR_INTERFACE__SRV__DETAIL__MAP_REQUEST__BUILDER_HPP_

#include "gazebo_map_creator_interface/srv/detail/map_request__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace gazebo_map_creator_interface
{

namespace srv
{

namespace builder
{

class Init_MapRequest_Request_filename
{
public:
  explicit Init_MapRequest_Request_filename(::gazebo_map_creator_interface::srv::MapRequest_Request & msg)
  : msg_(msg)
  {}
  ::gazebo_map_creator_interface::srv::MapRequest_Request filename(::gazebo_map_creator_interface::srv::MapRequest_Request::_filename_type arg)
  {
    msg_.filename = std::move(arg);
    return std::move(msg_);
  }

private:
  ::gazebo_map_creator_interface::srv::MapRequest_Request msg_;
};

class Init_MapRequest_Request_threshold_2d
{
public:
  explicit Init_MapRequest_Request_threshold_2d(::gazebo_map_creator_interface::srv::MapRequest_Request & msg)
  : msg_(msg)
  {}
  Init_MapRequest_Request_filename threshold_2d(::gazebo_map_creator_interface::srv::MapRequest_Request::_threshold_2d_type arg)
  {
    msg_.threshold_2d = std::move(arg);
    return Init_MapRequest_Request_filename(msg_);
  }

private:
  ::gazebo_map_creator_interface::srv::MapRequest_Request msg_;
};

class Init_MapRequest_Request_range_multiplier
{
public:
  explicit Init_MapRequest_Request_range_multiplier(::gazebo_map_creator_interface::srv::MapRequest_Request & msg)
  : msg_(msg)
  {}
  Init_MapRequest_Request_threshold_2d range_multiplier(::gazebo_map_creator_interface::srv::MapRequest_Request::_range_multiplier_type arg)
  {
    msg_.range_multiplier = std::move(arg);
    return Init_MapRequest_Request_threshold_2d(msg_);
  }

private:
  ::gazebo_map_creator_interface::srv::MapRequest_Request msg_;
};

class Init_MapRequest_Request_resolution
{
public:
  explicit Init_MapRequest_Request_resolution(::gazebo_map_creator_interface::srv::MapRequest_Request & msg)
  : msg_(msg)
  {}
  Init_MapRequest_Request_range_multiplier resolution(::gazebo_map_creator_interface::srv::MapRequest_Request::_resolution_type arg)
  {
    msg_.resolution = std::move(arg);
    return Init_MapRequest_Request_range_multiplier(msg_);
  }

private:
  ::gazebo_map_creator_interface::srv::MapRequest_Request msg_;
};

class Init_MapRequest_Request_skip_vertical_scan
{
public:
  explicit Init_MapRequest_Request_skip_vertical_scan(::gazebo_map_creator_interface::srv::MapRequest_Request & msg)
  : msg_(msg)
  {}
  Init_MapRequest_Request_resolution skip_vertical_scan(::gazebo_map_creator_interface::srv::MapRequest_Request::_skip_vertical_scan_type arg)
  {
    msg_.skip_vertical_scan = std::move(arg);
    return Init_MapRequest_Request_resolution(msg_);
  }

private:
  ::gazebo_map_creator_interface::srv::MapRequest_Request msg_;
};

class Init_MapRequest_Request_upperleft
{
public:
  explicit Init_MapRequest_Request_upperleft(::gazebo_map_creator_interface::srv::MapRequest_Request & msg)
  : msg_(msg)
  {}
  Init_MapRequest_Request_skip_vertical_scan upperleft(::gazebo_map_creator_interface::srv::MapRequest_Request::_upperleft_type arg)
  {
    msg_.upperleft = std::move(arg);
    return Init_MapRequest_Request_skip_vertical_scan(msg_);
  }

private:
  ::gazebo_map_creator_interface::srv::MapRequest_Request msg_;
};

class Init_MapRequest_Request_lowerright
{
public:
  Init_MapRequest_Request_lowerright()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_MapRequest_Request_upperleft lowerright(::gazebo_map_creator_interface::srv::MapRequest_Request::_lowerright_type arg)
  {
    msg_.lowerright = std::move(arg);
    return Init_MapRequest_Request_upperleft(msg_);
  }

private:
  ::gazebo_map_creator_interface::srv::MapRequest_Request msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::gazebo_map_creator_interface::srv::MapRequest_Request>()
{
  return gazebo_map_creator_interface::srv::builder::Init_MapRequest_Request_lowerright();
}

}  // namespace gazebo_map_creator_interface


namespace gazebo_map_creator_interface
{

namespace srv
{

namespace builder
{

class Init_MapRequest_Response_success
{
public:
  Init_MapRequest_Response_success()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::gazebo_map_creator_interface::srv::MapRequest_Response success(::gazebo_map_creator_interface::srv::MapRequest_Response::_success_type arg)
  {
    msg_.success = std::move(arg);
    return std::move(msg_);
  }

private:
  ::gazebo_map_creator_interface::srv::MapRequest_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::gazebo_map_creator_interface::srv::MapRequest_Response>()
{
  return gazebo_map_creator_interface::srv::builder::Init_MapRequest_Response_success();
}

}  // namespace gazebo_map_creator_interface

#endif  // GAZEBO_MAP_CREATOR_INTERFACE__SRV__DETAIL__MAP_REQUEST__BUILDER_HPP_
