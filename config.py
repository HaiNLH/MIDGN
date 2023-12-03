#!/usr/bin/env python3
# -*- coding: utf-8 -*-
CONFIG = {
    'name': '@4879',
    'path': './data',
    'log': './log',
    'visual': './visual',
    'gpu_id': "0",
    'note': 'some_note',
    'model': 'MIDGN',
<<<<<<< HEAD
    'dataset_name': 'iFashion',
=======
    'dataset_name': 'food',
>>>>>>> parent of 200557f (change)
    'task': 'tune',
    'eval_task': 'test',

    ## optimal hyperparameters
    'lrs': [1e-3],
    'message_dropouts': [0.3],
    'node_dropouts': [0],
    'decays': [1e-7],

    ## hard negative sample and further train
    'sample': 'simple',
    'hard_window': [0.7, 1.0], # top 30%
    'hard_prob': [0.3, 0.3], # probability 0.8
<<<<<<< HEAD
    'conti_train': 'log/iFashion/',
=======
    'conti_train': 'log/food/',
>>>>>>> parent of 200557f (change)

    ## other settings
    'epochs': 150,
    'early': 50,
    'log_interval': 20,
    'test_interval': 5,
    'retry': 1,

    ## test path
<<<<<<< HEAD
    'test':['log/iFashion']
=======
    'test':['log/food']
>>>>>>> parent of 200557f (change)
}

