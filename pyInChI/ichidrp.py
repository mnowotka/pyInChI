from enum import enum
from struct import Struct

##############################################
## Parameters for the structure drawing     ##
##############################################

TDP_LEN_LBL = 16

TBL_TYPES = enum(
    itBASIC = 0, 
    itISOTOPIC = 1, 
    itSTEREO = 2, 
    TDP_NUM_PAR =3
)

TBL_LABELS = enum(
    ilSHOWN = 0,
    TDP_NUM_LBL = 1
)

class TBL_DRAW_PARMS(Struct):
    ReqShownFoundTxt = None
    ReqShownFound = None
    nOrientation = None # 10*degrees: 0 or 2700
    bDrawTbl = None

class SET_DRAW_PARMS(Struct): # input only: how to draw or calculate
    tdp = None
    ulDisplTime = None
    bOrigAtom = None
    nFontSize = None
 
class RET_DRAW_PARMS(Struct):
    bEsc = None

class PER_DRAW_PARMS(Struct): # saved between displaying different structures
    rcPict = None

class DRAW_PARMS(Struct):
    sdp = None # how to draw: fill on the 1st call
    rdp = None # returned when drawing window is closed
    pdp = None # persistent: save between calls (window size)
    nEquLabels = None # num_inp_atoms elements, value>0 marks atoms in the set #value
    nNumEquSets = None # max mark value
    nCurEquLabel = None # current mark

MAX_NUM_PATHS = 4

INPUT_TYPE = enum(
    INPUT_NONE = 0, 
    INPUT_MOLFILE = 1, 
    INPUT_SDFILE = 2, 
    INPUT_INCHI_XML = 3, 
    INPUT_INCHI_PLAIN = 4, 
    INPUT_CMLFILE = 5, 
    INPUT_INCHI = 6, 
    INPUT_MAX = 7
)

## bCalcInChIHash values ##
INCHI_HASH_CALC = enum(  
    INCHIHASH_NONE = 0, 
    INCHIHASH_KEY = 1, 
    INCHIHASH_KEY_XTRA1 = 2, 
    INCHIHASH_KEY_XTRA2 = 3, 
    INCHIHASH_KEY_XTRA1_XTRA2 = 4 
)

class INPUT_PARMS(Struct):
    szSdfDataHeader = None
    pSdfLabel = None
    pSdfValue = None
    lSdfId = None
    lMolfileNumber = None
    dp = None
    pdp = None
    tdp = None
    path = None
    num_paths = None
    first_struct_number = None
    last_struct_number = None
    nInputType = None
    nMode = None
    bAbcNumbers = None
    bINChIOutputOptions = None # !(ip->bINChIOutputOptions & INCHI_OUT_PLAIN_TEXT)
    bCtPredecessors = None
    bXmlStarted = None
    bDisplayEachComponentINChI = None

    msec_MaxTime = None # was ulMaxTime; max time to run ProsessOneStructure
    msec_LeftTime = None

    ulDisplTime = None # not used: max structure or question display time
    bDisplay = None
    bDisplayIfRestoreWarnings = None # InChI->Struct debug
    bMergeAllInputStructures = None
    bSaveWarningStructsAsProblem = None
    bSaveAllGoodStructsAsProblem = None
    bGetSdfileId = None
    bGetMolfileNumber = None # read molfile number from the name line like "Structure #22"
    bCompareComponents = None # see flags CMP_COMPONENTS, etc.
    bDisplayCompositeResults = None
    bDoNotAddH = None
    bNoStructLabels = None
    bChiralFlag = None
    bAllowEmptyStructure = None
    
    bCalcInChIHash = None
    bFixNonUniformDraw = None # correct non-uniformly drawn oxoanions and amidinium cations.

    bTautFlags = None
    bTautFlagsDone = None

    bReadInChIOptions = None

    ## post v.1 features ##
    bUnderivatize = None
    bRing2Chain = None

    bIngnoreUnchanged = None

