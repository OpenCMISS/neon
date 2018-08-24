

Extensions
==========

Adding a new extensions
-----------------------

To add a new extension there needs to be a **class** defined in the opencmiss.neon.extensions package.  You can
use packages to separate out the extension classes defined.  With an extension defined in the extensions class you must
also define the same package and class inside the opencmiss.neon.extensions.handlers package.

The class defined in the opencmiss.neon.extensions.handlers package must define a static method called **instantiate**.
The **instantiate** method must take two parameters.  The first parameter that is passed to the **instantiate** method
is a handle to the main view of the Neon application.  The second parameter passed is the class that is to be
instantiated.  An example is given below::


  class NewExtension(object):

      @staticmethod
      def instantiate(main_view, cls):
          """Have a point to load some data and set up some graphics."""
          extension = cls(main_view)


Some of the methods that you can call on the main view are::

    main_view.persist_extension
    """
    Make the main_view hold a handle to the extension.
    """

    main_view.register_save_pair(('newextension', extension.save))
    """
    Register a save method with a unique identifier.
    """

    main_view.register_open_pair(('newextension', extension.open))
    """
    Register an open method with a unique identifier.
    """

Creating a new extension
------------------------

When it is time to start creating a new extension it must go in the opencmiss.extensions package.  Both the opencmiss
 package and the extensions package are namespace packages that must have the following code snippet in the __init__.py
file::

  from pkgutil import extend_path
  __path__ = extend_path(__path__, __name__)

When creating the new extension a class in the package must be derived from the stub class defined in the
opencmiss.neon.extensions package.

Also in the __init__.py file for the package of the new extension you must import the class that is derived from the
stub class created following the instructions in the :ref:`Adding a new extensions`.
