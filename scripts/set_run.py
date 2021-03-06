from collections import OrderedDict

# -------------------------------------------------------------------------------
# 
# Set which language and which graph object to generate meta for.
#
# -------------------------------------------------------------------------------

def languages():
    '''@languages@ -- Set list of languages'''
    _languages = [
        'python',
        'matlab',
        'r',
        'nodejs',
        'julia'
    ]
    return _languages

def graph_objs_info():
    ''' @graph_objs_info@
    Set list of all graph objects (needed to call methods in MakeMeta()), 
    divided up in category groups. Why:
    - for presentation purposes in plot.ly/<lang>/reference/
      (e.g. a table of content, and description)
    - split between 'trace' and other dictionary-like graph objects
      in the Python API.
    '''
    _graph_objs_info = OrderedDict([
        ('trace', dict(  # !important (python-api)
            group='Trace objects',
            description='Bind your data to traces with these',
            graph_objs=[
                'scatter',
                'bar',
                'histogram',
                'box', 
                'heatmap',
                'contour',
                'histogram2d',
                'histogram2dcontour',
                'area',
                'scatter3d',
                'surface'
            ]
        )),
        ('trace-aux', dict(
            group='Trace auxiliary objects',
            description='Add some spice to your traces with these',
            graph_objs=[
                'error_y',
                'error_x',
                'xbins',
                'ybins',
                'marker',
                'line',
                'contours',
                'colorbar',
                'stream',
                'error_z'
            ]
        )),
        ('axis', dict(
            group='Axis objects',
            description="Set the your axes' specifications and style with these",
            graph_objs=[
                'xaxis',
                'yaxis',
                'radialaxis',
                'angularaxis',
                'scene',
                'zaxis'
            ]
        )),
        ('layout', dict(
            group='Layout and layout style objects',
            description="Customize your figure's layout with these",
            graph_objs=[
                'layout',
                'font',
                'legend',
                'annotation',
                'margin'
            ]
        )),
        ('figure', dict(
            group='Figure object',
            description='Package layout and data with this object',
            graph_objs=[
                'figure'
            ]
        )),
        ('list-like', dict(
            group='List-like objects',
            description=False,  # => will not appear on plot.ly
            graph_objs=[
                'data',
                'annotations'
            ],
        ))
    ])
    return _graph_objs_info

def graph_objs():
    '''@graph_objs@ -- retrieve list of graph objects from graph_objs_info'''
    _graph_objs_info = graph_objs_info()
    _graph_objs = [graph_obj 
                  for info in _graph_objs_info.values()
                  for graph_obj in info['graph_objs']]
    return _graph_objs

# -------------------------------------------------------------------------------

