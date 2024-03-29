// generated from rosidl_typesupport_c/resource/idl__type_support.cpp.em
// with input from husky_msgs:msg/HuskyStatus.idl
// generated code does not contain a copyright notice

#include "cstddef"
#include "rosidl_runtime_c/message_type_support_struct.h"
#include "husky_msgs/msg/rosidl_typesupport_c__visibility_control.h"
#include "husky_msgs/msg/detail/husky_status__struct.h"
#include "rosidl_typesupport_c/identifier.h"
#include "rosidl_typesupport_c/message_type_support_dispatch.h"
#include "rosidl_typesupport_c/type_support_map.h"
#include "rosidl_typesupport_c/visibility_control.h"
#include "rosidl_typesupport_interface/macros.h"

namespace husky_msgs
{

namespace msg
{

namespace rosidl_typesupport_c
{

typedef struct _HuskyStatus_type_support_ids_t
{
  const char * typesupport_identifier[2];
} _HuskyStatus_type_support_ids_t;

static const _HuskyStatus_type_support_ids_t _HuskyStatus_message_typesupport_ids = {
  {
    "rosidl_typesupport_fastrtps_c",  // ::rosidl_typesupport_fastrtps_c::typesupport_identifier,
    "rosidl_typesupport_introspection_c",  // ::rosidl_typesupport_introspection_c::typesupport_identifier,
  }
};

typedef struct _HuskyStatus_type_support_symbol_names_t
{
  const char * symbol_name[2];
} _HuskyStatus_type_support_symbol_names_t;

#define STRINGIFY_(s) #s
#define STRINGIFY(s) STRINGIFY_(s)

static const _HuskyStatus_type_support_symbol_names_t _HuskyStatus_message_typesupport_symbol_names = {
  {
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, husky_msgs, msg, HuskyStatus)),
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, husky_msgs, msg, HuskyStatus)),
  }
};

typedef struct _HuskyStatus_type_support_data_t
{
  void * data[2];
} _HuskyStatus_type_support_data_t;

static _HuskyStatus_type_support_data_t _HuskyStatus_message_typesupport_data = {
  {
    0,  // will store the shared library later
    0,  // will store the shared library later
  }
};

static const type_support_map_t _HuskyStatus_message_typesupport_map = {
  2,
  "husky_msgs",
  &_HuskyStatus_message_typesupport_ids.typesupport_identifier[0],
  &_HuskyStatus_message_typesupport_symbol_names.symbol_name[0],
  &_HuskyStatus_message_typesupport_data.data[0],
};

static const rosidl_message_type_support_t HuskyStatus_message_type_support_handle = {
  rosidl_typesupport_c__typesupport_identifier,
  reinterpret_cast<const type_support_map_t *>(&_HuskyStatus_message_typesupport_map),
  rosidl_typesupport_c__get_message_typesupport_handle_function,
};

}  // namespace rosidl_typesupport_c

}  // namespace msg

}  // namespace husky_msgs

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_C_EXPORT_husky_msgs
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_c, husky_msgs, msg, HuskyStatus)() {
  return &::husky_msgs::msg::rosidl_typesupport_c::HuskyStatus_message_type_support_handle;
}

#ifdef __cplusplus
}
#endif
