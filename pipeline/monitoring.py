import numpy as np

class Monitor:
    def __init__(self): self.d = {"total":0,"errors":0,"lat":[]}
    def record(self, ms, ok=True):
        self.d["total"]+=1; self.d["lat"].append(ms)
        if not ok: self.d["errors"]+=1
    def stats(self):
        l=self.d["lat"]
        return {"p50":np.percentile(l,50),"p99":np.percentile(l,99)} if l else {}
