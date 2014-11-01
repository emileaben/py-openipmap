py-openipmap
============

Python query interface to openipmap

Code example:

     import openipmap
     oim = openipmap.OpenIPMap()
     oim.query('159.134.155.20')
     ## returns: {'city': u'Dublin,Leinster,IE', 'lat': 53.33306, 'lon': -6.24889}
