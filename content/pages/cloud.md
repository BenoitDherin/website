Title: Cloud
Slug: cloud


Cloud Machine Setup

How to access your cloud machine

Needed software and local installations {.c5 .c14}
=======================================

You’ll first need to install (if not already present) a remote desktop
program on your laptop, which may be different depending on the
operating system running on your computer:

-   Mac users need Microsoft Remote Desktop Connection (which comes with
    Office if you have it) or [CoRD](http://cord.sf.net/)
-   Linux users need [rdesktop](http://www.rdesktop.org/).
-   Windows user have Microsoft Remote Desktop Connection installed by
    default (so nothing to do, but searching for it on the search bar:
    type in “remote”)

Once you have the remote program above installed on your machine, you’ll
be able to use them to connect to your class account to the class cloud
machine, in the following way:

![](Cloud%20Machine%20Setup_files/pubimage.png)

-   Launch your the remote desktop program
-   Enter in it the following information:

-   Your cloud SCF user login

s133-UID (for Stat 133)

s135-UID (for Stat 135)

where you should replace “UID” above by your personal UID (to be found
in the [Berkeley
Directory](https://calnet.berkeley.edu/directory/index.pl)). See the
example above and to the right.

-   Your cloud SCF password (see below on how to set it up)
-   The IP address of the class cloud machine set up

-   98.143.35.12 for Stat 133 (s133-1)
-   98.143.35.205 for Stat 135 (s135-1)

-   Connect, and then enjoy the cloud experience!

Setting your cloud SCF password {.c5 .c16}
===============================

For that you’ll need to launch a terminal, which is installed by default
on Mac and Linux machines. For Windows users, you’ll first need to
install
[putty](http://www.chiark.greenend.org.uk/%7Esgtatham/putty/download.html).
Then do the following:

-   Lauch the terminal and type in the following command and press
    return

ssh Cloud-SCF-user-login@scf-ug01.berkeley.edu

        For example, ssh
[s133-123456@scf-ug01.berkeley.edu](mailto:s133-123456@scf-ug01.berkeley.edu).
You may alternatively connect

to scf-ug02.berkeley.edu through scf-ug10.berkeley.edu.

-   You’ll be prompted for a login and password. Enter your cloud SCF
    login and your SID as password. The password you’ll be asked to
    reset will be your cloud SCF password.

Published by [Google
Drive](https://docs.google.com/a/berkeley.edu/ "Learn more about Google Drive")–[Report
Abuse](https://docs.google.com/a/berkeley.edu/abuse?id=167NqV3ANI8YDmqqZTYqHUaTxaOxBQpHzcDCLyWjdfB8)–Updated
automatically every 5 minutes
