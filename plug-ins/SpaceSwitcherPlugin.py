import sys
import maya.OpenMayaMPx as OpenMayaMPx
import SpaceSwitcherNode

def initializePlugin(mobject):
    mplugin = OpenMayaMPx.MFnPlugin(mobject)
    try:
        mplugin.registerNode(SpaceSwitcherNode.SpaceSwitcherNode.kNodeName, SpaceSwitcherNode.SpaceSwitcherNode.kNodeId,
                             SpaceSwitcherNode.SpaceSwitcherNode.nodeCreator,
                             SpaceSwitcherNode.SpaceSwitcherNode.nodeInitializer,
                             OpenMayaMPx.MPxNode.kDependNode,
                             SpaceSwitcherNode.SpaceSwitcherNode.kNodeClassify)
    except:
        sys.stderr.write("Failed to register node: " + SpaceSwitcherNode.SpaceSwitcherNode.kNodeName)
        raise

def uninitializePlugin(mobject):
    mplugin = OpenMayaMPx.MFnPlugin(mobject)
    try:
        mplugin.deregisterNode(SpaceSwitcherNode.SpaceSwitcherNode.kNodeId)
    except:
        sys.stderr.write("Failed to unregister node: " + SpaceSwitcherNode.SpaceSwitcherNode.kNodeName)
        raise