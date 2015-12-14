# Ultros-Examples

This repository contains example code to help you get started with working on
and extending [Ultros](https://github.com/UltrosBot/Ultros). You can find 
a full set of API documentation [at this site](http://apidocs.ultros.io).
-------------------

Using [GitTorrent](https://github.com/cjb/GitTorrent)? `git clone gittorrent://b5177a0bf3fdf17caaade5be2db5feb0818e0566/Ultros-examples`

## Plugins

There are a number of example plugins here.

### Example

This is the standard example plugin - A fully documented, simple example of how
to write a plugin with a simple command. This is intended to be an example of
how you should structure your plugin.

### CljTest

This is our standard example plugin, rewritten in [ClojurePy](https://halgari.github.io/clojure-py/). 
If you want to test this on your instance, you'll need to install `clojure-py` 
from pip. Remember to add that to your module requirements if you're submitting 
your package to the contrib repo!

### HyTest

This is our standard example plugin, rewritten in [Hy](http://docs.hylang.org/en/stable/). 
Hy is not a default requirement for Ultros, and will require that you add it to your
module requirements if you're submitting your package to the contrib repo. This allows 
Ultros to import Hy plugins directly, for full integration with Ultros.

### WebRoute

This is a plugin that shows how to work with [the Web plugin](https://github.com/UltrosBot/Ultros-contrib/tree/master/Web) - 
Specifically, the correct way to add a route. As this plugin doesn't check 
for permissions, we do recommend that you don't load this plugin on a production server.
