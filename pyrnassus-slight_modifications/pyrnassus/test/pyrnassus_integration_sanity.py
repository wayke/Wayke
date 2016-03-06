import pyrnassus
import time

"""
This file makes a sanity check against a running muse-io server
"""

class Visitor(object):

    def __init__(self):
        self.visited={}

    def visit(self,path):
        def doVisit(data):
            if not path in self.visited:
                self.visited[path]=True
                print "Visited: ",path

        return doVisit



muse=pyrnassus.Muse(5002)
visitor=Visitor()
all_paths=pyrnassus.DATA_TYPES.keys()
#this event is created in muselab (I think)
all_paths.remove(pyrnassus.ANNOTATION)
#This might not occur
all_paths.remove(pyrnassus.EEG_DROPPED_SAMPLES)
#This might not occur
all_paths.remove(pyrnassus.ACC_DROPPED_SAMPLES)
#Check with the guys at muse why i'm not getting this
all_paths.remove(pyrnassus.CONFIG)
all_paths.remove(pyrnassus.VERSION)


#add all the possible paths
for path in all_paths:
    muse.register_callback(path,visitor.visit(path))


muse.start()
#check that all the possible paths are visted 
all_visited=False
while not all_visited:
    visited=map(lambda v: v in visitor.visited.keys(), all_paths)
    all_visited=all(visited)
    for v,p in zip(visited,all_paths):
        print v,p
    time.sleep(1)
    print "checking again"
print "out"
muse.stop()
print "All the paths have been visited!"

    



