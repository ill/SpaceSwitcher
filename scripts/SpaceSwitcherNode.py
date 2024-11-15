import sys
import maya.OpenMaya as OpenMaya
import maya.OpenMayaMPx as OpenMayaMPx

class SpaceSwitcherNode(OpenMayaMPx.MPxNode):
    kNodeName = "SpaceSwitcher"
    kNodeClassify = ""#"utility/general"
    kNodeId = OpenMaya.MTypeId(0x00001337)    # TODO: Register node id or whatever

    """
    The offset in case the target object wasn't zeroed out at the time this was created, so we can feed it a transform relative to this
    """
    inOffsetMatrix = OpenMaya.MObject()

    """
    Array of layers
    """
    inSpaceLayer = OpenMaya.MObject()

    """
    The space root target object, in whose space we're in
    """
    inSpaceLayer_spaceRootTarget = OpenMaya.MObject()
    """
    The weight of the layer
    """
    inSpaceLayer_weight = OpenMaya.MObject()

    """
    The transform matrix of the target object in local space. This should get fed into the Offset Parent Matrix or decomposed into the TRS
    """
    outTransformMatrix = OpenMaya.MObject()

    @staticmethod
    def nodeCreator():
        ''' Creates an instance of our node class and delivers it to Maya as a pointer. '''
        return OpenMayaMPx.asMPxPtr(SpaceSwitcherNode())

    @staticmethod
    def nodeInitializer():
        numericAttributeFn = OpenMaya.MFnNumericAttribute()
        compoundAttributeFn = OpenMaya.MFnCompoundAttribute()
        messageAttributeFn = OpenMaya.MFnMessageAttribute()
        matrixAttributeFn = OpenMaya.MFnMatrixAttribute()

        # ==================================
        # INPUT NODE ATTRIBUTE(S)
        # ==================================

        # Layer Space Root Target
        SpaceSwitcherNode.inSpaceLayer_spaceRootTarget = messageAttributeFn.create("Space Root Target", "Space Root Target")
        messageAttributeFn.setReadable(False)
        messageAttributeFn.setChannelBox(True)
        SpaceSwitcherNode.addAttribute(SpaceSwitcherNode.inSpaceLayer_spaceRootTarget)

        # Layer Weight
        SpaceSwitcherNode.inSpaceLayer_weight = numericAttributeFn.create("Weight", "Weight", OpenMaya.MFnNumericData.kFloat)
        numericAttributeFn.setReadable(False)
        numericAttributeFn.setKeyable(True)
        messageAttributeFn.setChannelBox(True)
        SpaceSwitcherNode.addAttribute(SpaceSwitcherNode.inSpaceLayer_weight)

        # Main Layer Parent Attribute
        SpaceSwitcherNode.inSpaceLayer = compoundAttributeFn.create("Layer", "Layer")
        compoundAttributeFn.setArray(True)
        compoundAttributeFn.setReadable(False)
        compoundAttributeFn.setChannelBox(True)
        compoundAttributeFn.addChild(SpaceSwitcherNode.inSpaceLayer_spaceRootTarget)
        compoundAttributeFn.addChild(SpaceSwitcherNode.inSpaceLayer_weight)
        SpaceSwitcherNode.addAttribute(SpaceSwitcherNode.inSpaceLayer)

        # ==================================
        # OUTPUT NODE ATTRIBUTE(S)
        # ==================================

        # Transform Matrix
        SpaceSwitcherNode.outTransformMatrix = matrixAttributeFn.create("Transform Matrix", "Transform Matrix")
        matrixAttributeFn.setStorable(False)
        matrixAttributeFn.setWritable(False)
        SpaceSwitcherNode.addAttribute(SpaceSwitcherNode.outTransformMatrix)

        # ==================================
        # NODE ATTRIBUTE DEPENDENCIES
        # ==================================

        # SpaceSwitcherNode.attributeAffects(SpaceSwitcherNode.inTestInputB, SpaceSwitcherNode.outTransformMatrix)
        SpaceSwitcherNode.attributeAffects(SpaceSwitcherNode.inSpaceLayer, SpaceSwitcherNode.outTransformMatrix)
        SpaceSwitcherNode.attributeAffects(SpaceSwitcherNode.inSpaceLayer_spaceRootTarget, SpaceSwitcherNode.outTransformMatrix)
        SpaceSwitcherNode.attributeAffects(SpaceSwitcherNode.inSpaceLayer_weight, SpaceSwitcherNode.outTransformMatrix)

    @staticmethod
    def registerNode(mplugin):
        try:
            mplugin.registerNode(SpaceSwitcherNode.kNodeName, SpaceSwitcherNode.kNodeId,
                                 SpaceSwitcherNode.nodeCreator,
                                 SpaceSwitcherNode.nodeInitializer,
                                 OpenMayaMPx.MPxNode.kDependNode,
                                 SpaceSwitcherNode.kNodeClassify)
        except:
            sys.stderr.write("Failed to register node: " + SpaceSwitcherNode.kNodeName)
            raise

    @staticmethod
    def deregisterNode(mplugin):
        try:
            mplugin.deregisterNode(SpaceSwitcherNode.kNodeId)
        except:
            sys.stderr.write("Failed to unregister node: " + SpaceSwitcherNode.kNodeName)
            raise


    def __init__(self):
        ''' Constructor. '''
        OpenMayaMPx.MPxNode.__init__(self)

    def compute(self, pPlug, pDataBlock):
        if (pPlug == SpaceSwitcherNode.outTransformMatrix):
            outTransformMatrixDataHandle = pDataBlock.outputValue(SpaceSwitcherNode.outTransformMatrix)

            outTransformMatrixDataHandle.setClean()
        else:
            return OpenMaya.kUnknownParameter