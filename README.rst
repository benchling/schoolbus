schoolbus
=========

A python library to guess whether an email is from an academic institution,
heavily based on the swot ruby gem: https://github.com/leereilly/swot.

Pull requests for missing institutions (see data.py) are welcome.

Available on PyPI:

    pip install schoolbus

Usage
-----

.. code:: python

	>>> schoolbus.is_academic('coryli@mit.edu')
	True
	>>> schoolbus.is_academic('josh@benchling.com')
	False

	>>> schoolbus.school_names('vineetg@mit.edu')
	[u'Massachusetts Institute of Technology']
	>>> schoolbus.school_names('sajith@scicu.org')
	[u'Claflin College', u'Allen University', u'Morris College']
