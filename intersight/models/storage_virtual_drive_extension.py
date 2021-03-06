# coding: utf-8

"""
    Intersight REST API

    This is Intersight REST API 

    OpenAPI spec version: 1.0.9-255
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class StorageVirtualDriveExtension(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'account_moid': 'str',
        'ancestors': 'list[MoBaseMoRef]',
        'create_time': 'datetime',
        'mod_time': 'datetime',
        'moid': 'str',
        'object_type': 'str',
        'owners': 'list[str]',
        'parent': 'MoBaseMoRef',
        'tags': 'list[MoTag]',
        'version_context': 'MoVersionContext',
        'device_mo_id': 'str',
        'dn': 'str',
        'rn': 'str',
        'bootable': 'str',
        'container_id': 'int',
        'drive_state': 'str',
        'name': 'str',
        'oper_device_id': 'str',
        'registered_device': 'AssetDeviceRegistrationRef',
        'storage_controller': 'StorageControllerRef',
        'uuid': 'str',
        'vendor_uuid': 'str',
        'virtual_drive': 'StorageVirtualDriveRef',
        'virtual_drive_dn': 'str',
        'virtual_drive_id': 'str'
    }

    attribute_map = {
        'account_moid': 'AccountMoid',
        'ancestors': 'Ancestors',
        'create_time': 'CreateTime',
        'mod_time': 'ModTime',
        'moid': 'Moid',
        'object_type': 'ObjectType',
        'owners': 'Owners',
        'parent': 'Parent',
        'tags': 'Tags',
        'version_context': 'VersionContext',
        'device_mo_id': 'DeviceMoId',
        'dn': 'Dn',
        'rn': 'Rn',
        'bootable': 'Bootable',
        'container_id': 'ContainerId',
        'drive_state': 'DriveState',
        'name': 'Name',
        'oper_device_id': 'OperDeviceId',
        'registered_device': 'RegisteredDevice',
        'storage_controller': 'StorageController',
        'uuid': 'Uuid',
        'vendor_uuid': 'VendorUuid',
        'virtual_drive': 'VirtualDrive',
        'virtual_drive_dn': 'VirtualDriveDn',
        'virtual_drive_id': 'VirtualDriveId'
    }

    def __init__(self, account_moid=None, ancestors=None, create_time=None, mod_time=None, moid=None, object_type=None, owners=None, parent=None, tags=None, version_context=None, device_mo_id=None, dn=None, rn=None, bootable=None, container_id=None, drive_state=None, name=None, oper_device_id=None, registered_device=None, storage_controller=None, uuid=None, vendor_uuid=None, virtual_drive=None, virtual_drive_dn=None, virtual_drive_id=None):
        """
        StorageVirtualDriveExtension - a model defined in Swagger
        """

        self._account_moid = None
        self._ancestors = None
        self._create_time = None
        self._mod_time = None
        self._moid = None
        self._object_type = None
        self._owners = None
        self._parent = None
        self._tags = None
        self._version_context = None
        self._device_mo_id = None
        self._dn = None
        self._rn = None
        self._bootable = None
        self._container_id = None
        self._drive_state = None
        self._name = None
        self._oper_device_id = None
        self._registered_device = None
        self._storage_controller = None
        self._uuid = None
        self._vendor_uuid = None
        self._virtual_drive = None
        self._virtual_drive_dn = None
        self._virtual_drive_id = None

        if account_moid is not None:
          self.account_moid = account_moid
        if ancestors is not None:
          self.ancestors = ancestors
        if create_time is not None:
          self.create_time = create_time
        if mod_time is not None:
          self.mod_time = mod_time
        if moid is not None:
          self.moid = moid
        if object_type is not None:
          self.object_type = object_type
        if owners is not None:
          self.owners = owners
        if parent is not None:
          self.parent = parent
        if tags is not None:
          self.tags = tags
        if version_context is not None:
          self.version_context = version_context
        if device_mo_id is not None:
          self.device_mo_id = device_mo_id
        if dn is not None:
          self.dn = dn
        if rn is not None:
          self.rn = rn
        if bootable is not None:
          self.bootable = bootable
        if container_id is not None:
          self.container_id = container_id
        if drive_state is not None:
          self.drive_state = drive_state
        if name is not None:
          self.name = name
        if oper_device_id is not None:
          self.oper_device_id = oper_device_id
        if registered_device is not None:
          self.registered_device = registered_device
        if storage_controller is not None:
          self.storage_controller = storage_controller
        if uuid is not None:
          self.uuid = uuid
        if vendor_uuid is not None:
          self.vendor_uuid = vendor_uuid
        if virtual_drive is not None:
          self.virtual_drive = virtual_drive
        if virtual_drive_dn is not None:
          self.virtual_drive_dn = virtual_drive_dn
        if virtual_drive_id is not None:
          self.virtual_drive_id = virtual_drive_id

    @property
    def account_moid(self):
        """
        Gets the account_moid of this StorageVirtualDriveExtension.
        The Account ID for this managed object.  

        :return: The account_moid of this StorageVirtualDriveExtension.
        :rtype: str
        """
        return self._account_moid

    @account_moid.setter
    def account_moid(self, account_moid):
        """
        Sets the account_moid of this StorageVirtualDriveExtension.
        The Account ID for this managed object.  

        :param account_moid: The account_moid of this StorageVirtualDriveExtension.
        :type: str
        """

        self._account_moid = account_moid

    @property
    def ancestors(self):
        """
        Gets the ancestors of this StorageVirtualDriveExtension.
        Ancestors is an array containing the MO references of the ancestors in the object containment hierarchy. 

        :return: The ancestors of this StorageVirtualDriveExtension.
        :rtype: list[MoBaseMoRef]
        """
        return self._ancestors

    @ancestors.setter
    def ancestors(self, ancestors):
        """
        Sets the ancestors of this StorageVirtualDriveExtension.
        Ancestors is an array containing the MO references of the ancestors in the object containment hierarchy. 

        :param ancestors: The ancestors of this StorageVirtualDriveExtension.
        :type: list[MoBaseMoRef]
        """

        self._ancestors = ancestors

    @property
    def create_time(self):
        """
        Gets the create_time of this StorageVirtualDriveExtension.
        The time when this managed object was created.  

        :return: The create_time of this StorageVirtualDriveExtension.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """
        Sets the create_time of this StorageVirtualDriveExtension.
        The time when this managed object was created.  

        :param create_time: The create_time of this StorageVirtualDriveExtension.
        :type: datetime
        """

        self._create_time = create_time

    @property
    def mod_time(self):
        """
        Gets the mod_time of this StorageVirtualDriveExtension.
        The time when this managed object was last modified.  

        :return: The mod_time of this StorageVirtualDriveExtension.
        :rtype: datetime
        """
        return self._mod_time

    @mod_time.setter
    def mod_time(self, mod_time):
        """
        Sets the mod_time of this StorageVirtualDriveExtension.
        The time when this managed object was last modified.  

        :param mod_time: The mod_time of this StorageVirtualDriveExtension.
        :type: datetime
        """

        self._mod_time = mod_time

    @property
    def moid(self):
        """
        Gets the moid of this StorageVirtualDriveExtension.
        A unique identifier of this Managed Object instance.  

        :return: The moid of this StorageVirtualDriveExtension.
        :rtype: str
        """
        return self._moid

    @moid.setter
    def moid(self, moid):
        """
        Sets the moid of this StorageVirtualDriveExtension.
        A unique identifier of this Managed Object instance.  

        :param moid: The moid of this StorageVirtualDriveExtension.
        :type: str
        """

        self._moid = moid

    @property
    def object_type(self):
        """
        Gets the object_type of this StorageVirtualDriveExtension.
        The fully-qualified type of this managed object, e.g. the class name.  

        :return: The object_type of this StorageVirtualDriveExtension.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """
        Sets the object_type of this StorageVirtualDriveExtension.
        The fully-qualified type of this managed object, e.g. the class name.  

        :param object_type: The object_type of this StorageVirtualDriveExtension.
        :type: str
        """

        self._object_type = object_type

    @property
    def owners(self):
        """
        Gets the owners of this StorageVirtualDriveExtension.
        An array of owners which represent effective ownership of this object.   

        :return: The owners of this StorageVirtualDriveExtension.
        :rtype: list[str]
        """
        return self._owners

    @owners.setter
    def owners(self, owners):
        """
        Sets the owners of this StorageVirtualDriveExtension.
        An array of owners which represent effective ownership of this object.   

        :param owners: The owners of this StorageVirtualDriveExtension.
        :type: list[str]
        """

        self._owners = owners

    @property
    def parent(self):
        """
        Gets the parent of this StorageVirtualDriveExtension.
        The direct ancestor of this managed object in the containment hierarchy. 

        :return: The parent of this StorageVirtualDriveExtension.
        :rtype: MoBaseMoRef
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """
        Sets the parent of this StorageVirtualDriveExtension.
        The direct ancestor of this managed object in the containment hierarchy. 

        :param parent: The parent of this StorageVirtualDriveExtension.
        :type: MoBaseMoRef
        """

        self._parent = parent

    @property
    def tags(self):
        """
        Gets the tags of this StorageVirtualDriveExtension.
        An array of tags, which allow to add key, value meta-data to managed objects.  

        :return: The tags of this StorageVirtualDriveExtension.
        :rtype: list[MoTag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this StorageVirtualDriveExtension.
        An array of tags, which allow to add key, value meta-data to managed objects.  

        :param tags: The tags of this StorageVirtualDriveExtension.
        :type: list[MoTag]
        """

        self._tags = tags

    @property
    def version_context(self):
        """
        Gets the version_context of this StorageVirtualDriveExtension.
        The versioning info for this managed object   

        :return: The version_context of this StorageVirtualDriveExtension.
        :rtype: MoVersionContext
        """
        return self._version_context

    @version_context.setter
    def version_context(self, version_context):
        """
        Sets the version_context of this StorageVirtualDriveExtension.
        The versioning info for this managed object   

        :param version_context: The version_context of this StorageVirtualDriveExtension.
        :type: MoVersionContext
        """

        self._version_context = version_context

    @property
    def device_mo_id(self):
        """
        Gets the device_mo_id of this StorageVirtualDriveExtension.

        :return: The device_mo_id of this StorageVirtualDriveExtension.
        :rtype: str
        """
        return self._device_mo_id

    @device_mo_id.setter
    def device_mo_id(self, device_mo_id):
        """
        Sets the device_mo_id of this StorageVirtualDriveExtension.

        :param device_mo_id: The device_mo_id of this StorageVirtualDriveExtension.
        :type: str
        """

        self._device_mo_id = device_mo_id

    @property
    def dn(self):
        """
        Gets the dn of this StorageVirtualDriveExtension.

        :return: The dn of this StorageVirtualDriveExtension.
        :rtype: str
        """
        return self._dn

    @dn.setter
    def dn(self, dn):
        """
        Sets the dn of this StorageVirtualDriveExtension.

        :param dn: The dn of this StorageVirtualDriveExtension.
        :type: str
        """

        self._dn = dn

    @property
    def rn(self):
        """
        Gets the rn of this StorageVirtualDriveExtension.

        :return: The rn of this StorageVirtualDriveExtension.
        :rtype: str
        """
        return self._rn

    @rn.setter
    def rn(self, rn):
        """
        Sets the rn of this StorageVirtualDriveExtension.

        :param rn: The rn of this StorageVirtualDriveExtension.
        :type: str
        """

        self._rn = rn

    @property
    def bootable(self):
        """
        Gets the bootable of this StorageVirtualDriveExtension.

        :return: The bootable of this StorageVirtualDriveExtension.
        :rtype: str
        """
        return self._bootable

    @bootable.setter
    def bootable(self, bootable):
        """
        Sets the bootable of this StorageVirtualDriveExtension.

        :param bootable: The bootable of this StorageVirtualDriveExtension.
        :type: str
        """

        self._bootable = bootable

    @property
    def container_id(self):
        """
        Gets the container_id of this StorageVirtualDriveExtension.

        :return: The container_id of this StorageVirtualDriveExtension.
        :rtype: int
        """
        return self._container_id

    @container_id.setter
    def container_id(self, container_id):
        """
        Sets the container_id of this StorageVirtualDriveExtension.

        :param container_id: The container_id of this StorageVirtualDriveExtension.
        :type: int
        """

        self._container_id = container_id

    @property
    def drive_state(self):
        """
        Gets the drive_state of this StorageVirtualDriveExtension.

        :return: The drive_state of this StorageVirtualDriveExtension.
        :rtype: str
        """
        return self._drive_state

    @drive_state.setter
    def drive_state(self, drive_state):
        """
        Sets the drive_state of this StorageVirtualDriveExtension.

        :param drive_state: The drive_state of this StorageVirtualDriveExtension.
        :type: str
        """

        self._drive_state = drive_state

    @property
    def name(self):
        """
        Gets the name of this StorageVirtualDriveExtension.

        :return: The name of this StorageVirtualDriveExtension.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this StorageVirtualDriveExtension.

        :param name: The name of this StorageVirtualDriveExtension.
        :type: str
        """

        self._name = name

    @property
    def oper_device_id(self):
        """
        Gets the oper_device_id of this StorageVirtualDriveExtension.

        :return: The oper_device_id of this StorageVirtualDriveExtension.
        :rtype: str
        """
        return self._oper_device_id

    @oper_device_id.setter
    def oper_device_id(self, oper_device_id):
        """
        Sets the oper_device_id of this StorageVirtualDriveExtension.

        :param oper_device_id: The oper_device_id of this StorageVirtualDriveExtension.
        :type: str
        """

        self._oper_device_id = oper_device_id

    @property
    def registered_device(self):
        """
        Gets the registered_device of this StorageVirtualDriveExtension.

        :return: The registered_device of this StorageVirtualDriveExtension.
        :rtype: AssetDeviceRegistrationRef
        """
        return self._registered_device

    @registered_device.setter
    def registered_device(self, registered_device):
        """
        Sets the registered_device of this StorageVirtualDriveExtension.

        :param registered_device: The registered_device of this StorageVirtualDriveExtension.
        :type: AssetDeviceRegistrationRef
        """

        self._registered_device = registered_device

    @property
    def storage_controller(self):
        """
        Gets the storage_controller of this StorageVirtualDriveExtension.

        :return: The storage_controller of this StorageVirtualDriveExtension.
        :rtype: StorageControllerRef
        """
        return self._storage_controller

    @storage_controller.setter
    def storage_controller(self, storage_controller):
        """
        Sets the storage_controller of this StorageVirtualDriveExtension.

        :param storage_controller: The storage_controller of this StorageVirtualDriveExtension.
        :type: StorageControllerRef
        """

        self._storage_controller = storage_controller

    @property
    def uuid(self):
        """
        Gets the uuid of this StorageVirtualDriveExtension.

        :return: The uuid of this StorageVirtualDriveExtension.
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """
        Sets the uuid of this StorageVirtualDriveExtension.

        :param uuid: The uuid of this StorageVirtualDriveExtension.
        :type: str
        """

        self._uuid = uuid

    @property
    def vendor_uuid(self):
        """
        Gets the vendor_uuid of this StorageVirtualDriveExtension.

        :return: The vendor_uuid of this StorageVirtualDriveExtension.
        :rtype: str
        """
        return self._vendor_uuid

    @vendor_uuid.setter
    def vendor_uuid(self, vendor_uuid):
        """
        Sets the vendor_uuid of this StorageVirtualDriveExtension.

        :param vendor_uuid: The vendor_uuid of this StorageVirtualDriveExtension.
        :type: str
        """

        self._vendor_uuid = vendor_uuid

    @property
    def virtual_drive(self):
        """
        Gets the virtual_drive of this StorageVirtualDriveExtension.

        :return: The virtual_drive of this StorageVirtualDriveExtension.
        :rtype: StorageVirtualDriveRef
        """
        return self._virtual_drive

    @virtual_drive.setter
    def virtual_drive(self, virtual_drive):
        """
        Sets the virtual_drive of this StorageVirtualDriveExtension.

        :param virtual_drive: The virtual_drive of this StorageVirtualDriveExtension.
        :type: StorageVirtualDriveRef
        """

        self._virtual_drive = virtual_drive

    @property
    def virtual_drive_dn(self):
        """
        Gets the virtual_drive_dn of this StorageVirtualDriveExtension.

        :return: The virtual_drive_dn of this StorageVirtualDriveExtension.
        :rtype: str
        """
        return self._virtual_drive_dn

    @virtual_drive_dn.setter
    def virtual_drive_dn(self, virtual_drive_dn):
        """
        Sets the virtual_drive_dn of this StorageVirtualDriveExtension.

        :param virtual_drive_dn: The virtual_drive_dn of this StorageVirtualDriveExtension.
        :type: str
        """

        self._virtual_drive_dn = virtual_drive_dn

    @property
    def virtual_drive_id(self):
        """
        Gets the virtual_drive_id of this StorageVirtualDriveExtension.

        :return: The virtual_drive_id of this StorageVirtualDriveExtension.
        :rtype: str
        """
        return self._virtual_drive_id

    @virtual_drive_id.setter
    def virtual_drive_id(self, virtual_drive_id):
        """
        Sets the virtual_drive_id of this StorageVirtualDriveExtension.

        :param virtual_drive_id: The virtual_drive_id of this StorageVirtualDriveExtension.
        :type: str
        """

        self._virtual_drive_id = virtual_drive_id

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, StorageVirtualDriveExtension):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
