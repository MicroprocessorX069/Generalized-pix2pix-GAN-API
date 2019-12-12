import argparse

def str2bool(v):
    return v.lower() in ('true')

def get_parameters():

    parser = argparse.ArgumentParser()

    parser.add_argument('--root_dir', type=str, default="")
    parser.add_argument('--output_dir', type=str, default=root_dir+"output/epoch/")
    parser.add_argument('--input_dir', type=str, default=root_dir+"data/augmented/")
    parser.add_argument('--model_dir', type=str, default=root_dir+"model/")
    parser.add_argument('--res_dir', type=str, default=root_dir+"res/")
    parser.add_argument('--report_dir', type=str, default=root_dir+"report/")

    #train setting
    parser.add_argument('--batch_size', type=int, default=1)
    parser.add_argument('--train_split', type=float, default=0.99)
    parser.add_argument('--train_epoch', type=int, default=10000)

    #input
    parser.add_argument('--inp_width', type=int, default=256)
    parser.add_argument('--inp_height', type=int, default=256)
    parser.add_argument('--inp_channels', type=int, default=3)


    # Model hyper-parameters
    parser.add_argument('--ngf', type=int, default=2)
    parser.add_argument('--ndf', type=int, default=2)
    parser.add_argument('--lrG', type=float, default=0.02)
    parser.add_argument('--lrD', type=float, default=0.02)
    parser.add_argument('--beta1', type=float, default=0.5)
    parser.add_argument('--beta2', type=float, default=0.999)
    parser.add_argument('--L1_lambda', type=float, default=1.5)
    
    # # using pretrained
    # parser.add_argument('--pretrained_model', type=int, default=None)

    # # Misc
    # parser.add_argument('--train', type=str2bool, default=True)
    # parser.add_argument('--parallel', type=str2bool, default=False)
    # parser.add_argument('--dataset', type=str, default='cifar', choices=['lsun', 'celeb'])
    # parser.add_argument('--use_tensorboard', type=str2bool, default=False)

    # # Step size
    # parser.add_argument('--log_step', type=int, default=10)
    # parser.add_argument('--sample_step', type=int, default=100)
    # parser.add_argument('--model_save_step', type=float, default=1.0)
    return parser.parse_args()