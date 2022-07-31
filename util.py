import json

HASH = "Hash"

BNAME_FIELD = "-b"
VORDER_FIELD = "-v"
TIMEOUT_FIELD = "-t"
UNATE_FIELD = "-u"
BOOL_FIELDS = [UNATE_FIELD,"-s","-o","-f"]
VAL_FIELDS = [ "-c", "-r", "-d", TIMEOUT_FIELD, "--unateTimeout"]
NON_BOOL_FIELDS = [BNAME_FIELD, VORDER_FIELD] + VAL_FIELDS
CONFIG_FIELDS = BOOL_FIELDS + VAL_FIELDS
FIELDS = [BNAME_FIELD, VORDER_FIELD] + CONFIG_FIELDS + [HASH]
# name, order, booleans, values

INIT_UN = "Initial unates"
FIN_UN = "Final unates"
TOT_OUTPUTS = "Total outputs without unate"
FIXED_OUTPUTS = "Outputs fixed"
NUM_CEX = "Number of cex"

# ["Benchmark", "VarOrder", "unate?","shannon?", "dynamic?", "fastCNF?"]
HEADER = FIELDS + ["Initial size", "Final size", INIT_UN, FIN_UN, "Number of iterations", NUM_CEX, FIXED_OUTPUTS, TOT_OUTPUTS, "Time taken", "repairTime", "conflictCnfTime", "satSolvingTime", "unateTime", "compressTime", "rectifyCnfTime", "rectifyUnsatCoreTime", "overallCnfTime", "ERROR"]


ALLUNATES = "allUnates"
NOCONFU = "noConflictsWithUnates"
NOCONF = "noConflicts"
NOU = "noUnates"
OTHER = "others"
ERROR = "error"

# row maps directly to HEADER
def analysis(row: list, error: bool) -> dict :
    # U in the end signifies Unate, no U means No Unate case
    def isAllU():
        return int(row[HEADER.index(TOT_OUTPUTS)]) == 0
    def isNoConfU():
        return (UNATE_FIELD in row) and (int(row[HEADER.index(NUM_CEX)] == 0)) and (int(row[HEADER.index(FIXED_OUTPUTS)]) == int(row[HEADER.index(TOT_OUTPUTS)]))
    def isNoConf():
        return (UNATE_FIELD not in row) and (int(row[HEADER.index(NUM_CEX)] == 0)) and (int(row[HEADER.index(FIXED_OUTPUTS)]) == int(row[HEADER.index(TOT_OUTPUTS)]))
    def isNoU():
        # fully solved but had no unates
        return (UNATE_FIELD in row) and (int(row[HEADER.index(FIN_UN)]) == 0) and (int(row[HEADER.index(FIXED_OUTPUTS)]) == int(row[HEADER.index(TOT_OUTPUTS)]))
    
    d = dict()
    if (error):
        d[ERROR] = True
    if isAllU():
        d[ALLUNATES] = True
    if isNoConfU():
        d[NOCONFU] = True
    if isNoConf():
        d[NOCONF] = True
    if isNoU():
        d[NOU] = True
    if (len(d) == 0):
        d[OTHER] = True
        
    return d


    


