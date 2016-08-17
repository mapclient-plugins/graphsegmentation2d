
'''
MAP Client Plugin
'''

__version__ = '0.1.0'
__author__ = 'Hugh Sorby'
__stepname__ = 'Graph Segmentation 2D'
__location__ = 'https://github.com/mapclient-plugins/graphsegmentation2d/archive/v0.1.0.zip'

# import class that derives itself from the step mountpoint.
from mapclientplugins.graphsegmentation2dstep import step

# Import the resource file when the module is loaded,
# this enables the framework to use the step icon.
from . import resources_rc