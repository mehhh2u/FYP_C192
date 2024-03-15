// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from gazebo_map_creator_interface:srv/MapRequest.idl
// generated code does not contain a copyright notice

#ifndef GAZEBO_MAP_CREATOR_INTERFACE__SRV__DETAIL__MAP_REQUEST__STRUCT_H_
#define GAZEBO_MAP_CREATOR_INTERFACE__SRV__DETAIL__MAP_REQUEST__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

/// Constant 'MAP_2D'.
enum
{
  gazebo_map_creator_interface__srv__MapRequest_Request__MAP_2D = 0
};

/// Constant 'MAP_3D'.
enum
{
  gazebo_map_creator_interface__srv__MapRequest_Request__MAP_3D = 1
};

// Include directives for member types
// Member 'lowerright'
// Member 'upperleft'
#include "geometry_msgs/msg/detail/point__struct.h"
// Member 'filename'
#include "rosidl_runtime_c/string.h"

// Struct defined in srv/MapRequest in the package gazebo_map_creator_interface.
typedef struct gazebo_map_creator_interface__srv__MapRequest_Request
{
  geometry_msgs__msg__Point lowerright;
  geometry_msgs__msg__Point upperleft;
  uint8_t skip_vertical_scan;
  double resolution;
  double range_multiplier;
  int32_t threshold_2d;
  rosidl_runtime_c__String filename;
} gazebo_map_creator_interface__srv__MapRequest_Request;

// Struct for a sequence of gazebo_map_creator_interface__srv__MapRequest_Request.
typedef struct gazebo_map_creator_interface__srv__MapRequest_Request__Sequence
{
  gazebo_map_creator_interface__srv__MapRequest_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} gazebo_map_creator_interface__srv__MapRequest_Request__Sequence;


// Constants defined in the message

// Struct defined in srv/MapRequest in the package gazebo_map_creator_interface.
typedef struct gazebo_map_creator_interface__srv__MapRequest_Response
{
  bool success;
} gazebo_map_creator_interface__srv__MapRequest_Response;

// Struct for a sequence of gazebo_map_creator_interface__srv__MapRequest_Response.
typedef struct gazebo_map_creator_interface__srv__MapRequest_Response__Sequence
{
  gazebo_map_creator_interface__srv__MapRequest_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} gazebo_map_creator_interface__srv__MapRequest_Response__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // GAZEBO_MAP_CREATOR_INTERFACE__SRV__DETAIL__MAP_REQUEST__STRUCT_H_
