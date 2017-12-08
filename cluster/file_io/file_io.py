
import superEEG as se
import numpy as np
from superEEG._helpers.stats import tal2mni
import glob
import sys
import os
from config import config

try:
    os.stat(config['resultsdir'])
except:
    os.makedirs(config['resultsdir'])

def npz2bo(infile):
    with open(infile, 'rb') as handle:
        f = np.load(handle)
        data = f['Y']
        sample_rate = f['samplerate']
        sessions = f['fname_labels']
        locs = tal2mni(f['R'])

    return se.Brain(data=data, locs=locs, sessions=sessions, sample_rate=sample_rate)

results_dir = config['resultsdir']

data_dir = config['datadir']

fname = sys.argv[1]

file_name = os.path.basename(os.path.splitext(fname)[0])
bo = npz2bo(fname)
bo.save(filepath=os.path.join(results_dir, file_name))


print('done')

# model_data = []
# bo_files = glob.glob(os.path.join('/Users/lucyowen/Desktop/analysis/bo','*.bo'))
# # bo_files = glob.glob(os.path.join('/idata/cdl/data/ECoG/pyFR/data/bo','*.bo'))
# # for i, b in enumerate(bo_files):
# #     if i < 2:
# #         bo = se.load(b)
# #         model_data.append(se.Brain(data=bo.data, locs=bo.locs))
# #     elif i == 2:
# #         bo = se.load(b)
# #         model_data.append(se.Brain(data=bo.data, locs=bo.locs))
# #         model = se.Model(data=model_data)
# #     else:
# #         bo = se.load(b)
# #         model = model.update(bo)
#
# model = se.Model([se.load(b) for b in bo_files[:2]])
# for b in bo_files[2:]:
#     model = model.update(se.load(b))
#
# #model = se.Model(data=model_data)
#
# print(model.n_subs)
#
# model.save(filepath=os.path.join('/Users/lucyowen/Desktop/analysis/ave_model/pyFR_20mm'))
# # model.save(filepath=os.path.join('/dartfs-hpc/scratch/lowen/ave_model/pyFR_20mm'))