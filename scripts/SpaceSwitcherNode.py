import sys
import maya.OpenMaya as OpenMaya
import maya.OpenMayaMPx as OpenMayaMPx

class SpaceSwitcherNode(OpenMayaMPx.MPxNode):
    kNodeName = 'SpaceSwitcher'
    kNodeClassify = 'utility/general'
    kNodeId = OpenMaya.MTypeId(0x00001337)    # TODO: Register node id or whatever

    # Static variables which will later be replaced by the node's attributes.
    # inTestInputA = OpenMaya.MObject()
    # inTestInputB = OpenMaya.MObject()
    inSpaceLayer = OpenMaya.MObject()
    inSpaceLayer_spaceRootTarget = OpenMaya.MObject()
    inSpaceLayer_weight = OpenMaya.MObject()
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