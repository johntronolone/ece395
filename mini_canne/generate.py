import sys
from mini_canne import *
import os
import argparse

mode = OperationMode(train=False,new_init=False,control=True)
synth = ANNeSynth(mode,corpus='lyre_frames.npy')

def get_arguments():
  parser = argparse.ArgumentParser(description='SampleRnn example network')
  parser.add_argument('--LFO_Rate',  	        type=float,   default='50')
  parser.add_argument('--n_frames',  	        type=int,   default='1000')
  return parser.parse_args()


def main():
	args = get_arguments()
	synth.load_weights_into_memory()
	vals = np.random.uniform(low=0.25, high=5, size=(1,9))
	vals[:,8] = 0
	synth.play_synth(vals,n_frames=args.n_frames,LFO=args.LFO_Rate)
	# synth.execute(vals,n_frames=100)
	
	
if __name__ == '__main__':
	main()
