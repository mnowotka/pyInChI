# common definitions -- do not change

from ichisize import *

# SDF treatment */
MAX_SDF_HEADER = 64 # max length of the SDFile data header
MAX_SDF_VALUE = 255 # max lenght of the SDFile data value

# size resrictions 
ATOM_EL_LEN = 6  # length of atom name string including zero termination 
ATOM_INFO_LEN = 36 # inf_ATOM output string ^123Al^+2H12..(+)/999/999/999/999: 32 chars 
MAXVAL = 20 # max number of bonds per atom 
MAX_STEREO_BONDS = 3  # max number of stereogenic bonds per atom 
NUM_H_ISOTOPES = 3  # number of hydrogen isotopes: protium, deuterium, tritium 
ATW_H = 1  # hydrogen atomic weight 

# input bond type definition 
MIN_INPUT_BOND_TYPE  = 1
MAX_INPUT_BOND_TYPE  = 4

BOND_TYPE_SINGLE = 1
BOND_TYPE_DOUBLE = 2
BOND_TYPE_TRIPLE = 3
BOND_TYPE_ALTERN = 4

STEREO_SNGL_UP = 1
STEREO_SNGL_EITHER = 4
STEREO_SNGL_DOWN = 6
STEREO_DBLE_EITHER = 3

# MOlfile
INPUT_STEREO_SNGL_UP = 1
INPUT_STEREO_SNGL_EITHER = 4
INPUT_STEREO_SNGL_DOWN = 6
INPUT_STEREO_DBLE_EITHER = 3

BOND_MARK_PARITY = 0x30
BOND_MARK_HIGHLIGHT = 0x40  # highlight equivalent components

BOND_MARK_ODD = '-'
BOND_MARK_EVEN = '+'
BOND_MARK_UNDF = '?'
BOND_MARK_UNKN = 'u'
BOND_MARK_ERR = '*'

SALT_DONOR_H = 1
SALT_DONOR_Neg = 2
SALT_ACCEPTOR = 4
SALT_p_DONOR = 8  # >C-SH
SALT_p_ACCEPTOR = 16  # >C-S(-)
SALT_DONOR_ALL = (SALT_DONOR_Neg | SALT_DONOR_H | SALT_p_ACCEPTOR | SALT_p_DONOR)
SALT_DONOR_Neg2 = (SALT_DONOR_Neg | SALT_p_ACCEPTOR)
SALT_DONOR_H2 = (SALT_DONOR_H   | SALT_p_DONOR)
SALT_DONOR = (SALT_DONOR_Neg | SALT_DONOR_H)

SALT_SELECTED = 32

# radical definitions
RADICAL_SINGLET = 1
RADICAL_DOUBLET = 2
RADICAL_TRIPLET = 3

# metal definition 
METAL = 1          # definition of an element: lowest valence 
METAL2 = 3          # definition of an element: lowest and next to it valence 
IS_METAL = 3          # metal bitmap 
# isotopic shift
ZERO_ATW_DIFF = 127   # mark mass of the most abundant isotope 

# other types
STR_ERR_LEN = 256
