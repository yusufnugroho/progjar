#!/usr/bin/env python

import random
import time


class TC:

    def __init__(self):
        self._tm = None
        self._bProblem = 0

    def setup(self):
        print("Setup connection")
        
        self._tm.prepareReporting()

    def execute(self):
        if not self._bProblem:
            print("Execute Command")
            
        else:
            print("Cannot Execute Command")

    def tearDown(self):
        if not self._bProblem:
            print("connection tearDown")
            self._tm.publishReport()
        else:
            print("problem occured")

    def setTM(self, tm):
        self._tm = tm

    def setProblem(self, value):
        self._bProblem = value


class Reporter:

    def __init__(self):
        self._tm = None

    def prepare(self):
        print("Prepare data...")
        

    def report(self):
        print("Report...")
        

    def setTM(self, tm):
        self._tm = tm


class DB:

    def __init__(self):
        self._tm = None

    def insert(self):
        print("Insert Data On DataBase")
        
    def update(self):
        print("Update Data On DataBase")
        
    def setTM(self, tm):
        self._tm = tm

class TestManager:

    def __init__(self):
        self._reporter = None
        self._db = None
        self._tc = None

    def prepareReporting(self):
        rvalue = self._db.insert()
        if rvalue == -1:
            self._tc.setProblem(1)
            self._reporter.prepare()

    def setReporter(self, reporter):
        self._reporter = reporter

    def setDB(self, db):
        self._db = db

    def publishReport(self):
        self._db.update()
        self._reporter.report()

    def setTC(self, tc):
        self._tc = tc


if __name__ == '__main__':
    reporter = Reporter()
    db = DB()
    tm = TestManager()
    tm.setReporter(reporter)
    tm.setDB(db)
    reporter.setTM(tm)
    db.setTM(tm)
    for i in range(1):
        tc = TC()
        tc.setTM(tm)
        tm.setTC(tc)
        tc.setup()
        tc.execute()
        tc.tearDown()