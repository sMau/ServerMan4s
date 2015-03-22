#!/usr/bin/env python3
from src.datastructure.service import Service


class CsGo(Service):

    def __init__(self, path, script_name):
        self.path = path
        self.script_name = script_name

    def start(self):
        pass

    def stop(self):
        pass

    def status(self):
        pass