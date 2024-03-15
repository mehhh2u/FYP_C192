# generated from rosidl_generator_py/resource/_idl.py.em
# with input from gazebo_map_creator_interface:srv/MapRequest.idl
# generated code does not contain a copyright notice


# Import statements for member types

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_MapRequest_Request(type):
    """Metaclass of message 'MapRequest_Request'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
        'MAP_2D': 0,
        'MAP_3D': 1,
    }

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('gazebo_map_creator_interface')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'gazebo_map_creator_interface.srv.MapRequest_Request')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__map_request__request
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__map_request__request
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__map_request__request
            cls._TYPE_SUPPORT = module.type_support_msg__srv__map_request__request
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__map_request__request

            from geometry_msgs.msg import Point
            if Point.__class__._TYPE_SUPPORT is None:
                Point.__class__.__import_type_support__()

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
            'MAP_2D': cls.__constants['MAP_2D'],
            'MAP_3D': cls.__constants['MAP_3D'],
            'SKIP_VERTICAL_SCAN__DEFAULT': 0,
            'RESOLUTION__DEFAULT': 0.01,
            'RANGE_MULTIPLIER__DEFAULT': 0.55,
            'THRESHOLD_2D__DEFAULT': 255,
            'FILENAME__DEFAULT': 'map',
        }

    @property
    def MAP_2D(self):
        """Message constant 'MAP_2D'."""
        return Metaclass_MapRequest_Request.__constants['MAP_2D']

    @property
    def MAP_3D(self):
        """Message constant 'MAP_3D'."""
        return Metaclass_MapRequest_Request.__constants['MAP_3D']

    @property
    def SKIP_VERTICAL_SCAN__DEFAULT(cls):
        """Return default value for message field 'skip_vertical_scan'."""
        return 0

    @property
    def RESOLUTION__DEFAULT(cls):
        """Return default value for message field 'resolution'."""
        return 0.01

    @property
    def RANGE_MULTIPLIER__DEFAULT(cls):
        """Return default value for message field 'range_multiplier'."""
        return 0.55

    @property
    def THRESHOLD_2D__DEFAULT(cls):
        """Return default value for message field 'threshold_2d'."""
        return 255

    @property
    def FILENAME__DEFAULT(cls):
        """Return default value for message field 'filename'."""
        return 'map'


class MapRequest_Request(metaclass=Metaclass_MapRequest_Request):
    """
    Message class 'MapRequest_Request'.

    Constants:
      MAP_2D
      MAP_3D
    """

    __slots__ = [
        '_lowerright',
        '_upperleft',
        '_skip_vertical_scan',
        '_resolution',
        '_range_multiplier',
        '_threshold_2d',
        '_filename',
    ]

    _fields_and_field_types = {
        'lowerright': 'geometry_msgs/Point',
        'upperleft': 'geometry_msgs/Point',
        'skip_vertical_scan': 'uint8',
        'resolution': 'double',
        'range_multiplier': 'double',
        'threshold_2d': 'int32',
        'filename': 'string',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.NamespacedType(['geometry_msgs', 'msg'], 'Point'),  # noqa: E501
        rosidl_parser.definition.NamespacedType(['geometry_msgs', 'msg'], 'Point'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint8'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('int32'),  # noqa: E501
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        from geometry_msgs.msg import Point
        self.lowerright = kwargs.get('lowerright', Point())
        from geometry_msgs.msg import Point
        self.upperleft = kwargs.get('upperleft', Point())
        self.skip_vertical_scan = kwargs.get(
            'skip_vertical_scan', MapRequest_Request.SKIP_VERTICAL_SCAN__DEFAULT)
        self.resolution = kwargs.get(
            'resolution', MapRequest_Request.RESOLUTION__DEFAULT)
        self.range_multiplier = kwargs.get(
            'range_multiplier', MapRequest_Request.RANGE_MULTIPLIER__DEFAULT)
        self.threshold_2d = kwargs.get(
            'threshold_2d', MapRequest_Request.THRESHOLD_2D__DEFAULT)
        self.filename = kwargs.get(
            'filename', MapRequest_Request.FILENAME__DEFAULT)

    def __repr__(self):
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args = []
        for s, t in zip(self.__slots__, self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s[1:] + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self.lowerright != other.lowerright:
            return False
        if self.upperleft != other.upperleft:
            return False
        if self.skip_vertical_scan != other.skip_vertical_scan:
            return False
        if self.resolution != other.resolution:
            return False
        if self.range_multiplier != other.range_multiplier:
            return False
        if self.threshold_2d != other.threshold_2d:
            return False
        if self.filename != other.filename:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @property
    def lowerright(self):
        """Message field 'lowerright'."""
        return self._lowerright

    @lowerright.setter
    def lowerright(self, value):
        if __debug__:
            from geometry_msgs.msg import Point
            assert \
                isinstance(value, Point), \
                "The 'lowerright' field must be a sub message of type 'Point'"
        self._lowerright = value

    @property
    def upperleft(self):
        """Message field 'upperleft'."""
        return self._upperleft

    @upperleft.setter
    def upperleft(self, value):
        if __debug__:
            from geometry_msgs.msg import Point
            assert \
                isinstance(value, Point), \
                "The 'upperleft' field must be a sub message of type 'Point'"
        self._upperleft = value

    @property
    def skip_vertical_scan(self):
        """Message field 'skip_vertical_scan'."""
        return self._skip_vertical_scan

    @skip_vertical_scan.setter
    def skip_vertical_scan(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'skip_vertical_scan' field must be of type 'int'"
            assert value >= 0 and value < 256, \
                "The 'skip_vertical_scan' field must be an unsigned integer in [0, 255]"
        self._skip_vertical_scan = value

    @property
    def resolution(self):
        """Message field 'resolution'."""
        return self._resolution

    @resolution.setter
    def resolution(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'resolution' field must be of type 'float'"
        self._resolution = value

    @property
    def range_multiplier(self):
        """Message field 'range_multiplier'."""
        return self._range_multiplier

    @range_multiplier.setter
    def range_multiplier(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'range_multiplier' field must be of type 'float'"
        self._range_multiplier = value

    @property
    def threshold_2d(self):
        """Message field 'threshold_2d'."""
        return self._threshold_2d

    @threshold_2d.setter
    def threshold_2d(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'threshold_2d' field must be of type 'int'"
            assert value >= -2147483648 and value < 2147483648, \
                "The 'threshold_2d' field must be an integer in [-2147483648, 2147483647]"
        self._threshold_2d = value

    @property
    def filename(self):
        """Message field 'filename'."""
        return self._filename

    @filename.setter
    def filename(self, value):
        if __debug__:
            assert \
                isinstance(value, str), \
                "The 'filename' field must be of type 'str'"
        self._filename = value


# Import statements for member types

# already imported above
# import rosidl_parser.definition


class Metaclass_MapRequest_Response(type):
    """Metaclass of message 'MapRequest_Response'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
    }

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('gazebo_map_creator_interface')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'gazebo_map_creator_interface.srv.MapRequest_Response')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__map_request__response
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__map_request__response
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__map_request__response
            cls._TYPE_SUPPORT = module.type_support_msg__srv__map_request__response
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__map_request__response

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class MapRequest_Response(metaclass=Metaclass_MapRequest_Response):
    """Message class 'MapRequest_Response'."""

    __slots__ = [
        '_success',
    ]

    _fields_and_field_types = {
        'success': 'boolean',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.success = kwargs.get('success', bool())

    def __repr__(self):
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args = []
        for s, t in zip(self.__slots__, self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s[1:] + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self.success != other.success:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @property
    def success(self):
        """Message field 'success'."""
        return self._success

    @success.setter
    def success(self, value):
        if __debug__:
            assert \
                isinstance(value, bool), \
                "The 'success' field must be of type 'bool'"
        self._success = value


class Metaclass_MapRequest(type):
    """Metaclass of service 'MapRequest'."""

    _TYPE_SUPPORT = None

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('gazebo_map_creator_interface')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'gazebo_map_creator_interface.srv.MapRequest')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._TYPE_SUPPORT = module.type_support_srv__srv__map_request

            from gazebo_map_creator_interface.srv import _map_request
            if _map_request.Metaclass_MapRequest_Request._TYPE_SUPPORT is None:
                _map_request.Metaclass_MapRequest_Request.__import_type_support__()
            if _map_request.Metaclass_MapRequest_Response._TYPE_SUPPORT is None:
                _map_request.Metaclass_MapRequest_Response.__import_type_support__()


class MapRequest(metaclass=Metaclass_MapRequest):
    from gazebo_map_creator_interface.srv._map_request import MapRequest_Request as Request
    from gazebo_map_creator_interface.srv._map_request import MapRequest_Response as Response

    def __init__(self):
        raise NotImplementedError('Service classes can not be instantiated')
