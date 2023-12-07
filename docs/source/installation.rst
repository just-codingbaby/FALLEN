Install
=======

For Linux
---------

1. Install venv:

   .. code-block:: sh

      sudo apt-get install python3-venv

2. Create a virtual environment:

   .. code-block:: sh

      python3 -m venv virtual

3. Start the virtual environment:

   .. code-block:: sh

      source virtual/bin/activate

4. Your path will change, and it will show the name of your virtual environment:

   .. code-block:: sh

      (virtual)

5. Install Django, Pillow, and django-crispy-forms:

   .. code-block:: sh

      pip install Django
      pip install pillow
      pip install django-crispy-forms

For Windows
-----------

1. Create a virtual environment:

   .. code-block:: sh

      python -m venv virtual

3. Activate the virtual environment:

   .. code-block:: sh

      .\virtual\Scripts\activate

5. Install Django, Pillow, and django-crispy-forms:

   .. code-block:: sh

      pip install Django pillow django-crispy-forms
