import maya.OpenMayaMPx as OpenMayaMPx
import SpaceSwitcherNode

'''
This is where we register and deregister everything in our plugin
'''

def initializePlugin(mobject):
    mplugin = OpenMayaMPx.MFnPlugin(mobject)
    SpaceSwitcherNode.SpaceSwitcherNode.registerNode(mplugin)

def uninitializePlugin(mobject):
    mplugin = OpenMayaMPx.MFnPlugin(mobject)
    SpaceSwitcherNode.SpaceSwitcherNode.deregisterNode(mplugin)
