class process_colors:
    black = 30
    red = 31
    green = 32
    yellow = 33
    blue = 34
    purple = 35
    cyan = 36
    white = 37

    style_none = 0
    style_bold = 1
    style_underline = 2
    style_negative1 = 3
    style_negative2 = 5

    bg_black = 40
    bg_red = 41
    bg_green = 42
    bg_yellow = 43
    bg_blue = 44
    bg_purple = 45
    bg_cyan = 46
    bg_white = 47

    def color (style,text,background):
        return "\033["+str(style)+";"+str(text)+";"+str(background)+"m"

    def get_colors ():
        py_compile.compile("etc/console/color","var/color.pyc")
        from var import color
        color = reload(color)
        style = color.style
        fgcolor = color.fgcolor
        bgcolor = color.bgcolor
        return "\033["+str(style)+";"+str(fgcolor)+";"+str(bgcolor)+"m"

    def get_style ():
        py_compile.compile("etc/console/color","var/color.pyc")
        from var import color
        color = reload(color)
        strv = color.style
        return strv

    def get_fgcolor ():
        py_compile.compile("etc/console/color","var/color.pyc")
        from var import color
        color = reload(color)
        strv = color.fgcolor
        return strv

    def get_bgcolor ():
        py_compile.compile("etc/console/color","var/color.pyc")
        from var import color
        color = reload(color)
        strv = color.bgcolor
        return strv

    def get_warning():
        py_compile.compile("etc/console/color", "var/color.pyc")
        from var import color
        color = reload(color)
        strv =  "\033[" + str(color.warning_style) + ";" + str(color.warning_fgcolor) + ";" + str(color.warning_bgcolor) + "m"
        return strv

    def get_path():
        py_compile.compile("etc/console/color", "var/color.pyc")
        from var import color
        color = reload(color)
        strv =  "\033[" + str(color.path_style) + ";" + str(color.path_fgcolor) + ";" + str(color.path_bgcolor) + "m"
        return strv

    def get_prompt():
        py_compile.compile("etc/console/color", "var/color.pyc")
        from var import color
        color = reload(color)
        strv =  "\033[" + str(color.prompt_style) + ";" + str(color.prompt_fgcolor) + ";" + str(color.prompt_bgcolor) + "m"
        return strv

    def get_fail():
        py_compile.compile("etc/console/color", "var/color.pyc")
        from var import color
        color = reload(color)
        strv =  "\033[" + str(color.fail_style) + ";" + str(color.fail_fgcolor) + ";" + str(color.fail_bgcolor) + "m"
        return strv

    def get_ok():
        py_compile.compile("etc/console/color", "var/color.pyc")
        from var import color
        color = reload(color)
        strv =  "\033[" + str(color.ok_style) + ";" + str(color.ok_fgcolor) + ";" + str(color.ok_bgcolor) + "m"
        return strv