import os
import platform

if platform.system() == 'Windows':
    os.system('cls')
else:
    os.system('clear')


# FOREGROUND COLORS
def black():
    return '\u001b[30;1m'


def red():
    return '\u001b[31;1m'


def green():
    return '\u001b[32;1m'


def yellow():
    return '\u001b[33;1m'


def blue():
    return '\u001b[34;1m'


def magenta():
    return '\u001b[35;1m'


def cyan():
    return '\u001b[36;1m'


def white():
    return '\u001b[37;1m'


def reset():
    return '\u001b[0m'


# BACKGROUND COLORS
def b_black():
    return '\u001b[40;1m'


def b_red():
    return '\u001b[41;1m'


def b_green():
    return '\u001b[42;1m'


def b_yellow():
    return '\u001b[43;1m'


def b_blue():
    return '\u001b[44;1m'


def b_magenta():
    return '\u001b[45;1m'


def b_cyan():
    return '\u001b[46;1m'


def b_white():
    return '\u001b[47;1m'


if __name__ == '__main__':
    print('You are not supposed to run this program.\nThis was made to be a module.')
    os.system('pause >NUL')
