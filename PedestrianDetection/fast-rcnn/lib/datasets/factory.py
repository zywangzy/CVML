# --------------------------------------------------------
# Fast R-CNN
# Copyright (c) 2015 Microsoft
# Licensed under The MIT License [see LICENSE for details]
# Written by Ross Girshick
# --------------------------------------------------------

"""Factory method for easily getting imdbs by name."""

__sets = {}

import datasets.caltech
import numpy as np

__sets = {}
imageset = 'INRIATrain'
devkit = '/home/zywang/INRIATrain/DataSet/'#this seems not sure!!
#Perhaps it should be replaced by below:
#devkit = '/home/zywang/DataSet/CaltechTrainFRCNN/'
#But still not sure what is the difference between this and zywang/CaltechTrain/DataSet/

#def _selective_search_IJCV_top_k(split, year, top_k):
#    """Return an imdb that uses the top k proposals from the selective search
#    IJCV code.
#    """
#    imdb = datasets.pascal_voc(split, year)
#    imdb.roidb_handler = imdb.selective_search_IJCV_roidb
#    imdb.config['top_k'] = top_k
#    return imdb

## Set up voc_<year>_<split> using selective search "fast" mode
#for year in ['2007', '2012']:
#    for split in ['train', 'val', 'trainval', 'test']:
#        name = 'voc_{}_{}'.format(year, split)
#        __sets[name] = (lambda split=split, year=year:
#                datasets.pascal_voc(split, year))

# Set up voc_<year>_<split>_top_<k> using selective search "quality" mode
# but only returning the first k boxes
#for top_k in np.arange(1000, 11000, 1000):
#    for year in ['2007', '2012']:
#        for split in ['train', 'val', 'trainval', 'test']:
#            name = 'voc_{}_{}_top_{:d}'.format(year, split, top_k)
#            __sets[name] = (lambda split=split, year=year, top_k=top_k:
#                    _selective_search_IJCV_top_k(split, year, top_k))

def get_imdb(name):
    """Get an imdb (image database) by name."""
    __sets['INRIATrain'] = (lambda imageset = imageset, devkit = devkit:datasets.caltech(imageset, devkit))#not sure if it should be 'CaltechTrain' or 'caltech'
    if not __sets.has_key(name):
        raise KeyError('Unknown dataset: {}'.format(name))
    return __sets[name]()

def list_imdbs():
    """List all registered imdbs."""
    return __sets.keys()
