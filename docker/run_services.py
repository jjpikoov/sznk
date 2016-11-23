#!/usr/bin/env python3
import argparse
import subprocess
from sys import platform

from services import Services


class ServiceRunner:

    def __init__(self):
        self.servs = Services()

    def activate_runner(self):
        parser = argparse.ArgumentParser()
        exclusive_args_group = parser.add_mutually_exclusive_group(required=True)

        exclusive_args_group.add_argument('-run', action='store_true',
                                          help="-r or -run to run services")
        exclusive_args_group.add_argument('-stop', action='store_true',
                                          help="-s or -stop to stop services")

        parser.add_argument('--exclude', type=str, nargs='*', metavar="service",
                            help="""Docker services to exclude as string, separated by space """
                                 """ex. --exclude="postgres mysql" """)
        args = parser.parse_args()

        excluded_services = []
        if args.exclude:
            excluded_services = args.exclude[0]
            excluded_services = excluded_services.split(' ')

        if args.run:
            for service in Services.SERVICES_NAMES:
                if service not in excluded_services:
                    self.run_service(service)
        elif args.stop:
            for service in Services.SERVICES_NAMES:
                if service not in excluded_services:
                    self.stop_service(service)

    def run_service(self, service_name):
        start_cmd = self.servs.get_start_command(service_name)
        try:
            self._execute_cmd_on_os(start_cmd)
        except Exception:
            enable_cmd = self.servs.get_enable_command(service_name)
            self._execute_cmd_on_os(enable_cmd)

    def stop_service(self, service_name):
        stop_cmd = self.servs.get_stop_command(service_name)
        self._execute_cmd_on_os(stop_cmd)

    def _execute_cmd_on_os(self, cmd):
        if platform == "linux" or platform == "linux2":
            self._execute_cmd_on_linux(cmd)
        elif platform == "win32":
            self._execute_cmd_on_windows(cmd)

    def _execute_cmd_on_linux(self, cmd):

        sp = subprocess.Popen(["/bin/bash", "-c", cmd])
        sp.communicate(timeout=5)

        if sp.returncode != 0:
            raise Exception("Command returned with non zero value!")

    def _execute_cmd_on_windows(self, cmd):
        sp = subprocess.Popen(["powershell.exe", cmd])
        sp.communicate(timeout=5)

        if sp.returncode != 0:
            raise Exception("Comma  nd returned with non zero value!")


if __name__ == '__main__':
    service_runner = ServiceRunner()
    service_runner.activate_runner()
