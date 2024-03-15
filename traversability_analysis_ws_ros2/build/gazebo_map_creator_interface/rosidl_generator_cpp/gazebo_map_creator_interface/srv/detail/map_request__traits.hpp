// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from gazebo_map_creator_interface:srv/MapRequest.idl
// generated code does not contain a copyright notice

#ifndef GAZEBO_MAP_CREATOR_INTERFACE__SRV__DETAIL__MAP_REQUEST__TRAITS_HPP_
#define GAZEBO_MAP_CREATOR_INTERFACE__SRV__DETAIL__MAP_REQUEST__TRAITS_HPP_

#include "gazebo_map_creator_interface/srv/detail/map_request__struct.hpp"
#include <rosidl_runtime_cpp/traits.hpp>
#include <stdint.h>
#include <type_traits>

// Include directives for member types
// Member 'lowerright'
// Member 'upperleft'
#include "geometry_msgs/msg/detail/point__traits.hpp"

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<gazebo_map_creator_interface::srv::MapRequest_Request>()
{
  return "gazebo_map_creator_interface::srv::MapRequest_Request";
}

template<>
inline const char * name<gazebo_map_creator_interface::srv::MapRequest_Request>()
{
  return "gazebo_map_creator_interface/srv/MapRequest_Request";
}

template<>
struct has_fixed_size<gazebo_map_creator_interface::srv::MapRequest_Request>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<gazebo_map_creator_interface::srv::MapRequest_Request>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<gazebo_map_creator_interface::srv::MapRequest_Request>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<gazebo_map_creator_interface::srv::MapRequest_Response>()
{
  return "gazebo_map_creator_interface::srv::MapRequest_Response";
}

template<>
inline const char * name<gazebo_map_creator_interface::srv::MapRequest_Response>()
{
  return "gazebo_map_creator_interface/srv/MapRequest_Response";
}

template<>
struct has_fixed_size<gazebo_map_creator_interface::srv::MapRequest_Response>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<gazebo_map_creator_interface::srv::MapRequest_Response>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<gazebo_map_creator_interface::srv::MapRequest_Response>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<gazebo_map_creator_interface::srv::MapRequest>()
{
  return "gazebo_map_creator_interface::srv::MapRequest";
}

template<>
inline const char * name<gazebo_map_creator_interface::srv::MapRequest>()
{
  return "gazebo_map_creator_interface/srv/MapRequest";
}

template<>
struct has_fixed_size<gazebo_map_creator_interface::srv::MapRequest>
  : std::integral_constant<
    bool,
    has_fixed_size<gazebo_map_creator_interface::srv::MapRequest_Request>::value &&
    has_fixed_size<gazebo_map_creator_interface::srv::MapRequest_Response>::value
  >
{
};

template<>
struct has_bounded_size<gazebo_map_creator_interface::srv::MapRequest>
  : std::integral_constant<
    bool,
    has_bounded_size<gazebo_map_creator_interface::srv::MapRequest_Request>::value &&
    has_bounded_size<gazebo_map_creator_interface::srv::MapRequest_Response>::value
  >
{
};

template<>
struct is_service<gazebo_map_creator_interface::srv::MapRequest>
  : std::true_type
{
};

template<>
struct is_service_request<gazebo_map_creator_interface::srv::MapRequest_Request>
  : std::true_type
{
};

template<>
struct is_service_response<gazebo_map_creator_interface::srv::MapRequest_Response>
  : std::true_type
{
};

}  // namespace rosidl_generator_traits

#endif  // GAZEBO_MAP_CREATOR_INTERFACE__SRV__DETAIL__MAP_REQUEST__TRAITS_HPP_
