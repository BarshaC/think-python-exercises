class Kangaroo(): 
    def __init__(self, pouch_contents):
        l= []
        l.append(pouch_contents)
        self.pouch_contents = l
    
    def put_in_pouch(self,objects):
        self.pouch_contents.append(objects)

    def __str__(self):
        return "%s" %(''.join(str(k) for k in self.pouch_contents))

if __name__ == '__main__':
    x = Kangaroo('kanga')
    y = Kangaroo('roo')
    x.put_in_pouch(y)
    print x 
    print y
