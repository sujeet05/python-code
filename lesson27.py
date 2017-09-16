states ={'UP': 'UttarPradesh',
		 'MP':'madhPradesh',
		 'AP':'AndhraPradesh',
		 'BH':'Bihar',
		 'DL':'Delhi'}
print states['UP']
states['RJ']='Rajasthan'
print "States:"
print '*'*40
print states
statesCapital ={
		 'UttarPradesh':'Lucknow',
		 'madhPradesh':'Bhopal',
		 'AndhraPradesh':'Hyderabad',
		 'Bihar':'Patna',
		 'Delhi':'Delhi',
		 'Rajasthan':'Jaipur'}
print "states Capitals :"
print statesCapital
print "UP represent for " ,states['UP']
print "MP represent for " ,states['MP']
print "AP represent for " ,states['AP']
print "BH represent for " ,states['BH']
print '*'*40
print "Uttarpradesh' Capital ",statesCapital['UttarPradesh']
print "MadhPradesh' Capital ",statesCapital['madhPradesh']
print "AndhraPradesh' Capital ",statesCapital['AndhraPradesh']
print "Bihar' Capital ",statesCapital['Bihar']

print '*'*40
print "Capital of UP is :", statesCapital[states['UP']]
print "Capital of MP is :", statesCapital[states['MP']]
print "Capital of BH is :", statesCapital[states['BH']]
print "Capital of DL is :", statesCapital[states['DL']]

print '*'*40
for state, shortname in states.items():
	print "%s short name is %s" %(shortname,state)
print '*'*40
for stateCapital,capital in statesCapital.items():
	print "%s capital of %s" %(capital,stateCapital)
print '*'*40
for state, capital in states.items():
	print"%s short name is %s and its capital is %s" %(capital,state,statesCapital[capital])
print '*'*40

state = states.get('KA',None)
if not state:
	print "No state called KA exist"
capital1 = statesCapital.get('WestBengal','Deos not exist')
capital2 = statesCapital.get('Bihar','Deos not exist')
if capital1:
	print "Capital of the WestBengal %s" %capital1;
if capital2:
	print "Capital of the Bihar %s" %capital2;
