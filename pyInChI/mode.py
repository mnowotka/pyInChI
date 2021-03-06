INCHI_VERSION = "1"
INCHI_NAME = "InChI"
INCHI_NAM_VER_DELIM = "="
TARGET_ID_STRING = ", Software version 1.04 (API Library) Build of September 9, 2011"
TARGET_EXE_STANDALONE = 1
TARGET_API_LIB = 0

if not TARGET_EXE_STANDALONE and not TARGET_API_LIB:
    I2S_MODIFY_OUTPUT = 1  # 1=> Allow various InChI2InChI output types from cInChI
else:
    I2S_MODIFY_OUTPUT = 0  # 0=> Always


BUILD_WITH_AMI = 1
ADD_CMLPP = 0
if not TARGET_EXE_STANDALONE:
    BUILD_WITH_AMI = 0
bRELEASE_VERSION = 1    
if bRELEASE_VERSION:
    DISPLAY_DEBUG_DATA_C_POINT  = 0
    DISPLAY_ORIG_AT_NUMBERS = 1
else:
    DISPLAY_DEBUG_DATA_C_POINT = 1 
    DISPLAY_ORIG_AT_NUMBERS = 1

if DISPLAY_DEBUG_DATA_C_POINT > 0:
    DISPLAY_DEBUG_DATA = DISPLAY_DEBUG_DATA_C_POINT

# BUG FIXES #

############################
## bug fixes in v1.00     ##
############################
FIX_ChCh_STEREO_CANON_BUG = 1  # 1=> (NEEDED)
ADD_ChCh_STEREO_CANON_CHK = 0  # 1 is NOT needed; let it always be 0
FIX_ChCh_CONSTIT_CANON_BUG = 1  # 1=> (NEEDED)
FIX_EITHER_STEREO_IN_AUX_INFO = 1  # 1=> fix bug: Either stereobond direction in Aux_Info; 0=> do not fix
FIX_NORM_BUG_ADD_ION_PAIR = 1  # 1=> (NEEDED) fix bug: Miscount number of charges when creating an ion pair
FIX_REM_PROTON_COUNT_BUG = 1  # 1=> (NEEDED) check for number of actually removed protons and issue an error if mismatch
FIX_READ_AUX_MEM_LEAK = 1
FIX_READ_LONG_LINE_BUG = 1  # 1=> (NEEDED) prevent failure when reading AuxInfo and InChI is too long
FIX_N_V_METAL_BONDS_GPF = 1  # 1=> (NEEDED) InChI v1 GPF bug fix
BNS_RAD_SEARCH = 1  # 1=> prevent normalization failures due to radical centers

#################################
## bug fixes in post-v1.00     ##
#################################
FIX_ODD_THINGS_REM_Plus_BUG = 0
FIX_N_MINUS_NORN_BUG = 0
FIX_CANCEL_CHARGE_COUNT_BUG = 0
FIX_2D_STEREO_BORDER_CASE = 0
FIX_REM_ION_PAIRS_Si_BUG = 0
FIX_STEREO_SCALING_BUG = 0
FIX_EMPTY_LAYER_BUG = 0
FIX_EITHER_DB_AS_NONSTEREO = 0
FIX_BOND23_IN_TAUT = 0
FIX_TACN_POSSIBLE_BUG = 0
FIX_KEEP_H_ON_NH_ANION = 0
FIX_AVOID_ADP = 0
# may change InChI
FIX_NUM_TG = 0  # increase number of t-groups for isothiocyanate
# changes InChI for isothiocyanate
FIX_CPOINT_BOND_CAP2 = 0

#################################
## bug fixes in post-v1.02b    ##
#################################

FIX_ISO_FIXEDH_BUG = 1 # (2007-09-24) 1=> Fix bug: missing fixed-H iso segment in case of single removed D(+)
FIX_ISO_FIXEDH_BUG_READ = 0 # (2007-09-24) 1=> Accommodate this InChI bug in reading InChI
FIX_DALKE_BUGS = 1  
FIX_TRANSPOSITION_CHARGE_BUG = 1	# (2008-01-02) fix bug that leads to missed charge in some cases when /o is present
FIX_I2I_STEREOCONVERSION_BUG = 1 # (2008-03-06)   1=> Fix bug of i2i conversion SAbs-->(SRel||Srac)
FIX_I2I_STEREOCONVERSION_BUG2 = 1 # (2008-04-02)   1=> Fix bug of i2i conversion (missed empty /t)
FIX_I2I_STEREOCONVERSION_BUG3 = 1 # (2008-04-10)   1=> Fix bug of i2i conversion
                                        # (missed repeating /s in FI after F for multi-component case)
FIX_TERM_H_CHRG_BUG = 1 # (2008-06-06) IPl)
#                                        fix bug: in some cases (dependent on ordering 
#                                        numbers), moving a charge from terminal H to heavy 
#                                        atom resulted in neutralizing H but not adjusting 
#                                        charge of heavy atom


FIX_AROM_RADICAL = 1 # (2011-05-09) 1=> Fix bug which leads for different InChI
# on atomic permitations for systems containing radical at
# atom in aromatic ring





FIX_NP_MINUS_BUG = 1         # 2010-03-11 DCh

############################
## additions to v1.00     ##
############################
FIX_ADJ_RAD = 0

SDF_OUTPUT_V2000 = 1  # 1=>always output V2000 SDfile, 0=>only if needed 
SDF_OUTPUT_DT = 1  # 1=> all option -SdfAtomsDT to output D and T into SDfile 
CHECK_AROMBOND2ALT = 1  # 1=> check whether arom->alt bond conversion succeeded 

READ_INCHI_STRING = 1  # 1=> input InChI string and process it

######################################################
## disabled extra external calls to InChI algorithm ##
######################################################
INCLUDE_NORMALIZATION_ENTRY_POINT = 0

############################
## Normalization settings ##
############################

# post version 1 features
KETO_ENOL_TAUT = 1 # include keto-enol tautomerism
TAUT_15_NON_RING = 1 # 1,5 tautomerism with endpoints not in ring

# v.1.04 : still experimental but may be exposed (set to 1)
UNDERIVATIZE = 0 # split to possible underivatized fragments
RING2CHAIN = 0 # open rings R-C(-OH)-O-R => R-C(=O) OH-R

# post-2004-04-27 features
HAL_ACID_H_XCHG = 1 # allow iso H exchange to HX (X=halogen) and H2Y (Y=halcogen)
CANON_FIXH_TRANS = 1 # produce canonical fixed-H transposition
STEREO_WEDGE_ONLY = 1 # 1=> only pointed ends stereo bonds define stereo; 0=> both ends

# current new (with respect to v1.12 Beta) preprocessing
REMOVE_ION_PAIRS_EARLY = 1 # 1=> new preprocessing: step 1 before disconnecting metals in fix_odd_things()
REMOVE_ION_PAIRS_DISC_STRU = 1 # 1=> new post-preprocessing: remove charhes after metal disconnection
REMOVE_ION_PAIRS_FIX_BONDS = 1 # 1=> step2: set unchangeable bonds around removed ion pairs
S_VI_O_PLUS_METAL_FIX_BOND = 1 # 1=> count double bond M-O(+)=S  as O=S in S(VI) ans S(VIII) fixing bonds
N_V_STEREOBONDS = 1 # 1=> detect stereobonds incident to N(V); 0 => don't
#for testing
REMOVE_ION_PAIRS_ORIG_STRU = 0 # 0=> normal mode (default)
#                              1=> testing mode only: remove ion pairs from the original structure 
#                              to save the changes in the output Molfile (/OutputSDF) or AuxInfo
#                              NIP=No Ion Pairs

# salts treatment
DISCONNECT_SALTS = 1  # 1=>disconnect metal atoms from salts, 0=>dont
TEST_REMOVE_S_ATOMS = 1  # 1=>default: after merging into one group test &
#                          remove unreachable,
#                          0=> old version: test only before merging into one t-group
CHARGED_SALTS_ONLY = 1  # 1=>(default)do not test far salts tautomerism if
#                         no negative charge(s) present
BNS_PROTECT_FROM_TAUT = 1  # 1=> do not allow testing of bonds to acetyl or nitro
BNS_MARK_EDGE_2_DISCONNECT = 1  # 1=> mark edge as temp forbidden instead of disconnection

REPLACE_ALT_WITH_TAUT = 1  # 1 => replace alt bonds with tautomeric bonds in case of standard t-groups
MOVE_CHARGES = 1  # 1 => take moveable charges into account */
NEUTRALIZE_ENDPOINTS = 1  # 1 => before checking whether an H is moveable make 2 endpoints neutral
                          #      implemented only if CHECK_TG_ALT_PATH = 0, defined in ichi_bns.c
FIX_H_CHECKING_TAUT = 1  # 1 => Fix moveable H or (-) before checking if taut. exchange is possible
ALWAYS_ADD_TG_ON_THE_FLY = 1  # 1 => disables radical calcellation by taut-charge movement
IGNORE_SINGLE_ENDPOINTS = 1  # 1 => see FindAccessibleEndPoints() in INChITaut.c

#recently added -- begin
INCL_NON_SALT_CANDIDATATES = 1  # 1=> allow H and (-) migrate between "acidic" O and
#                                 other possible endpoints
SALT_WITH_PROTONS = 1  # 1=> (new new) include proton migrarion C-SH, =C-OH, NH+
OPPOSITE_CHARGE_IN_CGROUP = 1  # 1=> allow N(-) in (+) c-group, 0=> disallow
MOVE_PPLUS_TO_REMOVE_PROTONS = 0  # 0=> default; 1=> (disabled) add P/P+ charge group during
                                  # 'hard' proton removal
ADD_MOVEABLE_O_PLUS = 1  # 1=> allow charges on O(+) to move
#recently added -- end

DISCONNECT_METALS = 1  # make main layer disconnected
RECONNECT_METALS = 0  # 1=> by default add reconnected layer in case of coord.
#                              compound disconnection
CHECK_METAL_VALENCE = 0  # 1=> disconnect only metals that have abnormal valence
bREUSE_INCHI = 1  # 1=> do not recalulate INChI for components in reconnected
#                          structure that are same as in the connected one
OUTPUT_CONNECTED_METAL_ONLY = 0  # 0=> default; 1 => (debug) create only reconnected or
#                                         initial struct. output
EMBED_REC_METALS_INCHI = 1  # 1=> (default) output Reconnected embedded in Disconnected INChI;
#                                    0=> separate output

bOUTPUT_ONE_STRUCT_TIME = 1  # 1 => output each structure time (non-release only)



# constants and array sizes

INCHI_NUM = 2    # = array size; member indexes:
INCHI_BAS = 0    # 0 => disconnected or normal
INCHI_REC = 1    # 1 => reconnected

TAUT_NUM = 2    # = array size; member indexes:
TAUT_NON = 0    # 0 => normal structure
TAUT_YES = 1    # 1 => tautomeric
TAUT_INI = 2    # 2 => intermediate tautomeric structure
def ALT_TAUT(x):
   return TAUT_YES if x > TAUT_YES else 1-x # was (1-(X))

# INChI output modes
OUT_N1 = 0    # non-tautomeric only
OUT_T1 = 1    # tautomeric if present otherwise non-tautomeric
OUT_NT = 2    # only non-taut representations of tautomeric
OUT_TN = 3    # tautomeric if present otherwise non-tautomeric;
              # separately output non-taut representations of tautomeric if present
OUT_NN = 4    # only non-taut representations: non-taut else tautomeric

# OUT_TN = OUT_T1 + OUT_NT

# torture test 

TEST_RENUMB_ATOMS = 0    # 1 => heavy duty test by multiple renumbering of atoms
TEST_RENUMB_NEIGH = 1    # 1 => randomly permutate neighbors
TEST_RENUMB_SWITCH = 0   # 1 => display & output another (different) picture
TEST_RENUMB_ATOMS_SAVE_LONGEST = 0 # 1 => save the component with largest processing time into the problem file


# stereo

NEW_STEREOCENTER_CHECK = 1    # 1 => add new stereocenter categories (see bCanInpAtomBeAStereoCenter(...))
MIN_SB_RING_SIZE = 8    # do not assume stereo bonds in rings containing 3..MIN_SB_RING_SIZE-1 atoms

REMOVE_KNOWN_NONSTEREO = 1 # 1=> check in advance known stereo to remove parities from non-stereogenic elements
REMOVE_CALC_NONSTEREO = 1 # 1=> check new stereo numberings to remove parities from non-stereogenic elements
PROPAGATE_ILL_DEF_STEREO = 1 # 1=> if at least one of the pair of constitutionally identical (far) neighbors
#                              (of the tested atom) has ill-defined stereo parity and another has any
#                              stereo parity then set the parity of the tested atom to ill-defined value.

ONLY_DOUBLE_BOND_STEREO = 0  # 1=> no alt bond stereo, no taut. bond attachment to stereo bond
                             # 0=> allow other definitions (below) to be active
ONE_BAD_SB_NEIGHBOR = 1  # 1 => allow 1 "bad" bond type neighbor to a stereobond atom. 2004-06-02

# more stereo settings
BREAK_ONE_MORE_SC_TIE = 1   # break one more tie when comparing possible stereocenter neighbors
BREAK_ALSO_NEIGH_TIE = 0   # post 1.12Beta 2004-08-20: if fixed neighbor has equ neighbors, fix the one with smaller canon. rank
BREAK_ALSO_NEIGH_TIE_ROTATE = 1   # post 1.12Beta 2004-09-02: break the second in 2nd psition; 1 works, 0 does not (example:MFCD01085607)

STEREO_CENTER_BONDS_NORM = 1   # set length of the bonds around a stereocenter = 1 before getting the parity
STEREO_CENTER_BOND4_NORM = 0   # set length of the added bond around a stereocenter = 1 before getting the parity
NORMALIZE_INP_COORD = 0   # 0=>keep unchanged, 1 => make atom coordinates integer values, avg bond len=20

# recent stereo
STEREO_WEDGE_ONLY = 1 # 1=> only pointed ends stereo bonds define stereo; 0=> both ends 1.12Beta
CHECK_C2v_S4_SYMM = 0 # post-1.12Beta 1=> check if a stereocenter has C2v or S4 symmetry; 0=>old mode

EQL_H_NUM_TOGETHER = 1 # 1=> output 1-3,5H2 intead of 1-3H2,5H2 (CT_MODE_EQL_H_TOGETHER)
ABC_CT_NUM_CLOSURES = 1 # 1=> in coinnections compressed format output decimal number of closures instead of '-'

# temporary fix
SINGLET_IS_TRIPLET = 1 # 'singlet' means two electrons make a lone pair instead of 2 bonds
#                               its effect on valence is same as the effect of a triplet

# defug: find structures where canonical partition is different from equitable
FIND_CANON_NE_EQUITABLE = 0  # 0=>normal mode */
#                            1=> extract (set EXTR_FLAGS = (EXTR_CANON_NE_EQUITABLE)
#                            set cmd line options: /onlynonTAUT /: /UNCHARGEDACIDS:1 /DISCONSALT:0 /MOVEPOS:0 /DISCONMETAL:0

# Debug: definitions for the extraction of the structures to the problem file

# definition of the flags for structure extraction to the
# problem file (for debugging and non-standard searching)
EXTR_KNOWN_USED_TO_REMOVE_PARITY = 0x000001
EXTR_CALC_USED_TO_REMOVE_PARITY = 0x000002
EXTR_2EQL2CENTER_TO_REMOVE_PARITY = 0x000004
EXTR_HAS_ATOM_WITH_DEFINED_PARITY = 0x000008
EXTR_REMOVE_PARITY_WARNING = 0x000010
EXTR_SALT_WAS_DISCONNECTED = 0x000020
EXTR_SALT_PROTON_MOVED = 0x000040
EXTR_SALT_PROTON_MOVE_ERR_WARN = 0x000080
EXTR_METAL_WAS_DISCONNECTED = 0x000100
EXTR_METAL_WAS_NOT_DISCONNECTED = 0x000200
EXTR_NON_TRIVIAL_STEREO = 0x000400 # (Inv != Abs stereo) && (parities can't be obtained by inverting them)
EXTR_UNUSUAL_VALENCES = 0x000800
EXTR_HAS_METAL_ATOM = 0x001000
EXTR_TEST_TAUT3_SALTS_DONE = 0x002000 # non-oxygen t-points used to discover tautomerism of merged t-groups
EXTR_CANON_NE_EQUITABLE = 0x004000 # find structures where canonical partition is different from equitable
EXTR_HAS_PROTON_PN = 0x008000 # has movable H+ attached to N or P
EXTR_HAS_FEATURE = 0x010000 # found a feature
EXTR_TAUT_TREATMENT_CHARGES = 0x020000 # tautomeric treatment of charges
EXTR_TRANSPOSITION_EXAMPLES = 0x040000 # extract structures that have different mobile-H and fixed-H orders

# define conditions of structure extraction to the problem file
EXTR_MASK = 0 # EXTR_TAUT_TREATMENT_CHARGES*/ /*(EXTR_HAS_FEATURE)*/ /*(EXTR_UNUSUAL_VALENCES | EXTR_HAS_METAL_ATOM)*/ /* 0 to disable 
EXTR_FLAGS = 0 # EXTR_TAUT_TREATMENT_CHARGES*/ /*(EXTR_HAS_FEATURE)*/ /*(EXTR_HAS_PROTON_PN)*/ /*(EXTR_UNUSUAL_VALENCES)*/ /*(EXTR_CANON_NE_EQUITABLE)*/ /*(EXTR_TEST_TAUT3_SALTS_DONE)(EXTR_HAS_METAL_ATOM)*/ /* (EXTR_NON_TRIVIAL_STEREO)*/ /*(EXTR_METAL_WAS_DISCONNECTED)*/ /* (EXTR_REMOVE_PARITY_WARNING)*/ /*(EXTR_HAS_ATOM_WITH_DEFINED_PARITY)


ENTITY_REFS_IN_XML_MESSAGES = 1 # 1=> replace ' " < > & in error/warning messages with xml entity references

# added tautomeric structures

TAUT_TROPOLONE_7 = 1  # 1=> tautomeric 7-member rings ON
TAUT_TROPOLONE_5 = 1  # 1=> taut. similar to tropolone, 5-member ring
TAUT_4PYRIDINOL_RINGS = 1  # 1=> OH-C5H4N rings tautomerism
TAUT_PYRAZOLE_RINGS = 1  # 1=> tautomerizm in pyrazole rings
# limitation on tautomerism detection:
TAUT_IGNORE_EQL_ENDPOINTS = 0  # 0=> even though 2 endpoints belong to same t-group check
#                                them to find more alt bonds (new)
#                                1=> ignore and do not check (old mode)
TAUT_RINGS_ATTACH_CHAIN = 1  # 1=> allow only chain attachments to tautomeric endpoints
#                              (except pyrazole, where is no tautomeric attachment)
#                              0=> allow taut. attachments from same ring system. Default=1

FIND_RING_SYSTEMS = 1  # 1 => find and mark ring systems, blocks, cut-vertices
#                        Needed for 5- and 6-member ring tautomers and in other places

FIND_RINS_SYSTEMS_DISTANCES = 0  # 1 => find ring system and atom distance from terminal
USE_DISTANCES_FOR_RANKING = 0  # 1 => rank ring systems according to distances from terminal

DISPLAY_RING_SYSTEMS = 0  # 1 => for debug only; displays:
#                           "block no"/"ring system no"/"cut-vertex (num. intersecting blocks-1)"
#                           instead of ranks

# consistency

if bRELEASE_VERSION and bOUTPUT_ONE_STRUCT_TIME:
    bOUTPUT_ONE_STRUCT_TIME = 0

# consistency: bRELEASE_VERSION==1 needs FIND_RING_SYSTEMS=1
if bRELEASE_VERSION and FIND_RING_SYSTEMS:
    FIND_RING_SYSTEMS = 1

# consistency: FIND_RINS_SYSTEMS_DISTANCES needs FIND_RING_SYSTEMS
if  not FIND_RING_SYSTEMS:
    if FIND_RINS_SYSTEMS_DISTANCES:
        FIND_RINS_SYSTEMS_DISTANCES = 0

# consistency: USE_DISTANCES_FOR_RANKING and DISPLAY_RING_SYSTEMS need FIND_RINS_SYSTEMS_DISTANCES
if not FIND_RINS_SYSTEMS_DISTANCES:
    if USE_DISTANCES_FOR_RANKING:
        USE_DISTANCES_FOR_RANKING = 0

    if DISPLAY_RING_SYSTEMS:
        DISPLAY_RING_SYSTEMS = 0

if FIND_RING_SYSTEMS and (TAUT_TROPOLONE_7 or TAUT_TROPOLONE_5 or TAUT_4PYRIDINOL_RINGS or TAUT_PYRAZOLE_RINGS):
    TAUT_OTHER = 1
else:
    TAUT_OTHER = 0


APPLY_IMPLICIT_H_DOWN_RULE = 0 # 1=> if 3 non-H atoms around stereocenter are in same plane
#                              then add "down" hydrogen to obtain sterecenter oparity
#                              0=> Implicit H stereo is unknown if all bonds to 3 non-H atoms
#                              are in XY plane
ALLOW_TAUT_ATTACHMENTS_TO_STEREO_BONDS = 1 # 1=> consider bond in an alternating circuit stereogenic
#                                            even though it has adjacent tautomeric atom(s)

IGNORE_TGROUP_WITHOUT_H = 1    # ignore tautomeric groups containing charges only

if DISCONNECT_SALTS:
    REMOVE_TGROUP_CHARGE = 0    # 0: do not remove charge information from tautomeric groups
else:
    REMOVE_TGROUP_CHARGE = 1    # 1: remove charge information from tautomeric groups

if REMOVE_TGROUP_CHARGE:
    INCHI_T_NUM_MOVABLE = 1
else:
    INCHI_T_NUM_MOVABLE = 2

############################################
##   define canonicalization modes here   ##
############################################

USE_AUX_RANKING = 1 # 1=> get auxiliary ranking to accelerate canonicalization of H layers
USE_AUX_RANKING_ALL = 1 # 1=> include all vertices in CellGetMinNode() selection 0=> only vertices with highest ranks

USE_ISO_SORT_KEY_HFIXED = 0 # 0=> normal mode: merge isotopic taut H to isotopic atom sorting key in
#                             taut H-fixed canonicalization;
#                             1=> add one more "string" iso_sort_Hfixed to the canonicalization

############################
##  questionable behavior ##
############################
REL_RAC_STEREO_IGN_1_SC = 0 # 1=> drop from InChI sp3 stereo in components that have a single stereocenter
#                             0=> old-old mode (all such sp3 stereo is in the Identifier)

# internal definitions; see also REQ_MODE_BASIC etc in ichi.h
CMODE_CT = 0x000001
CMODE_ISO = 0x000002
CMODE_ISO_OUT = 0x000004 # obsolete ?
CMODE_STEREO = 0x000008
CMODE_ISO_STEREO = 0x000010
CMODE_TAUT = 0x000020
CMODE_NOEQ_STEREO = 0x000040 # 5-24-2002: do not use stereo equivalence to accelerate
CMODE_REDNDNT_STEREO = 0x000080 # 6-11-2002: do not check for redundant stereo elements
CMODE_NO_ALT_SBONDS = 0x000100 # 6-14-2002: do not assign stereo to alternating bonds
# new 10-10-2003
CMODE_RELATIVE_STEREO = 0x000200    # REL All Relative Stereo
CMODE_RACEMIC_STEREO = 0x000400    # RAC All Racemic Stereo 
CMODE_SC_IGN_ALL_UU = 0x000800    # IAUSC Ignore stereocenters if All Undef/Unknown
CMODE_SB_IGN_ALL_UU = 0x001000    # IAUSC Ignore stereobonds if All Undef/Unknown
# end of 10-10-2003

# external definitions
CANON_MODE_CT = CMODE_CT
CANON_MODE_TAUT = (CMODE_CT|CMODE_TAUT)
CANON_MODE_ISO = (CMODE_CT|CMODE_ISO|CMODE_ISO_OUT)
CANON_MODE_STEREO = (CMODE_CT|CMODE_STEREO)
CANON_MODE_ISO_STEREO = (CMODE_CT|CMODE_ISO|CMODE_ISO_OUT|CMODE_ISO_STEREO)

CANON_MODE_MASK = 0x00FF # used to determine canonicalization mode

# implemented definitions for CT_ATOMID
CT_ATOMID_DONTINCLUDE = 1
CT_ATOMID_IS_INITRANK = 2
CT_ATOMID_IS_CURRANK = 3

##################################
## canonicalization settings  I ##
##################################

CANON_TAUTOMERS = 1  # 1=> process tautomers 
HYDROGENS_IN_INIT_RANKS = 1  # 1=> include num_H in initial ranking 

DOUBLE_BOND_NEIGH_LIST = 0  # 1 => include double bond neighbor in NeighList 2 times 
INCL_NON_6AROM = 1  # 1 => mark all arom. bonds; 0=>mark arom. bonds only in 6-member rings 

CT_SMALLEST = None

CT_NEIGH_SMALLER = None

CT_ATOMID = CT_ATOMID_IS_CURRANK # CT_ATOMID_DONTINCLUDE

CT_NEIGH_INCREASE = None # in CT, neighbors ranks increase

USE_SYMMETRY_TO_ACCELERATE = 1   # 1 => for fast CT canonicalization, to avoid full enumeration 

# dependent definitions due to settings

if CT_SMALLEST is not None:
    CT_GREATER_THAN = ">"
    CT_INITVALUE = "~0"
    BEST_PARITY = 1  # odd
    WORSE_PARITY = 2
else:
    CT_GREATER_THAN = "<"
    CT_INITVALUE = "0"
    BEST_PARITY = 2  # even
    WORSE_PARITY = 1

if CT_NEIGH_SMALLER is not None:
    CT_NEIGH_SMALLER_THAN = "<"
else:
    CT_NEIGH_SMALLER_THAN = ">"

# verify corectness of dependent settings 
if CT_ATOMID is None:
  raise("error  You have to define CT_ATOMID")
else:
    if CT_ATOMID is not None and CT_ATOMID==CT_ATOMID_DONTINCLUDE:
        raise("CT_DELIMITER should be defined if CT_ATOMID is not included")

###################################
## canonicalization settings  II ##
###################################

ALL_ALT_AS_AROMATIC = 1  # 1 => all altrnate bonds (even in cyclooctateraene) treat as aromatic 
                                       #      and set DOUBLE_BOND_NEIGH_LIST = 0 
ANY_ATOM_IN_ALT_CYCLE = 1  # 1=> accept any atom in alternating bond circuit, 0=>only some 

EXCL_ALL_AROM_BOND_PARITY = 0  # 1 => any arom atom cannot belong to stereo bond. 
#                                This has presedence over ADD_6MEMB_AROM_BOND_PARITY=1 
#                                0 => include arom bonds parities according to 
#                                ADD_6MEMB_AROM_BOND_PARITY definition 

if not EXCL_ALL_AROM_BOND_PARITY:
    ADD_6MEMB_AROM_BOND_PARITY = 1  # 1 => all arom bonds are stereo bonds 
#                                            0 => only those arom bonds which do not belong to 
#                                            6-member arom rings are stereo bonds 
else:
    ADD_6MEMB_AROM_BOND_PARITY = 0  # 0 => standard; 1 => meaningless: ignore parities of non-6-member ring alt. bonds 


CML_NUM_AT_IN_ATREF4 = 4
MAX_NUM_STEREO_BONDS = 3
MAX_NUM_STEREO_BOND_NEIGH = 3
MIN_NUM_STEREO_BOND_NEIGH = 2

MAX_NUM_STEREO_ATOM_NEIGH = 4
STEREO_AT_MARK = 8 # > MAX_NUM_STEREO_BONDS

if ONLY_DOUBLE_BOND_STEREO:
    ALLOW_TAUT_ATTACHMENTS_TO_STEREO_BONDS = 0
    EXCL_ALL_AROM_BOND_PARITY = 1
    ADD_6MEMB_AROM_BOND_PARITY  = 0


# dependent definitions due to settings 
if ALL_ALT_AS_AROMATIC and DOUBLE_BOND_NEIGH_LIST:
    DOUBLE_BOND_NEIGH_LIST = 0



DRAW_AROM_TAUT = 1              # 1=> draw distinct aromatic & tautomer bonds, 0=> don't 

########################################################
##       C O M M O N     D E F I N I T I O N S        ##
########################################################


## input bTautFlags flags 
TG_FLAG_TEST_TAUT__ATOMS = 0x00000001   # find regular tautomerism
TG_FLAG_DISCONNECT_SALTS = 0x00000002   # DISCONNECT_SALTS disconnect
TG_FLAG_TEST_TAUT__SALTS = 0x00000004   # DISCONNECT_SALTS if possible find long-range H/(-) taut. on =C-OH, >C=O   
TG_FLAG_MOVE_POS_CHARGES = 0x00000008   # MOVE_CHARGES allow long-range movement of N(+), P(+) charges           
TG_FLAG_TEST_TAUT2_SALTS = 0x00000010   # TEST_REMOVE_S_ATOMS multi-attachement long-range H/(-) taut. on =C-OH, >C=O   
TG_FLAG_ALLOW_NO_NEGTV_O = 0x00000020   # CHARGED_SALTS_ONLY=0 (debug) find long-range H-only tautomerism on =C-OH, >C=O 
TG_FLAG_MERGE_TAUT_SALTS = 0x00000040   # DISCONNECT_SALTS merge all "salt"-t-groups and other =C-OH into one t-group 
                                       
TG_FLAG_ALL_TAUTOMERIC = (TG_FLAG_TEST_TAUT__ATOMS| \
                                         TG_FLAG_TEST_TAUT__SALTS| \
                                         TG_FLAG_TEST_TAUT2_SALTS| \
                                         TG_FLAG_MERGE_TAUT_SALTS)
                                       
TG_FLAG_DISCONNECT_COORD = 0x00000080   # find "coord. centers" and disconnect them 
TG_FLAG_RECONNECT_COORD = 0x00000100   # reconnect disconnected "coord. centers" 
TG_FLAG_CHECK_VALENCE_COORD = 0x00000200   # do not disconnect "coord. centers" with usual valence 
TG_FLAG_MOVE_HPLUS2NEUTR = 0x00000400   # move protons to neutralize 
TG_FLAG_VARIABLE_PROTONS = 0x00000800   # add/remove protons to neutralize 
TG_FLAG_HARD_ADD_REM_PROTONS = 0x00001000   # add/remove protons to neutralize in hard way 
TG_FLAG_POINTED_EDGE_STEREO = 0x00002000   # only pointed edge of stereo bond defines stereo 
if FIX_ADJ_RAD:
    TG_FLAG_FIX_ADJ_RADICALS = 0x00004000   # remove adjacent radical-doubletes, fix valence 

TG_FLAG_PHOSPHINE_STEREO = 0x00008000   # add phosphine sp3 stereo 
TG_FLAG_ARSINE_STEREO = 0x00010000   # add arsine sp3 stereo 
TG_FLAG_H_ALREADY_REMOVED = 0x00020000   # processing structure restored from InChI 
TG_FLAG_FIX_SP3_BUG = 0x00040000   # fix sp3 stereo bug: overlapping 2D stereo bond & coordinate scaling 

TG_FLAG_KETO_ENOL_TAUT = 0x00080000   # turn on keto-enol tautomerism detection 
TG_FLAG_1_5_TAUT = 0x00100000   # turn on 1,5 tautomerism detection 
               

TG_FLAG_FIX_ISO_FIXEDH_BUG = 0x00200000   # fix bug found after v.102b (isotopic H representation) 
TG_FLAG_FIX_TERM_H_CHRG_BUG = 0x00400000   # fix bug found after v.102b (moving H charge in 'remove_terminal_HDT') 
                        
# output bTautFlags flags      
                                       
TG_FLAG_MOVE_HPLUS2NEUTR_DONE = 0x00000001   # protons have been moved to neutralize 
TG_FLAG_TEST_TAUT__ATOMS_DONE = 0x00000002 
TG_FLAG_DISCONNECT_SALTS_DONE = 0x00000004
TG_FLAG_TEST_TAUT__SALTS_DONE = 0x00000008   # multiple H tautomerism 
TG_FLAG_MOVE_POS_CHARGES_DONE = 0x00000010
TG_FLAG_TEST_TAUT2_SALTS_DONE = 0x00000020   # merged t-groups 
TG_FLAG_ALLOW_NO_NEGTV_O_DONE = 0x00000040
TG_FLAG_MERGE_TAUT_SALTS_DONE = 0x00000080   # added non-taut O to taut groups 

TG_FLAG_ALL_SALT_DONE = (TG_FLAG_TEST_TAUT__SALTS_DONE | \
                                        TG_FLAG_TEST_TAUT2_SALTS_DONE | \
                                        TG_FLAG_MERGE_TAUT_SALTS_DONE )

TG_FLAG_DISCONNECT_COORD_DONE = 0x00000100   # found and disconnected "coord. centers" 
TG_FLAG_CHECK_VALENCE_COORD_DONE = 0x00000200   # did not disconnect "coord. centers" with usual valence 
TG_FLAG_MOVE_CHARGE_COORD_DONE = 0x00000400   # changed charge of a disconnected ligand to fit its valence 
TG_FLAG_FIX_ODD_THINGS_DONE = 0x00000800   # fixed drawing ambiguities in fix_odd_things 
TG_FLAG_TEST_TAUT3_SALTS_DONE = 0x00001000   # merged t-groups + non-O taut atoms 
TG_FLAG_FOUND_SALT_CHARGES_DONE = 0x00002000   # not assigned: preprocessing detected possibility of salt-type tautomerism 
TG_FLAG_FOUND_ISOTOPIC_H_DONE = 0x00004000   # preprocessing detected isotopic H on "good" heteroatoms or isotopic H(+) 
TG_FLAG_FOUND_ISOTOPIC_ATOM_DONE = 0x00008000   # preprocessing detected isotopic H on "good" heteroatoms or isotopic H(+) 
if FIX_ADJ_RAD:
    TG_FLAG_FIX_ADJ_RADICALS_DONE = 0x00010000


if READ_INCHI_STRING:
    READ_INCHI_OUTPUT_INCHI = 0x00000001
    READ_INCHI_SPLIT_OUTPUT = 0x00000002
    READ_INCHI_KEEP_BALANCE_P = 0x00000004
    READ_INCHI_TO_STRUCTURE = 0x00000008

INCHI_IOSTREAM_NONE = 0
INCHI_IOSTREAM_STRING = 1
INCHI_IOSTREAM_FILE = 2













