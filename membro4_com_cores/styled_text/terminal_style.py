class InvalidColor(ValueError):
    pass


class InvalidBoldValue(ValueError):
    pass


class TerminalStyle:
    """ Class representing a style terminal. """

    background_codes = {
        "black": "40",
        "blue": "44",
        "green": "42",
        "cyan": "46",
        "red": "41",
        "magenta": "45",
        "yellow": "43",
        "gray": "47",
        "light_gray": "100",
        "light_blue": "104",
        "light_green": "102",
        "light_cyan": "106",
        "light_red": "101",
        "light_magenta": "105",
        "light_yellow": "103",
        "white": "107"
    }

    foreground_codes = {
        "black": "30",
        "blue": "34",
        "green": "32",
        "cyan": "36",
        "red": "31",
        "magenta": "35",
        "yellow": "33",
        "gray": "37",
        "light_gray": "90",
        "light_blue": "94",
        "light_green": "92",
        "light_cyan": "96",
        "light_red": "91",
        "light_magenta": "95",
        "light_yellow": "93",
        "white": "97"
    }

    def __init__(self, background_color="black", foreground_color="white", bold=False):
        self.background_color = background_color
        self.foreground_color = foreground_color
        self.bold = bold

    @property
    def background_color(self):
        return self._background_color

    @background_color.setter
    def background_color(self, color):
        if color in TerminalStyle.background_codes:
            self._background_color = color
        else:
            raise InvalidColor(f"Invalid background color, {color} is not a valid color.")

    @property
    def foreground_color(self):
        return self._foreground_color

    @foreground_color.setter
    def foreground_color(self, color):
        if color in TerminalStyle.foreground_codes:
            self._foreground_color = color
        else:
            raise InvalidColor(f"Invalid foreground color, {color} is not a valid color.")

    @property
    def bold(self):
        return self._bold

    @bold.setter
    def bold(self, value):
        if isinstance(value, bool):
            self._bold = value
        else:
            raise InvalidBoldValue("Invalid bold type, must be boolean.")

    def render(self):
        codes = []
        if self.bold == True:
            codes.append("1")
        else:
            codes.append("0")

        codes.append(TerminalStyle.background_codes[self.background_color])

        codes.append(TerminalStyle.foreground_codes[self.foreground_color])

        codes_str = ";".join(codes)

        return f"\033[{codes_str}m"

    def __copy__(self):
        return TerminalStyle(self.background_color, self.foreground_color, self.bold)

    def __eq__(self, other):
        return self.__class__ == other.__class__ and self.__dict__ == other.__dict__
