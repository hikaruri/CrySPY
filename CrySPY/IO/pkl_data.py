'''
Save data in ./data/pkl_data/xxx
'''

import pickle


def load_init_struc():
    with open('./data/pkl_data/init_struc_data.pkl', 'rb') as f:
        init_struc_data = pickle.load(f)
    return init_struc_data


def save_init_struc(init_struc_data):
    with open('./data/pkl_data/init_struc_data.pkl', 'wb') as f:
        pickle.dump(init_struc_data, f)


def load_opt_struc():
    with open('./data/pkl_data/opt_struc_data.pkl', 'rb') as f:
        opt_struc_data = pickle.load(f)
    return opt_struc_data


def save_opt_struc(opt_struc_data):
    with open('./data/pkl_data/opt_struc_data.pkl', 'wb') as f:
        pickle.dump(opt_struc_data, f)


def load_rslt():
    with open('./data/pkl_data/rslt_data.pkl', 'rb') as f:
        rslt_data = pickle.load(f)
    return rslt_data


def save_rslt(rslt_data):
    with open('./data/pkl_data/rslt_data.pkl', 'wb') as f:
        pickle.dump(rslt_data, f)


def load_kpt():
    with open('./data/pkl_data/kpt_data.pkl', 'rb') as f:
        kpt_data = pickle.load(f)
    return kpt_data


def save_kpt(kpt_data):
    with open('./data/pkl_data/kpt_data.pkl', 'wb') as f:
        pickle.dump(kpt_data, f)


def load_energy_step():
    with open('./data/pkl_data/energy_step_data.pkl', 'rb') as f:
        energy_step_data = pickle.load(f)
    return energy_step_data


def save_energy_step(energy_step_data):
    with open('./data/pkl_data/energy_step_data.pkl', 'wb') as f:
        pickle.dump(energy_step_data, f)


def load_struc_step():
    with open('./data/pkl_data/struc_step_data.pkl', 'rb') as f:
        struc_step_data = pickle.load(f)
    return struc_step_data


def save_struc_step(struc_step_data):
    with open('./data/pkl_data/struc_step_data.pkl', 'wb') as f:
        pickle.dump(struc_step_data, f)


def load_fs_step():
    with open('./data/pkl_data/fs_step_data.pkl', 'rb') as f:
        fs_step_data = pickle.load(f)
    return fs_step_data


def save_fs_step(fs_step_data):
    with open('./data/pkl_data/fs_step_data.pkl', 'wb') as f:
        pickle.dump(fs_step_data, f)


def load_rs_id():
    with open('./data/pkl_data/RS_id_data.pkl', 'rb') as f:
        rs_id_data = pickle.load(f)
    return rs_id_data


def save_rs_id(rs_id_data):
    with open('./data/pkl_data/RS_id_data.pkl', 'wb') as f:
        pickle.dump(rs_id_data, f)


def load_bo_id():
    with open('./data/pkl_data/BO_id_data.pkl', 'rb') as f:
        bo_id_data = pickle.load(f)
    return bo_id_data


def save_bo_id(bo_id_data):
    with open('./data/pkl_data/BO_id_data.pkl', 'wb') as f:
        pickle.dump(bo_id_data, f)


def load_bo_data():
    with open('./data/pkl_data/BO_data.pkl', 'rb') as f:
        bo_data = pickle.load(f)
    return bo_data


def save_bo_data(bo_data):
    with open('./data/pkl_data/BO_data.pkl', 'wb') as f:
        pickle.dump(bo_data, f)


def load_laqa_id():
    with open('./data/pkl_data/LAQA_id_data.pkl', 'rb') as f:
        laqa_id_data = pickle.load(f)
    return laqa_id_data


def save_laqa_id(laqa_id_data):
    with open('./data/pkl_data/LAQA_id_data.pkl', 'wb') as f:
        pickle.dump(laqa_id_data, f)


def load_laqa_data():
    with open('./data/pkl_data/LAQA_data.pkl', 'rb') as f:
        laqa_data = pickle.load(f)
    return laqa_data


def save_laqa_data(laqa_data):
    with open('./data/pkl_data/LAQA_data.pkl', 'wb') as f:
        pickle.dump(laqa_data, f)


def load_ea_id():
    with open('./data/pkl_data/EA_id_data.pkl', 'rb') as f:
        ea_id_data = pickle.load(f)
    return ea_id_data


def save_ea_id(ea_id_data):
    with open('./data/pkl_data/EA_id_data.pkl', 'wb') as f:
        pickle.dump(ea_id_data, f)


def load_ea_data():
    with open('./data/pkl_data/EA_data.pkl', 'rb') as f:
        ea_data = pickle.load(f)
    return ea_data


def save_ea_data(ea_data):
    with open('./data/pkl_data/EA_data.pkl', 'wb') as f:
        pickle.dump(ea_data, f)
