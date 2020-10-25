'''
Utility for structures
'''

import os

import numpy as np
from pymatgen import Structure, Molecule
from pymatgen.io.cif import CifWriter


def out_poscar(struc, cid, fpath):
    # ---------- poscar format
    pos = struc.to(fmt='poscar')
    pos = pos.split('\n')
    blank_indx = pos.index('')    # cut unnecessary parts
    pos = pos[:blank_indx]
    pos[0] = 'ID_{}'.format(cid)    # replace with ID
    lines = [line+'\n' for line in pos]

    # ---------- append POSCAR
    with open(fpath, 'a') as f:
        for line in lines:
            f.write(line)


def out_cif(struc, cid, tmp_path, fpath, symprec=0.1):
    # ---------- opt_CIFS
    cif = CifWriter(struc, symprec=symprec)
    cif.write_file(tmp_path+'tmp.cif')

    # ---------- correct title for VESTA
    #                (need to delete '_chemical_formula_sum')
    with open(tmp_path+'tmp.cif', 'r') as fcif:
        ciflines = fcif.readlines()
    ciflines[1] = 'data_ID_{}\n'.format(cid)
    if ciflines[11][:21] == '_chemical_formula_sum':
        ciflines.pop(11)
    else:
        raise ValueError('ciflines[11] is not _chemical_formula_sum,'
                         ' have to fix bag')

    # ---------- cif --> opt_cifs
    with open(fpath, 'a') as foptcif:
        for line in ciflines:
            foptcif.write(line)

    # ---------- clean tmp.cif
    os.remove(tmp_path+'tmp.cif')


def frac_coord_zero_one(struc_in):
    '''
    fractional coordinates: 0.0 <= x,y,z < 1.0
    e.g. [0.0, -0.25, 0.7] --> [0.0, 0.75, 0.7]

    # ---------- args
    struc_in: structure data in pymatgen format
    '''
    struc = struc_in.copy()
    for i in range(struc.num_sites):
        struc[i] = struc[i].to_unit_cell()
    return struc


def origin_shift(struc_in):
    '''
    Randomly shift the origin of struc_in

    # ---------- args
    struc_in: structure data in pymatgen format

    # ---------- return
    origin shifted structure (not change original struc_in)
    '''
    struc = struc_in.copy()
    coords_trans = struc.frac_coords + np.random.rand(3)
    struc_shift = Structure(struc.lattice, struc.species, coords_trans)
    struc_shift = frac_coord_zero_one(struc_shift)
    return struc_shift


def sort_by_atype(struc, atype):
    '''
    return a structre sorted by atype order as a new structure
    '''
    return struc.get_sorted_structure(
        key=lambda x: atype.index(x.species_string))


def check_distance(struc, atype, mindist, check_all=False):
    '''
    # ---------- args
    struc: structure data in pymatgen format
    atype (list): e.g. ['Li', 'Co, 'O']
    mindist (2d list) : e.g. [[2.0, 2.0, 1.2],
                              [2.0, 2.0, 1.2],
                              [1.2, 1.2, 1.5]]
    check_all (bool) : if True, check all atom pairs, return dist_list.
                       if False, stop when (dist < mindist) is found,
                                 return True or False (see below)
    # ---------- return
    (check_all=False) True: nothing smaller than mindist
    (check_all=False) False: something smaller than mindst
    (check_all=True) dist_list: if dist_list is vacant,
                                    nothing smaller than mindist
    '''

    # ---------- initialize
    if check_all:
        dist_list = []    # [(i, j, dist), (i, j, dist), ...]

    # ---------- in case there is only one atom
    if struc.num_sites == 1:
        dist = min(struc.lattice.abc)
        if dist < mindist[0][0]:
            if check_all:
                dist_list.append((0, 0, dist))
                return dist_list
            return False
        return True

    # ---------- normal case
    for i in range(struc.num_sites):
        for j in range(i):
            dist = struc.get_distance(j, i)
            i_type = atype.index(struc[i].species_string)
            j_type = atype.index(struc[j].species_string)
            if dist < mindist[i_type][j_type]:
                if check_all:
                    dist_list.append((j, i, dist))
                else:
                    return False

    # ---------- return
    if check_all:
        if dist_list:
            dist_list.sort()    # sort
            return dist_list
        else:
            return dist_list    # dist_list is vacant list
    return True


def scale_cell_mol(struc, mol_file, volume):
    '''
    scale cell without changing molecule size
    for molecular structures generated by PyXtal
    '''
    # ---------- get molecules
    molecules = []
    for mf in mol_file:
        mol = Molecule.from_file(mf)
        if len(mol.species) > 1:    # mol.species == 1 <-- atom
            molecules.append(mol.species)

    # ---------- original lattice
    lattice_orig = struc.lattice

    # ---------- structure of molecule
    mols_coords = []
    mols_frac_G = []
    for molecule in molecules:
        struc_element = struc.species
        # ------ start atom for the molecule
        mol_pos = []
        for i, element in enumerate(struc_element):
            # -- check len
            if len(struc_element) < len(molecule) + i:
                break
            # -- check number of atoms
            count = 0
            for j in range(len(molecule)):
                if struc_element[i+j] == molecule[j]:
                    count += 1
            if count == len(molecule):
                mol_pos.append(i)
        # ------ calculate the center of gravity
        cart_coords = struc.cart_coords
        frac_coords = struc.frac_coords
        mol_frac_G = []
        mol_cart = []
        # ------ take periodic boundary into account
        for st in mol_pos:
            frac_mol_coord = frac_coords[st:st+len(molecule)]
            for ele_index in range(len(molecule)):
                frac_dists = frac_mol_coord[ele_index] - frac_mol_coord[0]
                for axis, dist in enumerate(frac_dists):
                    if abs(dist) > 0.5:
                        if frac_mol_coord[0][axis] >= 0.5:
                            frac_coords[st+ele_index][axis] += 1.0
                        elif frac_mol_coord[0][axis] <= 0.5:
                            frac_coords[st+ele_index][axis] -= 1.0
            # -- get the center of gravity
            frac_G = frac_mol_coord.sum(axis=0) / len(molecule)
            mol_frac_G.append(frac_G)
            # -- save structure of mol
            cart_mol_coord = lattice_orig.get_cartesian_coords(frac_mol_coord)
            cart_G = cart_mol_coord.sum(axis=0)/len(molecule)
            cart_mol = cart_mol_coord - cart_G
            mol_cart.append(cart_mol)
        mols_frac_G.append(mol_frac_G)
        mols_coords.append(mol_cart)
        # ------ remove the molecule from struc
        for st in reversed(mol_pos):
            struc.remove_sites(range(st, st+len(molecule)))

    # ---------- scale lattice
    struc.scale_lattice(volume)

    # ---------- lattice for frac2cart
    lattice_new = struc.lattice

    # ---------- put the molecule of original size
    for mol_index in range(len((molecules))):
        for mol_count, frac_G in enumerate(mols_frac_G[mol_index]):
            cart_G = lattice_new.get_cartesian_coords(frac_G)
            cart_mol_coord = mols_coords[mol_index][mol_count] + cart_G
            for mol_spe, spe_coord in zip(molecules[mol_index], cart_mol_coord):
                struc.append(mol_spe, spe_coord, coords_are_cartesian=True)

    # ---------- return new struc
    return struc
