import numpy as np
import tensorflow as tf #from tensorflow.contrib.training
import HParams

def default_hparams():
	retrun HParams(n_vocab=0,n_ctx_1024,n_embed=768,	n_head=12,n_layer=12,)
