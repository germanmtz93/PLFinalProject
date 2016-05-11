class human(object):
    def f(self):
        data = {
            'name': 'Rita',
            '$name': lambda x: data.update({'name': x}),
            'age': 67,
            '$age': lambda x: data.update({'age': x}),
            'height': '60 inches',
            '$height': lambda x: data.update({'height': x}),
            'weight': '150 lbs',
            '$weight': lambda x: data.update({'weight': x}),
        }
        def cf(self, d):
            if d in data:
                return data[d]
            else:
                return None
        return cf
    run = f(1)

s1 = human()
s1.run('$name')('Mike')
s1.run('$age')('66')
s1.run('$height')('72 inches')
s1.run('$weight')('200 lbs')
print("running python closure file")
print("now running for human closure")
print s1.run('name')
print s1.run('age')
print s1.run('height')
print s1.run('weight')

# print s1.data

class customer(human):
    #def run(self, a): return super(animal, self).run(a)
    def f(self):
        data = {
            'name': 'Customer',
        }
        def cf(self, d):
            if d in data:
                return data[d]
            else:
                return super(customer, self).run(d)
        return cf
    run = f(1)

a1 = customer()
print
print "Now printing for customer closure"
print a1.run('name')
print a1.run('age')
print a1.run('height')
print a1.run('weight')
