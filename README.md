# CaffeModelCompress
Compress caffemodel using multiple methods written by Dezhi Jiang.

# Methods Specification
K-means: Alexnet down to 14M.
quantize(float32 to int8): Alexnet down to 41M.

K-Means:
We use 6-bit for Convolution layer weights which means we will use 64 clusters to represent all weights per convolution layer. We use 2-bit for fc layer. So, every convolution layer weight fp number is stored as 6-bit and 32-bit can store 5 ones. To fc layer weight, the number is 16. 

Round down:
We also tried another quantization method(round quantization). Every float point number will be converted to a unint8 number.

# Code Usage
This is a code written by python + cpp.
To Compile cpp code:
        ./build.sh
To just run caffemodel_compress.py:
        python caffemodel_compress.py [FileOption] [ConvBit] [FcBit]
[FileOption]:   alex vgg16 vgg19 resnet50
[ConvBit]:      better be 6
[FcBit]:        better be 2

Example:
        python caffemodel_compress.py resnet50 6 2 2>&1 | tee resulttmp.md
This command compress resnet50.caffemodel using parameter 6 and 2.The caffemodel path is configed in compress_resnet50(convbit=6, fcbit=2) in caffemodel_compress.py.
Some Explanation:
        This code configs origin caffemodel and compressed *zip.npz path in hard code, it compress *.caffemodel to *zip.npz, than decompress *zip.npz to *_xx.caffemodel. Those 3 file paths can be found in
 code.

