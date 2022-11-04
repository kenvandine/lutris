#!/usr/bin/env python3
# This program is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License version 3, as published
# by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranties of
# MERCHANTABILITY, SATISFACTORY QUALITY, or FITNESS FOR A PARTICULAR
# PURPOSE.  See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program.  If not, see <http://www.gnu.org/licenses/>.

"""Main entry point for Lutris"""
import gettext
import locale
import os
import sys
from os.path import dirname, normpath, realpath

LAUNCH_PATH = dirname(realpath(__file__))

def main():
    if os.path.isdir(os.path.join(LAUNCH_PATH, "../lutris")):
        sys.dont_write_bytecode = True
        SOURCE_PATH = normpath(os.path.join(LAUNCH_PATH, '..'))
        sys.path.insert(0, SOURCE_PATH)
    else:
        sys.path.insert(0, os.path.normpath(os.path.join(LAUNCH_PATH, "../lib/lutris")))

    try:
        locale.setlocale(locale.LC_ALL, "")
    except locale.Error:
        sys.stderr.write("Unsupported locale setting. Fix your locales\n")

    try:
        # optional_settings does not exist if you don't use the meson build system
        from lutris import optional_settings

        try:
            locale.bindtextdomain("lutris", optional_settings.LOCALE_DIR)
            gettext.bindtextdomain("lutris", optional_settings.LOCALE_DIR)
            locale.textdomain("lutris")
            gettext.textdomain("lutris")
        except:
            sys.stderr.write(
                "Couldn't bind gettext domain, translations won't work.\n"
                "LOCALE_DIR: %s\n" % optional_settings.LOCALE_DIR
            )
    except ImportError:
        pass

    from lutris.gui.application import Application  # pylint: disable=no-name-in-module

    app = Application()  # pylint: disable=invalid-name
    sys.exit(app.run(sys.argv))

if __name__ == '__main__':
    main()