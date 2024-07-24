#No of Params = 7m


out_dir = 'out-New'
eval_interval = 2000
eval_iters = 200
log_interval = 1
vocab_size = 257
always_save_checkpoint = True

dataset = 'openwebtext'
block_size = 1024


size=32 #ffw_
n_embd = 256 #d_model

#

wandb_log = False 
wandb_project = 'training runs'
wandb_run_name = 'ScaleLM'


learning_rate = 6e-4
max_iters = 100

n_layer = 3
n_head = 4
n_embd = 256
device = 'cuda'

weight_decay = 1e-1

compile = False
device = 'cpu'
