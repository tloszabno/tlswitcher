#!/usr/bin/env python3
import wmctrl
import sys
import subprocess

def activate_or_run_app(app_name):
    window = list(filter(lambda window: app_name in window.wm_class, wmctrl.Window.list()))
    if len(window) > 0:
        window[0].activate()
    else:
        subprocess.Popen([app_name])


if __name__ == "__main__":
    activate_or_run_app(sys.argv[1])



