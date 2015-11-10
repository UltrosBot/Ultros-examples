# Ultros-Examples

This repository contains example code to help you get started with working on
and extending [Ultros](https://github.com/UltrosBot/Ultros). You can find 
a full set of API documentation [at this site](http://apidocs.ultros.io).

## Plugins

There are a number of example plugins here.

### CljTest

This is our standard example plugin, rewritten in [ClojurePy](https://halgari.github.io/clojure-py/). 
If you want to test this on your instance, you'll need to install `clojure-py` 
from pip. Remember to add that to your module requirements if you're submitting 
your package to the contrib repo!

### Example

This is the standard example plugin - A fully documented, simple example of how
to write a plugin with a simple command. This is intended to be an example of
how you should structure your plugin.

### HyTest

This is our standard example plugin, rewritten in [Hy](http://docs.hylang.org/en/stable/). 
Hy is included as a default Ultros requirement, as this allows it to import Hy 
plugins directly, for full integration with Ultros.
