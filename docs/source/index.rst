Welcome to test-sphinx-to-documenter-links's documentation!
===========================================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:


Hello World!

The :mod:`numpy` library is used for numerical computing in Python.

Use the :py:func:`matplotlib.pyplot.subplots` function to create a new plot. We can also link to a section in the matplotlib documentation, like :external:ref:`anatomy_local`.

Via the custom Fortran domain, we can link to Fortran functions, e.g., :f:func:`prop` (This isn't actually handled by ``interspinx`` but by a custom ``missing_references`` function for the Fortran domain – but that's just because we implemented the Fortran domain in a weird way)

We can also link to sections in the QDYN documentation like :external+qdyn:ref:`/using.ipynb`
and :external+qdyn:doc:`howto/units`.

We can also link to Julia objects, e.g., the :external:jl:func:`QuantumPropagators.propagate`
or :jl:func:`init_prop(…; method=Cheby) <QuantumPropagators.init_prop-Tuple{Any, Any, Any, Val{:Cheby}}>`
function, as well as a heading in the ``QuantumPropagators``
documentation, e.g., :external+QuantumPropagators:ref:`overview_dynamical_generators`.
