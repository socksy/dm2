dm2
===

Datamining Practical 2


Setting up
-----------

Don't know how proficient you guys are --- if this is too condescending, apologies. If it's too complicated or you're having trouble, send me an email/fb message (bjl7/blovell respectively).

Using ipython with ipython notebook, scikit learn, and pandas (R in Python).

You'll need python, which all macs should have installed by default, and most linux distros. If you're running windows, either get cygwin, or linux, or use the lab computers. If you don't have them, install pip (the python package manager) and virtualenv.

In the terminal:

```bash
sudo easy_install pip
sudo pip install virtualenv
```

Make a virtualenv using `virtualenv dm2` and activate it with `source bin/activate`. The prompt should change to begin with (dm2). Now install the requirements using `pip install -r requirements.txt` This will take a while. Maybe take the time to look up ipython if you're not familiar? Maybe not. Your call. Perhaps there's something on iplayer.

Wooo it's done. Now you can run `ipython notebook` and a browser window should pop open with a choice of notebooks. Select the dm2 notebook, and you should now have an interactive shell. Shift enter runs a command.
