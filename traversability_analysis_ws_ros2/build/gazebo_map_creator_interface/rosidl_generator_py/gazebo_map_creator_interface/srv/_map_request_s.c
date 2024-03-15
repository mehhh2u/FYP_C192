// generated from rosidl_generator_py/resource/_idl_support.c.em
// with input from gazebo_map_creator_interface:srv/MapRequest.idl
// generated code does not contain a copyright notice
#define NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION
#include <Python.h>
#include <stdbool.h>
#ifndef _WIN32
# pragma GCC diagnostic push
# pragma GCC diagnostic ignored "-Wunused-function"
#endif
#include "numpy/ndarrayobject.h"
#ifndef _WIN32
# pragma GCC diagnostic pop
#endif
#include "rosidl_runtime_c/visibility_control.h"
#include "gazebo_map_creator_interface/srv/detail/map_request__struct.h"
#include "gazebo_map_creator_interface/srv/detail/map_request__functions.h"

#include "rosidl_runtime_c/string.h"
#include "rosidl_runtime_c/string_functions.h"

ROSIDL_GENERATOR_C_IMPORT
bool geometry_msgs__msg__point__convert_from_py(PyObject * _pymsg, void * _ros_message);
ROSIDL_GENERATOR_C_IMPORT
PyObject * geometry_msgs__msg__point__convert_to_py(void * raw_ros_message);
ROSIDL_GENERATOR_C_IMPORT
bool geometry_msgs__msg__point__convert_from_py(PyObject * _pymsg, void * _ros_message);
ROSIDL_GENERATOR_C_IMPORT
PyObject * geometry_msgs__msg__point__convert_to_py(void * raw_ros_message);

ROSIDL_GENERATOR_C_EXPORT
bool gazebo_map_creator_interface__srv__map_request__request__convert_from_py(PyObject * _pymsg, void * _ros_message)
{
  // check that the passed message is of the expected Python class
  {
    char full_classname_dest[65];
    {
      char * class_name = NULL;
      char * module_name = NULL;
      {
        PyObject * class_attr = PyObject_GetAttrString(_pymsg, "__class__");
        if (class_attr) {
          PyObject * name_attr = PyObject_GetAttrString(class_attr, "__name__");
          if (name_attr) {
            class_name = (char *)PyUnicode_1BYTE_DATA(name_attr);
            Py_DECREF(name_attr);
          }
          PyObject * module_attr = PyObject_GetAttrString(class_attr, "__module__");
          if (module_attr) {
            module_name = (char *)PyUnicode_1BYTE_DATA(module_attr);
            Py_DECREF(module_attr);
          }
          Py_DECREF(class_attr);
        }
      }
      if (!class_name || !module_name) {
        return false;
      }
      snprintf(full_classname_dest, sizeof(full_classname_dest), "%s.%s", module_name, class_name);
    }
    assert(strncmp("gazebo_map_creator_interface.srv._map_request.MapRequest_Request", full_classname_dest, 64) == 0);
  }
  gazebo_map_creator_interface__srv__MapRequest_Request * ros_message = _ros_message;
  {  // lowerright
    PyObject * field = PyObject_GetAttrString(_pymsg, "lowerright");
    if (!field) {
      return false;
    }
    if (!geometry_msgs__msg__point__convert_from_py(field, &ros_message->lowerright)) {
      Py_DECREF(field);
      return false;
    }
    Py_DECREF(field);
  }
  {  // upperleft
    PyObject * field = PyObject_GetAttrString(_pymsg, "upperleft");
    if (!field) {
      return false;
    }
    if (!geometry_msgs__msg__point__convert_from_py(field, &ros_message->upperleft)) {
      Py_DECREF(field);
      return false;
    }
    Py_DECREF(field);
  }
  {  // skip_vertical_scan
    PyObject * field = PyObject_GetAttrString(_pymsg, "skip_vertical_scan");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->skip_vertical_scan = (uint8_t)PyLong_AsUnsignedLong(field);
    Py_DECREF(field);
  }
  {  // resolution
    PyObject * field = PyObject_GetAttrString(_pymsg, "resolution");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->resolution = PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // range_multiplier
    PyObject * field = PyObject_GetAttrString(_pymsg, "range_multiplier");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->range_multiplier = PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // threshold_2d
    PyObject * field = PyObject_GetAttrString(_pymsg, "threshold_2d");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->threshold_2d = (int32_t)PyLong_AsLong(field);
    Py_DECREF(field);
  }
  {  // filename
    PyObject * field = PyObject_GetAttrString(_pymsg, "filename");
    if (!field) {
      return false;
    }
    assert(PyUnicode_Check(field));
    PyObject * encoded_field = PyUnicode_AsUTF8String(field);
    if (!encoded_field) {
      Py_DECREF(field);
      return false;
    }
    rosidl_runtime_c__String__assign(&ros_message->filename, PyBytes_AS_STRING(encoded_field));
    Py_DECREF(encoded_field);
    Py_DECREF(field);
  }

  return true;
}

ROSIDL_GENERATOR_C_EXPORT
PyObject * gazebo_map_creator_interface__srv__map_request__request__convert_to_py(void * raw_ros_message)
{
  /* NOTE(esteve): Call constructor of MapRequest_Request */
  PyObject * _pymessage = NULL;
  {
    PyObject * pymessage_module = PyImport_ImportModule("gazebo_map_creator_interface.srv._map_request");
    assert(pymessage_module);
    PyObject * pymessage_class = PyObject_GetAttrString(pymessage_module, "MapRequest_Request");
    assert(pymessage_class);
    Py_DECREF(pymessage_module);
    _pymessage = PyObject_CallObject(pymessage_class, NULL);
    Py_DECREF(pymessage_class);
    if (!_pymessage) {
      return NULL;
    }
  }
  gazebo_map_creator_interface__srv__MapRequest_Request * ros_message = (gazebo_map_creator_interface__srv__MapRequest_Request *)raw_ros_message;
  {  // lowerright
    PyObject * field = NULL;
    field = geometry_msgs__msg__point__convert_to_py(&ros_message->lowerright);
    if (!field) {
      return NULL;
    }
    {
      int rc = PyObject_SetAttrString(_pymessage, "lowerright", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // upperleft
    PyObject * field = NULL;
    field = geometry_msgs__msg__point__convert_to_py(&ros_message->upperleft);
    if (!field) {
      return NULL;
    }
    {
      int rc = PyObject_SetAttrString(_pymessage, "upperleft", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // skip_vertical_scan
    PyObject * field = NULL;
    field = PyLong_FromUnsignedLong(ros_message->skip_vertical_scan);
    {
      int rc = PyObject_SetAttrString(_pymessage, "skip_vertical_scan", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // resolution
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->resolution);
    {
      int rc = PyObject_SetAttrString(_pymessage, "resolution", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // range_multiplier
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->range_multiplier);
    {
      int rc = PyObject_SetAttrString(_pymessage, "range_multiplier", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // threshold_2d
    PyObject * field = NULL;
    field = PyLong_FromLong(ros_message->threshold_2d);
    {
      int rc = PyObject_SetAttrString(_pymessage, "threshold_2d", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // filename
    PyObject * field = NULL;
    field = PyUnicode_DecodeUTF8(
      ros_message->filename.data,
      strlen(ros_message->filename.data),
      "strict");
    if (!field) {
      return NULL;
    }
    {
      int rc = PyObject_SetAttrString(_pymessage, "filename", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }

  // ownership of _pymessage is transferred to the caller
  return _pymessage;
}

#define NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION
// already included above
// #include <Python.h>
// already included above
// #include <stdbool.h>
// already included above
// #include "numpy/ndarrayobject.h"
// already included above
// #include "rosidl_runtime_c/visibility_control.h"
// already included above
// #include "gazebo_map_creator_interface/srv/detail/map_request__struct.h"
// already included above
// #include "gazebo_map_creator_interface/srv/detail/map_request__functions.h"


ROSIDL_GENERATOR_C_EXPORT
bool gazebo_map_creator_interface__srv__map_request__response__convert_from_py(PyObject * _pymsg, void * _ros_message)
{
  // check that the passed message is of the expected Python class
  {
    char full_classname_dest[66];
    {
      char * class_name = NULL;
      char * module_name = NULL;
      {
        PyObject * class_attr = PyObject_GetAttrString(_pymsg, "__class__");
        if (class_attr) {
          PyObject * name_attr = PyObject_GetAttrString(class_attr, "__name__");
          if (name_attr) {
            class_name = (char *)PyUnicode_1BYTE_DATA(name_attr);
            Py_DECREF(name_attr);
          }
          PyObject * module_attr = PyObject_GetAttrString(class_attr, "__module__");
          if (module_attr) {
            module_name = (char *)PyUnicode_1BYTE_DATA(module_attr);
            Py_DECREF(module_attr);
          }
          Py_DECREF(class_attr);
        }
      }
      if (!class_name || !module_name) {
        return false;
      }
      snprintf(full_classname_dest, sizeof(full_classname_dest), "%s.%s", module_name, class_name);
    }
    assert(strncmp("gazebo_map_creator_interface.srv._map_request.MapRequest_Response", full_classname_dest, 65) == 0);
  }
  gazebo_map_creator_interface__srv__MapRequest_Response * ros_message = _ros_message;
  {  // success
    PyObject * field = PyObject_GetAttrString(_pymsg, "success");
    if (!field) {
      return false;
    }
    assert(PyBool_Check(field));
    ros_message->success = (Py_True == field);
    Py_DECREF(field);
  }

  return true;
}

ROSIDL_GENERATOR_C_EXPORT
PyObject * gazebo_map_creator_interface__srv__map_request__response__convert_to_py(void * raw_ros_message)
{
  /* NOTE(esteve): Call constructor of MapRequest_Response */
  PyObject * _pymessage = NULL;
  {
    PyObject * pymessage_module = PyImport_ImportModule("gazebo_map_creator_interface.srv._map_request");
    assert(pymessage_module);
    PyObject * pymessage_class = PyObject_GetAttrString(pymessage_module, "MapRequest_Response");
    assert(pymessage_class);
    Py_DECREF(pymessage_module);
    _pymessage = PyObject_CallObject(pymessage_class, NULL);
    Py_DECREF(pymessage_class);
    if (!_pymessage) {
      return NULL;
    }
  }
  gazebo_map_creator_interface__srv__MapRequest_Response * ros_message = (gazebo_map_creator_interface__srv__MapRequest_Response *)raw_ros_message;
  {  // success
    PyObject * field = NULL;
    field = PyBool_FromLong(ros_message->success ? 1 : 0);
    {
      int rc = PyObject_SetAttrString(_pymessage, "success", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }

  // ownership of _pymessage is transferred to the caller
  return _pymessage;
}
