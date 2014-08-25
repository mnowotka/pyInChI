from mode import *
from incomdef import *
from ichidrp import *

#bDrawingLabelLeftShift = endpoint # for drawing only

## inp_ATOM::at_type ##
ATT_NONE = 0x0000
ATT_ACIDIC_CO = 0x0001
ATT_ACIDIC_S = 0x0002
ATT_OO = 0x0004
ATT_ZOO = 0x0008
ATT_NO = 0x0010
ATT_N_O = 0x0020
ATT_ATOM_N = 0x0040
ATT_ATOM_P = 0x0080
ATT_OTHER_NEG_O = 0x0100
ATT_OTHER_ZO = 0x0200 # -Z=O or =Z=O
ATT_OH_MINUS = 0x0400 # OH(-), O=O,S,Se,Te
ATT_O_PLUS = 0x0800 # -OH2(+), =OH(+), -OH(+)-, OH3(+), =O(+)-, etc; O=O,S,Se,Te
ATT_PROTON = 0x1000
ATT_HalAnion = 0x2000
ATT_HalAcid = 0x4000
if FIX_NP_MINUS_BUG:
    ATT_NP_MINUS_V23 = 0x8000 # =N(-) or =P(-) where = previously was triple

AT_FLAG_ISO_H_POINT = 0x01  # may have isotopic H

PERIODIC_NUMBER_H = 1

def NUM_ISO_H(AT,N):
    return AT[N].num_iso_H[0] + AT[N].num_iso_H[1] + AT[N].num_iso_H[2]

def NUMH(AT,N):
    return AT[N].num_H + NUM_ISO_H(AT,N)

FlagSC_0D = 1  # bUsed0DParity
FlagSB_0D = 2  # bUsed0DParity

SB_PARITY_FLAG = 0x38 # mask for disconnected metal parity if it is different 
SB_PARITY_SHFT = 3    # number of right shift bits to get disconnected metal parity
SB_PARITY_MASK = 0x07

def SB_PARITY_1(X):
    return X & SB_PARITY_MASK  # refers to connected structure 
def SB_PARITY_2(X):
    return ((X) >> SB_PARITY_SHFT) & SB_PARITY_MASK # refers to connected structure

class inp_ATOM(Struct):
    elname = None # chem. element name
    el_number = None # number of the element in the Periodic Table
    neighbor = None # positions (from 0) of the neighbors in the inp_ATOM array
    orig_at_number = None # original atom number
    orig_compt_at_numb = None # atom number within the component before terminal H removal
    bond_stereo = None # 1=Up,4=Either,6=Down; this atom is at the pointing wedge,
                       # negative => on the opposite side; 3=Either double bond
    bond_type = None # 1..4; 4="aromatic", should be discouraged on input

    valence = None # number of bonds = number of neighbors
    chem_bonds_valence = None # sum of bond types (type 4 needs special treatment)
    num_H = None # number of implicit hydrogens including D and T
    num_iso_H = None # number of implicit 1H, 2H(D), 3H(T) < 16
    iso_atw_diff = None # =0 => natural isotopic abundances  
                        # >0 => (mass) - (mass of the most abundant isotope) + 1 
                        # <0 => (mass) - (mass of the most abundant isotope) 
    charge = None # charge
    radical = None # RADICAL_SINGLET, RADICAL_DOUBLET, or RADICAL_TRIPLET
    bAmbiguousStereo = None
    cFlags = None # AT_FLAG_ISO_H_POINT
    at_type = None # ATT_NONE, ATT_ACIDIC
    component = None # number of the structure component > 0
    endpoint = None # id of a tautomeric group
    c_point = None # id of a positive charge group
    x = None
    y = None
    z = None
    ## cml 0D parities ##
    bUsed0DParity = None # bit=1 => stereobond; bit=2 => stereocenter
    ## cml tetrahedral parity ##
    p_parity = None
    p_orig_at_num = None
    ## cml bond parities ##
    sb_ord = None # stereo bond/neighbor ordering number, starts from 0
    ## neighbors on both sides of stereobond have same sign=> trans/T/E, diff. signs => cis/C/Z ##
    sn_ord = None # ord. num. of the neighbor adjacent to the SB; starts from 0;
                  # -1 means removed explicit H 
    ## neighbors on both sides of stereobond have same parity => trans/T/E/2, diff. parities => cis/C/Z/1 ##
    sb_parity = None
    sn_orig_at_num = None # orig. at number of sn_ord[] neighbors

    if FIND_RING_SYSTEMS:
        bCutVertex = None
        nRingSystem = None
        nNumAtInRingSystem = None
        nBlockSystem = None

    if FIND_RINS_SYSTEMS_DISTANCES:
        nDistanceFromTerminal = None # terminal atom or ring system has 1, next has 2, etc.

class ORIG_ATOM_DATA(Struct):
    ''' initially filled out by MolfileToOrigAtom
    may be changed by disconnecting salts and disconnecting metals '''
    at = None
    num_dimensions = None
    num_inp_bonds = None
    num_inp_atoms = None
    ## may be changed by disconnecting salts and disconnecting metals ##
    num_components = None # set by MarkDisconnectedComponents() and disconnecting metals
    bDisconnectSalts = None # whether salt disconnection is possible
    bDisconnectCoord = None # 0 if no disconnection needed else (Num Implicit H to disconnect)+1
    if bRELEASE_VERSION == 0:
        bExtract = None

    nCurAtLen = None # has max_num_components elements
    nOldCompNumber = None # 0 or component number in previous numbering
    nNumEquSets = None # number of found component equivalence sets
    nEquLabels = None # num_inp_atoms elements, value>0 marks atoms in the set #value
    nSortedOrder = None # num_components elements, values = 1..num_components; only if num_components > 1
    bSavedInINCHI_LIB = None
    bPreprocessed = None
    szCoord = None

class ORIG_STRUCT(Struct):
    num_atoms = None
    szAtoms = None
    szBonds = None
    szCoord = None

class inf_ATOM(Struct):
    at_string = None
    DrawingLabelLeftShift = None
    DrawingLabelLength = None
    nCanonNbr = None # if zero then do not use all data for the atom
    nCanonEquNbr = None
    nTautGroupCanonNbr = None
    nTautGroupEquNbr = None
    cFlags = None # AT_FLAG_ISO_H_POINT
    nDebugData = None
    cHighlightTheAtom = None
    cStereoCenterParity = None
    cStereoBondParity = None
    cStereoBondWarning = None
    cStereoBondNumber = None

INF_STEREO_ABS = 0x0001
INF_STEREO_REL = 0x0002
INF_STEREO_RAC = 0x0004
INF_STEREO_NORM = 0x0008
INF_STEREO_INV = 0x0010
INF_STEREO = 0x0020
INF_STEREO_ABS_REL_RAC = (INF_STEREO_ABS | INF_STEREO_REL | INF_STEREO_RAC)
INF_STEREO_NORM_INV = (INF_STEREO_NORM | INF_STEREO_INV)

MAX_LEN_REMOVED_PROTONS = 128

class INF_ATOM_DATA(Struct):
    at = None
    num_at = None
    StereoFlags = None
    num_components = None
    pStereoFlags = None

    nNumRemovedProtons = None
    num_removed_iso_H = None # number of exchangable isotopic H
    num_iso_H = None # number of exchangable isotopic H
    szRemovedProtons = None

class INP_ATOM_DATA(Struct):
    at = None
    at_fixed_bonds = None # tautomeric case, added or removed H */
    num_at = None
    num_removed_H = None
    num_bonds = None
    num_isotopic = None
    bExists = None
    bDeleted = None
    bHasIsotopicLayer = None
    bTautomeric = None
    bTautPreprocessed = None
    nNumRemovedProtons = None
    nNumRemovedProtonsIsotopic = None # isotopic composition of removed protons, not included in num_iso_H[]
    num_iso_H = None # isotopic H on tautomeric atoms and those in nIsotopicEndpointAtomNumber
    bTautFlags = None
    bTautFlagsDone = None
    bNormalizationFlags = None

class NORM_CANON_FLAGS(Struct):
    bTautFlags = None
    bTautFlagsDone = None
    bNormalizationFlags = None
    nCanonFlags = None

class COMP_ATOM_DATA(Struct):
    at = None
    num_at = None
    num_removed_H = None
    num_bonds = None
    num_isotopic = None
    bExists = None
    bDeleted = None # unused
    bHasIsotopicLayer = None
    bTautomeric = None
    nNumRemovedProtons = None
    nNumRemovedProtonsIsotopic = None # isotopic composition of removed protons, not included in num_iso_H[]
    num_iso_H = None # isotopic H on tautomeric atoms and those in nIsotopicEndpointAtomNumber

    nOffsetAtAndH = None
    num_components = None


ADD_LEN_STRUCT_FPTRS = 100  # allocation increments

class STRUCT_FPTRS(Struct):
    fptr = None # input:  fptr[cur_fptr]   = file pointer to the structure to read
                # output: fptr[cur_fptr+1] = file pointer to the next structure or EOF 
    len_fptr = None # allocated length of fptr
    cur_fptr = None # input: k-1 to read the kth struct, k = 1, 2, 3,...; left unchanged; struct number := cur_fptr+1
    max_fptr = None # length of the filled out portion of fptr

FLAG_INP_AT_CHIRAL = 1
FLAG_INP_AT_NONCHIRAL = 2
FLAG_SET_INP_AT_CHIRAL = 4
FLAG_SET_INP_AT_NONCHIRAL = 8


