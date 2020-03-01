What is this?
=============

- Git repository containing internet radio playlists.
- Playlists are grouped by the radio name in the directory structure.
  (Symlinks can be used to create different directory structure.)
- The ``radio_update`` script can re-download the playlists.
- ``radio`` script allows quick access to recently played stations
- **Pull requests welcome.**

radio_update dependencies
-------------------------

- python3
- beautifulsoup4

radio
-----

``radio`` script will prompt user for ID of the station to play
via ``mpv``. It also allows filtering list of the stations by a substring::

        radio soma
