#!/usr/bin/env python3


class Service:
    def __init__(self, name):
        self.name = name

    def start(self):
        raise NotImplementedError('not implemented')

    def stop(self):
        raise NotImplementedError('not implemented')

    def status(self):
        raise NotImplementedError('not implemented')