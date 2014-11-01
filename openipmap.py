#!/usr/bin/env python
import json
import urllib2
import sys

class OpenIPMap:
   def __init__(self):
      self.query_template = 'https://marmot.ripe.net/openipmap/ipmeta.json?ip=%s'
      self.result = {}
      self.have_result = False
   def query(self, ip):
      rv = {'lat': None, 'lon': None, 'city': None}
      try:
         locinfo = urllib2.urlopen( self.query_template % ( ip ) )
         locjson = json.load( locinfo )
         if len( locjson['crowdsourced'] ) > 0:
            loc = locjson['crowdsourced'][0]
            if 'lat' in loc and 'lon' in loc:
               rv['lat'] = loc['lat']
               rv['lon'] = loc['lon']
            if 'canonical_georesult' in loc:
               rv['city'] = loc['canonical_georesult']
      except:
         sys.stderr.write("problem in loading routergeoloc for ip: %s\n" % ( ip ) )
      return rv 

if __name__ == '__main__':
   oim = OpenIPMap()
   for ip in sys.argv[1:]:
      res = oim.query( ip )
      print "%s\t%s" % (ip, res)
   
