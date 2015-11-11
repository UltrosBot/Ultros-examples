# coding=utf-8

from plugins.web.request_handler import RequestHandler

__author__ = 'Gareth Coles'


class Route(RequestHandler):
    """
    Example web route that list all channels under all protocols
    """

    # Match this with the name of your navbar entry, if you have one
    name = "example"

    # "get" is our verb here - you could use "post", "put", "head", etc too
    def get(self, *args, **kwargs):
        protocols = [  # Get a list of protocol objects
            x.protocol for x in self.plugin.factory_manager.factories.items()
        ]

        # Render the example.html Mako template, passing it our list of
        # protocols
        self.render(
            "example.html",
            protocols=protocols
        )
