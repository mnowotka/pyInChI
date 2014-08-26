from struct import Struct

from mode import *
from ichisize import *
from incomdef import *

class AtData(Struct):
     element = None
     maxvalence = None

NUM_CHEM_ELEMENTS = 127 # well above number of known chem. elements


AT_ISO_SORT_KEY_MULT = 32 # up to 32 identical hydrogen isotopes
                          # (similar to T_GROUP_ISOWT_MULT)
                          # changed from 16 9-12-2003

class AT_STEREO_CARB(Struct):
    at_num = None
    parity = None

class AT_STEREO_DBLE(Struct):
    at_num1 = None
    at_num2 = None
    parity = None

class AT_ISOTOPIC(Struct):
    at_num = None
    num_1H = None
    num_D = None
    num_T = None
    iso_atw_diff = None

BYTE_BITS = 8 # number of bits in one byte

BOND_MASK = 0xf # 4 bits
BOND_BITS = 4 # 3 or 4 does not matter; 2 is too small for BOND_TAUTOM
BOND_ADD = (-1 if BOND_BITS==2 else 0) # subtract 1 from bonds stored in CT

class sp_ATOM(Struct):
    elname = None
    neighbor = None # changed to unsigned 2-2-95. D.Ch.
    init_rank = None # also used in remove_terminal_HDT() to save orig. at. number
    orig_at_number = None
    orig_compt_at_numb = None
    # low 3 bits=bond type;
    #   high 5 bits (in case of cut-vertex atom) = an attached part number
    #
    bond_type = None
    el_number = None # periodic table number = charge of the nucleus = number of the protons
    valence = None
    chem_bonds_valence = None # 8-24-00 to treat tautomer centerpoints, etc.
    num_H = None # first not including D, T; add_DT_to_num_H() includes.
    num_iso_H = None # num 1H, 2H(D), 3H(T)
    cFlags = None
    iso_atw_diff = None # abs(iso_atw_diff) < 127 or 31 - ???
    iso_sort_key = None # = num_1H + AT_ISO_SORT_KEY_MULT^1*num_D
                        # + AT_ISO_SORT_KEY_MULT^2*num_T
                        # + AT_ISO_SORT_KEY_MULT^3*iso_atw_diff
    charge = None
    radical = None # 1=>doublet(.), 2=> triplet as singlet (:) ???? why are they same ????
    marked = None
    
    endpoint = None # tautomer analysis. If != 0 then the hydrogens & (-)charge are in the tautomer group.

    #   Pairs stereo_bond_neighbor[] and stereo_bond_neighbor2[], etc
    #   initially refer to non-isotopic and isotopic cases, respectively.
    #   To use same stereo processing code these arrays are swapped when
    #   switching from non-isotopic to isotopic processing and back.
    
    stereo_bond_neighbor = None # Original number of an opposite atom
    stereo_bond_neighbor2 = None #     (stereo bond neighbor) +1;
    stereo_bond_ord = None # Ordering number of a bond/neighbor in the direction to the
    stereo_bond_ord2 = None # stereo bond opposite atom (important for cumulenes);
    stereo_bond_z_prod = None # Relative  atom-neighbors
    stereo_bond_z_prod2 = None # double bond planes orientation;
    stereo_bond_parity = None # parity + MULT_STEREOBOND*chain_length,
    stereo_bond_parity2 = None # where: 
              #
              #   parity (Mask 0x07=BITS_PARITY):
              #  
              #   0   = AB_PARITY_NONE = not a stereo bond
              #   1/2 = AB_PARITY_ODD/EVEN = bond parity defined from initial ranks
              #   3   = AB_PARITY_UNKN = geometry is unknown to the user
              #   4   = AB_PARITY_UNDF = not enough geometry info to find the parity
              #   6   = AB_PARITY_CALC = calculate later from the neighbor ranks; some ot them can be
              #         replaced with AB_PARITY_ODD/EVEN after equivalence ranks have been determined
              #  
              #   length (Mask 0x38=MASK_CUMULENE_LEN, length=stereo_bond_parity[i]/MULT_STEREOBOND):
              #  
              #   0   => double or alternating stereogenic bond
              #   1   => cumulene with 2 double bonds (stereogenic center)
              #   2   => cumulene with 3 double bonds (stereogenic bond)
              #   length <= (MAX_CUMULENE_LEN=2)
              #   bit KNOWN_PARITIES_EQL =  0x40: all pairs of const. equ. atoms are connected by stereo bonds
              #                                  and these bonds have identical parities
              #

    parity = None # -- Mask 0x07=BITS_PARITY: --
                  # 0 = AB_PARITY_NONE => no parity; also parity&0x38 = 0
                  # 1 = AB_PARITY_ODD  => odd parity
                  # 2 = AB_PARITY_EVEN => even parity
                  # 3 = AB_PARITY_UNKN => user marked as unknown parity
                  # 4 = AB_PARITY_UNDF => parity cannot be defined because of symmetry or not well defined geometry
                  
    parity2 = None # parity including parity due to isotopic terminal H
    # bit msks: 0x07 => known parity (1,2,3,4) or AB_PARITY_CALC=6, AB_PARITY_IISO = 6
    #           0x40 => KNOWN_PARITIES_EQL
    stereo_atom_parity = None # similar to stereo_bond_parity[]: known in advance AB_PARITY_* value + KNOWN_PARITIES_EQL bit
    stereo_atom_parity2 = None
    final_parity = None # defined by equivalence ranks
    final_parity2 = None # defined by equivalence ranks, incl. due to terminal isotopic H
    bAmbiguousStereo = None
    bHasStereoOrEquToStereo = None
    bHasStereoOrEquToStereo2 = None
    if FIND_RING_SYSTEMS:
        bCutVertex = None
        nRingSystem = None
        nNumAtInRingSystem = None
        nBlockSystem = None
        if FIND_RINS_SYSTEMS_DISTANCES:
            nDistanceFromTerminal = None
    z_dir = None

BOND_SINGLE = BOND_TYPE_SINGLE  # 1
BOND_DOUBLE = BOND_TYPE_DOUBLE  # 2
BOND_TRIPLE = BOND_TYPE_TRIPLE  # 3
BOND_ALTERN = BOND_TYPE_ALTERN  # 4 single/double

BOND_ALT_123 = 5  # single/double/triple
BOND_ALT_13 = 6  # single/triple
BOND_ALT_23 = 7  # double/triple
BOND_TAUTOM = 8
BOND_ALT12NS = 9
BOND_NUMDIF = 9  # number of different kinds of bonds

BOND_TYPE_MASK = 0x0f

BOND_MARK_ALL = 0xf0 # complement to BOND_TYPE_MASK

BOND_MARK_ALT12 = 0x10
BOND_MARK_ALT123 = 0x20
BOND_MARK_ALT13 = 0x30
BOND_MARK_ALT23 = 0x40
BOND_MARK_ALT12NS = 0x50 # 1 or 2, non-stereo
BOND_MARK_MASK = 0x70

def ACTUAL_ORDER(PBNS, IAT,IBOND, BTYPE):
    return ( PBNS.edge[PBNS.vert[IAT].iedge[IBOND]].flow + BOND_TYPE_SINGLE if (PBNS and PBNS.edge and PBNS.vert and (BTYPE == BOND_ALT_123 or BTYPE == BOND_ALT_13 or BTYPE == BOND_ALT_23)) else BTYPE)


BITS_PARITY = 0x07 # mask to retrieve half-bond parity
MASK_CUMULENE_LEN = 0x38  # mask to retrieve (cumulene chain length - 1)*MULT_STEREOBOND
KNOWN_PARITIES_EQL = 0x40 # parity is same for all pairs of constit. equivalent atoms
MAX_CUMULENE_LEN = 2 # max number of bonds in a cumulene chain - 1

MULT_STEREOBOND = 0x08 # multiplier for cumulene chain length
                       # odd length => chiral, even length => stereogenic bond

def MAKE_BITS_CUMULENE_LEN(X):
    return X * MULT_STEREOBOND

def GET_BITS_CUMULENE_LEN(X):
    return X & MASK_CUMULENE_LEN

def BOND_CHAIN_LEN(X):
    return GET_BITS_CUMULENE_LEN(X) / MULT_STEREOBOND # 0 => double bond, 1 => allene, 2 => cumulene,..

def IS_ALLENE_CHAIN(X):
    return (GET_BITS_CUMULENE_LEN(X) / MULT_STEREOBOND) % 2

## atom or bond parity value definitions ##
AB_PARITY_NONE = 0  # 0 => no parity; also parity&0x38 = 0
AB_PARITY_ODD = 1  # 1 => odd parity
AB_PARITY_EVEN = 2  # 2 => even parity
AB_PARITY_UNKN = 3  # 3 => user marked as unknown parity
AB_PARITY_UNDF = 4  # 4 => parity cannot be defined because of symmetry or not well defined geometry
AB_PARITY_IISO = 5  # 5 => no parity because of identical atoms
AB_PARITY_CALC = 6  # 6 => calculate parity later
AB_PARITY_0D = 8  # 8 => bit signifies 0D case -- not used

AB_INV_PARITY_BITS = (AB_PARITY_ODD ^ AB_PARITY_EVEN)


AB_MAX_KNOWN_PARITY = 4 # precalculated from const. equivalence parities
AB_MIN_KNOWN_PARITY = 1

AB_MAX_PART_DEFINED_PARITY = 3 # 1, 2, 3 => defined parities, uncluding 'unknown'
AB_MIN_PART_DEFINED_PARITY = 1 # min(AB_PARITY_ODD, AB_PARITY_EVEN, AB_PARITY_UNKN)

AB_MAX_WELL_DEFINED_PARITY = 2 # 1, 2 => well defined parities, uncluding 'unknown'
AB_MIN_WELL_DEFINED_PARITY = 1 # min(AB_PARITY_ODD, AB_PARITY_EVEN)

AB_MIN_ILL_DEFINED_PARITY = 3
AB_MAX_ILL_DEFINED_PARITY = 4

AB_MAX_ANY_PARITY = 4
AB_MIN_ANY_PARITY = 1

AMBIGUOUS_STEREO = 1
AMBIGUOUS_STEREO_ATOM = 2
AMBIGUOUS_STEREO_BOND = 4
AMBIGUOUS_STEREO_ATOM_ISO = 8
AMBIGUOUS_STEREO_BOND_ISO = 16
AMBIGUOUS_STEREO_ERROR = 32


MIN_DOT_PROD = 50 # min value of at->stereo_bond_z_prod[i] to define parity

def ATOM_PARITY_VAL(X):
    return X

def ATOM_PARITY_PART_DEF(X):
    return AB_MIN_PART_DEFINED_PARITY <= X and X <= AB_MAX_PART_DEFINED_PARITY

def ATOM_PARITY_ILL_DEF(X):
    return AB_MIN_ILL_DEFINED_PARITY <= X and X <= AB_MAX_ILL_DEFINED_PARITY

def ATOM_PARITY_KNOWN(X):
    return AB_MIN_KNOWN_PARITY <= X and X <= AB_MAX_KNOWN_PARITY

def ATOM_PARITY_WELL_DEF(X):
    return AB_MIN_WELL_DEFINED_PARITY <= X and X <= AB_MAX_WELL_DEFINED_PARITY

def ATOM_PARITY_NOT_UNKN(X):
    return ATOM_PARITY_KNOWN(X) and X != AB_PARITY_UNKN

def PARITY_VAL(X):
    return X & BITS_PARITY

def PARITY_PART_DEF(X):
    return AB_MIN_PART_DEFINED_PARITY <= PARITY_VAL(X) and PARITY_VAL(X) <= AB_MAX_PART_DEFINED_PARITY

def PARITY_ILL_DEF(X):
    return AB_MIN_ILL_DEFINED_PARITY <= PARITY_VAL(X) and PARITY_VAL(X) <= AB_MAX_ILL_DEFINED_PARITY

def PARITY_KNOWN(X):
    return AB_MIN_KNOWN_PARITY <= PARITY_VAL(X) and PARITY_VAL(X) <= AB_MAX_KNOWN_PARITY

def PARITY_WELL_DEF(X):
    return AB_MIN_WELL_DEFINED_PARITY <= PARITY_VAL(X) and PARITY_VAL(X) <= AB_MAX_WELL_DEFINED_PARITY

def PARITY_CALCULATE(X):
    return AB_PARITY_CALC == PARITY_VAL(X)

def BOND_PARITY_PART_DEFINED(X):
    return PARITY_PART_DEF(X) or PARITY_CALCULATE(X)

def BOND_PARITY_PART_KNOWN(X):
    return PARITY_KNOWN(X) or PARITY_CALCULATE(X)

def ALL_BUT_PARITY(X):
    return X & ~BITS_PARITY

ALWAYS_SET_STEREO_PARITY = 0
NO_ISOLATED_NON_6RING_AROM_BOND = 0 # for Yuri
SAVE_6_AROM_CENTERS = 0 # for Yuri



