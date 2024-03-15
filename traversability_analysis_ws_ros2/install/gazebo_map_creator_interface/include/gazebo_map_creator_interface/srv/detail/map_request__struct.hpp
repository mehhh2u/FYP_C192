// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from gazebo_map_creator_interface:srv/MapRequest.idl
// generated code does not contain a copyright notice

#ifndef GAZEBO_MAP_CREATOR_INTERFACE__SRV__DETAIL__MAP_REQUEST__STRUCT_HPP_
#define GAZEBO_MAP_CREATOR_INTERFACE__SRV__DETAIL__MAP_REQUEST__STRUCT_HPP_

#include <rosidl_runtime_cpp/bounded_vector.hpp>
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>


// Include directives for member types
// Member 'lowerright'
// Member 'upperleft'
#include "geometry_msgs/msg/detail/point__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__gazebo_map_creator_interface__srv__MapRequest_Request __attribute__((deprecated))
#else
# define DEPRECATED__gazebo_map_creator_interface__srv__MapRequest_Request __declspec(deprecated)
#endif

namespace gazebo_map_creator_interface
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct MapRequest_Request_
{
  using Type = MapRequest_Request_<ContainerAllocator>;

  explicit MapRequest_Request_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : lowerright(_init),
    upperleft(_init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::DEFAULTS_ONLY == _init)
    {
      this->skip_vertical_scan = 0;
      this->resolution = 0.01;
      this->range_multiplier = 0.55;
      this->threshold_2d = 255l;
      this->filename = "map";
    } else if (rosidl_runtime_cpp::MessageInitialization::ZERO == _init) {
      this->skip_vertical_scan = 0;
      this->resolution = 0.0;
      this->range_multiplier = 0.0;
      this->threshold_2d = 0l;
      this->filename = "";
    }
  }

  explicit MapRequest_Request_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : lowerright(_alloc, _init),
    upperleft(_alloc, _init),
    filename(_alloc)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::DEFAULTS_ONLY == _init)
    {
      this->skip_vertical_scan = 0;
      this->resolution = 0.01;
      this->range_multiplier = 0.55;
      this->threshold_2d = 255l;
      this->filename = "map";
    } else if (rosidl_runtime_cpp::MessageInitialization::ZERO == _init) {
      this->skip_vertical_scan = 0;
      this->resolution = 0.0;
      this->range_multiplier = 0.0;
      this->threshold_2d = 0l;
      this->filename = "";
    }
  }

  // field types and members
  using _lowerright_type =
    geometry_msgs::msg::Point_<ContainerAllocator>;
  _lowerright_type lowerright;
  using _upperleft_type =
    geometry_msgs::msg::Point_<ContainerAllocator>;
  _upperleft_type upperleft;
  using _skip_vertical_scan_type =
    uint8_t;
  _skip_vertical_scan_type skip_vertical_scan;
  using _resolution_type =
    double;
  _resolution_type resolution;
  using _range_multiplier_type =
    double;
  _range_multiplier_type range_multiplier;
  using _threshold_2d_type =
    int32_t;
  _threshold_2d_type threshold_2d;
  using _filename_type =
    std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other>;
  _filename_type filename;

  // setters for named parameter idiom
  Type & set__lowerright(
    const geometry_msgs::msg::Point_<ContainerAllocator> & _arg)
  {
    this->lowerright = _arg;
    return *this;
  }
  Type & set__upperleft(
    const geometry_msgs::msg::Point_<ContainerAllocator> & _arg)
  {
    this->upperleft = _arg;
    return *this;
  }
  Type & set__skip_vertical_scan(
    const uint8_t & _arg)
  {
    this->skip_vertical_scan = _arg;
    return *this;
  }
  Type & set__resolution(
    const double & _arg)
  {
    this->resolution = _arg;
    return *this;
  }
  Type & set__range_multiplier(
    const double & _arg)
  {
    this->range_multiplier = _arg;
    return *this;
  }
  Type & set__threshold_2d(
    const int32_t & _arg)
  {
    this->threshold_2d = _arg;
    return *this;
  }
  Type & set__filename(
    const std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other> & _arg)
  {
    this->filename = _arg;
    return *this;
  }

  // constant declarations
  static constexpr uint8_t MAP_2D =
    0u;
  static constexpr uint8_t MAP_3D =
    1u;

  // pointer types
  using RawPtr =
    gazebo_map_creator_interface::srv::MapRequest_Request_<ContainerAllocator> *;
  using ConstRawPtr =
    const gazebo_map_creator_interface::srv::MapRequest_Request_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<gazebo_map_creator_interface::srv::MapRequest_Request_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<gazebo_map_creator_interface::srv::MapRequest_Request_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      gazebo_map_creator_interface::srv::MapRequest_Request_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<gazebo_map_creator_interface::srv::MapRequest_Request_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      gazebo_map_creator_interface::srv::MapRequest_Request_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<gazebo_map_creator_interface::srv::MapRequest_Request_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<gazebo_map_creator_interface::srv::MapRequest_Request_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<gazebo_map_creator_interface::srv::MapRequest_Request_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__gazebo_map_creator_interface__srv__MapRequest_Request
    std::shared_ptr<gazebo_map_creator_interface::srv::MapRequest_Request_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__gazebo_map_creator_interface__srv__MapRequest_Request
    std::shared_ptr<gazebo_map_creator_interface::srv::MapRequest_Request_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const MapRequest_Request_ & other) const
  {
    if (this->lowerright != other.lowerright) {
      return false;
    }
    if (this->upperleft != other.upperleft) {
      return false;
    }
    if (this->skip_vertical_scan != other.skip_vertical_scan) {
      return false;
    }
    if (this->resolution != other.resolution) {
      return false;
    }
    if (this->range_multiplier != other.range_multiplier) {
      return false;
    }
    if (this->threshold_2d != other.threshold_2d) {
      return false;
    }
    if (this->filename != other.filename) {
      return false;
    }
    return true;
  }
  bool operator!=(const MapRequest_Request_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct MapRequest_Request_

// alias to use template instance with default allocator
using MapRequest_Request =
  gazebo_map_creator_interface::srv::MapRequest_Request_<std::allocator<void>>;

// constant definitions
template<typename ContainerAllocator>
constexpr uint8_t MapRequest_Request_<ContainerAllocator>::MAP_2D;
template<typename ContainerAllocator>
constexpr uint8_t MapRequest_Request_<ContainerAllocator>::MAP_3D;

}  // namespace srv

}  // namespace gazebo_map_creator_interface


#ifndef _WIN32
# define DEPRECATED__gazebo_map_creator_interface__srv__MapRequest_Response __attribute__((deprecated))
#else
# define DEPRECATED__gazebo_map_creator_interface__srv__MapRequest_Response __declspec(deprecated)
#endif

namespace gazebo_map_creator_interface
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct MapRequest_Response_
{
  using Type = MapRequest_Response_<ContainerAllocator>;

  explicit MapRequest_Response_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->success = false;
    }
  }

  explicit MapRequest_Response_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->success = false;
    }
  }

  // field types and members
  using _success_type =
    bool;
  _success_type success;

  // setters for named parameter idiom
  Type & set__success(
    const bool & _arg)
  {
    this->success = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    gazebo_map_creator_interface::srv::MapRequest_Response_<ContainerAllocator> *;
  using ConstRawPtr =
    const gazebo_map_creator_interface::srv::MapRequest_Response_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<gazebo_map_creator_interface::srv::MapRequest_Response_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<gazebo_map_creator_interface::srv::MapRequest_Response_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      gazebo_map_creator_interface::srv::MapRequest_Response_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<gazebo_map_creator_interface::srv::MapRequest_Response_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      gazebo_map_creator_interface::srv::MapRequest_Response_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<gazebo_map_creator_interface::srv::MapRequest_Response_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<gazebo_map_creator_interface::srv::MapRequest_Response_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<gazebo_map_creator_interface::srv::MapRequest_Response_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__gazebo_map_creator_interface__srv__MapRequest_Response
    std::shared_ptr<gazebo_map_creator_interface::srv::MapRequest_Response_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__gazebo_map_creator_interface__srv__MapRequest_Response
    std::shared_ptr<gazebo_map_creator_interface::srv::MapRequest_Response_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const MapRequest_Response_ & other) const
  {
    if (this->success != other.success) {
      return false;
    }
    return true;
  }
  bool operator!=(const MapRequest_Response_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct MapRequest_Response_

// alias to use template instance with default allocator
using MapRequest_Response =
  gazebo_map_creator_interface::srv::MapRequest_Response_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace gazebo_map_creator_interface

namespace gazebo_map_creator_interface
{

namespace srv
{

struct MapRequest
{
  using Request = gazebo_map_creator_interface::srv::MapRequest_Request;
  using Response = gazebo_map_creator_interface::srv::MapRequest_Response;
};

}  // namespace srv

}  // namespace gazebo_map_creator_interface

#endif  // GAZEBO_MAP_CREATOR_INTERFACE__SRV__DETAIL__MAP_REQUEST__STRUCT_HPP_
