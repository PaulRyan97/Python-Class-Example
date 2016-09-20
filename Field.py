#Field.py
#
#Uses the Sheep class implemented in Sheep.py to test its methods.
#
#
#@author Paul Ryan
#@id 114546767


from sheep import Sheep
class Field:

    def Main(self):
        Flock = []
        Dolly = Sheep('Dolly')
        Flock += [Dolly]

        Dolly.Call('Dolly')
        
        Dolly.reproduce('Bembo', Flock)
        Dolly.reproduce('Daisy', Flock)
        Dolly.reproduce('Patsy', Flock)

        if len(Flock) > 1:
            for n in range(1, len(Flock)):
                Dolly.recoglamb(Flock[n].name, Flock)


        for e in Flock:
            Dolly.identify(e.name)
        
        

self = Field()
    
    
