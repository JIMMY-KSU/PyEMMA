
r"""
.. currentmodule:: pyemma.coordinates

User API
========

**Data handling and IO**

.. autosummary::
   :toctree: generated/

   featurizer
   load
   source
   pipeline
   discretizer
   save_traj
   save_trajs

**Transformations**

.. autosummary::
   :toctree: generated/

   pca
   tica

**Clustering Algorithms**

.. autosummary::
   :toctree: generated/

   cluster_kmeans
   cluster_regspace
   cluster_uniform_time
   assign_to_centers

Classes
=======
**Coordinate classes** encapsulating complex functionality. You don't need to
construct these classes yourself, as this is done by the user API functions above.
Find here a documentation how to extract features from them.

.. autosummary::
   :toctree: generated/

   pipelines.Pipeline
   transform.PCA
   transform.TICA

"""
from .api import *
