python train.py --lr 0.001 --momentum 0.9 --pretrain false --num_hidden 2 --sizes 300,300\
				--activation sigmoid --loss ce --opt adam --batch_size 50 --anneal true\
				--save_dir /home/satti/Documents/Sem8/DL/PA1/code/weights\
				--expt_dir /home/satti/Documents/Sem8/DL/PA1/code/log_files\
				--train /home/satti/Documents/Sem8/DL/PA1/data/train.csv\
				--val /home/satti/Documents/Sem8/DL/PA1/data/val.csv\
				--test /home/satti/Documents/Sem8/DL/PA1/data/test.csv

				# --save_dir /home/ubuntu/PA1/code/weights\
				# --expt_dir /home/ubuntu/PA1/code/log_files\
				# --train /home/ubuntu/PA1/data/train.csv\
				# --val /home/ubuntu/PA1/data/val.csv\
				# --test /home/ubuntu/PA1/data/test.csv