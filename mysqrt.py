
"""
Assuming this is file mymodule.py, then this string, being the
first statement in the file, will become the "mymodule" module's
docstring when the file is imported.
"""

def sqrt2(x, debug=False):
	""" this is a test of docstring """
	
	from numpy import nan

	if x==0:
		return 0
	elif x<0:
		print "*** cannot have negative values"
		return nan

	assert x>0 and type(x) is not str, "should not get here"

	s = 1.
	kmax = 100
	tol = 1.e-14
	for k in range(kmax):
		if debug:
			print "Before iteration %s, s = %20.15f" % (k,s)
		s0 = s
		s = 0.5 * (s + x/s)
		delta_s = s - s0
		if abs(delta_s / x ) < tol:
			break
	if debug:
		print "After %s iterations, s = %20.15f" % (k+1,s)
	return s

def test():
	""" UNIT TEST FOR SQRT2 """
	from numpy import sqrt
	xvalues = [0., 2, 100, 10000, 1e-4]
	for x in xvalues:
		print "testing with x = %20.15e" % x
		s = sqrt2(x)
		s_numpy = sqrt(x)
		print " s = %20.15e, numpy.sqrt = %20.15e" % (s, s_numpy)
		assert abs(s - s_numpy) < 1e-14, "Disagree for x = %20.15e" % x
