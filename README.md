# CaffeModelCompress
Compress caffemodel using multiple methods.

# Methods Specification
K-means: Alexnet down to 14M.
quantize(float32 to int8): Alexnet down to 41M.

K-Means:
We use 6-bit for Convolution layer weights which means we will use 64 clusters to represent all weights per convolution layer. We use 2-bit for fc layer. So, every convolution layer weight fp number is stored as 6-bit and 32-bit can store 5 ones. To fc layer weight, the number is 16. 

Round down:
We also tried another quantization method(round quantization). Every float point number will be converted to a unint8 number.
