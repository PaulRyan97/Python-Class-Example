#Sheep.py
#
#This program implements a proper class, with a proper well-defined API.
#
#
#@author Paul Ryan
#@id 114546767

class Sheep:

    def __init__( self, name ):
        self.name = name

    def get_name(self):
        return self.name

    def Call(self, name):
        if self.recognise(name):
            self.bleat()


    def recognise(self, name):
        if self.name == name:
            return True
        return False

    def recoglamb( self, lamb, Flock ):
        if len(Flock) == 2:
            if lamb == Flock[1].name:
                print('"%s" is my child.' % (lamb))
        elif len(Flock) > 2:
            for e in range( len(Flock) - 2, len(Flock)):
                if lamb == Flock[e].name:
                    print('"%s" is my child.' % ( lamb ))
                    break
            else:
                print('I don''t recognise "%s".' % ( lamb ))
            
            
        

    def bleat(self):
        print("Bleat")

    def reproduce( self, lambname, Flock):
        lamb = Sheep(lambname)
        Flock += [lamb]
    
    def identify(self, name):
        print('I am a Sheep. My name is "%s".' % (name))
        
        
    
        
#s = Sheep('Dolly')
