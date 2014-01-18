website
=======

Source for generating website using pelican

Installation
============

Install Pelican and a few other packages (something like):

    pip install pelican markdown ghp-import shovel

Then:    

    mkdir -p ~/src/pelican
    cd  ~/src/pelican
    git clone https://github.com/getpelican/pelican-plugins.git

Developing
==========

To run Pelican in regeneration mode and serve the output at
http://localhost:8000, type:

    make devserver

Once you are happy with your changes, type:

    ./develop_server.sh stop

Publishing
==========

To build the site and push it to github, type:

    make github

The updated page can be viewed here: http://berkeley-stat133.github.io/
