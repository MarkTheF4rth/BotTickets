from task import task
import os
from collections import OrderedDict
import pickle

@task(run_time='init')
async def startup(self):
    os.chdir(self.data_dir)
    if os.path.isfile('requests.p'):
        print('Loading cached info...')
        self.reports = pickle.load(open("reports.p", "rb"))
        self.requests = pickle.load(open("requests.p", "rb"))
        self.votes = pickle.load(open("votes.p", "rb"))
        self.index = pickle.load(open("index.p", "rb"))
    else:
        print('No cached info found, initialising...')
        self.reports = {}
        self.requests = {}
        self.votes = {}
        self.index = 0
        pickle.dump(self.reports, open("reports.p", "wb"))
        pickle.dump(self.requests, open("requests.p", "wb"))
        pickle.dump(self.index, open("index.p", "wb"))
        pickle.dump(self.votes, open("votes.p", "wb"))
    os.chdir(self.home_dir)
    self.buffer = {}
