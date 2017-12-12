import argparse

def str2bool(v):
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')

ap = argparse.ArgumentParser()
ap.add_argument('--lr', type=float, default=0.01)
ap.add_argument('--momentum', type=float, default=0.9)
ap.add_argument('--num_hidden', type=int,default=2)
ap.add_argument('--sizes', type=str,default='100,100')
ap.add_argument('--batch_size', type=int, default=1)
ap.add_argument('--anneal', type=str2bool, default=False)
ap.add_argument('--loss', type=str, default='ce' , choices =['sq','ce'])
ap.add_argument('--activation', type=str, default='tanh',choices=['tanh','sigmoid'])
ap.add_argument('--opt',  type=str, default='adam', choices=['gd', 'momentum', 'nag', 'adam'])
ap.add_argument('--save_dir', type=str)
ap.add_argument('--expt_dir', type=str)
ap.add_argument('--mnist', type=str)



args = vars(ap.parse_args())

if args['batch_size']%5 == 0 or args['batch_size'] == 1 :
	batch_size  = args['batch_size']
else:
	ap.error('valid values are 1 and multiples of 5')

lr = args['lr']
momentum = args['momentum']
num_hidden = args['num_hidden']
sizes  = map(int,args['sizes'].split(','))
opt = args['opt']
loss  = args['loss']
anneal  = args['anneal']
activation = args['activation']
save_dir  = args['save_dir']
expt_dir  = args['expt_dir']
mnist  = args['mnist']

# print lr,momentum,num_hidden,sizes,batch_size,opt,loss,anneal,activation,save_dir,expt_dir,mnist
# if anneal:
# 	print 'anneal--true'