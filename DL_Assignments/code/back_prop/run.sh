python backpropagation.py --lr 0.01 --momentum 0.9 --num_hidden 2 --sizes 500,500\
						  --activation sigmoid --loss sq --opt nag --batch_size 50\
						  --anneal false --save_dir /home/satti/Documents/Projects/Acads/DL_Assignments/code/back_prop/weights\
						  --expt_dir /home/satti/Documents/Projects/Acads/DL_Assignments/code/back_prop/log_files\
						  --mnist /home/satti/Documents/Projects/Acads/DL_Assignments/data/mnist.pkl.gz


# python backpropagation.py --lr 0.01 --momentum 0 --num_hidden 2 --sizes 500,500\
# 						  --activation sigmoid --loss sq --opt gd --batch_size 50\
# 						  --anneal true --save_dir /home/satti/Documents/Projects/Acads/DL_Assignments/code/back_prop/weights\
# 						  --expt_dir /home/satti/Documents/Projects/Acads/DL_Assignments/code/back_prop/log_files\
# 						  --mnist /home/satti/Documents/Projects/Acads/DL_Assignments/data/mnist.pkl.gz