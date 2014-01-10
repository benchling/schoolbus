schoolbus
=========

A python library to guess whether an email is from an academic institution,
heavily based on the swot ruby gem: https://github.com/leereilly/swot.

Pull requests for missing institutions (see data.py) are welcome.

Usage
-----

.. code:: python

	>>> schoolbus.is_academic('joshma@mit.edu')
	True
	>>> schoolbus.is_academic('josh@benchling.com')
	False

	>>> schoolbus.school_names('joshma@mit.edu')
	[u'Massachusetts Institute of Technology']
	>>> schoolbus.school_names('josh@scicu.org')
	[u'Claflin College', u'Allen University', u'Morris College']
