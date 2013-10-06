WHAT IS THIS
============
A modified version of sonata's rhapsodycovers plugin for fetching album art from last.fm.

INSTALL
============
Clone the original git: `git clone git://git.berlios.de/sonata`. This description is written for version 1.6.2.1.

Copy the lastfmcovers.py to the sonata's folder (the same folder in which the rhapsodycovers.py file is located). Open the sonata's `main.py` file and add two lines. The first is an import line next to other imports:
```
import lastfmcovers
```

The second line is to make sonata aware of the plugin. Find the line `self.rhapsodycovers = rhapsodycovers.RhapsodyCovers()` and then underneath it put:
```
self.lastfmcovers = lastfmcovers.LastfmCovers()
```

Next, run sonata and enable the plugin in it's settings. You can disable the rhapsody covers plugin.
