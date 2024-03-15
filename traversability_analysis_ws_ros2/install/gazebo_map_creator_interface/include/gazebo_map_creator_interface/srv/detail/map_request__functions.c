// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from gazebo_map_creator_interface:srv/MapRequest.idl
// generated code does not contain a copyright notice
#include "gazebo_map_creator_interface/srv/detail/map_request__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"

// Include directives for member types
// Member `lowerright`
// Member `upperleft`
#include "geometry_msgs/msg/detail/point__functions.h"
// Member `filename`
#include "rosidl_runtime_c/string_functions.h"

bool
gazebo_map_creator_interface__srv__MapRequest_Request__init(gazebo_map_creator_interface__srv__MapRequest_Request * msg)
{
  if (!msg) {
    return false;
  }
  // lowerright
  if (!geometry_msgs__msg__Point__init(&msg->lowerright)) {
    gazebo_map_creator_interface__srv__MapRequest_Request__fini(msg);
    return false;
  }
  // upperleft
  if (!geometry_msgs__msg__Point__init(&msg->upperleft)) {
    gazebo_map_creator_interface__srv__MapRequest_Request__fini(msg);
    return false;
  }
  // skip_vertical_scan
  msg->skip_vertical_scan = 0;
  // resolution
  msg->resolution = 0.01l;
  // range_multiplier
  msg->range_multiplier = 0.55l;
  // threshold_2d
  msg->threshold_2d = 255l;
  // filename
  if (!rosidl_runtime_c__String__init(&msg->filename)) {
    gazebo_map_creator_interface__srv__MapRequest_Request__fini(msg);
    return false;
  }
  {
    bool success = rosidl_runtime_c__String__assign(&msg->filename, "map");
    if (!success) {
      goto abort_init_0;
    }
  }
  return true;
abort_init_0:
  return false;
}

void
gazebo_map_creator_interface__srv__MapRequest_Request__fini(gazebo_map_creator_interface__srv__MapRequest_Request * msg)
{
  if (!msg) {
    return;
  }
  // lowerright
  geometry_msgs__msg__Point__fini(&msg->lowerright);
  // upperleft
  geometry_msgs__msg__Point__fini(&msg->upperleft);
  // skip_vertical_scan
  // resolution
  // range_multiplier
  // threshold_2d
  // filename
  rosidl_runtime_c__String__fini(&msg->filename);
}

bool
gazebo_map_creator_interface__srv__MapRequest_Request__are_equal(const gazebo_map_creator_interface__srv__MapRequest_Request * lhs, const gazebo_map_creator_interface__srv__MapRequest_Request * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // lowerright
  if (!geometry_msgs__msg__Point__are_equal(
      &(lhs->lowerright), &(rhs->lowerright)))
  {
    return false;
  }
  // upperleft
  if (!geometry_msgs__msg__Point__are_equal(
      &(lhs->upperleft), &(rhs->upperleft)))
  {
    return false;
  }
  // skip_vertical_scan
  if (lhs->skip_vertical_scan != rhs->skip_vertical_scan) {
    return false;
  }
  // resolution
  if (lhs->resolution != rhs->resolution) {
    return false;
  }
  // range_multiplier
  if (lhs->range_multiplier != rhs->range_multiplier) {
    return false;
  }
  // threshold_2d
  if (lhs->threshold_2d != rhs->threshold_2d) {
    return false;
  }
  // filename
  if (!rosidl_runtime_c__String__are_equal(
      &(lhs->filename), &(rhs->filename)))
  {
    return false;
  }
  return true;
}

bool
gazebo_map_creator_interface__srv__MapRequest_Request__copy(
  const gazebo_map_creator_interface__srv__MapRequest_Request * input,
  gazebo_map_creator_interface__srv__MapRequest_Request * output)
{
  if (!input || !output) {
    return false;
  }
  // lowerright
  if (!geometry_msgs__msg__Point__copy(
      &(input->lowerright), &(output->lowerright)))
  {
    return false;
  }
  // upperleft
  if (!geometry_msgs__msg__Point__copy(
      &(input->upperleft), &(output->upperleft)))
  {
    return false;
  }
  // skip_vertical_scan
  output->skip_vertical_scan = input->skip_vertical_scan;
  // resolution
  output->resolution = input->resolution;
  // range_multiplier
  output->range_multiplier = input->range_multiplier;
  // threshold_2d
  output->threshold_2d = input->threshold_2d;
  // filename
  if (!rosidl_runtime_c__String__copy(
      &(input->filename), &(output->filename)))
  {
    return false;
  }
  return true;
}

gazebo_map_creator_interface__srv__MapRequest_Request *
gazebo_map_creator_interface__srv__MapRequest_Request__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  gazebo_map_creator_interface__srv__MapRequest_Request * msg = (gazebo_map_creator_interface__srv__MapRequest_Request *)allocator.allocate(sizeof(gazebo_map_creator_interface__srv__MapRequest_Request), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(gazebo_map_creator_interface__srv__MapRequest_Request));
  bool success = gazebo_map_creator_interface__srv__MapRequest_Request__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
gazebo_map_creator_interface__srv__MapRequest_Request__destroy(gazebo_map_creator_interface__srv__MapRequest_Request * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    gazebo_map_creator_interface__srv__MapRequest_Request__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
gazebo_map_creator_interface__srv__MapRequest_Request__Sequence__init(gazebo_map_creator_interface__srv__MapRequest_Request__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  gazebo_map_creator_interface__srv__MapRequest_Request * data = NULL;

  if (size) {
    data = (gazebo_map_creator_interface__srv__MapRequest_Request *)allocator.zero_allocate(size, sizeof(gazebo_map_creator_interface__srv__MapRequest_Request), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = gazebo_map_creator_interface__srv__MapRequest_Request__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        gazebo_map_creator_interface__srv__MapRequest_Request__fini(&data[i - 1]);
      }
      allocator.deallocate(data, allocator.state);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
gazebo_map_creator_interface__srv__MapRequest_Request__Sequence__fini(gazebo_map_creator_interface__srv__MapRequest_Request__Sequence * array)
{
  if (!array) {
    return;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();

  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      gazebo_map_creator_interface__srv__MapRequest_Request__fini(&array->data[i]);
    }
    allocator.deallocate(array->data, allocator.state);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

gazebo_map_creator_interface__srv__MapRequest_Request__Sequence *
gazebo_map_creator_interface__srv__MapRequest_Request__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  gazebo_map_creator_interface__srv__MapRequest_Request__Sequence * array = (gazebo_map_creator_interface__srv__MapRequest_Request__Sequence *)allocator.allocate(sizeof(gazebo_map_creator_interface__srv__MapRequest_Request__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = gazebo_map_creator_interface__srv__MapRequest_Request__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
gazebo_map_creator_interface__srv__MapRequest_Request__Sequence__destroy(gazebo_map_creator_interface__srv__MapRequest_Request__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    gazebo_map_creator_interface__srv__MapRequest_Request__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
gazebo_map_creator_interface__srv__MapRequest_Request__Sequence__are_equal(const gazebo_map_creator_interface__srv__MapRequest_Request__Sequence * lhs, const gazebo_map_creator_interface__srv__MapRequest_Request__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!gazebo_map_creator_interface__srv__MapRequest_Request__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
gazebo_map_creator_interface__srv__MapRequest_Request__Sequence__copy(
  const gazebo_map_creator_interface__srv__MapRequest_Request__Sequence * input,
  gazebo_map_creator_interface__srv__MapRequest_Request__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(gazebo_map_creator_interface__srv__MapRequest_Request);
    gazebo_map_creator_interface__srv__MapRequest_Request * data =
      (gazebo_map_creator_interface__srv__MapRequest_Request *)realloc(output->data, allocation_size);
    if (!data) {
      return false;
    }
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!gazebo_map_creator_interface__srv__MapRequest_Request__init(&data[i])) {
        /* free currently allocated and return false */
        for (; i-- > output->capacity; ) {
          gazebo_map_creator_interface__srv__MapRequest_Request__fini(&data[i]);
        }
        free(data);
        return false;
      }
    }
    output->data = data;
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!gazebo_map_creator_interface__srv__MapRequest_Request__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}


bool
gazebo_map_creator_interface__srv__MapRequest_Response__init(gazebo_map_creator_interface__srv__MapRequest_Response * msg)
{
  if (!msg) {
    return false;
  }
  // success
  return true;
}

void
gazebo_map_creator_interface__srv__MapRequest_Response__fini(gazebo_map_creator_interface__srv__MapRequest_Response * msg)
{
  if (!msg) {
    return;
  }
  // success
}

bool
gazebo_map_creator_interface__srv__MapRequest_Response__are_equal(const gazebo_map_creator_interface__srv__MapRequest_Response * lhs, const gazebo_map_creator_interface__srv__MapRequest_Response * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // success
  if (lhs->success != rhs->success) {
    return false;
  }
  return true;
}

bool
gazebo_map_creator_interface__srv__MapRequest_Response__copy(
  const gazebo_map_creator_interface__srv__MapRequest_Response * input,
  gazebo_map_creator_interface__srv__MapRequest_Response * output)
{
  if (!input || !output) {
    return false;
  }
  // success
  output->success = input->success;
  return true;
}

gazebo_map_creator_interface__srv__MapRequest_Response *
gazebo_map_creator_interface__srv__MapRequest_Response__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  gazebo_map_creator_interface__srv__MapRequest_Response * msg = (gazebo_map_creator_interface__srv__MapRequest_Response *)allocator.allocate(sizeof(gazebo_map_creator_interface__srv__MapRequest_Response), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(gazebo_map_creator_interface__srv__MapRequest_Response));
  bool success = gazebo_map_creator_interface__srv__MapRequest_Response__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
gazebo_map_creator_interface__srv__MapRequest_Response__destroy(gazebo_map_creator_interface__srv__MapRequest_Response * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    gazebo_map_creator_interface__srv__MapRequest_Response__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
gazebo_map_creator_interface__srv__MapRequest_Response__Sequence__init(gazebo_map_creator_interface__srv__MapRequest_Response__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  gazebo_map_creator_interface__srv__MapRequest_Response * data = NULL;

  if (size) {
    data = (gazebo_map_creator_interface__srv__MapRequest_Response *)allocator.zero_allocate(size, sizeof(gazebo_map_creator_interface__srv__MapRequest_Response), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = gazebo_map_creator_interface__srv__MapRequest_Response__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        gazebo_map_creator_interface__srv__MapRequest_Response__fini(&data[i - 1]);
      }
      allocator.deallocate(data, allocator.state);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
gazebo_map_creator_interface__srv__MapRequest_Response__Sequence__fini(gazebo_map_creator_interface__srv__MapRequest_Response__Sequence * array)
{
  if (!array) {
    return;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();

  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      gazebo_map_creator_interface__srv__MapRequest_Response__fini(&array->data[i]);
    }
    allocator.deallocate(array->data, allocator.state);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

gazebo_map_creator_interface__srv__MapRequest_Response__Sequence *
gazebo_map_creator_interface__srv__MapRequest_Response__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  gazebo_map_creator_interface__srv__MapRequest_Response__Sequence * array = (gazebo_map_creator_interface__srv__MapRequest_Response__Sequence *)allocator.allocate(sizeof(gazebo_map_creator_interface__srv__MapRequest_Response__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = gazebo_map_creator_interface__srv__MapRequest_Response__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
gazebo_map_creator_interface__srv__MapRequest_Response__Sequence__destroy(gazebo_map_creator_interface__srv__MapRequest_Response__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    gazebo_map_creator_interface__srv__MapRequest_Response__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
gazebo_map_creator_interface__srv__MapRequest_Response__Sequence__are_equal(const gazebo_map_creator_interface__srv__MapRequest_Response__Sequence * lhs, const gazebo_map_creator_interface__srv__MapRequest_Response__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!gazebo_map_creator_interface__srv__MapRequest_Response__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
gazebo_map_creator_interface__srv__MapRequest_Response__Sequence__copy(
  const gazebo_map_creator_interface__srv__MapRequest_Response__Sequence * input,
  gazebo_map_creator_interface__srv__MapRequest_Response__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(gazebo_map_creator_interface__srv__MapRequest_Response);
    gazebo_map_creator_interface__srv__MapRequest_Response * data =
      (gazebo_map_creator_interface__srv__MapRequest_Response *)realloc(output->data, allocation_size);
    if (!data) {
      return false;
    }
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!gazebo_map_creator_interface__srv__MapRequest_Response__init(&data[i])) {
        /* free currently allocated and return false */
        for (; i-- > output->capacity; ) {
          gazebo_map_creator_interface__srv__MapRequest_Response__fini(&data[i]);
        }
        free(data);
        return false;
      }
    }
    output->data = data;
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!gazebo_map_creator_interface__srv__MapRequest_Response__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
