import maya.OpenMaya as OpenMaya
import maya.OpenMayaMPx as OpenMayaMPx

class SpaceSwitcherNode(OpenMayaMPx.MPxNode):
    kNodeName = 'SpaceSwitcher'
    kNodeClassify = 'utility/general'
    kNodeId = OpenMaya.MTypeId(0x00001337)    # TODO: Register node id or whatever

    # Static variables which will later be replaced by the node's attributes.
    sampleInAttribute = OpenMaya.MObject()
    sampleOutAttribute = OpenMaya.MObject()

    @staticmethod
    def nodeCreator():
        ''' Creates an instance of our node class and delivers it to Maya as a pointer. '''
        return OpenMayaMPx.asMPxPtr(SpaceSwitcherNode())

    @staticmethod
    def nodeInitializer():
        pass

    def __init__(self):
        ''' Constructor. '''
        OpenMayaMPx.MPxNode.__init__(self)

    def compute(self, pPlug, pDataBlock):
        pass