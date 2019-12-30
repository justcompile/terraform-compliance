import sys
import colorful
from emoji import emojize


class Defaults(object):
    def __init__(self):
        if '--no-ansi' in sys.argv:
            self.skip_colour = \
            self.warning_colour = \
            self.failure_colour = \
            self.info_colour = \
            self.yellow = \
            self.red = \
            self.green = \
            self.blue = \
                self.no_coloured_output

            self.info_icon = '*'
            self.warning_icon = '!'
            self.tada = ''
            self.icon = '>'

        else:
            self.skip_colour = colorful.bold_purple
            self.failure_colour = colorful.bold_red
            self.warning_colour = colorful.bold_yellow
            self.info_colour = colorful.bold_blue
            self.yellow = colorful.yellow
            self.red = colorful.red
            self.green = colorful.green
            self.blue = colorful.blue

            self.info_icon = emojize(':bulb:', use_aliases=True)
            self.warning_icon = emojize(':exclamation:', use_aliases=True)
            self.tada = emojize(':tada:', use_aliases=True)
            self.icon = emojize(':triangular_flag_on_post:', use_aliases=True)

    @staticmethod
    def no_coloured_output(param):
        return param