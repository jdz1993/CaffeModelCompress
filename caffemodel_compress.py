import os 
import sys

import caffe 
import numpy as np
from math import ceil
#from quantz_kit.weights_quantization import weights_quantization
sys.path.append("./quantz_kit")
import weights_quantization as wqtz
import time

def caffe_model_compress_maxmin(model, weights, storefile, convbit=6, fcbit=2, use_savez_compressed=True):
	net = caffe.Net(model, caffe.TEST);
	net.copy_from(weights);

	xdict = dict()
	#version 1 ; bits of conv layer and bits of full-connected layer
	xdict['compz_info'] = (1, int(convbit), int(fcbit))
	
	for item in net.params.items():
		name, layer = item
		print "compressing layer", name
		
		weights = net.params[name][0].data
		bais    = net.params[name][1].data

		weights_vec = weights.flatten().astype(np.float32)
		vec_length = weights_vec.size
		newweights_vec=np.empty(vec_length,dtype=np.uint8)
		scale=np.empty(2,dtype=np.float32)

		Option = 1
		if Option == 1:
			nSeg=256
		elif Option == 2:
			if "fc" in name:
				nSeg = 4
			elif "conv" in name:
				nSeg = 64

		wqtz.quantize_buffer_maxmin(weights_vec,newweights_vec,vec_length,nSeg,scale)

		print "new weight size:\t",newweights_vec.size

		xdict[name+'_newweights'] = newweights_vec
		xdict[name+'_bias'] = bais
		xdict[name+'_scale']=scale
		#print "python scale",scale
	use_savez_compressed=False
	if (use_savez_compressed):
		np.savez_compressed(storefile, **xdict)
	else:
		np.savez(storefile, **xdict)


def caffe_model_decompress_maxmin(model, weights, loadfile):
	net = caffe.Net(model, caffe.TEST);
	cmpr_model = np.load(loadfile)
	
	print cmpr_model.files
	
	version, convbit, fcbit = cmpr_model['compz_info']
	
	assert(version == 1), "compz version not support"
	
	
	for item in net.params.items():
		name, layer = item
		#newlabels = cmpr_model[name+'_weight_labels']
		#codebook = cmpr_model[name+'_weight_codebook']
		newweights = cmpr_model[name+'_newweights']
		scale=cmpr_model[name+'_scale']
		origin_size = net.params[name][0].data.flatten().size
		calcu_weights=np.empty(origin_size, dtype=np.float32)

		nSeg=1024
		#if "fc" in name:
		#	nSeg = 4
		#elif "conv" in name:
		#	nSeg = 64

		wqtz.dequantize_buffer_maxmin(newweights,calcu_weights,origin_size,nSeg,scale)

		calcu_weights_shape=calcu_weights.reshape(net.params[name][0].data.shape)
		net.params[name][0].data[...] = calcu_weights_shape
		newbias = cmpr_model[name+'_bias']
		net.params[name][1].data[...] = newbias[...]
	net.save(weights)

def caffe_model_compress_int8(model, weights, storefile, convbit=6, fcbit=2, use_savez_compressed=True):
	net = caffe.Net(model, caffe.TEST);
	net.copy_from(weights);

	xdict = dict()
	#version 1 ; bits of conv layer and bits of full-connected layer
	xdict['compz_info'] = (1, int(convbit), int(fcbit))
	
	for item in net.params.items():
		name, layer = item
		print "compressing layer", name
		
		#compress weights
		weights = net.params[name][0].data
		#don't compress bais
		
		para_len=len(net.params[name])
		if para_len >=2:
			bais    = net.params[name][1].data
		if para_len>=3:
			third = net.params[name][2].data

		#bits for conv and full-connected layer.
		if "fc" in name:
			nbit = int(fcbit)
		elif "conv" in name:
			nbit = int(convbit)

		weights_vec = weights.flatten().astype(np.float32)
		vec_length = weights_vec.size
		print "vec_length",vec_length
		newweights_vec=np.empty(vec_length,dtype=np.int8)
		scale=np.empty(1,dtype=np.int)
		wqtz.quantize_buffer(weights_vec,newweights_vec,vec_length,scale)

		#print "vec_length",vec_length
		#nelem = 32 / nbit
		#newlabel = np.empty(((vec_length+nelem-1)/nelem),dtype=np.int32) 
		#codebook_INT = np.empty((2**nbit),dtype=np.int8)
		#codebook = np.empty((2**nbit),dtype=np.float32)

		#t_start = time.time()
		#wqtz.compress_layer_weights(newlabel, codebook_INT, weights_vec, vec_length, nbit)
		#t_stop = time.time()
		#kmeans_time = kmeans_time + t_stop - t_start
				
		#xdict[name+'_weight_labels'] = newlabel
		#xdict[name+'_weight_codebook'] = codebook
		xdict[name+'_newweights'] = newweights_vec
		if para_len>=2:
			xdict[name+'_bias'] = bais
		xdict[name+'_scale']=scale
		if para_len>=3:
			xdict[name+'_third']=net.params[name][2].data
		print "python scale",scale

	#keep result into output file
	use_savez_compressed = False
	if (use_savez_compressed):
		np.savez_compressed(storefile, **xdict)
	else:
		np.savez(storefile, **xdict)


def caffe_model_decompress_int8(model, weights, loadfile):
	net = caffe.Net(model, caffe.TEST);
	cmpr_model = np.load(loadfile)
	
	print cmpr_model.files
	
	version, convbit, fcbit = cmpr_model['compz_info']
	
	assert(version == 1), "compz version not support"
	
	
	for item in net.params.items():
		name, layer = item
		#newlabels = cmpr_model[name+'_weight_labels']
		#codebook = cmpr_model[name+'_weight_codebook']
		newweights = cmpr_model[name+'_newweights']
		scale=cmpr_model[name+'_scale']
		origin_size = net.params[name][0].data.flatten().size
		calcu_weights=np.empty(origin_size, dtype=np.float32)
		wqtz.dequantize_buffer(newweights,calcu_weights,origin_size,scale)

		#origin_size = net.params[name][0].data.flatten().size
		#weights_vec = np.empty(origin_size, dtype=np.float32)
		#vec_length = weights_vec.size
		
		#need have a way to get bits for fc and conv
		if "fc" in name:
			nbit = fcbit
		elif "conv" in name:
			nbit = convbit

		#wqtz.decompress_layer_weights(weights_vec, newlabels, codebook, vec_length, nbit)
		#newweights = weights_vec.reshape(net.params[name][0].data.shape)
		#net.params[name][0].data[...] = newweights
		calcu_weights_shape=calcu_weights.reshape(net.params[name][0].data.shape)
		net.params[name][0].data[...] = calcu_weights_shape
		if "res" not in name:
			newbias = cmpr_model[name+'_bias']
			net.params[name][1].data[...] = newbias[...]
		if "bn" in name:
			net.params[name][2].data[...] = cmpr_model[name+'_third']
	net.save(weights)

def caffe_model_compress(model, weights, storefile, convbit=6, fcbit=2, use_savez_compressed=True):
	net = caffe.Net(model, caffe.TEST);
	net.copy_from(weights);

	xdict = dict()
	#version 1 ; bits of conv layer and bits of full-connected layer
	xdict['compz_info'] = (1, int(convbit), int(fcbit))

	bais_all=0
	weights_all=0
	weights_fc=0
	weights_conv=0
	
	codebook_all=0
	newlabel_all=0
	newlabel_fc=0
	newlabel_conv=0
	
	for item in net.params.items():
		name, layer = item
		#if len(net.params[name])==2 and "scale" in name:
		#	print "true"
		#elif len(net.params[name])!=2 and "scale" not in name:
		#	print "true"
		#else:
		#	print "false"
		print "compressing layer", name, "len:",len(net.params[name])

	#	if "res" in name and "_branch" in name:
	#		continue		
	#	if "res2a_branch" in name:
	#		continue
	#	if "res2b_branch" in name:
	#		continue
	#	if "res2c_branch" in name:
	#		continue
		
		#compress weights
		weights = net.params[name][0].data
		print "weights size:",weights.flatten().astype(np.float32).size

		
		#print "type of weights:",type(weights)
		#print "type of net params:",type(net.params[name]),dir(net.params[name]),len(net.params[name])
	
		#don't compress bais
		if "res" not in name:
			bais    = net.params[name][1].data

		if "bn" in name:
			third = net.params[name][2].data		

		#bits for conv and full-connected layer.
		nbit=6
		if "fc" in name:
			nbit = int(fcbit)
			weights_fc = weights_fc + weights.flatten().astype(np.float32).size
		elif "conv" in name:
			nbit = int(convbit)
			weights_conv = weights_conv + weights.flatten().astype(np.float32).size
		elif "res" in name:
			nbit=int(convbit)
			

		#print "bais size:",bais.flatten().astype(np.float32).size
		bais_all = bais_all + bais.flatten().astype(np.float32).size
		#print "weights size:",weights.flatten().astype(np.float32).size
		weights_all = weights_all + weights.flatten().astype(np.float32).size

		weights_vec = weights.flatten().astype(np.float32)
		vec_length = weights_vec.size
		#print "vec_length",vec_length
		nelem = 32 / nbit
		newlabel = np.empty(((vec_length+nelem-1)/nelem),dtype=np.int32) 
		
		if "fc" in name:
			newlabel_fc = newlabel_fc + newlabel.size
		elif "conv" in name:
			newlabel_conv = newlabel_conv + newlabel.size
		newlabel_all = newlabel_all + newlabel.size


		#codebook_INT = np.empty((2**nbit),dtype=np.int8)
		codebook = np.empty((2**nbit),dtype=np.float32)

		codebook_all = codebook_all + codebook.size

		#t_start = time.time()
		#if "bn" not in name or "scale" not in name:
		#if "_" not in name:
		if "res" in name:
			wqtz.compress_layer_weights(newlabel, codebook, weights_vec, vec_length, nbit)
		else:
			xdict[name+'_bnweights']=net.params[name][0].data
		#t_stop = time.time()
		#kmeans_time = kmeans_time + t_stop - t_start
				
		xdict[name+'_weight_labels'] = newlabel
		xdict[name+'_weight_codebook'] = codebook
		xdict[name+'_bias'] = bais
		if "bn" in name:
			xdict[name+'_third']=third

#	print "calculation is done."
#
#	print "bais_all:",bais_all*4
#	print "weights_all:",weights_all*4
#	print "weights_fc:",weights_fc*4
#	print "weights_conv:",weights_conv*4
#
#	print "codebook_all:",codebook_all*4
#	print "newlabel_all:",newlabel_all*4
#	print "newlabel_fc:",newlabel_fc*4
#	print "newlabel_conv:",newlabel_conv*4

	use_savez_compressed=False
	#keep result into output file
	if (use_savez_compressed):
		np.savez_compressed(storefile, **xdict)
	else:
		np.savez(storefile, **xdict)
	print "store is done."

	
def caffe_model_decompress(model, weights, loadfile):
	net = caffe.Net(model, caffe.TEST);
	cmpr_model = np.load(loadfile)
	
	print cmpr_model.files
	
	version, convbit, fcbit = cmpr_model['compz_info']
	
	assert(version == 1), "compz version not support"
	
	
	for item in net.params.items():
		name, layer = item
		newlabels = cmpr_model[name+'_weight_labels']
		codebook = cmpr_model[name+'_weight_codebook']

		origin_size = net.params[name][0].data.flatten().size
		weights_vec = np.empty(origin_size, dtype=np.float32)
		vec_length = weights_vec.size
		
		#need have a way to get bits for fc and conv
		nbit=6
		if "fc" in name:
			nbit = fcbit
		elif "conv" in name:
			nbit = convbit
		elif "res" in name:
			nbit=convbit

		#if "bn" not in name or "scale" not in name:
		#if "_" not in name:
		if "res" in name:
			wqtz.decompress_layer_weights(weights_vec, newlabels, codebook, vec_length, nbit)
			newweights = weights_vec.reshape(net.params[name][0].data.shape)
		else:
			newweights = cmpr_model[name+'_bnweights']
		net.params[name][0].data[...] = newweights

		if "res" not in name:
			newbias = cmpr_model[name+'_bias']
			net.params[name][1].data[...] = newbias[...]
		if "bn" in name:
			net.params[name][2].data[...]=cmpr_model[name+'_third']
	net.save(weights)

def compress_alex(convbit=6, fcbit=2):
	LENET_PATH = "/home/eikan/dezhi/caffe/models/bvlc_alexnet"

	netmodel   = os.path.join(LENET_PATH, "train_val.prototxt")
	netweights = os.path.join(LENET_PATH, "bvlc_alexnet.caffemodel")
	output = os.path.join(LENET_PATH,"alexnetzip.npz")


	new_weights=os.path.join(LENET_PATH,"alexnet_xx.caffemodel")

	Option = 1
	if Option == 1:
		caffe_model_compress(netmodel, netweights, output, convbit, fcbit)
		#caffe_model_compress(netmodel, netweights, output, 8, 8)
		print "it seems that compress has finished"
		caffe_model_decompress(netmodel, new_weights, output)
	elif Option == 2:
		caffe_model_compress_int8(netmodel, netweights, output, convbit, fcbit)
		caffe_model_decompress_int8(netmodel, new_weights, output)
	elif Option == 3:
		caffe_model_compress_maxmin(netmodel, netweights, output, convbit, fcbit)
		caffe_model_decompress_maxmin(netmodel, new_weights, output)
	
	print "Done"


def compress_vgg_16(convbit=6, fcbit=2):
	LENET_PATH = "/home/eikan/dezhi/caffe/models/default_vgg_16"

	netmodel   = os.path.join(LENET_PATH, "train_val.prototxt")
	netweights = os.path.join(LENET_PATH, "VGG_ILSVRC_16_layers.caffemodel")
	output = os.path.join(LENET_PATH,"vgg16zip.npz")


	new_weights=os.path.join(LENET_PATH,"vgg16_xx.caffemodel")

	Option = 1
	if Option == 1:
		caffe_model_compress(netmodel, netweights, output, convbit, fcbit)
		#caffe_model_compress(netmodel, netweights, output, 8, 8)
		print "it seems that compress has finished"
		caffe_model_decompress(netmodel, new_weights, output)
	elif Option == 2:
		caffe_model_compress_int8(netmodel, netweights, output, convbit, fcbit)
		caffe_model_decompress_int8(netmodel, new_weights, output)
	elif Option == 3:
		caffe_model_compress_maxmin(netmodel, netweights, output, convbit, fcbit)
		caffe_model_decompress_maxmin(netmodel, new_weights, output)
	
	print "Done"


def compress_vgg_19(convbit=6, fcbit=2):
	LENET_PATH = "/home/eikan/dezhi/caffe/models/vgg_19"

	netmodel   = os.path.join(LENET_PATH, "vgg19_real.prototxt")
	netweights = os.path.join(LENET_PATH, "vgg_19.caffemodel")
	output = os.path.join(LENET_PATH,"vgg19zip.npz")


	new_weights=os.path.join(LENET_PATH,"vgg19_xx.caffemodel")

	Option = 1
	if Option == 1:
		caffe_model_compress(netmodel, netweights, output, convbit, fcbit)
		#caffe_model_compress(netmodel, netweights, output, 8, 8)
		print "it seems that compress has finished"
		caffe_model_decompress(netmodel, new_weights, output)
	elif Option == 2:
		caffe_model_compress_int8(netmodel, netweights, output, convbit, fcbit)
		caffe_model_decompress_int8(netmodel, new_weights, output)
	elif Option == 3:
		caffe_model_compress_maxmin(netmodel, netweights, output, convbit, fcbit)
		caffe_model_decompress_maxmin(netmodel, new_weights, output)
	
	print "Done"

def compress_resnet50(convbit=6, fcbit=2):
        LENET_PATH = "/home/eikan/dezhi/caffe/models/ResNet-50"

        netmodel   = os.path.join(LENET_PATH, "resnet50.prototxt")
        netweights = os.path.join(LENET_PATH, "ResNet-50-model.caffemodel")
        output = os.path.join(LENET_PATH,"resnet50zip.npz")


        new_weights=os.path.join(LENET_PATH,"resnet50_xx.caffemodel")
	print "output:",output
	print "new_weights:",new_weights

        Option = 2
        if Option == 1:
                caffe_model_compress(netmodel, netweights, output, convbit, fcbit)
                #caffe_model_compress(netmodel, netweights, output, 8, 8)
                print "it seems that compress has finished"
                caffe_model_decompress(netmodel, new_weights, output)
        elif Option == 2:
                caffe_model_compress_int8(netmodel, netweights, output, convbit, fcbit)
                caffe_model_decompress_int8(netmodel, new_weights, output)
        elif Option == 3:
                caffe_model_compress_maxmin(netmodel, netweights, output, convbit, fcbit)
                caffe_model_decompress_maxmin(netmodel, new_weights, output)

        print "Done"

def main(argv):
	if len(argv)==2:
		compress_vgg_16(argv[0],argv[1])
	elif len(argv)==3:
		if argv[0]=="alex":
			compress_alex(argv[1],argv[2])
		elif argv[0]=="vgg16":
			compress_vgg_16(argv[1],argv[2])
		elif argv[0]=="vgg19":
			compress_vgg_19(argv[1],argv[2])
		elif argv[0]=="resnet50":
			compress_resnet50(argv[1],argv[2])
		
	else:
		compress_vgg_16()

if __name__ == "__main__":
	
	main(sys.argv[1:])

#if __name__ == "__main__":
#	
#	LENET_PATH = "/home/intel/Downloads/caffe/examples/mnist"
#
#	netmodel   = os.path.join(LENET_PATH, "lenet_train_test.prototxt")
#	netweights = os.path.join(LENET_PATH, "lenet_iter_10000.caffemodel")
#	output = os.path.join(LENET_PATH,"lenetzip.npz")
#	caffe_model_compress(netmodel, netweights, output, 6, 2)
#
#	new_weights=os.path.join(LENET_PATH,"lenet_xx.caffemodel")
#	caffe_model_decompress(netmodel, new_weights, output)
#	
#	print "Done"
