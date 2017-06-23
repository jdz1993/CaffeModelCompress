 > experiment_test_result.md

export PYTHONPATH=/home/eikan/dezhi/caffe/python:$PYTHONPATH
export LD_LIBRARY_PATH=/opt/intel/compilers_and_libraries_2016.3.210/linux/mkl/lib/intel64_lin/:$LD_LIBRARY_PATH


for (( i=6;i<7;++i ))
do
	for (( j=2;j<3;++j ))
	do
		echo "" >> experiment_test_result.md
		cd /home/eikan/dezhi/CaffeModelCompress
		echo "Test Round: " $i " " $j >> experiment_test_result.md
		echo "Compressing alexnet"
		python caffemodel_compress.py alex $i $j >/dev/null 2>&1 
		wc -c /home/eikan/dezhi/caffe/models/bvlc_alexnet/alexnetzip.npz >> experiment_test_result.md
		echo "Compressing vgg16"
		python caffemodel_compress.py vgg16 $i $j >/dev/null 2>&1 
		wc -c /home/eikan/dezhi/caffe/models/default_vgg_16/vgg16zip.npz >> experiment_test_result.md
		echo "Compressing vgg19"
		python caffemodel_compress.py vgg19 $i $j >/dev/null 2>&1 
		wc -c /home/eikan/dezhi/caffe/models/vgg_19/vgg19zip.npz >> experiment_test_result.md
		

		cd /home/eikan/dezhi/caffe

		echo "Testing Alexet"
		echo "testing alexnet_default " $i " " $j
		./examples/imagenet/test_alexnet.sh 2> tmptmp.md
		echo "alexnet_default:" >> /home/eikan/dezhi/CaffeModelCompress/experiment_test_result.md
		grep  "] accuracy =" tmptmp.md >> /home/eikan/dezhi/CaffeModelCompress/experiment_test_result.md
		echo "testing alexnet_compressed " $i " " $j
		./examples/imagenet/test_alexnet_compressed.sh 2> tmptmp.md
		echo "alexnet_compressed:" >> /home/eikan/dezhi/CaffeModelCompress/experiment_test_result.md
		grep  "] accuracy =" tmptmp.md >> /home/eikan/dezhi/CaffeModelCompress/experiment_test_result.md

		echo "Testing vgg16"
		echo "testing vgg16_default " $i " " $j
		./examples/imagenet/test_vgg16_default.sh 2> tmptmp.md
		echo "vgg16_default:" >> /home/eikan/dezhi/CaffeModelCompress/experiment_test_result.md
		grep  "] accuracy@1 =" tmptmp.md >> /home/eikan/dezhi/CaffeModelCompress/experiment_test_result.md
		grep  "] accuracy@5 =" tmptmp.md >> /home/eikan/dezhi/CaffeModelCompress/experiment_test_result.md
		echo "testing vgg16_compressed " $i " " $j
		./examples/imagenet/test_vgg16_compressed.sh 2> tmptmp.md
		echo "vgg16_compressed:" >> /home/eikan/dezhi/CaffeModelCompress/experiment_test_result.md
		grep  "] accuracy@1 =" tmptmp.md >> /home/eikan/dezhi/CaffeModelCompress/experiment_test_result.md
		grep  "] accuracy@5 =" tmptmp.md >> /home/eikan/dezhi/CaffeModelCompress/experiment_test_result.md

		echo "Testing Alexet"
		echo "testing vgg19_default " $i " " $j
		./examples/imagenet/test_vgg19_default.sh 2> tmptmp.md
		echo "vgg19_default:" >> /home/eikan/dezhi/CaffeModelCompress/experiment_test_result.md
		grep  "] accuracy@1 =" tmptmp.md >> /home/eikan/dezhi/CaffeModelCompress/experiment_test_result.md
		grep  "] accuracy@5 =" tmptmp.md >> /home/eikan/dezhi/CaffeModelCompress/experiment_test_result.md
		echo "testing vgg19_compressed " $i " " $j
		./examples/imagenet/test_vgg19_compressed.sh 2> tmptmp.md
		echo "vgg19_compressed:" >> /home/eikan/dezhi/CaffeModelCompress/experiment_test_result.md
		grep  "] accuracy@1 =" tmptmp.md >> /home/eikan/dezhi/CaffeModelCompress/experiment_test_result.md
		grep  "] accuracy@5 =" tmptmp.md >> /home/eikan/dezhi/CaffeModelCompress/experiment_test_result.md


	done
done	
