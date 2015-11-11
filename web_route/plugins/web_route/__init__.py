# coding=utf-8

import system.plugins.plugin as plugin  # Import the plugin base class

"""
An example plugin for you to refer to when you're creating your own ones.
Now with added Web plugin!
"""

__author__ = "Gareth Coles"  # Who are you?


class ExampleWebPlugin(plugin.PluginObject):  # Create the plugin class
    """
    Example plugin object
    """

    @property
    def web(self):
        """
        Grab the currently-loaded instance of the Web plugin

        We do it this way to avoid causing memory leaks and outdated plugin
        references, in the case that the web plugin is unloaded or reloaded
        """
        return self.plugins.get_plugin("Web")

    def setup(self):
        """
        Called when the plugin is loaded. Performs initial setup.
        """

        self.events.add_callback(  # Listen for the Web server start event
            "Web/ServerStartedEvent",  # Name of the event
            self,  # This plugin
            self.web_started,  # The function to call
            1
        )

    def web_started(self, _=None):  # We don't need the event object
        """
        Called when the Web plugin has started its server
        """

        self.web.add_handler(
            r"/example",  # Regular expression defining the web path
            "plugins.web_route.route.Route"  # Module containing the route
        )
        self.web.add_handler(r"/example/", "plugins.web_route.route.Route")

        self.web.add_navbar_entry(
            "example",  # Name of navbar entry; also used for text
            "/example",  # Path of navbar entry
            "code"  # Legacy semantic-ui icon name
            # More icons: http://legacy.semantic-ui.com/elements/icon.html
        )

    def deactivate(self):
        """
        Called when our plugin is unloaded; use this to clean up
        """

        # Unregister the handler and nav entry as our plugin is being unloaded
        self.web.remove_handlers(r"/example", r"/example/")
        self.web.remove_navbar_entry("example")
