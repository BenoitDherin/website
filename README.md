website
=======

Source for generating and uploading a [template website Stat 133](http://berkeley-stat133.github.io/]) at the
url: [http://berkeley-stat133.github.io/](http://berkeley-stat133.github.io/]). This uses

* [pelican blog generator](http://blog.getpelican.com/)
* [pelican-boostrap3 theme](https://github.com/DandyDev/pelican-bootstrap3)
* [pelican plugins](https://github.com/getpelican/pelican-plugins)


Installation
============

From within [OskiBox](https://docs.google.com/document/d/1ybM5k73-b38dvYDbr8QX01l15SNgfysdS7wDmlQDBcY/pub), 
you may need to install node.js, if you wish to use convert iPython notebooks with pelican:

	sudo apt-get update
	sudo apt-get install nodejs


Then, it's best to install in a virtualenv because you need a specific version of
IPython, in particualar.  Something like::

    virtualenv pelican-blog
    source pelican-blog/bin/activate
    pip install -r requirements.txt


Developing
==========

To run Pelican in regeneration mode and serve the output at
http://localhost:8000, type:

    make devserver

Once you are happy with your changes, type::

    make stopserver

Publishing
==========

To build the site and push it to github, type:

    make github

The updated page can be viewed here: http://berkeley-stat133.github.io/

Cleaning up
===========

When you've finished working on the blog, deactivate the virtualenv::

    deactivate

To start working on it again, ``cd`` into this directory and::

    . pelican-blog/bin/activate
