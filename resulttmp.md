WARNING: Logging before InitGoogleLogging() is written to STDERR
I0623 09:45:02.632624  1897 net.cpp:294] The NetState phase (1) differed from the phase (0) specified by a rule in layer data
I0623 09:45:02.633586  1897 net.cpp:51] Initializing net from parameters: 
name: "ResNet-50"
state {
  phase: TEST
  level: 0
}
layer {
  name: "data"
  type: "Data"
  top: "data"
  top: "label"
  include {
    phase: TEST
  }
  transform_param {
    mean_value: 104
    mean_value: 117
    mean_value: 123
  }
  data_param {
    source: "/home/eikan/dezhi/caffe/examples/imagenet/ilsvrc12_val_lmdb"
    batch_size: 8
    crop_size: 224
    backend: LMDB
  }
}
layer {
  name: "conv1"
  type: "Convolution"
  bottom: "data"
  top: "conv1"
  convolution_param {
    num_output: 64
    pad: 3
    kernel_size: 7
    stride: 2
  }
}
layer {
  name: "bn_conv1"
  type: "BatchNorm"
  bottom: "conv1"
  top: "conv1"
  batch_norm_param {
    use_global_stats: true
  }
}
layer {
  name: "scale_conv1"
  type: "Scale"
  bottom: "conv1"
  top: "conv1"
  scale_param {
    bias_term: true
  }
}
layer {
  name: "conv1_relu"
  type: "ReLU"
  bottom: "conv1"
  top: "conv1"
}
layer {
  name: "pool1"
  type: "Pooling"
  bottom: "conv1"
  top: "pool1"
  pooling_param {
    pool: MAX
    kernel_size: 3
    stride: 2
  }
}
layer {
  name: "res2a_branch1"
  type: "Convolution"
  bottom: "pool1"
  top: "res2a_branch1"
  convolution_param {
    num_output: 256
    bias_term: false
    pad: 0
    kernel_size: 1
    stride: 1
  }
}
layer {
  name: "bn2a_branch1"
  type: "BatchNorm"
  bottom: "res2a_branch1"
  top: "res2a_branch1"
  batch_norm_param {
    use_global_stats: true
  }
}
layer {
  name: "scale2a_branch1"
  type: "Scale"
  bottom: "res2a_branch1"
  top: "res2a_branch1"
  scale_param {
    bias_term: true
  }
}
layer {
  name: "res2a_branch2a"
  type: "Convolution"
  bottom: "pool1"
  top: "res2a_branch2a"
  convolution_param {
    num_output: 64
    bias_term: false
    pad: 0
    kernel_size: 1
    stride: 1
  }
}
layer {
  name: "bn2a_branch2a"
  type: "BatchNorm"
  bottom: "res2a_branch2a"
  top: "res2a_branch2a"
  batch_norm_param {
    use_global_stats: true
  }
}
layer {
  name: "scale2a_branch2a"
  type: "Scale"
  bottom: "res2a_branch2a"
  top: "res2a_branch2a"
  scale_param {
    bias_term: true
  }
}
layer {
  name: "res2a_branch2a_relu"
  type: "ReLU"
  bottom: "res2a_branch2a"
  top: "res2a_branch2a"
}
layer {
  name: "res2a_branch2b"
  type: "Convolution"
  bottom: "res2a_branch2a"
  top: "res2a_branch2b"
  convolution_param {
    num_output: 64
    bias_term: false
    pad: 1
    kernel_size: 3
    stride: 1
  }
}
layer {
  name: "bn2a_branch2b"
  type: "BatchNorm"
  bottom: "res2a_branch2b"
  top: "res2a_branch2b"
  batch_norm_param {
    use_global_stats: true
  }
}
layer {
  name: "scale2a_branch2b"
  type: "Scale"
  bottom: "res2a_branch2b"
  top: "res2a_branch2b"
  scale_param {
    bias_term: true
  }
}
layer {
  name: "res2a_branch2b_relu"
  type: "ReLU"
  bottom: "res2a_branch2b"
  top: "res2a_branch2b"
}
layer {
  name: "res2a_branch2c"
  type: "Convolution"
  bottom: "res2a_branch2b"
  top: "res2a_branch2c"
  convolution_param {
    num_output: 256
    bias_term: false
    pad: 0
    kernel_size: 1
    stride: 1
  }
}
layer {
  name: "bn2a_branch2c"
  type: "BatchNorm"
  bottom: "res2a_branch2c"
  top: "res2a_branch2c"
  batch_norm_param {
    use_global_stats: true
  }
}
layer {
  name: "scale2a_branch2c"
  type: "Scale"
  bottom: "res2a_branch2c"
  top: "res2a_branch2c"
  scale_param {
    bias_term: true
  }
}
layer {
  name: "res2a"
  type: "Eltwise"
  bottom: "res2a_branch1"
  bottom: "res2a_branch2c"
  top: "res2a"
}
layer {
  name: "res2a_relu"
  type: "ReLU"
  bottom: "res2a"
  top: "res2a"
}
layer {
  name: "res2b_branch2a"
  type: "Convolution"
  bottom: "res2a"
  top: "res2b_branch2a"
  convolution_param {
    num_output: 64
    bias_term: false
    pad: 0
    kernel_size: 1
    stride: 1
  }
}
layer {
  name: "bn2b_branch2a"
  type: "BatchNorm"
  bottom: "res2b_branch2a"
  top: "res2b_branch2a"
  batch_norm_param {
    use_global_stats: true
  }
}
layer {
  name: "scale2b_branch2a"
  type: "Scale"
  bottom: "res2b_branch2a"
  top: "res2b_branch2a"
  scale_param {
    bias_term: true
  }
}
layer {
  name: "res2b_branch2a_relu"
  type: "ReLU"
  bottom: "res2b_branch2a"
  top: "res2b_branch2a"
}
layer {
  name: "res2b_branch2b"
  type: "Convolution"
  bottom: "res2b_branch2a"
  top: "res2b_branch2b"
  convolution_param {
    num_output: 64
    bias_term: false
    pad: 1
    kernel_size: 3
    stride: 1
  }
}
layer {
  name: "bn2b_branch2b"
  type: "BatchNorm"
  bottom: "res2b_branch2b"
  top: "res2b_branch2b"
  batch_norm_param {
    use_global_stats: true
  }
}
layer {
  name: "scale2b_branch2b"
  type: "Scale"
  bottom: "res2b_branch2b"
  top: "res2b_branch2b"
  scale_param {
    bias_term: true
  }
}
layer {
  name: "res2b_branch2b_relu"
  type: "ReLU"
  bottom: "res2b_branch2b"
  top: "res2b_branch2b"
}
layer {
  name: "res2b_branch2c"
  type: "Convolution"
  bottom: "res2b_branch2b"
  top: "res2b_branch2c"
  convolution_param {
    num_output: 256
    bias_term: false
    pad: 0
    kernel_size: 1
    stride: 1
  }
}
layer {
  name: "bn2b_branch2c"
  type: "BatchNorm"
  bottom: "res2b_branch2c"
  top: "res2b_branch2c"
  batch_norm_param {
    use_global_stats: true
  }
}
layer {
  name: "scale2b_branch2c"
  type: "Scale"
  bottom: "res2b_branch2c"
  top: "res2b_branch2c"
  scale_param {
    bias_term: true
  }
}
layer {
  name: "res2b"
  type: "Eltwise"
  bottom: "res2a"
  bottom: "res2b_branch2c"
  top: "res2b"
}
layer {
  name: "res2b_relu"
  type: "ReLU"
  bottom: "res2b"
  top: "res2b"
}
layer {
  name: "res2c_branch2a"
  type: "Convolution"
  bottom: "res2b"
  top: "res2c_branch2a"
  convolution_param {
    num_output: 64
    bias_term: false
    pad: 0
    kernel_size: 1
    stride: 1
  }
}
layer {
  name: "bn2c_branch2a"
  type: "BatchNorm"
  bottom: "res2c_branch2a"
  top: "res2c_branch2a"
  batch_norm_param {
    use_global_stats: true
  }
}
layer {
  name: "scale2c_branch2a"
  type: "Scale"
  bottom: "res2c_branch2a"
  top: "res2c_branch2a"
  scale_param {
    bias_term: true
  }
}
layer {
  name: "res2c_branch2a_relu"
  type: "ReLU"
  bottom: "res2c_branch2a"
  top: "res2c_branch2a"
}
layer {
  name: "res2c_branch2b"
  type: "Convolution"
  bottom: "res2c_branch2a"
  top: "res2c_branch2b"
  convolution_param {
    num_output: 64
    bias_term: false
    pad: 1
    kernel_size: 3
    stride: 1
  }
}
layer {
  name: "bn2c_branch2b"
  type: "BatchNorm"
  bottom: "res2c_branch2b"
  top: "res2c_branch2b"
  batch_norm_param {
    use_global_stats: true
  }
}
layer {
  name: "scale2c_branch2b"
  type: "Scale"
  bottom: "res2c_branch2b"
  top: "res2c_branch2b"
  scale_param {
    bias_term: true
  }
}
layer {
  name: "res2c_branch2b_relu"
  type: "ReLU"
  bottom: "res2c_branch2b"
  top: "res2c_branch2b"
}
layer {
  name: "res2c_branch2c"
  type: "Convolution"
  bottom: "res2c_branch2b"
  top: "res2c_branch2c"
  convolution_param {
    num_output: 256
    bias_term: false
    pad: 0
    kernel_size: 1
    stride: 1
  }
}
layer {
  name: "bn2c_branch2c"
  type: "BatchNorm"
  bottom: "res2c_branch2c"
  top: "res2c_branch2c"
  batch_norm_param {
    use_global_stats: true
  }
}
layer {
  name: "scale2c_branch2c"
  type: "Scale"
  bottom: "res2c_branch2c"
  top: "res2c_branch2c"
  scale_param {
    bias_term: true
  }
}
layer {
  name: "res2c"
  type: "Eltwise"
  bottom: "res2b"
  bottom: "res2c_branch2c"
  top: "res2c"
}
layer {
  name: "res2c_relu"
  type: "ReLU"
  bottom: "res2c"
  top: "res2c"
}
layer {
  name: "res3a_branch1"
  type: "Convolution"
  bottom: "res2c"
  top: "res3a_branch1"
  convolution_param {
    num_output: 512
    bias_term: false
    pad: 0
    kernel_size: 1
    stride: 2
  }
}
layer {
  name: "bn3a_branch1"
  type: "BatchNorm"
  bottom: "res3a_branch1"
  top: "res3a_branch1"
  batch_norm_param {
    use_global_stats: true
  }
}
layer {
  name: "scale3a_branch1"
  type: "Scale"
  bottom: "res3a_branch1"
  top: "res3a_branch1"
  scale_param {
    bias_term: true
  }
}
layer {
  name: "res3a_branch2a"
  type: "Convolution"
  bottom: "res2c"
  top: "res3a_branch2a"
  convolution_param {
    num_output: 128
    bias_term: false
    pad: 0
    kernel_size: 1
    stride: 2
  }
}
layer {
  name: "bn3a_branch2a"
  type: "BatchNorm"
  bottom: "res3a_branch2a"
  top: "res3a_branch2a"
  batch_norm_param {
    use_global_stats: true
  }
}
layer {
  name: "scale3a_branch2a"
  type: "Scale"
  bottom: "res3a_branch2a"
  top: "res3a_branch2a"
  scale_param {
    bias_term: true
  }
}
layer {
  name: "res3a_branch2a_relu"
  type: "ReLU"
  bottom: "res3a_branch2a"
  top: "res3a_branch2a"
}
layer {
  name: "res3a_branch2b"
  type: "Convolution"
  bottom: "res3a_branch2a"
  top: "res3a_branch2b"
  convolution_param {
    num_output: 128
    bias_term: false
    pad: 1
    kernel_size: 3
    stride: 1
  }
}
layer {
  name: "bn3a_branch2b"
  type: "BatchNorm"
  bottom: "res3a_branch2b"
  top: "res3a_branch2b"
  batch_norm_param {
    use_global_stats: true
  }
}
layer {
  name: "scale3a_branch2b"
  type: "Scale"
  bottom: "res3a_branch2b"
  top: "res3a_branch2b"
  scale_param {
    bias_term: true
  }
}
layer {
  name: "res3a_branch2b_relu"
  type: "ReLU"
  bottom: "res3a_branch2b"
  top: "res3a_branch2b"
}
layer {
  name: "res3a_branch2c"
  type: "Convolution"
  bottom: "res3a_branch2b"
  top: "res3a_branch2c"
  convolution_param {
    num_output: 512
    bias_term: false
    pad: 0
    kernel_size: 1
    stride: 1
  }
}
layer {
  name: "bn3a_branch2c"
  type: "BatchNorm"
  bottom: "res3a_branch2c"
  top: "res3a_branch2c"
  batch_norm_param {
    use_global_stats: true
  }
}
layer {
  name: "scale3a_branch2c"
  type: "Scale"
  bottom: "res3a_branch2c"
  top: "res3a_branch2c"
  scale_param {
    bias_term: true
  }
}
layer {
  name: "res3a"
  type: "Eltwise"
  bottom: "res3a_branch1"
  bottom: "res3a_branch2c"
  top: "res3a"
}
layer {
  name: "res3a_relu"
  type: "ReLU"
  bottom: "res3a"
  top: "res3a"
}
layer {
  name: "res3b_branch2a"
  type: "Convolution"
  bottom: "res3a"
  top: "res3b_branch2a"
  convolution_param {
    num_output: 128
    bias_term: false
    pad: 0
    kernel_size: 1
    stride: 1
  }
}
layer {
  name: "bn3b_branch2a"
  type: "BatchNorm"
  bottom: "res3b_branch2a"
  top: "res3b_branch2a"
  batch_norm_param {
    use_global_stats: true
  }
}
layer {
  name: "scale3b_branch2a"
  type: "Scale"
  bottom: "res3b_branch2a"
  top: "res3b_branch2a"
  scale_param {
    bias_term: true
  }
}
layer {
  name: "res3b_branch2a_relu"
  type: "ReLU"
  bottom: "res3b_branch2a"
  top: "res3b_branch2a"
}
layer {
  name: "res3b_branch2b"
  type: "Convolution"
  bottom: "res3b_branch2a"
  top: "res3b_branch2b"
  convolution_param {
    num_output: 128
    bias_term: false
    pad: 1
    kernel_size: 3
    stride: 1
  }
}
layer {
  name: "bn3b_branch2b"
  type: "BatchNorm"
  bottom: "res3b_branch2b"
  top: "res3b_branch2b"
  batch_norm_param {
    use_global_stats: true
  }
}
layer {
  name: "scale3b_branch2b"
  type: "Scale"
  bottom: "res3b_branch2b"
  top: "res3b_branch2b"
  scale_param {
    bias_term: true
  }
}
layer {
  name: "res3b_branch2b_relu"
  type: "ReLU"
  bottom: "res3b_branch2b"
  top: "res3b_branch2b"
}
layer {
  name: "res3b_branch2c"
  type: "Convolution"
  bottom: "res3b_branch2b"
  top: "res3b_branch2c"
  convolution_param {
    num_output: 512
    bias_term: false
    pad: 0
    kernel_size: 1
    stride: 1
  }
}
layer {
  name: "bn3b_branch2c"
  type: "BatchNorm"
  bottom: "res3b_branch2c"
  top: "res3b_branch2c"
  batch_norm_param {
    use_global_stats: true
  }
}
layer {
  name: "scale3b_branch2c"
  type: "Scale"
  bottom: "res3b_branch2c"
  top: "res3b_branch2c"
  scale_param {
    bias_term: true
  }
}
layer {
  name: "res3b"
  type: "Eltwise"
  bottom: "res3a"
  bottom: "res3b_branch2c"
  top: "res3b"
}
layer {
  name: "res3b_relu"
  type: "ReLU"
  bottom: "res3b"
  top: "res3b"
}
layer {
  name: "res3c_branch2a"
  type: "Convolution"
  bottom: "res3b"
  top: "res3c_branch2a"
  convolution_param {
    num_output: 128
    bias_term: false
    pad: 0
    kernel_size: 1
    stride: 1
  }
}
layer {
  name: "bn3c_branch2a"
  type: "BatchNorm"
  bottom: "res3c_branch2a"
  top: "res3c_branch2a"
  batch_norm_param {
    use_global_stats: true
  }
}
layer {
  name: "scale3c_branch2a"
  type: "Scale"
  bottom: "res3c_branch2a"
  top: "res3c_branch2a"
  scale_param {
    bias_term: true
  }
}
layer {
  name: "res3c_branch2a_relu"
  type: "ReLU"
  bottom: "res3c_branch2a"
  top: "res3c_branch2a"
}
layer {
  name: "res3c_branch2b"
  type: "Convolution"
  bottom: "res3c_branch2a"
  top: "res3c_branch2b"
  convolution_param {
    num_output: 128
    bias_term: false
    pad: 1
    kernel_size: 3
    stride: 1
  }
}
layer {
  name: "bn3c_branch2b"
  type: "BatchNorm"
  bottom: "res3c_branch2b"
  top: "res3c_branch2b"
  batch_norm_param {
    use_global_stats: true
  }
}
layer {
  name: "scale3c_branch2b"
  type: "Scale"
  bottom: "res3c_branch2b"
  top: "res3c_branch2b"
  scale_param {
    bias_term: true
  }
}
layer {
  name: "res3c_branch2b_relu"
  type: "ReLU"
  bottom: "res3c_branch2b"
  top: "res3c_branch2b"
}
layer {
  name: "res3c_branch2c"
  type: "Convolution"
  bottom: "res3c_branch2b"
  top: "res3c_branch2c"
  convolution_param {
    num_output: 512
    bias_term: false
    pad: 0
    kernel_size: 1
    stride: 1
  }
}
layer {
  name: "bn3c_branch2c"
  type: "BatchNorm"
  bottom: "res3c_branch2c"
  top: "res3c_branch2c"
  batch_norm_param {
    use_global_stats: true
  }
}
layer {
  name: "scale3c_branch2c"
  type: "Scale"
  bottom: "res3c_branch2c"
  top: "res3c_branch2c"
  scale_param {
    bias_term: true
  }
}
layer {
  name: "res3c"
  type: "Eltwise"
  bottom: "res3b"
  bottom: "res3c_branch2c"
  top: "res3c"
}
layer {
  name: "res3c_relu"
  type: "ReLU"
  bottom: "res3c"
  top: "res3c"
}
layer {
  name: "res3d_branch2a"
  type: "Convolution"
  bottom: "res3c"
  top: "res3d_branch2a"
  convolution_param {
    num_output: 128
    bias_term: false
    pad: 0
    kernel_size: 1
    stride: 1
  }
}
layer {
  name: "bn3d_branch2a"
  type: "BatchNorm"
  bottom: "res3d_branch2a"
  top: "res3d_branch2a"
  batch_norm_param {
    use_global_stats: true
  }
}
layer {
  name: "scale3d_branch2a"
  type: "Scale"
  bottom: "res3d_branch2a"
  top: "res3d_branch2a"
  scale_param {
    bias_term: true
  }
}
layer {
  name: "res3d_branch2a_relu"
  type: "ReLU"
  bottom: "res3d_branch2a"
  top: "res3d_branch2a"
}
layer {
  name: "res3d_branch2b"
  type: "Convolution"
  bottom: "res3d_branch2a"
  top: "res3d_branch2b"
  convolution_param {
    num_output: 128
    bias_term: false
    pad: 1
    kernel_size: 3
    stride: 1
  }
}
layer {
  name: "bn3d_branch2b"
  type: "BatchNorm"
  bottom: "res3d_branch2b"
  top: "res3d_branch2b"
  batch_norm_param {
    use_global_stats: true
  }
}
layer {
  name: "scale3d_branch2b"
  type: "Scale"
  bottom: "res3d_branch2b"
  top: "res3d_branch2b"
  scale_param {
    bias_term: true
  }
}
layer {
  name: "res3d_branch2b_relu"
  type: "ReLU"
  bottom: "res3d_branch2b"
  top: "res3d_branch2b"
}
layer {
  name: "res3d_branch2c"
  type: "Convolution"
  bottom: "res3d_branch2b"
  top: "res3d_branch2c"
  convolution_param {
    num_output: 512
    bias_term: false
    pad: 0
    kernel_size: 1
    stride: 1
  }
}
layer {
  name: "bn3d_branch2c"
  type: "BatchNorm"
  bottom: "res3d_branch2c"
  top: "res3d_branch2c"
  batch_norm_param {
    use_global_stats: true
  }
}
layer {
  name: "scale3d_branch2c"
  type: "Scale"
  bottom: "res3d_branch2c"
  top: "res3d_branch2c"
  scale_param {
    bias_term: true
  }
}
layer {
  name: "res3d"
  type: "Eltwise"
  bottom: "res3c"
  bottom: "res3d_branch2c"
  top: "res3d"
}
layer {
  name: "res3d_relu"
  type: "ReLU"
  bottom: "res3d"
  top: "res3d"
}
layer {
  name: "res4a_branch1"
  type: "Convolution"
  bottom: "res3d"
  top: "res4a_branch1"
  convolution_param {
    num_output: 1024
    bias_term: false
    pad: 0
    kernel_size: 1
    stride: 2
  }
}
layer {
  name: "bn4a_branch1"
  type: "BatchNorm"
  bottom: "res4a_branch1"
  top: "res4a_branch1"
  batch_norm_param {
    use_global_stats: true
  }
}
layer {
  name: "scale4a_branch1"
  type: "Scale"
  bottom: "res4a_branch1"
  top: "res4a_branch1"
  scale_param {
    bias_term: true
  }
}
layer {
  name: "res4a_branch2a"
  type: "Convolution"
  bottom: "res3d"
  top: "res4a_branch2a"
  convolution_param {
    num_output: 256
    bias_term: false
    pad: 0
    kernel_size: 1
    stride: 2
  }
}
layer {
  name: "bn4a_branch2a"
  type: "BatchNorm"
  bottom: "res4a_branch2a"
  top: "res4a_branch2a"
  batch_norm_param {
    use_global_stats: true
  }
}
layer {
  name: "scale4a_branch2a"
  type: "Scale"
  bottom: "res4a_branch2a"
  top: "res4a_branch2a"
  scale_param {
    bias_term: true
  }
}
layer {
  name: "res4a_branch2a_relu"
  type: "ReLU"
  bottom: "res4a_branch2a"
  top: "res4a_branch2a"
}
layer {
  name: "res4a_branch2b"
  type: "Convolution"
  bottom: "res4a_branch2a"
  top: "res4a_branch2b"
  convolution_param {
    num_output: 256
    bias_term: false
    pad: 1
    kernel_size: 3
    stride: 1
  }
}
layer {
  name: "bn4a_branch2b"
  type: "BatchNorm"
  bottom: "res4a_branch2b"
  top: "res4a_branch2b"
  batch_norm_param {
    use_global_stats: true
  }
}
layer {
  name: "scale4a_branch2b"
  type: "Scale"
  bottom: "res4a_branch2b"
  top: "res4a_branch2b"
  scale_param {
    bias_term: true
  }
}
layer {
  name: "res4a_branch2b_relu"
  type: "ReLU"
  bottom: "res4a_branch2b"
  top: "res4a_branch2b"
}
layer {
  name: "res4a_branch2c"
  type: "Convolution"
  bottom: "res4a_branch2b"
  top: "res4a_branch2c"
  convolution_param {
    num_output: 1024
    bias_term: false
    pad: 0
    kernel_size: 1
    stride: 1
  }
}
layer {
  name: "bn4a_branch2c"
  type: "BatchNorm"
  bottom: "res4a_branch2c"
  top: "res4a_branch2c"
  batch_norm_param {
    use_global_stats: true
  }
}
layer {
  name: "scale4a_branch2c"
  type: "Scale"
  bottom: "res4a_branch2c"
  top: "res4a_branch2c"
  scale_param {
    bias_term: true
  }
}
layer {
  name: "res4a"
  type: "Eltwise"
  bottom: "res4a_branch1"
  bottom: "res4a_branch2c"
  top: "res4a"
}
layer {
  name: "res4a_relu"
  type: "ReLU"
  bottom: "res4a"
  top: "res4a"
}
layer {
  name: "res4b_branch2a"
  type: "Convolution"
  bottom: "res4a"
  top: "res4b_branch2a"
  convolution_param {
    num_output: 256
    bias_term: false
    pad: 0
    kernel_size: 1
    stride: 1
  }
}
layer {
  name: "bn4b_branch2a"
  type: "BatchNorm"
  bottom: "res4b_branch2a"
  top: "res4b_branch2a"
  batch_norm_param {
    use_global_stats: true
  }
}
layer {
  name: "scale4b_branch2a"
  type: "Scale"
  bottom: "res4b_branch2a"
  top: "res4b_branch2a"
  scale_param {
    bias_term: true
  }
}
layer {
  name: "res4b_branch2a_relu"
  type: "ReLU"
  bottom: "res4b_branch2a"
  top: "res4b_branch2a"
}
layer {
  name: "res4b_branch2b"
  type: "Convolution"
  bottom: "res4b_branch2a"
  top: "res4b_branch2b"
  convolution_param {
    num_output: 256
    bias_term: false
    pad: 1
    kernel_size: 3
    stride: 1
  }
}
layer {
  name: "bn4b_branch2b"
  type: "BatchNorm"
  bottom: "res4b_branch2b"
  top: "res4b_branch2b"
  batch_norm_param {
    use_global_stats: true
  }
}
layer {
  name: "scale4b_branch2b"
  type: "Scale"
  bottom: "res4b_branch2b"
  top: "res4b_branch2b"
  scale_param {
    bias_term: true
  }
}
layer {
  name: "res4b_branch2b_relu"
  type: "ReLU"
  bottom: "res4b_branch2b"
  top: "res4b_branch2b"
}
layer {
  name: "res4b_branch2c"
  type: "Convolution"
  bottom: "res4b_branch2b"
  top: "res4b_branch2c"
  convolution_param {
    num_output: 1024
    bias_term: false
    pad: 0
    kernel_size: 1
    stride: 1
  }
}
layer {
  name: "bn4b_branch2c"
  type: "BatchNorm"
  bottom: "res4b_branch2c"
  top: "res4b_branch2c"
  batch_norm_param {
    use_global_stats: true
  }
}
layer {
  name: "scale4b_branch2c"
  type: "Scale"
  bottom: "res4b_branch2c"
  top: "res4b_branch2c"
  scale_param {
    bias_term: true
  }
}
layer {
  name: "res4b"
  type: "Eltwise"
  bottom: "res4a"
  bottom: "res4b_branch2c"
  top: "res4b"
}
layer {
  name: "res4b_relu"
  type: "ReLU"
  bottom: "res4b"
  top: "res4b"
}
layer {
  name: "res4c_branch2a"
  type: "Convolution"
  bottom: "res4b"
  top: "res4c_branch2a"
  convolution_param {
    num_output: 256
    bias_term: false
    pad: 0
    kernel_size: 1
    stride: 1
  }
}
layer {
  name: "bn4c_branch2a"
  type: "BatchNorm"
  bottom: "res4c_branch2a"
  top: "res4c_branch2a"
  batch_norm_param {
    use_global_stats: true
  }
}
layer {
  name: "scale4c_branch2a"
  type: "Scale"
  bottom: "res4c_branch2a"
  top: "res4c_branch2a"
  scale_param {
    bias_term: true
  }
}
layer {
  name: "res4c_branch2a_relu"
  type: "ReLU"
  bottom: "res4c_branch2a"
  top: "res4c_branch2a"
}
layer {
  name: "res4c_branch2b"
  type: "Convolution"
  bottom: "res4c_branch2a"
  top: "res4c_branch2b"
  convolution_param {
    num_output: 256
    bias_term: false
    pad: 1
    kernel_size: 3
    stride: 1
  }
}
layer {
  name: "bn4c_branch2b"
  type: "BatchNorm"
  bottom: "res4c_branch2b"
  top: "res4c_branch2b"
  batch_norm_param {
    use_global_stats: true
  }
}
layer {
  name: "scale4c_branch2b"
  type: "Scale"
  bottom: "res4c_branch2b"
  top: "res4c_branch2b"
  scale_param {
    bias_term: true
  }
}
layer {
  name: "res4c_branch2b_relu"
  type: "ReLU"
  bottom: "res4c_branch2b"
  top: "res4c_branch2b"
}
layer {
  name: "res4c_branch2c"
  type: "Convolution"
  bottom: "res4c_branch2b"
  top: "res4c_branch2c"
  convolution_param {
    num_output: 1024
    bias_term: false
    pad: 0
    kernel_size: 1
    stride: 1
  }
}
layer {
  name: "bn4c_branch2c"
  type: "BatchNorm"
  bottom: "res4c_branch2c"
  top: "res4c_branch2c"
  batch_norm_param {
    use_global_stats: true
  }
}
layer {
  name: "scale4c_branch2c"
  type: "Scale"
  bottom: "res4c_branch2c"
  top: "res4c_branch2c"
  scale_param {
    bias_term: true
  }
}
layer {
  name: "res4c"
  type: "Eltwise"
  bottom: "res4b"
  bottom: "res4c_branch2c"
  top: "res4c"
}
layer {
  name: "res4c_relu"
  type: "ReLU"
  bottom: "res4c"
  top: "res4c"
}
layer {
  name: "res4d_branch2a"
  type: "Convolution"
  bottom: "res4c"
  top: "res4d_branch2a"
  convolution_param {
    num_output: 256
    bias_term: false
    pad: 0
    kernel_size: 1
    stride: 1
  }
}
layer {
  name: "bn4d_branch2a"
  type: "BatchNorm"
  bottom: "res4d_branch2a"
  top: "res4d_branch2a"
  batch_norm_param {
    use_global_stats: true
  }
}
layer {
  name: "scale4d_branch2a"
  type: "Scale"
  bottom: "res4d_branch2a"
  top: "res4d_branch2a"
  scale_param {
    bias_term: true
  }
}
layer {
  name: "res4d_branch2a_relu"
  type: "ReLU"
  bottom: "res4d_branch2a"
  top: "res4d_branch2a"
}
layer {
  name: "res4d_branch2b"
  type: "Convolution"
  bottom: "res4d_branch2a"
  top: "res4d_branch2b"
  convolution_param {
    num_output: 256
    bias_term: false
    pad: 1
    kernel_size: 3
    stride: 1
  }
}
layer {
  name: "bn4d_branch2b"
  type: "BatchNorm"
  bottom: "res4d_branch2b"
  top: "res4d_branch2b"
  batch_norm_param {
    use_global_stats: true
  }
}
layer {
  name: "scale4d_branch2b"
  type: "Scale"
  bottom: "res4d_branch2b"
  top: "res4d_branch2b"
  scale_param {
    bias_term: true
  }
}
layer {
  name: "res4d_branch2b_relu"
  type: "ReLU"
  bottom: "res4d_branch2b"
  top: "res4d_branch2b"
}
layer {
  name: "res4d_branch2c"
  type: "Convolution"
  bottom: "res4d_branch2b"
  top: "res4d_branch2c"
  convolution_param {
    num_output: 1024
    bias_term: false
    pad: 0
    kernel_size: 1
    stride: 1
  }
}
layer {
  name: "bn4d_branch2c"
  type: "BatchNorm"
  bottom: "res4d_branch2c"
  top: "res4d_branch2c"
  batch_norm_param {
    use_global_stats: true
  }
}
layer {
  name: "scale4d_branch2c"
  type: "Scale"
  bottom: "res4d_branch2c"
  top: "res4d_branch2c"
  scale_param {
    bias_term: true
  }
}
layer {
  name: "res4d"
  type: "Eltwise"
  bottom: "res4c"
  bottom: "res4d_branch2c"
  top: "res4d"
}
layer {
  name: "res4d_relu"
  type: "ReLU"
  bottom: "res4d"
  top: "res4d"
}
layer {
  name: "res4e_branch2a"
  type: "Convolution"
  bottom: "res4d"
  top: "res4e_branch2a"
  convolution_param {
    num_output: 256
    bias_term: false
    pad: 0
    kernel_size: 1
    stride: 1
  }
}
layer {
  name: "bn4e_branch2a"
  type: "BatchNorm"
  bottom: "res4e_branch2a"
  top: "res4e_branch2a"
  batch_norm_param {
    use_global_stats: true
  }
}
layer {
  name: "scale4e_branch2a"
  type: "Scale"
  bottom: "res4e_branch2a"
  top: "res4e_branch2a"
  scale_param {
    bias_term: true
  }
}
layer {
  name: "res4e_branch2a_relu"
  type: "ReLU"
  bottom: "res4e_branch2a"
  top: "res4e_branch2a"
}
layer {
  name: "res4e_branch2b"
  type: "Convolution"
  bottom: "res4e_branch2a"
  top: "res4e_branch2b"
  convolution_param {
    num_output: 256
    bias_term: false
    pad: 1
    kernel_size: 3
    stride: 1
  }
}
layer {
  name: "bn4e_branch2b"
  type: "BatchNorm"
  bottom: "res4e_branch2b"
  top: "res4e_branch2b"
  batch_norm_param {
    use_global_stats: true
  }
}
layer {
  name: "scale4e_branch2b"
  type: "Scale"
  bottom: "res4e_branch2b"
  top: "res4e_branch2b"
  scale_param {
    bias_term: true
  }
}
layer {
  name: "res4e_branch2b_relu"
  type: "ReLU"
  bottom: "res4e_branch2b"
  top: "res4e_branch2b"
}
layer {
  name: "res4e_branch2c"
  type: "Convolution"
  bottom: "res4e_branch2b"
  top: "res4e_branch2c"
  convolution_param {
    num_output: 1024
    bias_term: false
    pad: 0
    kernel_size: 1
    stride: 1
  }
}
layer {
  name: "bn4e_branch2c"
  type: "BatchNorm"
  bottom: "res4e_branch2c"
  top: "res4e_branch2c"
  batch_norm_param {
    use_global_stats: true
  }
}
layer {
  name: "scale4e_branch2c"
  type: "Scale"
  bottom: "res4e_branch2c"
  top: "res4e_branch2c"
  scale_param {
    bias_term: true
  }
}
layer {
  name: "res4e"
  type: "Eltwise"
  bottom: "res4d"
  bottom: "res4e_branch2c"
  top: "res4e"
}
layer {
  name: "res4e_relu"
  type: "ReLU"
  bottom: "res4e"
  top: "res4e"
}
layer {
  name: "res4f_branch2a"
  type: "Convolution"
  bottom: "res4e"
  top: "res4f_branch2a"
  convolution_param {
    num_output: 256
    bias_term: false
    pad: 0
    kernel_size: 1
    stride: 1
  }
}
layer {
  name: "bn4f_branch2a"
  type: "BatchNorm"
  bottom: "res4f_branch2a"
  top: "res4f_branch2a"
  batch_norm_param {
    use_global_stats: true
  }
}
layer {
  name: "scale4f_branch2a"
  type: "Scale"
  bottom: "res4f_branch2a"
  top: "res4f_branch2a"
  scale_param {
    bias_term: true
  }
}
layer {
  name: "res4f_branch2a_relu"
  type: "ReLU"
  bottom: "res4f_branch2a"
  top: "res4f_branch2a"
}
layer {
  name: "res4f_branch2b"
  type: "Convolution"
  bottom: "res4f_branch2a"
  top: "res4f_branch2b"
  convolution_param {
    num_output: 256
    bias_term: false
    pad: 1
    kernel_size: 3
    stride: 1
  }
}
layer {
  name: "bn4f_branch2b"
  type: "BatchNorm"
  bottom: "res4f_branch2b"
  top: "res4f_branch2b"
  batch_norm_param {
    use_global_stats: true
  }
}
layer {
  name: "scale4f_branch2b"
  type: "Scale"
  bottom: "res4f_branch2b"
  top: "res4f_branch2b"
  scale_param {
    bias_term: true
  }
}
layer {
  name: "res4f_branch2b_relu"
  type: "ReLU"
  bottom: "res4f_branch2b"
  top: "res4f_branch2b"
}
layer {
  name: "res4f_branch2c"
  type: "Convolution"
  bottom: "res4f_branch2b"
  top: "res4f_branch2c"
  convolution_param {
    num_output: 1024
    bias_term: false
    pad: 0
    kernel_size: 1
    stride: 1
  }
}
layer {
  name: "bn4f_branch2c"
  type: "BatchNorm"
  bottom: "res4f_branch2c"
  top: "res4f_branch2c"
  batch_norm_param {
    use_global_stats: true
  }
}
layer {
  name: "scale4f_branch2c"
  type: "Scale"
  bottom: "res4f_branch2c"
  top: "res4f_branch2c"
  scale_param {
    bias_term: true
  }
}
layer {
  name: "res4f"
  type: "Eltwise"
  bottom: "res4e"
  bottom: "res4f_branch2c"
  top: "res4f"
}
layer {
  name: "res4f_relu"
  type: "ReLU"
  bottom: "res4f"
  top: "res4f"
}
layer {
  name: "res5a_branch1"
  type: "Convolution"
  bottom: "res4f"
  top: "res5a_branch1"
  convolution_param {
    num_output: 2048
    bias_term: false
    pad: 0
    kernel_size: 1
    stride: 2
  }
}
layer {
  name: "bn5a_branch1"
  type: "BatchNorm"
  bottom: "res5a_branch1"
  top: "res5a_branch1"
  batch_norm_param {
    use_global_stats: true
  }
}
layer {
  name: "scale5a_branch1"
  type: "Scale"
  bottom: "res5a_branch1"
  top: "res5a_branch1"
  scale_param {
    bias_term: true
  }
}
layer {
  name: "res5a_branch2a"
  type: "Convolution"
  bottom: "res4f"
  top: "res5a_branch2a"
  convolution_param {
    num_output: 512
    bias_term: false
    pad: 0
    kernel_size: 1
    stride: 2
  }
}
layer {
  name: "bn5a_branch2a"
  type: "BatchNorm"
  bottom: "res5a_branch2a"
  top: "res5a_branch2a"
  batch_norm_param {
    use_global_stats: true
  }
}
layer {
  name: "scale5a_branch2a"
  type: "Scale"
  bottom: "res5a_branch2a"
  top: "res5a_branch2a"
  scale_param {
    bias_term: true
  }
}
layer {
  name: "res5a_branch2a_relu"
  type: "ReLU"
  bottom: "res5a_branch2a"
  top: "res5a_branch2a"
}
layer {
  name: "res5a_branch2b"
  type: "Convolution"
  bottom: "res5a_branch2a"
  top: "res5a_branch2b"
  convolution_param {
    num_output: 512
    bias_term: false
    pad: 1
    kernel_size: 3
    stride: 1
  }
}
layer {
  name: "bn5a_branch2b"
  type: "BatchNorm"
  bottom: "res5a_branch2b"
  top: "res5a_branch2b"
  batch_norm_param {
    use_global_stats: true
  }
}
layer {
  name: "scale5a_branch2b"
  type: "Scale"
  bottom: "res5a_branch2b"
  top: "res5a_branch2b"
  scale_param {
    bias_term: true
  }
}
layer {
  name: "res5a_branch2b_relu"
  type: "ReLU"
  bottom: "res5a_branch2b"
  top: "res5a_branch2b"
}
layer {
  name: "res5a_branch2c"
  type: "Convolution"
  bottom: "res5a_branch2b"
  top: "res5a_branch2c"
  convolution_param {
    num_output: 2048
    bias_term: false
    pad: 0
    kernel_size: 1
    stride: 1
  }
}
layer {
  name: "bn5a_branch2c"
  type: "BatchNorm"
  bottom: "res5a_branch2c"
  top: "re
I0623 09:45:02.634352  1897 layer_factory.hpp:77] Creating layer data
I0623 09:45:02.634414  1897 db_lmdb.cpp:35] Opened lmdb /home/eikan/dezhi/caffe/examples/imagenet/ilsvrc12_val_lmdb
I0623 09:45:02.634452  1897 net.cpp:84] Creating Layer data
I0623 09:45:02.634461  1897 net.cpp:380] data -> data
I0623 09:45:02.634495  1897 net.cpp:380] data -> label
I0623 09:45:02.635228  1897 data_layer.cpp:45] output data size: 8,3,256,256
I0623 09:45:02.932060  1897 net.cpp:122] Setting up data
I0623 09:45:02.932133  1897 net.cpp:129] Top shape: 8 3 256 256 (1572864)
I0623 09:45:02.932152  1897 net.cpp:129] Top shape: 8 (8)
I0623 09:45:02.932165  1897 net.cpp:137] Memory required for data: 6291488
I0623 09:45:02.932184  1897 layer_factory.hpp:77] Creating layer label_data_1_split
I0623 09:45:02.932219  1897 net.cpp:84] Creating Layer label_data_1_split
I0623 09:45:02.932237  1897 net.cpp:406] label_data_1_split <- label
I0623 09:45:02.932258  1897 net.cpp:380] label_data_1_split -> label_data_1_split_0
I0623 09:45:02.932284  1897 net.cpp:380] label_data_1_split -> label_data_1_split_1
I0623 09:45:02.932314  1897 net.cpp:122] Setting up label_data_1_split
I0623 09:45:02.932335  1897 net.cpp:129] Top shape: 8 (8)
I0623 09:45:02.932353  1897 net.cpp:129] Top shape: 8 (8)
I0623 09:45:02.932369  1897 net.cpp:137] Memory required for data: 6291552
I0623 09:45:02.932385  1897 layer_factory.hpp:77] Creating layer conv1
I0623 09:45:02.932410  1897 net.cpp:84] Creating Layer conv1
I0623 09:45:02.932427  1897 net.cpp:406] conv1 <- data
I0623 09:45:02.932446  1897 net.cpp:380] conv1 -> conv1
I0623 09:45:02.932516  1897 net.cpp:122] Setting up conv1
I0623 09:45:02.932541  1897 net.cpp:129] Top shape: 8 64 128 128 (8388608)
I0623 09:45:02.932557  1897 net.cpp:137] Memory required for data: 39845984
I0623 09:45:02.932582  1897 layer_factory.hpp:77] Creating layer bn_conv1
I0623 09:45:02.932610  1897 net.cpp:84] Creating Layer bn_conv1
I0623 09:45:02.932627  1897 net.cpp:406] bn_conv1 <- conv1
I0623 09:45:02.932646  1897 net.cpp:367] bn_conv1 -> conv1 (in-place)
I0623 09:45:02.932688  1897 net.cpp:122] Setting up bn_conv1
I0623 09:45:02.932709  1897 net.cpp:129] Top shape: 8 64 128 128 (8388608)
I0623 09:45:02.932726  1897 net.cpp:137] Memory required for data: 73400416
I0623 09:45:02.932751  1897 layer_factory.hpp:77] Creating layer scale_conv1
I0623 09:45:02.932780  1897 net.cpp:84] Creating Layer scale_conv1
I0623 09:45:02.932796  1897 net.cpp:406] scale_conv1 <- conv1
I0623 09:45:02.932816  1897 net.cpp:367] scale_conv1 -> conv1 (in-place)
I0623 09:45:02.932848  1897 layer_factory.hpp:77] Creating layer scale_conv1
I0623 09:45:02.932925  1897 net.cpp:122] Setting up scale_conv1
I0623 09:45:02.932948  1897 net.cpp:129] Top shape: 8 64 128 128 (8388608)
I0623 09:45:02.932965  1897 net.cpp:137] Memory required for data: 106954848
I0623 09:45:02.932984  1897 layer_factory.hpp:77] Creating layer conv1_relu
I0623 09:45:02.933007  1897 net.cpp:84] Creating Layer conv1_relu
I0623 09:45:02.933023  1897 net.cpp:406] conv1_relu <- conv1
I0623 09:45:02.933043  1897 net.cpp:367] conv1_relu -> conv1 (in-place)
I0623 09:45:02.933061  1897 net.cpp:122] Setting up conv1_relu
I0623 09:45:02.933080  1897 net.cpp:129] Top shape: 8 64 128 128 (8388608)
I0623 09:45:02.933097  1897 net.cpp:137] Memory required for data: 140509280
I0623 09:45:02.933113  1897 layer_factory.hpp:77] Creating layer pool1
I0623 09:45:02.933137  1897 net.cpp:84] Creating Layer pool1
I0623 09:45:02.933157  1897 net.cpp:406] pool1 <- conv1
I0623 09:45:02.933176  1897 net.cpp:380] pool1 -> pool1
I0623 09:45:02.933204  1897 net.cpp:122] Setting up pool1
I0623 09:45:02.933224  1897 net.cpp:129] Top shape: 8 64 64 64 (2097152)
I0623 09:45:02.933240  1897 net.cpp:137] Memory required for data: 148897888
I0623 09:45:02.933255  1897 layer_factory.hpp:77] Creating layer pool1_pool1_0_split
I0623 09:45:02.933276  1897 net.cpp:84] Creating Layer pool1_pool1_0_split
I0623 09:45:02.933295  1897 net.cpp:406] pool1_pool1_0_split <- pool1
I0623 09:45:02.933313  1897 net.cpp:380] pool1_pool1_0_split -> pool1_pool1_0_split_0
I0623 09:45:02.933334  1897 net.cpp:380] pool1_pool1_0_split -> pool1_pool1_0_split_1
I0623 09:45:02.933357  1897 net.cpp:122] Setting up pool1_pool1_0_split
I0623 09:45:02.933377  1897 net.cpp:129] Top shape: 8 64 64 64 (2097152)
I0623 09:45:02.933395  1897 net.cpp:129] Top shape: 8 64 64 64 (2097152)
I0623 09:45:02.933411  1897 net.cpp:137] Memory required for data: 165675104
I0623 09:45:02.933428  1897 layer_factory.hpp:77] Creating layer res2a_branch1
I0623 09:45:02.933449  1897 net.cpp:84] Creating Layer res2a_branch1
I0623 09:45:02.933466  1897 net.cpp:406] res2a_branch1 <- pool1_pool1_0_split_0
I0623 09:45:02.933487  1897 net.cpp:380] res2a_branch1 -> res2a_branch1
I0623 09:45:02.933549  1897 net.cpp:122] Setting up res2a_branch1
I0623 09:45:02.933573  1897 net.cpp:129] Top shape: 8 256 64 64 (8388608)
I0623 09:45:02.933589  1897 net.cpp:137] Memory required for data: 199229536
I0623 09:45:02.933609  1897 layer_factory.hpp:77] Creating layer bn2a_branch1
I0623 09:45:02.933629  1897 net.cpp:84] Creating Layer bn2a_branch1
I0623 09:45:02.933647  1897 net.cpp:406] bn2a_branch1 <- res2a_branch1
I0623 09:45:02.933665  1897 net.cpp:367] bn2a_branch1 -> res2a_branch1 (in-place)
I0623 09:45:02.933703  1897 net.cpp:122] Setting up bn2a_branch1
I0623 09:45:02.933724  1897 net.cpp:129] Top shape: 8 256 64 64 (8388608)
I0623 09:45:02.933742  1897 net.cpp:137] Memory required for data: 232783968
I0623 09:45:02.933765  1897 layer_factory.hpp:77] Creating layer scale2a_branch1
I0623 09:45:02.933789  1897 net.cpp:84] Creating Layer scale2a_branch1
I0623 09:45:02.933807  1897 net.cpp:406] scale2a_branch1 <- res2a_branch1
I0623 09:45:02.933825  1897 net.cpp:367] scale2a_branch1 -> res2a_branch1 (in-place)
I0623 09:45:02.933851  1897 layer_factory.hpp:77] Creating layer scale2a_branch1
I0623 09:45:02.933897  1897 net.cpp:122] Setting up scale2a_branch1
I0623 09:45:02.933918  1897 net.cpp:129] Top shape: 8 256 64 64 (8388608)
I0623 09:45:02.933934  1897 net.cpp:137] Memory required for data: 266338400
I0623 09:45:02.933954  1897 layer_factory.hpp:77] Creating layer res2a_branch2a
I0623 09:45:02.933974  1897 net.cpp:84] Creating Layer res2a_branch2a
I0623 09:45:02.933991  1897 net.cpp:406] res2a_branch2a <- pool1_pool1_0_split_1
I0623 09:45:02.934012  1897 net.cpp:380] res2a_branch2a -> res2a_branch2a
I0623 09:45:02.934052  1897 net.cpp:122] Setting up res2a_branch2a
I0623 09:45:02.934074  1897 net.cpp:129] Top shape: 8 64 64 64 (2097152)
I0623 09:45:02.934090  1897 net.cpp:137] Memory required for data: 274727008
I0623 09:45:02.934108  1897 layer_factory.hpp:77] Creating layer bn2a_branch2a
I0623 09:45:02.934134  1897 net.cpp:84] Creating Layer bn2a_branch2a
I0623 09:45:02.934152  1897 net.cpp:406] bn2a_branch2a <- res2a_branch2a
I0623 09:45:02.934171  1897 net.cpp:367] bn2a_branch2a -> res2a_branch2a (in-place)
I0623 09:45:02.934207  1897 net.cpp:122] Setting up bn2a_branch2a
I0623 09:45:02.934227  1897 net.cpp:129] Top shape: 8 64 64 64 (2097152)
I0623 09:45:02.934244  1897 net.cpp:137] Memory required for data: 283115616
I0623 09:45:02.934270  1897 layer_factory.hpp:77] Creating layer scale2a_branch2a
I0623 09:45:02.934293  1897 net.cpp:84] Creating Layer scale2a_branch2a
I0623 09:45:02.934310  1897 net.cpp:406] scale2a_branch2a <- res2a_branch2a
I0623 09:45:02.934330  1897 net.cpp:367] scale2a_branch2a -> res2a_branch2a (in-place)
I0623 09:45:02.934355  1897 layer_factory.hpp:77] Creating layer scale2a_branch2a
I0623 09:45:02.934398  1897 net.cpp:122] Setting up scale2a_branch2a
I0623 09:45:02.934420  1897 net.cpp:129] Top shape: 8 64 64 64 (2097152)
I0623 09:45:02.934437  1897 net.cpp:137] Memory required for data: 291504224
I0623 09:45:02.934456  1897 layer_factory.hpp:77] Creating layer res2a_branch2a_relu
I0623 09:45:02.934478  1897 net.cpp:84] Creating Layer res2a_branch2a_relu
I0623 09:45:02.934495  1897 net.cpp:406] res2a_branch2a_relu <- res2a_branch2a
I0623 09:45:02.934514  1897 net.cpp:367] res2a_branch2a_relu -> res2a_branch2a (in-place)
I0623 09:45:02.934535  1897 net.cpp:122] Setting up res2a_branch2a_relu
I0623 09:45:02.934554  1897 net.cpp:129] Top shape: 8 64 64 64 (2097152)
I0623 09:45:02.934571  1897 net.cpp:137] Memory required for data: 299892832
I0623 09:45:02.934587  1897 layer_factory.hpp:77] Creating layer res2a_branch2b
I0623 09:45:02.934607  1897 net.cpp:84] Creating Layer res2a_branch2b
I0623 09:45:02.934624  1897 net.cpp:406] res2a_branch2b <- res2a_branch2a
I0623 09:45:02.934644  1897 net.cpp:380] res2a_branch2b -> res2a_branch2b
I0623 09:45:02.934749  1897 net.cpp:122] Setting up res2a_branch2b
I0623 09:45:02.934775  1897 net.cpp:129] Top shape: 8 64 64 64 (2097152)
I0623 09:45:02.934793  1897 net.cpp:137] Memory required for data: 308281440
I0623 09:45:02.934813  1897 layer_factory.hpp:77] Creating layer bn2a_branch2b
I0623 09:45:02.934839  1897 net.cpp:84] Creating Layer bn2a_branch2b
I0623 09:45:02.934857  1897 net.cpp:406] bn2a_branch2b <- res2a_branch2b
I0623 09:45:02.934877  1897 net.cpp:367] bn2a_branch2b -> res2a_branch2b (in-place)
I0623 09:45:02.934916  1897 net.cpp:122] Setting up bn2a_branch2b
I0623 09:45:02.934937  1897 net.cpp:129] Top shape: 8 64 64 64 (2097152)
I0623 09:45:02.934952  1897 net.cpp:137] Memory required for data: 316670048
I0623 09:45:02.934973  1897 layer_factory.hpp:77] Creating layer scale2a_branch2b
I0623 09:45:02.934995  1897 net.cpp:84] Creating Layer scale2a_branch2b
I0623 09:45:02.935012  1897 net.cpp:406] scale2a_branch2b <- res2a_branch2b
I0623 09:45:02.935031  1897 net.cpp:367] scale2a_branch2b -> res2a_branch2b (in-place)
I0623 09:45:02.935056  1897 layer_factory.hpp:77] Creating layer scale2a_branch2b
I0623 09:45:02.935097  1897 net.cpp:122] Setting up scale2a_branch2b
I0623 09:45:02.935118  1897 net.cpp:129] Top shape: 8 64 64 64 (2097152)
I0623 09:45:02.935134  1897 net.cpp:137] Memory required for data: 325058656
I0623 09:45:02.935153  1897 layer_factory.hpp:77] Creating layer res2a_branch2b_relu
I0623 09:45:02.935173  1897 net.cpp:84] Creating Layer res2a_branch2b_relu
I0623 09:45:02.935190  1897 net.cpp:406] res2a_branch2b_relu <- res2a_branch2b
I0623 09:45:02.935210  1897 net.cpp:367] res2a_branch2b_relu -> res2a_branch2b (in-place)
I0623 09:45:02.935230  1897 net.cpp:122] Setting up res2a_branch2b_relu
I0623 09:45:02.935250  1897 net.cpp:129] Top shape: 8 64 64 64 (2097152)
I0623 09:45:02.935266  1897 net.cpp:137] Memory required for data: 333447264
I0623 09:45:02.935281  1897 layer_factory.hpp:77] Creating layer res2a_branch2c
I0623 09:45:02.935302  1897 net.cpp:84] Creating Layer res2a_branch2c
I0623 09:45:02.935320  1897 net.cpp:406] res2a_branch2c <- res2a_branch2b
I0623 09:45:02.935346  1897 net.cpp:380] res2a_branch2c -> res2a_branch2c
I0623 09:45:02.935417  1897 net.cpp:122] Setting up res2a_branch2c
I0623 09:45:02.935441  1897 net.cpp:129] Top shape: 8 256 64 64 (8388608)
I0623 09:45:02.935456  1897 net.cpp:137] Memory required for data: 367001696
I0623 09:45:02.935475  1897 layer_factory.hpp:77] Creating layer bn2a_branch2c
I0623 09:45:02.935497  1897 net.cpp:84] Creating Layer bn2a_branch2c
I0623 09:45:02.935513  1897 net.cpp:406] bn2a_branch2c <- res2a_branch2c
I0623 09:45:02.935533  1897 net.cpp:367] bn2a_branch2c -> res2a_branch2c (in-place)
I0623 09:45:02.935570  1897 net.cpp:122] Setting up bn2a_branch2c
I0623 09:45:02.935590  1897 net.cpp:129] Top shape: 8 256 64 64 (8388608)
I0623 09:45:02.935607  1897 net.cpp:137] Memory required for data: 400556128
I0623 09:45:02.935629  1897 layer_factory.hpp:77] Creating layer scale2a_branch2c
I0623 09:45:02.935649  1897 net.cpp:84] Creating Layer scale2a_branch2c
I0623 09:45:02.935667  1897 net.cpp:406] scale2a_branch2c <- res2a_branch2c
I0623 09:45:02.935688  1897 net.cpp:367] scale2a_branch2c -> res2a_branch2c (in-place)
I0623 09:45:02.935714  1897 layer_factory.hpp:77] Creating layer scale2a_branch2c
I0623 09:45:02.935756  1897 net.cpp:122] Setting up scale2a_branch2c
I0623 09:45:02.935777  1897 net.cpp:129] Top shape: 8 256 64 64 (8388608)
I0623 09:45:02.935794  1897 net.cpp:137] Memory required for data: 434110560
I0623 09:45:02.935813  1897 layer_factory.hpp:77] Creating layer res2a
I0623 09:45:02.935835  1897 net.cpp:84] Creating Layer res2a
I0623 09:45:02.935853  1897 net.cpp:406] res2a <- res2a_branch1
I0623 09:45:02.935870  1897 net.cpp:406] res2a <- res2a_branch2c
I0623 09:45:02.935889  1897 net.cpp:380] res2a -> res2a
I0623 09:45:02.935912  1897 net.cpp:122] Setting up res2a
I0623 09:45:02.935932  1897 net.cpp:129] Top shape: 8 256 64 64 (8388608)
I0623 09:45:02.935948  1897 net.cpp:137] Memory required for data: 467664992
I0623 09:45:02.935964  1897 layer_factory.hpp:77] Creating layer res2a_relu
I0623 09:45:02.935986  1897 net.cpp:84] Creating Layer res2a_relu
I0623 09:45:02.936003  1897 net.cpp:406] res2a_relu <- res2a
I0623 09:45:02.936022  1897 net.cpp:367] res2a_relu -> res2a (in-place)
I0623 09:45:02.936043  1897 net.cpp:122] Setting up res2a_relu
I0623 09:45:02.936065  1897 net.cpp:129] Top shape: 8 256 64 64 (8388608)
I0623 09:45:02.936081  1897 net.cpp:137] Memory required for data: 501219424
I0623 09:45:02.936098  1897 layer_factory.hpp:77] Creating layer res2a_res2a_relu_0_split
I0623 09:45:02.936117  1897 net.cpp:84] Creating Layer res2a_res2a_relu_0_split
I0623 09:45:02.936136  1897 net.cpp:406] res2a_res2a_relu_0_split <- res2a
I0623 09:45:02.936158  1897 net.cpp:380] res2a_res2a_relu_0_split -> res2a_res2a_relu_0_split_0
I0623 09:45:02.936182  1897 net.cpp:380] res2a_res2a_relu_0_split -> res2a_res2a_relu_0_split_1
I0623 09:45:02.936204  1897 net.cpp:122] Setting up res2a_res2a_relu_0_split
I0623 09:45:02.936224  1897 net.cpp:129] Top shape: 8 256 64 64 (8388608)
I0623 09:45:02.936241  1897 net.cpp:129] Top shape: 8 256 64 64 (8388608)
I0623 09:45:02.936259  1897 net.cpp:137] Memory required for data: 568328288
I0623 09:45:02.936278  1897 layer_factory.hpp:77] Creating layer res2b_branch2a
I0623 09:45:02.936302  1897 net.cpp:84] Creating Layer res2b_branch2a
I0623 09:45:02.936322  1897 net.cpp:406] res2b_branch2a <- res2a_res2a_relu_0_split_0
I0623 09:45:02.936343  1897 net.cpp:380] res2b_branch2a -> res2b_branch2a
I0623 09:45:02.936406  1897 net.cpp:122] Setting up res2b_branch2a
I0623 09:45:02.936434  1897 net.cpp:129] Top shape: 8 64 64 64 (2097152)
I0623 09:45:02.936460  1897 net.cpp:137] Memory required for data: 576716896
I0623 09:45:02.936480  1897 layer_factory.hpp:77] Creating layer bn2b_branch2a
I0623 09:45:02.936499  1897 net.cpp:84] Creating Layer bn2b_branch2a
I0623 09:45:02.936518  1897 net.cpp:406] bn2b_branch2a <- res2b_branch2a
I0623 09:45:02.936539  1897 net.cpp:367] bn2b_branch2a -> res2b_branch2a (in-place)
I0623 09:45:02.936578  1897 net.cpp:122] Setting up bn2b_branch2a
I0623 09:45:02.936599  1897 net.cpp:129] Top shape: 8 64 64 64 (2097152)
I0623 09:45:02.936620  1897 net.cpp:137] Memory required for data: 585105504
I0623 09:45:02.936651  1897 layer_factory.hpp:77] Creating layer scale2b_branch2a
I0623 09:45:02.936672  1897 net.cpp:84] Creating Layer scale2b_branch2a
I0623 09:45:02.936691  1897 net.cpp:406] scale2b_branch2a <- res2b_branch2a
I0623 09:45:02.936708  1897 net.cpp:367] scale2b_branch2a -> res2b_branch2a (in-place)
I0623 09:45:02.936734  1897 layer_factory.hpp:77] Creating layer scale2b_branch2a
I0623 09:45:02.936776  1897 net.cpp:122] Setting up scale2b_branch2a
I0623 09:45:02.936797  1897 net.cpp:129] Top shape: 8 64 64 64 (2097152)
I0623 09:45:02.936815  1897 net.cpp:137] Memory required for data: 593494112
I0623 09:45:02.936835  1897 layer_factory.hpp:77] Creating layer res2b_branch2a_relu
I0623 09:45:02.936854  1897 net.cpp:84] Creating Layer res2b_branch2a_relu
I0623 09:45:02.936870  1897 net.cpp:406] res2b_branch2a_relu <- res2b_branch2a
I0623 09:45:02.936890  1897 net.cpp:367] res2b_branch2a_relu -> res2b_branch2a (in-place)
I0623 09:45:02.936911  1897 net.cpp:122] Setting up res2b_branch2a_relu
I0623 09:45:02.936931  1897 net.cpp:129] Top shape: 8 64 64 64 (2097152)
I0623 09:45:02.936947  1897 net.cpp:137] Memory required for data: 601882720
I0623 09:45:02.936964  1897 layer_factory.hpp:77] Creating layer res2b_branch2b
I0623 09:45:02.936985  1897 net.cpp:84] Creating Layer res2b_branch2b
I0623 09:45:02.937003  1897 net.cpp:406] res2b_branch2b <- res2b_branch2a
I0623 09:45:02.937023  1897 net.cpp:380] res2b_branch2b -> res2b_branch2b
I0623 09:45:02.937124  1897 net.cpp:122] Setting up res2b_branch2b
I0623 09:45:02.937150  1897 net.cpp:129] Top shape: 8 64 64 64 (2097152)
I0623 09:45:02.937167  1897 net.cpp:137] Memory required for data: 610271328
I0623 09:45:02.937188  1897 layer_factory.hpp:77] Creating layer bn2b_branch2b
I0623 09:45:02.937208  1897 net.cpp:84] Creating Layer bn2b_branch2b
I0623 09:45:02.937227  1897 net.cpp:406] bn2b_branch2b <- res2b_branch2b
I0623 09:45:02.937247  1897 net.cpp:367] bn2b_branch2b -> res2b_branch2b (in-place)
I0623 09:45:02.937286  1897 net.cpp:122] Setting up bn2b_branch2b
I0623 09:45:02.937309  1897 net.cpp:129] Top shape: 8 64 64 64 (2097152)
I0623 09:45:02.937325  1897 net.cpp:137] Memory required for data: 618659936
I0623 09:45:02.937345  1897 layer_factory.hpp:77] Creating layer scale2b_branch2b
I0623 09:45:02.937367  1897 net.cpp:84] Creating Layer scale2b_branch2b
I0623 09:45:02.937386  1897 net.cpp:406] scale2b_branch2b <- res2b_branch2b
I0623 09:45:02.937405  1897 net.cpp:367] scale2b_branch2b -> res2b_branch2b (in-place)
I0623 09:45:02.937430  1897 layer_factory.hpp:77] Creating layer scale2b_branch2b
I0623 09:45:02.937470  1897 net.cpp:122] Setting up scale2b_branch2b
I0623 09:45:02.937494  1897 net.cpp:129] Top shape: 8 64 64 64 (2097152)
I0623 09:45:02.937510  1897 net.cpp:137] Memory required for data: 627048544
I0623 09:45:02.937530  1897 layer_factory.hpp:77] Creating layer res2b_branch2b_relu
I0623 09:45:02.937552  1897 net.cpp:84] Creating Layer res2b_branch2b_relu
I0623 09:45:02.937569  1897 net.cpp:406] res2b_branch2b_relu <- res2b_branch2b
I0623 09:45:02.937587  1897 net.cpp:367] res2b_branch2b_relu -> res2b_branch2b (in-place)
I0623 09:45:02.937608  1897 net.cpp:122] Setting up res2b_branch2b_relu
I0623 09:45:02.937626  1897 net.cpp:129] Top shape: 8 64 64 64 (2097152)
I0623 09:45:02.937643  1897 net.cpp:137] Memory required for data: 635437152
I0623 09:45:02.937659  1897 layer_factory.hpp:77] Creating layer res2b_branch2c
I0623 09:45:02.937681  1897 net.cpp:84] Creating Layer res2b_branch2c
I0623 09:45:02.937698  1897 net.cpp:406] res2b_branch2c <- res2b_branch2b
I0623 09:45:02.937719  1897 net.cpp:380] res2b_branch2c -> res2b_branch2c
I0623 09:45:02.937779  1897 net.cpp:122] Setting up res2b_branch2c
I0623 09:45:02.937803  1897 net.cpp:129] Top shape: 8 256 64 64 (8388608)
I0623 09:45:02.937819  1897 net.cpp:137] Memory required for data: 668991584
I0623 09:45:02.937837  1897 layer_factory.hpp:77] Creating layer bn2b_branch2c
I0623 09:45:02.937865  1897 net.cpp:84] Creating Layer bn2b_branch2c
I0623 09:45:02.937885  1897 net.cpp:406] bn2b_branch2c <- res2b_branch2c
I0623 09:45:02.937904  1897 net.cpp:367] bn2b_branch2c -> res2b_branch2c (in-place)
I0623 09:45:02.937942  1897 net.cpp:122] Setting up bn2b_branch2c
I0623 09:45:02.937964  1897 net.cpp:129] Top shape: 8 256 64 64 (8388608)
I0623 09:45:02.937980  1897 net.cpp:137] Memory required for data: 702546016
I0623 09:45:02.938016  1897 layer_factory.hpp:77] Creating layer scale2b_branch2c
I0623 09:45:02.938037  1897 net.cpp:84] Creating Layer scale2b_branch2c
I0623 09:45:02.938055  1897 net.cpp:406] scale2b_branch2c <- res2b_branch2c
I0623 09:45:02.938076  1897 net.cpp:367] scale2b_branch2c -> res2b_branch2c (in-place)
I0623 09:45:02.938102  1897 layer_factory.hpp:77] Creating layer scale2b_branch2c
I0623 09:45:02.938144  1897 net.cpp:122] Setting up scale2b_branch2c
I0623 09:45:02.938168  1897 net.cpp:129] Top shape: 8 256 64 64 (8388608)
I0623 09:45:02.938184  1897 net.cpp:137] Memory required for data: 736100448
I0623 09:45:02.938205  1897 layer_factory.hpp:77] Creating layer res2b
I0623 09:45:02.938226  1897 net.cpp:84] Creating Layer res2b
I0623 09:45:02.938243  1897 net.cpp:406] res2b <- res2a_res2a_relu_0_split_1
I0623 09:45:02.938261  1897 net.cpp:406] res2b <- res2b_branch2c
I0623 09:45:02.938279  1897 net.cpp:380] res2b -> res2b
I0623 09:45:02.938302  1897 net.cpp:122] Setting up res2b
I0623 09:45:02.938321  1897 net.cpp:129] Top shape: 8 256 64 64 (8388608)
I0623 09:45:02.938338  1897 net.cpp:137] Memory required for data: 769654880
I0623 09:45:02.938354  1897 layer_factory.hpp:77] Creating layer res2b_relu
I0623 09:45:02.938374  1897 net.cpp:84] Creating Layer res2b_relu
I0623 09:45:02.938391  1897 net.cpp:406] res2b_relu <- res2b
I0623 09:45:02.938410  1897 net.cpp:367] res2b_relu -> res2b (in-place)
I0623 09:45:02.938429  1897 net.cpp:122] Setting up res2b_relu
I0623 09:45:02.938449  1897 net.cpp:129] Top shape: 8 256 64 64 (8388608)
I0623 09:45:02.938464  1897 net.cpp:137] Memory required for data: 803209312
I0623 09:45:02.938480  1897 layer_factory.hpp:77] Creating layer res2b_res2b_relu_0_split
I0623 09:45:02.938498  1897 net.cpp:84] Creating Layer res2b_res2b_relu_0_split
I0623 09:45:02.938515  1897 net.cpp:406] res2b_res2b_relu_0_split <- res2b
I0623 09:45:02.938534  1897 net.cpp:380] res2b_res2b_relu_0_split -> res2b_res2b_relu_0_split_0
I0623 09:45:02.938556  1897 net.cpp:380] res2b_res2b_relu_0_split -> res2b_res2b_relu_0_split_1
I0623 09:45:02.938581  1897 net.cpp:122] Setting up res2b_res2b_relu_0_split
I0623 09:45:02.938601  1897 net.cpp:129] Top shape: 8 256 64 64 (8388608)
I0623 09:45:02.938619  1897 net.cpp:129] Top shape: 8 256 64 64 (8388608)
I0623 09:45:02.938635  1897 net.cpp:137] Memory required for data: 870318176
I0623 09:45:02.938652  1897 layer_factory.hpp:77] Creating layer res2c_branch2a
I0623 09:45:02.938685  1897 net.cpp:84] Creating Layer res2c_branch2a
I0623 09:45:02.938706  1897 net.cpp:406] res2c_branch2a <- res2b_res2b_relu_0_split_0
I0623 09:45:02.938726  1897 net.cpp:380] res2c_branch2a -> res2c_branch2a
I0623 09:45:02.938788  1897 net.cpp:122] Setting up res2c_branch2a
I0623 09:45:02.938812  1897 net.cpp:129] Top shape: 8 64 64 64 (2097152)
I0623 09:45:02.938829  1897 net.cpp:137] Memory required for data: 878706784
I0623 09:45:02.938848  1897 layer_factory.hpp:77] Creating layer bn2c_branch2a
I0623 09:45:02.938870  1897 net.cpp:84] Creating Layer bn2c_branch2a
I0623 09:45:02.938887  1897 net.cpp:406] bn2c_branch2a <- res2c_branch2a
I0623 09:45:02.938905  1897 net.cpp:367] bn2c_branch2a -> res2c_branch2a (in-place)
I0623 09:45:02.938942  1897 net.cpp:122] Setting up bn2c_branch2a
I0623 09:45:02.938963  1897 net.cpp:129] Top shape: 8 64 64 64 (2097152)
I0623 09:45:02.938980  1897 net.cpp:137] Memory required for data: 887095392
I0623 09:45:02.939002  1897 layer_factory.hpp:77] Creating layer scale2c_branch2a
I0623 09:45:02.939023  1897 net.cpp:84] Creating Layer scale2c_branch2a
I0623 09:45:02.939041  1897 net.cpp:406] scale2c_branch2a <- res2c_branch2a
I0623 09:45:02.939065  1897 net.cpp:367] scale2c_branch2a -> res2c_branch2a (in-place)
I0623 09:45:02.939090  1897 layer_factory.hpp:77] Creating layer scale2c_branch2a
I0623 09:45:02.939132  1897 net.cpp:122] Setting up scale2c_branch2a
I0623 09:45:02.939154  1897 net.cpp:129] Top shape: 8 64 64 64 (2097152)
I0623 09:45:02.939170  1897 net.cpp:137] Memory required for data: 895484000
I0623 09:45:02.939190  1897 layer_factory.hpp:77] Creating layer res2c_branch2a_relu
I0623 09:45:02.939211  1897 net.cpp:84] Creating Layer res2c_branch2a_relu
I0623 09:45:02.939229  1897 net.cpp:406] res2c_branch2a_relu <- res2c_branch2a
I0623 09:45:02.939247  1897 net.cpp:367] res2c_branch2a_relu -> res2c_branch2a (in-place)
I0623 09:45:02.939266  1897 net.cpp:122] Setting up res2c_branch2a_relu
I0623 09:45:02.939285  1897 net.cpp:129] Top shape: 8 64 64 64 (2097152)
I0623 09:45:02.939302  1897 net.cpp:137] Memory required for data: 903872608
I0623 09:45:02.939319  1897 layer_factory.hpp:77] Creating layer res2c_branch2b
I0623 09:45:02.939342  1897 net.cpp:84] Creating Layer res2c_branch2b
I0623 09:45:02.939360  1897 net.cpp:406] res2c_branch2b <- res2c_branch2a
I0623 09:45:02.939380  1897 net.cpp:380] res2c_branch2b -> res2c_branch2b
I0623 09:45:02.939478  1897 net.cpp:122] Setting up res2c_branch2b
I0623 09:45:02.939502  1897 net.cpp:129] Top shape: 8 64 64 64 (2097152)
I0623 09:45:02.939518  1897 net.cpp:137] Memory required for data: 912261216
I0623 09:45:02.939538  1897 layer_factory.hpp:77] Creating layer bn2c_branch2b
I0623 09:45:02.939558  1897 net.cpp:84] Creating Layer bn2c_branch2b
I0623 09:45:02.939576  1897 net.cpp:406] bn2c_branch2b <- res2c_branch2b
I0623 09:45:02.939597  1897 net.cpp:367] bn2c_branch2b -> res2c_branch2b (in-place)
I0623 09:45:02.939635  1897 net.cpp:122] Setting up bn2c_branch2b
I0623 09:45:02.939656  1897 net.cpp:129] Top shape: 8 64 64 64 (2097152)
I0623 09:45:02.939673  1897 net.cpp:137] Memory required for data: 920649824
I0623 09:45:02.939695  1897 layer_factory.hpp:77] Creating layer scale2c_branch2b
I0623 09:45:02.939715  1897 net.cpp:84] Creating Layer scale2c_branch2b
I0623 09:45:02.939733  1897 net.cpp:406] scale2c_branch2b <- res2c_branch2b
I0623 09:45:02.939752  1897 net.cpp:367] scale2c_branch2b -> res2c_branch2b (in-place)
I0623 09:45:02.939786  1897 layer_factory.hpp:77] Creating layer scale2c_branch2b
I0623 09:45:02.939827  1897 net.cpp:122] Setting up scale2c_branch2b
I0623 09:45:02.939849  1897 net.cpp:129] Top shape: 8 64 64 64 (2097152)
I0623 09:45:02.939865  1897 net.cpp:137] Memory required for data: 929038432
I0623 09:45:02.939885  1897 layer_factory.hpp:77] Creating layer res2c_branch2b_relu
I0623 09:45:02.939906  1897 net.cpp:84] Creating Layer res2c_branch2b_relu
I0623 09:45:02.939924  1897 net.cpp:406] res2c_branch2b_relu <- res2c_branch2b
I0623 09:45:02.939942  1897 net.cpp:367] res2c_branch2b_relu -> res2c_branch2b (in-place)
I0623 09:45:02.939961  1897 net.cpp:122] Setting up res2c_branch2b_relu
I0623 09:45:02.939980  1897 net.cpp:129] Top shape: 8 64 64 64 (2097152)
I0623 09:45:02.939996  1897 net.cpp:137] Memory required for data: 937427040
I0623 09:45:02.940011  1897 layer_factory.hpp:77] Creating layer res2c_branch2c
I0623 09:45:02.940033  1897 net.cpp:84] Creating Layer res2c_branch2c
I0623 09:45:02.940052  1897 net.cpp:406] res2c_branch2c <- res2c_branch2b
I0623 09:45:02.940070  1897 net.cpp:380] res2c_branch2c -> res2c_branch2c
I0623 09:45:02.940134  1897 net.cpp:122] Setting up res2c_branch2c
I0623 09:45:02.940158  1897 net.cpp:129] Top shape: 8 256 64 64 (8388608)
I0623 09:45:02.940176  1897 net.cpp:137] Memory required for data: 970981472
I0623 09:45:02.940193  1897 layer_factory.hpp:77] Creating layer bn2c_branch2c
I0623 09:45:02.940212  1897 net.cpp:84] Creating Layer bn2c_branch2c
I0623 09:45:02.940229  1897 net.cpp:406] bn2c_branch2c <- res2c_branch2c
I0623 09:45:02.940248  1897 net.cpp:367] bn2c_branch2c -> res2c_branch2c (in-place)
I0623 09:45:02.940287  1897 net.cpp:122] Setting up bn2c_branch2c
I0623 09:45:02.940309  1897 net.cpp:129] Top shape: 8 256 64 64 (8388608)
I0623 09:45:02.940328  1897 net.cpp:137] Memory required for data: 1004535904
I0623 09:45:02.940361  1897 layer_factory.hpp:77] Creating layer scale2c_branch2c
I0623 09:45:02.940382  1897 net.cpp:84] Creating Layer scale2c_branch2c
I0623 09:45:02.940399  1897 net.cpp:406] scale2c_branch2c <- res2c_branch2c
I0623 09:45:02.940418  1897 net.cpp:367] scale2c_branch2c -> res2c_branch2c (in-place)
I0623 09:45:02.940446  1897 layer_factory.hpp:77] Creating layer scale2c_branch2c
I0623 09:45:02.940490  1897 net.cpp:122] Setting up scale2c_branch2c
I0623 09:45:02.940511  1897 net.cpp:129] Top shape: 8 256 64 64 (8388608)
I0623 09:45:02.940527  1897 net.cpp:137] Memory required for data: 1038090336
I0623 09:45:02.940548  1897 layer_factory.hpp:77] Creating layer res2c
I0623 09:45:02.940569  1897 net.cpp:84] Creating Layer res2c
I0623 09:45:02.940587  1897 net.cpp:406] res2c <- res2b_res2b_relu_0_split_1
I0623 09:45:02.940604  1897 net.cpp:406] res2c <- res2c_branch2c
I0623 09:45:02.940623  1897 net.cpp:380] res2c -> res2c
I0623 09:45:02.940646  1897 net.cpp:122] Setting up res2c
I0623 09:45:02.940666  1897 net.cpp:129] Top shape: 8 256 64 64 (8388608)
I0623 09:45:02.940683  1897 net.cpp:137] Memory required for data: 1071644768
I0623 09:45:02.940699  1897 layer_factory.hpp:77] Creating layer res2c_relu
I0623 09:45:02.940717  1897 net.cpp:84] Creating Layer res2c_relu
I0623 09:45:02.940734  1897 net.cpp:406] res2c_relu <- res2c
I0623 09:45:02.940752  1897 net.cpp:367] res2c_relu -> res2c (in-place)
I0623 09:45:02.940773  1897 net.cpp:122] Setting up res2c_relu
I0623 09:45:02.940791  1897 net.cpp:129] Top shape: 8 256 64 64 (8388608)
I0623 09:45:02.940807  1897 net.cpp:137] Memory required for data: 1105199200
I0623 09:45:02.940824  1897 layer_factory.hpp:77] Creating layer res2c_res2c_relu_0_split
I0623 09:45:02.940841  1897 net.cpp:84] Creating Layer res2c_res2c_relu_0_split
I0623 09:45:02.940857  1897 net.cpp:406] res2c_res2c_relu_0_split <- res2c
I0623 09:45:02.940879  1897 net.cpp:380] res2c_res2c_relu_0_split -> res2c_res2c_relu_0_split_0
I0623 09:45:02.940903  1897 net.cpp:380] res2c_res2c_relu_0_split -> res2c_res2c_relu_0_split_1
I0623 09:45:02.940927  1897 net.cpp:122] Setting up res2c_res2c_relu_0_split
I0623 09:45:02.940946  1897 net.cpp:129] Top shape: 8 256 64 64 (8388608)
I0623 09:45:02.940963  1897 net.cpp:129] Top shape: 8 256 64 64 (8388608)
I0623 09:45:02.940979  1897 net.cpp:137] Memory required for data: 1172308064
I0623 09:45:02.940995  1897 layer_factory.hpp:77] Creating layer res3a_branch1
I0623 09:45:02.941017  1897 net.cpp:84] Creating Layer res3a_branch1
I0623 09:45:02.941035  1897 net.cpp:406] res3a_branch1 <- res2c_res2c_relu_0_split_0
I0623 09:45:02.941054  1897 net.cpp:380] res3a_branch1 -> res3a_branch1
I0623 09:45:02.941315  1897 net.cpp:122] Setting up res3a_branch1
I0623 09:45:02.941339  1897 net.cpp:129] Top shape: 8 512 32 32 (4194304)
I0623 09:45:02.941355  1897 net.cpp:137] Memory required for data: 1189085280
I0623 09:45:02.941375  1897 layer_factory.hpp:77] Creating layer bn3a_branch1
I0623 09:45:02.941393  1897 net.cpp:84] Creating Layer bn3a_branch1
I0623 09:45:02.941411  1897 net.cpp:406] bn3a_branch1 <- res3a_branch1
I0623 09:45:02.941431  1897 net.cpp:367] bn3a_branch1 -> res3a_branch1 (in-place)
I0623 09:45:02.941468  1897 net.cpp:122] Setting up bn3a_branch1
I0623 09:45:02.941495  1897 net.cpp:129] Top shape: 8 512 32 32 (4194304)
I0623 09:45:02.941516  1897 net.cpp:137] Memory required for data: 1205862496
I0623 09:45:02.941540  1897 layer_factory.hpp:77] Creating layer scale3a_branch1
I0623 09:45:02.941561  1897 net.cpp:84] Creating Layer scale3a_branch1
I0623 09:45:02.941579  1897 net.cpp:406] scale3a_branch1 <- res3a_branch1
I0623 09:45:02.941598  1897 net.cpp:367] scale3a_branch1 -> res3a_branch1 (in-place)
I0623 09:45:02.941625  1897 layer_factory.hpp:77] Creating layer scale3a_branch1
I0623 09:45:02.941659  1897 net.cpp:122] Setting up scale3a_branch1
I0623 09:45:02.941680  1897 net.cpp:129] Top shape: 8 512 32 32 (4194304)
I0623 09:45:02.941696  1897 net.cpp:137] Memory required for data: 1222639712
I0623 09:45:02.941725  1897 layer_factory.hpp:77] Creating layer res3a_branch2a
I0623 09:45:02.941748  1897 net.cpp:84] Creating Layer res3a_branch2a
I0623 09:45:02.941766  1897 net.cpp:406] res3a_branch2a <- res2c_res2c_relu_0_split_1
I0623 09:45:02.941787  1897 net.cpp:380] res3a_branch2a -> res3a_branch2a
I0623 09:45:02.941876  1897 net.cpp:122] Setting up res3a_branch2a
I0623 09:45:02.941900  1897 net.cpp:129] Top shape: 8 128 32 32 (1048576)
I0623 09:45:02.941915  1897 net.cpp:137] Memory required for data: 1226834016
I0623 09:45:02.941934  1897 layer_factory.hpp:77] Creating layer bn3a_branch2a
I0623 09:45:02.941953  1897 net.cpp:84] Creating Layer bn3a_branch2a
I0623 09:45:02.941970  1897 net.cpp:406] bn3a_branch2a <- res3a_branch2a
I0623 09:45:02.941992  1897 net.cpp:367] bn3a_branch2a -> res3a_branch2a (in-place)
I0623 09:45:02.942025  1897 net.cpp:122] Setting up bn3a_branch2a
I0623 09:45:02.942046  1897 net.cpp:129] Top shape: 8 128 32 32 (1048576)
I0623 09:45:02.942062  1897 net.cpp:137] Memory required for data: 1231028320
I0623 09:45:02.942085  1897 layer_factory.hpp:77] Creating layer scale3a_branch2a
I0623 09:45:02.942106  1897 net.cpp:84] Creating Layer scale3a_branch2a
I0623 09:45:02.942124  1897 net.cpp:406] scale3a_branch2a <- res3a_branch2a
I0623 09:45:02.942142  1897 net.cpp:367] scale3a_branch2a -> res3a_branch2a (in-place)
I0623 09:45:02.942167  1897 layer_factory.hpp:77] Creating layer scale3a_branch2a
I0623 09:45:02.942203  1897 net.cpp:122] Setting up scale3a_branch2a
I0623 09:45:02.942224  1897 net.cpp:129] Top shape: 8 128 32 32 (1048576)
I0623 09:45:02.942239  1897 net.cpp:137] Memory required for data: 1235222624
I0623 09:45:02.942260  1897 layer_factory.hpp:77] Creating layer res3a_branch2a_relu
I0623 09:45:02.942279  1897 net.cpp:84] Creating Layer res3a_branch2a_relu
I0623 09:45:02.942296  1897 net.cpp:406] res3a_branch2a_relu <- res3a_branch2a
I0623 09:45:02.942317  1897 net.cpp:367] res3a_branch2a_relu -> res3a_branch2a (in-place)
I0623 09:45:02.942337  1897 net.cpp:122] Setting up res3a_branch2a_relu
I0623 09:45:02.942355  1897 net.cpp:129] Top shape: 8 128 32 32 (1048576)
I0623 09:45:02.942373  1897 net.cpp:137] Memory required for data: 1239416928
I0623 09:45:02.942389  1897 layer_factory.hpp:77] Creating layer res3a_branch2b
I0623 09:45:02.942409  1897 net.cpp:84] Creating Layer res3a_branch2b
I0623 09:45:02.942426  1897 net.cpp:406] res3a_branch2b <- res3a_branch2a
I0623 09:45:02.942445  1897 net.cpp:380] res3a_branch2b -> res3a_branch2b
I0623 09:45:02.942739  1897 net.cpp:122] Setting up res3a_branch2b
I0623 09:45:02.942764  1897 net.cpp:129] Top shape: 8 128 32 32 (1048576)
I0623 09:45:02.942781  1897 net.cpp:137] Memory required for data: 1243611232
I0623 09:45:02.942801  1897 layer_factory.hpp:77] Creating layer bn3a_branch2b
I0623 09:45:02.942822  1897 net.cpp:84] Creating Layer bn3a_branch2b
I0623 09:45:02.942840  1897 net.cpp:406] bn3a_branch2b <- res3a_branch2b
I0623 09:45:02.942859  1897 net.cpp:367] bn3a_branch2b -> res3a_branch2b (in-place)
I0623 09:45:02.942893  1897 net.cpp:122] Setting up bn3a_branch2b
I0623 09:45:02.942914  1897 net.cpp:129] Top shape: 8 128 32 32 (1048576)
I0623 09:45:02.942930  1897 net.cpp:137] Memory required for data: 1247805536
I0623 09:45:02.942952  1897 layer_factory.hpp:77] Creating layer scale3a_branch2b
I0623 09:45:02.942973  1897 net.cpp:84] Creating Layer scale3a_branch2b
I0623 09:45:02.942991  1897 net.cpp:406] scale3a_branch2b <- res3a_branch2b
I0623 09:45:02.943009  1897 net.cpp:367] scale3a_branch2b -> res3a_branch2b (in-place)
I0623 09:45:02.943037  1897 layer_factory.hpp:77] Creating layer scale3a_branch2b
I0623 09:45:02.943071  1897 net.cpp:122] Setting up scale3a_branch2b
I0623 09:45:02.943092  1897 net.cpp:129] Top shape: 8 128 32 32 (1048576)
I0623 09:45:02.943109  1897 net.cpp:137] Memory required for data: 1251999840
I0623 09:45:02.943130  1897 layer_factory.hpp:77] Creating layer res3a_branch2b_relu
I0623 09:45:02.943148  1897 net.cpp:84] Creating Layer res3a_branch2b_relu
I0623 09:45:02.943171  1897 net.cpp:406] res3a_branch2b_relu <- res3a_branch2b
I0623 09:45:02.943189  1897 net.cpp:367] res3a_branch2b_relu -> res3a_branch2b (in-place)
I0623 09:45:02.943209  1897 net.cpp:122] Setting up res3a_branch2b_relu
I0623 09:45:02.943229  1897 net.cpp:129] Top shape: 8 128 32 32 (1048576)
I0623 09:45:02.943246  1897 net.cpp:137] Memory required for data: 1256194144
I0623 09:45:02.943262  1897 layer_factory.hpp:77] Creating layer res3a_branch2c
I0623 09:45:02.943289  1897 net.cpp:84] Creating Layer res3a_branch2c
I0623 09:45:02.943306  1897 net.cpp:406] res3a_branch2c <- res3a_branch2b
I0623 09:45:02.943336  1897 net.cpp:380] res3a_branch2c -> res3a_branch2c
I0623 09:45:02.943478  1897 net.cpp:122] Setting up res3a_branch2c
I0623 09:45:02.943503  1897 net.cpp:129] Top shape: 8 512 32 32 (4194304)
I0623 09:45:02.943521  1897 net.cpp:137] Memory required for data: 1272971360
I0623 09:45:02.943541  1897 layer_factory.hpp:77] Creating layer bn3a_branch2c
I0623 09:45:02.943562  1897 net.cpp:84] Creating Layer bn3a_branch2c
I0623 09:45:02.943579  1897 net.cpp:406] bn3a_branch2c <- res3a_branch2c
I0623 09:45:02.943598  1897 net.cpp:367] bn3a_branch2c -> res3a_branch2c (in-place)
I0623 09:45:02.943632  1897 net.cpp:122] Setting up bn3a_branch2c
I0623 09:45:02.943652  1897 net.cpp:129] Top shape: 8 512 32 32 (4194304)
I0623 09:45:02.943670  1897 net.cpp:137] Memory required for data: 1289748576
I0623 09:45:02.943693  1897 layer_factory.hpp:77] Creating layer scale3a_branch2c
I0623 09:45:02.943717  1897 net.cpp:84] Creating Layer scale3a_branch2c
I0623 09:45:02.943734  1897 net.cpp:406] scale3a_branch2c <- res3a_branch2c
I0623 09:45:02.943753  1897 net.cpp:367] scale3a_branch2c -> res3a_branch2c (in-place)
I0623 09:45:02.943780  1897 layer_factory.hpp:77] Creating layer scale3a_branch2c
I0623 09:45:02.943820  1897 net.cpp:122] Setting up scale3a_branch2c
I0623 09:45:02.943841  1897 net.cpp:129] Top shape: 8 512 32 32 (4194304)
I0623 09:45:02.943857  1897 net.cpp:137] Memory required for data: 1306525792
I0623 09:45:02.943877  1897 layer_factory.hpp:77] Creating layer res3a
I0623 09:45:02.943899  1897 net.cpp:84] Creating Layer res3a
I0623 09:45:02.943917  1897 net.cpp:406] res3a <- res3a_branch1
I0623 09:45:02.943934  1897 net.cpp:406] res3a <- res3a_branch2c
I0623 09:45:02.943955  1897 net.cpp:380] res3a -> res3a
I0623 09:45:02.943981  1897 net.cpp:122] Setting up res3a
I0623 09:45:02.944002  1897 net.cpp:129] Top shape: 8 512 32 32 (4194304)
I0623 09:45:02.944018  1897 net.cpp:137] Memory required for data: 1323303008
I0623 09:45:02.944036  1897 layer_factory.hpp:77] Creating layer res3a_relu
I0623 09:45:02.944053  1897 net.cpp:84] Creating Layer res3a_relu
I0623 09:45:02.944070  1897 net.cpp:406] res3a_relu <- res3a
I0623 09:45:02.944088  1897 net.cpp:367] res3a_relu -> res3a (in-place)
I0623 09:45:02.944108  1897 net.cpp:122] Setting up res3a_relu
I0623 09:45:02.944126  1897 net.cpp:129] Top shape: 8 512 32 32 (4194304)
I0623 09:45:02.944141  1897 net.cpp:137] Memory required for data: 1340080224
I0623 09:45:02.944157  1897 layer_factory.hpp:77] Creating layer res3a_res3a_relu_0_split
I0623 09:45:02.944176  1897 net.cpp:84] Creating Layer res3a_res3a_relu_0_split
I0623 09:45:02.944192  1897 net.cpp:406] res3a_res3a_relu_0_split <- res3a
I0623 09:45:02.944212  1897 net.cpp:380] res3a_res3a_relu_0_split -> res3a_res3a_relu_0_split_0
I0623 09:45:02.944238  1897 net.cpp:380] res3a_res3a_relu_0_split -> res3a_res3a_relu_0_split_1
I0623 09:45:02.944262  1897 net.cpp:122] Setting up res3a_res3a_relu_0_split
I0623 09:45:02.944281  1897 net.cpp:129] Top shape: 8 512 32 32 (4194304)
I0623 09:45:02.944299  1897 net.cpp:129] Top shape: 8 512 32 32 (4194304)
I0623 09:45:02.944315  1897 net.cpp:137] Memory required for data: 1373634656
I0623 09:45:02.944331  1897 layer_factory.hpp:77] Creating layer res3b_branch2a
I0623 09:45:02.944352  1897 net.cpp:84] Creating Layer res3b_branch2a
I0623 09:45:02.944370  1897 net.cpp:406] res3b_branch2a <- res3a_res3a_relu_0_split_0
I0623 09:45:02.944391  1897 net.cpp:380] res3b_branch2a -> res3b_branch2a
I0623 09:45:02.944542  1897 net.cpp:122] Setting up res3b_branch2a
I0623 09:45:02.944567  1897 net.cpp:129] Top shape: 8 128 32 32 (1048576)
I0623 09:45:02.944583  1897 net.cpp:137] Memory required for data: 1377828960
I0623 09:45:02.944603  1897 layer_factory.hpp:77] Creating layer bn3b_branch2a
I0623 09:45:02.944624  1897 net.cpp:84] Creating Layer bn3b_branch2a
I0623 09:45:02.944643  1897 net.cpp:406] bn3b_branch2a <- res3b_branch2a
I0623 09:45:02.944663  1897 net.cpp:367] bn3b_branch2a -> res3b_branch2a (in-place)
I0623 09:45:02.944694  1897 net.cpp:122] Setting up bn3b_branch2a
I0623 09:45:02.944716  1897 net.cpp:129] Top shape: 8 128 32 32 (1048576)
I0623 09:45:02.944732  1897 net.cpp:137] Memory required for data: 1382023264
I0623 09:45:02.944754  1897 layer_factory.hpp:77] Creating layer scale3b_branch2a
I0623 09:45:02.944774  1897 net.cpp:84] Creating Layer scale3b_branch2a
I0623 09:45:02.944792  1897 net.cpp:406] scale3b_branch2a <- res3b_branch2a
I0623 09:45:02.944809  1897 net.cpp:367] scale3b_branch2a -> res3b_branch2a (in-place)
I0623 09:45:02.944836  1897 layer_factory.hpp:77] Creating layer scale3b_branch2a
I0623 09:45:02.944871  1897 net.cpp:122] Setting up scale3b_branch2a
I0623 09:45:02.944892  1897 net.cpp:129] Top shape: 8 128 32 32 (1048576)
I0623 09:45:02.944908  1897 net.cpp:137] Memory required for data: 1386217568
I0623 09:45:02.944928  1897 layer_factory.hpp:77] Creating layer res3b_branch2a_relu
I0623 09:45:02.944950  1897 net.cpp:84] Creating Layer res3b_branch2a_relu
I0623 09:45:02.944968  1897 net.cpp:406] res3b_branch2a_relu <- res3b_branch2a
I0623 09:45:02.944988  1897 net.cpp:367] res3b_branch2a_relu -> res3b_branch2a (in-place)
I0623 09:45:02.945008  1897 net.cpp:122] Setting up res3b_branch2a_relu
I0623 09:45:02.945027  1897 net.cpp:129] Top shape: 8 128 32 32 (1048576)
I0623 09:45:02.945044  1897 net.cpp:137] Memory required for data: 1390411872
I0623 09:45:02.945060  1897 layer_factory.hpp:77] Creating layer res3b_branch2b
I0623 09:45:02.945080  1897 net.cpp:84] Creating Layer res3b_branch2b
I0623 09:45:02.945097  1897 net.cpp:406] res3b_branch2b <- res3b_branch2a
I0623 09:45:02.945116  1897 net.cpp:380] res3b_branch2b -> res3b_branch2b
I0623 09:45:02.945395  1897 net.cpp:122] Setting up res3b_branch2b
I0623 09:45:02.945420  1897 net.cpp:129] Top shape: 8 128 32 32 (1048576)
I0623 09:45:02.945437  1897 net.cpp:137] Memory required for data: 1394606176
I0623 09:45:02.945456  1897 layer_factory.hpp:77] Creating layer bn3b_branch2b
I0623 09:45:02.945477  1897 net.cpp:84] Creating Layer bn3b_branch2b
I0623 09:45:02.945493  1897 net.cpp:406] bn3b_branch2b <- res3b_branch2b
I0623 09:45:02.945516  1897 net.cpp:367] bn3b_branch2b -> res3b_branch2b (in-place)
I0623 09:45:02.945549  1897 net.cpp:122] Setting up bn3b_branch2b
I0623 09:45:02.945570  1897 net.cpp:129] Top shape: 8 128 32 32 (1048576)
I0623 09:45:02.945586  1897 net.cpp:137] Memory required for data: 1398800480
I0623 09:45:02.945610  1897 layer_factory.hpp:77] Creating layer scale3b_branch2b
I0623 09:45:02.945631  1897 net.cpp:84] Creating Layer scale3b_branch2b
I0623 09:45:02.945648  1897 net.cpp:406] scale3b_branch2b <- res3b_branch2b
I0623 09:45:02.945667  1897 net.cpp:367] scale3b_branch2b -> res3b_branch2b (in-place)
I0623 09:45:02.945691  1897 layer_factory.hpp:77] Creating layer scale3b_branch2b
I0623 09:45:02.945726  1897 net.cpp:122] Setting up scale3b_branch2b
I0623 09:45:02.945746  1897 net.cpp:129] Top shape: 8 128 32 32 (1048576)
I0623 09:45:02.945762  1897 net.cpp:137] Memory required for data: 1402994784
I0623 09:45:02.945783  1897 layer_factory.hpp:77] Creating layer res3b_branch2b_relu
I0623 09:45:02.945802  1897 net.cpp:84] Creating Layer res3b_branch2b_relu
I0623 09:45:02.945819  1897 net.cpp:406] res3b_branch2b_relu <- res3b_branch2b
I0623 09:45:02.945838  1897 net.cpp:367] res3b_branch2b_relu -> res3b_branch2b (in-place)
I0623 09:45:02.945859  1897 net.cpp:122] Setting up res3b_branch2b_relu
I0623 09:45:02.945878  1897 net.cpp:129] Top shape: 8 128 32 32 (1048576)
I0623 09:45:02.945894  1897 net.cpp:137] Memory required for data: 1407189088
I0623 09:45:02.945914  1897 layer_factory.hpp:77] Creating layer res3b_branch2c
I0623 09:45:02.945935  1897 net.cpp:84] Creating Layer res3b_branch2c
I0623 09:45:02.945952  1897 net.cpp:406] res3b_branch2c <- res3b_branch2b
I0623 09:45:02.945971  1897 net.cpp:380] res3b_branch2c -> res3b_branch2c
I0623 09:45:02.946115  1897 net.cpp:122] Setting up res3b_branch2c
I0623 09:45:02.946140  1897 net.cpp:129] Top shape: 8 512 32 32 (4194304)
I0623 09:45:02.946156  1897 net.cpp:137] Memory required for data: 1423966304
I0623 09:45:02.946174  1897 layer_factory.hpp:77] Creating layer bn3b_branch2c
I0623 09:45:02.946197  1897 net.cpp:84] Creating Layer bn3b_branch2c
I0623 09:45:02.946215  1897 net.cpp:406] bn3b_branch2c <- res3b_branch2c
I0623 09:45:02.946233  1897 net.cpp:367] bn3b_branch2c -> res3b_branch2c (in-place)
I0623 09:45:02.946266  1897 net.cpp:122] Setting up bn3b_branch2c
I0623 09:45:02.946287  1897 net.cpp:129] Top shape: 8 512 32 32 (4194304)
I0623 09:45:02.946305  1897 net.cpp:137] Memory required for data: 1440743520
I0623 09:45:02.946326  1897 layer_factory.hpp:77] Creating layer scale3b_branch2c
I0623 09:45:02.946348  1897 net.cpp:84] Creating Layer scale3b_branch2c
I0623 09:45:02.946365  1897 net.cpp:406] scale3b_branch2c <- res3b_branch2c
I0623 09:45:02.946385  1897 net.cpp:367] scale3b_branch2c -> res3b_branch2c (in-place)
I0623 09:45:02.946413  1897 layer_factory.hpp:77] Creating layer scale3b_branch2c
I0623 09:45:02.946449  1897 net.cpp:122] Setting up scale3b_branch2c
I0623 09:45:02.946470  1897 net.cpp:129] Top shape: 8 512 32 32 (4194304)
I0623 09:45:02.946486  1897 net.cpp:137] Memory required for data: 1457520736
I0623 09:45:02.946506  1897 layer_factory.hpp:77] Creating layer res3b
I0623 09:45:02.946527  1897 net.cpp:84] Creating Layer res3b
I0623 09:45:02.946543  1897 net.cpp:406] res3b <- res3a_res3a_relu_0_split_1
I0623 09:45:02.946561  1897 net.cpp:406] res3b <- res3b_branch2c
I0623 09:45:02.946583  1897 net.cpp:380] res3b -> res3b
I0623 09:45:02.946605  1897 net.cpp:122] Setting up res3b
I0623 09:45:02.946626  1897 net.cpp:129] Top shape: 8 512 32 32 (4194304)
I0623 09:45:02.946642  1897 net.cpp:137] Memory required for data: 1474297952
I0623 09:45:02.946658  1897 layer_factory.hpp:77] Creating layer res3b_relu
I0623 09:45:02.946689  1897 net.cpp:84] Creating Layer res3b_relu
I0623 09:45:02.946708  1897 net.cpp:406] res3b_relu <- res3b
I0623 09:45:02.946727  1897 net.cpp:367] res3b_relu -> res3b (in-place)
I0623 09:45:02.946746  1897 net.cpp:122] Setting up res3b_relu
I0623 09:45:02.946765  1897 net.cpp:129] Top shape: 8 512 32 32 (4194304)
I0623 09:45:02.946781  1897 net.cpp:137] Memory required for data: 1491075168
I0623 09:45:02.946799  1897 layer_factory.hpp:77] Creating layer res3b_res3b_relu_0_split
I0623 09:45:02.946816  1897 net.cpp:84] Creating Layer res3b_res3b_relu_0_split
I0623 09:45:02.946833  1897 net.cpp:406] res3b_res3b_relu_0_split <- res3b
I0623 09:45:02.946853  1897 net.cpp:380] res3b_res3b_relu_0_split -> res3b_res3b_relu_0_split_0
I0623 09:45:02.946876  1897 net.cpp:380] res3b_res3b_relu_0_split -> res3b_res3b_relu_0_split_1
I0623 09:45:02.946897  1897 net.cpp:122] Setting up res3b_res3b_relu_0_split
I0623 09:45:02.946916  1897 net.cpp:129] Top shape: 8 512 32 32 (4194304)
I0623 09:45:02.946935  1897 net.cpp:129] Top shape: 8 512 32 32 (4194304)
I0623 09:45:02.946950  1897 net.cpp:137] Memory required for data: 1524629600
I0623 09:45:02.946966  1897 layer_factory.hpp:77] Creating layer res3c_branch2a
I0623 09:45:02.946990  1897 net.cpp:84] Creating Layer res3c_branch2a
I0623 09:45:02.947007  1897 net.cpp:406] res3c_branch2a <- res3b_res3b_relu_0_split_0
I0623 09:45:02.947026  1897 net.cpp:380] res3c_branch2a -> res3c_branch2a
I0623 09:45:02.947170  1897 net.cpp:122] Setting up res3c_branch2a
I0623 09:45:02.947193  1897 net.cpp:129] Top shape: 8 128 32 32 (1048576)
I0623 09:45:02.947211  1897 net.cpp:137] Memory required for data: 1528823904
I0623 09:45:02.947229  1897 layer_factory.hpp:77] Creating layer bn3c_branch2a
I0623 09:45:02.947254  1897 net.cpp:84] Creating Layer bn3c_branch2a
I0623 09:45:02.947273  1897 net.cpp:406] bn3c_branch2a <- res3c_branch2a
I0623 09:45:02.947293  1897 net.cpp:367] bn3c_branch2a -> res3c_branch2a (in-place)
I0623 09:45:02.947327  1897 net.cpp:122] Setting up bn3c_branch2a
I0623 09:45:02.947350  1897 net.cpp:129] Top shape: 8 128 32 32 (1048576)
I0623 09:45:02.947366  1897 net.cpp:137] Memory required for data: 1533018208
I0623 09:45:02.947388  1897 layer_factory.hpp:77] Creating layer scale3c_branch2a
I0623 09:45:02.947410  1897 net.cpp:84] Creating Layer scale3c_branch2a
I0623 09:45:02.947428  1897 net.cpp:406] scale3c_branch2a <- res3c_branch2a
I0623 09:45:02.947446  1897 net.cpp:367] scale3c_branch2a -> res3c_branch2a (in-place)
I0623 09:45:02.947471  1897 layer_factory.hpp:77] Creating layer scale3c_branch2a
I0623 09:45:02.947509  1897 net.cpp:122] Setting up scale3c_branch2a
I0623 09:45:02.947530  1897 net.cpp:129] Top shape: 8 128 32 32 (1048576)
I0623 09:45:02.947546  1897 net.cpp:137] Memory required for data: 1537212512
I0623 09:45:02.947566  1897 layer_factory.hpp:77] Creating layer res3c_branch2a_relu
I0623 09:45:02.947587  1897 net.cpp:84] Creating Layer res3c_branch2a_relu
I0623 09:45:02.947603  1897 net.cpp:406] res3c_branch2a_relu <- res3c_branch2a
I0623 09:45:02.947623  1897 net.cpp:367] res3c_branch2a_relu -> res3c_branch2a (in-place)
I0623 09:45:02.947643  1897 net.cpp:122] Setting up res3c_branch2a_relu
I0623 09:45:02.947662  1897 net.cpp:129] Top shape: 8 128 32 32 (1048576)
I0623 09:45:02.947679  1897 net.cpp:137] Memory required for data: 1541406816
I0623 09:45:02.947695  1897 layer_factory.hpp:77] Creating layer res3c_branch2b
I0623 09:45:02.947715  1897 net.cpp:84] Creating Layer res3c_branch2b
I0623 09:45:02.947731  1897 net.cpp:406] res3c_branch2b <- res3c_branch2a
I0623 09:45:02.947751  1897 net.cpp:380] res3c_branch2b -> res3c_branch2b
I0623 09:45:02.948029  1897 net.cpp:122] Setting up res3c_branch2b
I0623 09:45:02.948053  1897 net.cpp:129] Top shape: 8 128 32 32 (1048576)
I0623 09:45:02.948070  1897 net.cpp:137] Memory required for data: 1545601120
I0623 09:45:02.948088  1897 layer_factory.hpp:77] Creating layer bn3c_branch2b
I0623 09:45:02.948110  1897 net.cpp:84] Creating Layer bn3c_branch2b
I0623 09:45:02.948127  1897 net.cpp:406] bn3c_branch2b <- res3c_branch2b
I0623 09:45:02.948146  1897 net.cpp:367] bn3c_branch2b -> res3c_branch2b (in-place)
I0623 09:45:02.948179  1897 net.cpp:122] Setting up bn3c_branch2b
I0623 09:45:02.948199  1897 net.cpp:129] Top shape: 8 128 32 32 (1048576)
I0623 09:45:02.948215  1897 net.cpp:137] Memory required for data: 1549795424
I0623 09:45:02.948236  1897 layer_factory.hpp:77] Creating layer scale3c_branch2b
I0623 09:45:02.948257  1897 net.cpp:84] Creating Layer scale3c_branch2b
I0623 09:45:02.948276  1897 net.cpp:406] scale3c_branch2b <- res3c_branch2b
I0623 09:45:02.948297  1897 net.cpp:367] scale3c_branch2b -> res3c_branch2b (in-place)
I0623 09:45:02.948323  1897 layer_factory.hpp:77] Creating layer scale3c_branch2b
I0623 09:45:02.948359  1897 net.cpp:122] Setting up scale3c_branch2b
I0623 09:45:02.948380  1897 net.cpp:129] Top shape: 8 128 32 32 (1048576)
I0623 09:45:02.948396  1897 net.cpp:137] Memory required for data: 1553989728
I0623 09:45:02.948416  1897 layer_factory.hpp:77] Creating layer res3c_branch2b_relu
I0623 09:45:02.948436  1897 net.cpp:84] Creating Layer res3c_branch2b_relu
I0623 09:45:02.948453  1897 net.cpp:406] res3c_branch2b_relu <- res3c_branch2b
I0623 09:45:02.948472  1897 net.cpp:367] res3c_branch2b_relu -> res3c_branch2b (in-place)
I0623 09:45:02.948492  1897 net.cpp:122] Setting up res3c_branch2b_relu
I0623 09:45:02.948510  1897 net.cpp:129] Top shape: 8 128 32 32 (1048576)
I0623 09:45:02.948526  1897 net.cpp:137] Memory required for data: 1558184032
I0623 09:45:02.948542  1897 layer_factory.hpp:77] Creating layer res3c_branch2c
I0623 09:45:02.948565  1897 net.cpp:84] Creating Layer res3c_branch2c
I0623 09:45:02.948582  1897 net.cpp:406] res3c_branch2c <- res3c_branch2b
I0623 09:45:02.948601  1897 net.cpp:380] res3c_branch2c -> res3c_branch2c
I0623 09:45:02.948750  1897 net.cpp:122] Setting up res3c_branch2c
I0623 09:45:02.948774  1897 net.cpp:129] Top shape: 8 512 32 32 (4194304)
I0623 09:45:02.948791  1897 net.cpp:137] Memory required for data: 1574961248
I0623 09:45:02.948809  1897 layer_factory.hpp:77] Creating layer bn3c_branch2c
I0623 09:45:02.948829  1897 net.cpp:84] Creating Layer bn3c_branch2c
I0623 09:45:02.948848  1897 net.cpp:406] bn3c_branch2c <- res3c_branch2c
I0623 09:45:02.948868  1897 net.cpp:367] bn3c_branch2c -> res3c_branch2c (in-place)
I0623 09:45:02.948899  1897 net.cpp:122] Setting up bn3c_branch2c
I0623 09:45:02.948921  1897 net.cpp:129] Top shape: 8 512 32 32 (4194304)
I0623 09:45:02.948938  1897 net.cpp:137] Memory required for data: 1591738464
I0623 09:45:02.948961  1897 layer_factory.hpp:77] Creating layer scale3c_branch2c
I0623 09:45:02.948981  1897 net.cpp:84] Creating Layer scale3c_branch2c
I0623 09:45:02.948997  1897 net.cpp:406] scale3c_branch2c <- res3c_branch2c
I0623 09:45:02.949015  1897 net.cpp:367] scale3c_branch2c -> res3c_branch2c (in-place)
I0623 09:45:02.949043  1897 layer_factory.hpp:77] Creating layer scale3c_branch2c
I0623 09:45:02.949077  1897 net.cpp:122] Setting up scale3c_branch2c
I0623 09:45:02.949098  1897 net.cpp:129] Top shape: 8 512 32 32 (4194304)
I0623 09:45:02.949117  1897 net.cpp:137] Memory required for data: 1608515680
I0623 09:45:02.949141  1897 layer_factory.hpp:77] Creating layer res3c
I0623 09:45:02.949163  1897 net.cpp:84] Creating Layer res3c
I0623 09:45:02.949182  1897 net.cpp:406] res3c <- res3b_res3b_relu_0_split_1
I0623 09:45:02.949200  1897 net.cpp:406] res3c <- res3c_branch2c
I0623 09:45:02.949221  1897 net.cpp:380] res3c -> res3c
I0623 09:45:02.949244  1897 net.cpp:122] Setting up res3c
I0623 09:45:02.949265  1897 net.cpp:129] Top shape: 8 512 32 32 (4194304)
I0623 09:45:02.949280  1897 net.cpp:137] Memory required for data: 1625292896
I0623 09:45:02.949296  1897 layer_factory.hpp:77] Creating layer res3c_relu
I0623 09:45:02.949319  1897 net.cpp:84] Creating Layer res3c_relu
I0623 09:45:02.949339  1897 net.cpp:406] res3c_relu <- res3c
I0623 09:45:02.949360  1897 net.cpp:367] res3c_relu -> res3c (in-place)
I0623 09:45:02.949383  1897 net.cpp:122] Setting up res3c_relu
I0623 09:45:02.949405  1897 net.cpp:129] Top shape: 8 512 32 32 (4194304)
I0623 09:45:02.949424  1897 net.cpp:137] Memory required for data: 1642070112
I0623 09:45:02.949440  1897 layer_factory.hpp:77] Creating layer res3c_res3c_relu_0_split
I0623 09:45:02.949460  1897 net.cpp:84] Creating Layer res3c_res3c_relu_0_split
I0623 09:45:02.949476  1897 net.cpp:406] res3c_res3c_relu_0_split <- res3c
I0623 09:45:02.949494  1897 net.cpp:380] res3c_res3c_relu_0_split -> res3c_res3c_relu_0_split_0
I0623 09:45:02.949515  1897 net.cpp:380] res3c_res3c_relu_0_split -> res3c_res3c_relu_0_split_1
I0623 09:45:02.949538  1897 net.cpp:122] Setting up res3c_res3c_relu_0_split
I0623 09:45:02.949558  1897 net.cpp:129] Top shape: 8 512 32 32 (4194304)
I0623 09:45:02.949575  1897 net.cpp:129] Top shape: 8 512 32 32 (4194304)
I0623 09:45:02.949591  1897 net.cpp:137] Memory required for data: 1675624544
I0623 09:45:02.949607  1897 layer_factory.hpp:77] Creating layer res3d_branch2a
I0623 09:45:02.949630  1897 net.cpp:84] Creating Layer res3d_branch2a
I0623 09:45:02.949648  1897 net.cpp:406] res3d_branch2a <- res3c_res3c_relu_0_split_0
I0623 09:45:02.949667  1897 net.cpp:380] res3d_branch2a -> res3d_branch2a
I0623 09:45:02.949810  1897 net.cpp:122] Setting up res3d_branch2a
I0623 09:45:02.949833  1897 net.cpp:129] Top shape: 8 128 32 32 (1048576)
I0623 09:45:02.949849  1897 net.cpp:137] Memory required for data: 1679818848
I0623 09:45:02.949867  1897 layer_factory.hpp:77] Creating layer bn3d_branch2a
I0623 09:45:02.949889  1897 net.cpp:84] Creating Layer bn3d_branch2a
I0623 09:45:02.949908  1897 net.cpp:406] bn3d_branch2a <- res3d_branch2a
I0623 09:45:02.949926  1897 net.cpp:367] bn3d_branch2a -> res3d_branch2a (in-place)
I0623 09:45:02.949957  1897 net.cpp:122] Setting up bn3d_branch2a
I0623 09:45:02.949976  1897 net.cpp:129] Top shape: 8 128 32 32 (1048576)
I0623 09:45:02.949997  1897 net.cpp:137] Memory required for data: 1684013152
I0623 09:45:02.950037  1897 layer_factory.hpp:77] Creating layer scale3d_branch2a
I0623 09:45:02.950059  1897 net.cpp:84] Creating Layer scale3d_branch2a
I0623 09:45:02.950078  1897 net.cpp:406] scale3d_branch2a <- res3d_branch2a
I0623 09:45:02.950096  1897 net.cpp:367] scale3d_branch2a -> res3d_branch2a (in-place)
I0623 09:45:02.950124  1897 layer_factory.hpp:77] Creating layer scale3d_branch2a
I0623 09:45:02.950156  1897 net.cpp:122] Setting up scale3d_branch2a
I0623 09:45:02.950178  1897 net.cpp:129] Top shape: 8 128 32 32 (1048576)
I0623 09:45:02.950194  1897 net.cpp:137] Memory required for data: 1688207456
I0623 09:45:02.950215  1897 layer_factory.hpp:77] Creating layer res3d_branch2a_relu
I0623 09:45:02.950237  1897 net.cpp:84] Creating Layer res3d_branch2a_relu
I0623 09:45:02.950254  1897 net.cpp:406] res3d_branch2a_relu <- res3d_branch2a
I0623 09:45:02.950273  1897 net.cpp:367] res3d_branch2a_relu -> res3d_branch2a (in-place)
I0623 09:45:02.950292  1897 net.cpp:122] Setting up res3d_branch2a_relu
I0623 09:45:02.950311  1897 net.cpp:129] Top shape: 8 128 32 32 (1048576)
I0623 09:45:02.950327  1897 net.cpp:137] Memory required for data: 1692401760
I0623 09:45:02.950343  1897 layer_factory.hpp:77] Creating layer res3d_branch2b
I0623 09:45:02.950366  1897 net.cpp:84] Creating Layer res3d_branch2b
I0623 09:45:02.950384  1897 net.cpp:406] res3d_branch2b <- res3d_branch2a
I0623 09:45:02.950405  1897 net.cpp:380] res3d_branch2b -> res3d_branch2b
I0623 09:45:02.950700  1897 net.cpp:122] Setting up res3d_branch2b
I0623 09:45:02.950726  1897 net.cpp:129] Top shape: 8 128 32 32 (1048576)
I0623 09:45:02.950742  1897 net.cpp:137] Memory required for data: 1696596064
I0623 09:45:02.950762  1897 layer_factory.hpp:77] Creating layer bn3d_branch2b
I0623 09:45:02.950783  1897 net.cpp:84] Creating Layer bn3d_branch2b
I0623 09:45:02.950800  1897 net.cpp:406] bn3d_branch2b <- res3d_branch2b
I0623 09:45:02.950819  1897 net.cpp:367] bn3d_branch2b -> res3d_branch2b (in-place)
I0623 09:45:02.950850  1897 net.cpp:122] Setting up bn3d_branch2b
I0623 09:45:02.950872  1897 net.cpp:129] Top shape: 8 128 32 32 (1048576)
I0623 09:45:02.950889  1897 net.cpp:137] Memory required for data: 1700790368
I0623 09:45:02.950911  1897 layer_factory.hpp:77] Creating layer scale3d_branch2b
I0623 09:45:02.950932  1897 net.cpp:84] Creating Layer scale3d_branch2b
I0623 09:45:02.950948  1897 net.cpp:406] scale3d_branch2b <- res3d_branch2b
I0623 09:45:02.950966  1897 net.cpp:367] scale3d_branch2b -> res3d_branch2b (in-place)
I0623 09:45:02.950994  1897 layer_factory.hpp:77] Creating layer scale3d_branch2b
I0623 09:45:02.951028  1897 net.cpp:122] Setting up scale3d_branch2b
I0623 09:45:02.951048  1897 net.cpp:129] Top shape: 8 128 32 32 (1048576)
I0623 09:45:02.951064  1897 net.cpp:137] Memory required for data: 1704984672
I0623 09:45:02.951086  1897 layer_factory.hpp:77] Creating layer res3d_branch2b_relu
I0623 09:45:02.951105  1897 net.cpp:84] Creating Layer res3d_branch2b_relu
I0623 09:45:02.951123  1897 net.cpp:406] res3d_branch2b_relu <- res3d_branch2b
I0623 09:45:02.951141  1897 net.cpp:367] res3d_branch2b_relu -> res3d_branch2b (in-place)
I0623 09:45:02.951161  1897 net.cpp:122] Setting up res3d_branch2b_relu
I0623 09:45:02.951181  1897 net.cpp:129] Top shape: 8 128 32 32 (1048576)
I0623 09:45:02.951197  1897 net.cpp:137] Memory required for data: 1709178976
I0623 09:45:02.951213  1897 layer_factory.hpp:77] Creating layer res3d_branch2c
I0623 09:45:02.951233  1897 net.cpp:84] Creating Layer res3d_branch2c
I0623 09:45:02.951251  1897 net.cpp:406] res3d_branch2c <- res3d_branch2b
I0623 09:45:02.951269  1897 net.cpp:380] res3d_branch2c -> res3d_branch2c
I0623 09:45:02.951411  1897 net.cpp:122] Setting up res3d_branch2c
I0623 09:45:02.951436  1897 net.cpp:129] Top shape: 8 512 32 32 (4194304)
I0623 09:45:02.951454  1897 net.cpp:137] Memory required for data: 1725956192
I0623 09:45:02.951473  1897 layer_factory.hpp:77] Creating layer bn3d_branch2c
I0623 09:45:02.951498  1897 net.cpp:84] Creating Layer bn3d_branch2c
I0623 09:45:02.951515  1897 net.cpp:406] bn3d_branch2c <- res3d_branch2c
I0623 09:45:02.951536  1897 net.cpp:367] bn3d_branch2c -> res3d_branch2c (in-place)
I0623 09:45:02.951571  1897 net.cpp:122] Setting up bn3d_branch2c
I0623 09:45:02.951592  1897 net.cpp:129] Top shape: 8 512 32 32 (4194304)
I0623 09:45:02.951609  1897 net.cpp:137] Memory required for data: 1742733408
I0623 09:45:02.951632  1897 layer_factory.hpp:77] Creating layer scale3d_branch2c
I0623 09:45:02.951653  1897 net.cpp:84] Creating Layer scale3d_branch2c
I0623 09:45:02.951671  1897 net.cpp:406] scale3d_branch2c <- res3d_branch2c
I0623 09:45:02.951691  1897 net.cpp:367] scale3d_branch2c -> res3d_branch2c (in-place)
I0623 09:45:02.951719  1897 layer_factory.hpp:77] Creating layer scale3d_branch2c
I0623 09:45:02.951756  1897 net.cpp:122] Setting up scale3d_branch2c
I0623 09:45:02.951776  1897 net.cpp:129] Top shape: 8 512 32 32 (4194304)
I0623 09:45:02.951792  1897 net.cpp:137] Memory required for data: 1759510624
I0623 09:45:02.951813  1897 layer_factory.hpp:77] Creating layer res3d
I0623 09:45:02.951833  1897 net.cpp:84] Creating Layer res3d
I0623 09:45:02.951849  1897 net.cpp:406] res3d <- res3c_res3c_relu_0_split_1
I0623 09:45:02.951867  1897 net.cpp:406] res3d <- res3d_branch2c
I0623 09:45:02.951886  1897 net.cpp:380] res3d -> res3d
I0623 09:45:02.951907  1897 net.cpp:122] Setting up res3d
I0623 09:45:02.951926  1897 net.cpp:129] Top shape: 8 512 32 32 (4194304)
I0623 09:45:02.951943  1897 net.cpp:137] Memory required for data: 1776287840
I0623 09:45:02.951958  1897 layer_factory.hpp:77] Creating layer res3d_relu
I0623 09:45:02.951977  1897 net.cpp:84] Creating Layer res3d_relu
I0623 09:45:02.951993  1897 net.cpp:406] res3d_relu <- res3d
I0623 09:45:02.952013  1897 net.cpp:367] res3d_relu -> res3d (in-place)
I0623 09:45:02.952038  1897 net.cpp:122] Setting up res3d_relu
I0623 09:45:02.952066  1897 net.cpp:129] Top shape: 8 512 32 32 (4194304)
I0623 09:45:02.952083  1897 net.cpp:137] Memory required for data: 1793065056
I0623 09:45:02.952100  1897 layer_factory.hpp:77] Creating layer res3d_res3d_relu_0_split
I0623 09:45:02.952118  1897 net.cpp:84] Creating Layer res3d_res3d_relu_0_split
I0623 09:45:02.952134  1897 net.cpp:406] res3d_res3d_relu_0_split <- res3d
I0623 09:45:02.952155  1897 net.cpp:380] res3d_res3d_relu_0_split -> res3d_res3d_relu_0_split_0
I0623 09:45:02.952178  1897 net.cpp:380] res3d_res3d_relu_0_split -> res3d_res3d_relu_0_split_1
I0623 09:45:02.952199  1897 net.cpp:122] Setting up res3d_res3d_relu_0_split
I0623 09:45:02.952219  1897 net.cpp:129] Top shape: 8 512 32 32 (4194304)
I0623 09:45:02.952237  1897 net.cpp:129] Top shape: 8 512 32 32 (4194304)
I0623 09:45:02.952253  1897 net.cpp:137] Memory required for data: 1826619488
I0623 09:45:02.952270  1897 layer_factory.hpp:77] Creating layer res4a_branch1
I0623 09:45:02.952289  1897 net.cpp:84] Creating Layer res4a_branch1
I0623 09:45:02.952306  1897 net.cpp:406] res4a_branch1 <- res3d_res3d_relu_0_split_0
I0623 09:45:02.952327  1897 net.cpp:380] res4a_branch1 -> res4a_branch1
I0623 09:45:02.953245  1897 net.cpp:122] Setting up res4a_branch1
I0623 09:45:02.953274  1897 net.cpp:129] Top shape: 8 1024 16 16 (2097152)
I0623 09:45:02.953290  1897 net.cpp:137] Memory required for data: 1835008096
I0623 09:45:02.953310  1897 layer_factory.hpp:77] Creating layer bn4a_branch1
I0623 09:45:02.953331  1897 net.cpp:84] Creating Layer bn4a_branch1
I0623 09:45:02.953349  1897 net.cpp:406] bn4a_branch1 <- res4a_branch1
I0623 09:45:02.953368  1897 net.cpp:367] bn4a_branch1 -> res4a_branch1 (in-place)
I0623 09:45:02.953400  1897 net.cpp:122] Setting up bn4a_branch1
I0623 09:45:02.953423  1897 net.cpp:129] Top shape: 8 1024 16 16 (2097152)
I0623 09:45:02.953440  1897 net.cpp:137] Memory required for data: 1843396704
I0623 09:45:02.953462  1897 layer_factory.hpp:77] Creating layer scale4a_branch1
I0623 09:45:02.953482  1897 net.cpp:84] Creating Layer scale4a_branch1
I0623 09:45:02.953500  1897 net.cpp:406] scale4a_branch1 <- res4a_branch1
I0623 09:45:02.953523  1897 net.cpp:367] scale4a_branch1 -> res4a_branch1 (in-place)
I0623 09:45:02.953552  1897 layer_factory.hpp:77] Creating layer scale4a_branch1
I0623 09:45:02.953584  1897 net.cpp:122] Setting up scale4a_branch1
I0623 09:45:02.953604  1897 net.cpp:129] Top shape: 8 1024 16 16 (2097152)
I0623 09:45:02.953621  1897 net.cpp:137] Memory required for data: 1851785312
I0623 09:45:02.953645  1897 layer_factory.hpp:77] Creating layer res4a_branch2a
I0623 09:45:02.953677  1897 net.cpp:84] Creating Layer res4a_branch2a
I0623 09:45:02.953694  1897 net.cpp:406] res4a_branch2a <- res3d_res3d_relu_0_split_1
I0623 09:45:02.953714  1897 net.cpp:380] res4a_branch2a -> res4a_branch2a
I0623 09:45:02.953969  1897 net.cpp:122] Setting up res4a_branch2a
I0623 09:45:02.953995  1897 net.cpp:129] Top shape: 8 256 16 16 (524288)
I0623 09:45:02.954011  1897 net.cpp:137] Memory required for data: 1853882464
I0623 09:45:02.954030  1897 layer_factory.hpp:77] Creating layer bn4a_branch2a
I0623 09:45:02.954051  1897 net.cpp:84] Creating Layer bn4a_branch2a
I0623 09:45:02.954067  1897 net.cpp:406] bn4a_branch2a <- res4a_branch2a
I0623 09:45:02.954088  1897 net.cpp:367] bn4a_branch2a -> res4a_branch2a (in-place)
I0623 09:45:02.954120  1897 net.cpp:122] Setting up bn4a_branch2a
I0623 09:45:02.954140  1897 net.cpp:129] Top shape: 8 256 16 16 (524288)
I0623 09:45:02.954159  1897 net.cpp:137] Memory required for data: 1855979616
I0623 09:45:02.954180  1897 layer_factory.hpp:77] Creating layer scale4a_branch2a
I0623 09:45:02.954202  1897 net.cpp:84] Creating Layer scale4a_branch2a
I0623 09:45:02.954221  1897 net.cpp:406] scale4a_branch2a <- res4a_branch2a
I0623 09:45:02.954239  1897 net.cpp:367] scale4a_branch2a -> res4a_branch2a (in-place)
I0623 09:45:02.954267  1897 layer_factory.hpp:77] Creating layer scale4a_branch2a
I0623 09:45:02.954299  1897 net.cpp:122] Setting up scale4a_branch2a
I0623 09:45:02.954319  1897 net.cpp:129] Top shape: 8 256 16 16 (524288)
I0623 09:45:02.954336  1897 net.cpp:137] Memory required for data: 1858076768
I0623 09:45:02.954356  1897 layer_factory.hpp:77] Creating layer res4a_branch2a_relu
I0623 09:45:02.954377  1897 net.cpp:84] Creating Layer res4a_branch2a_relu
I0623 09:45:02.954396  1897 net.cpp:406] res4a_branch2a_relu <- res4a_branch2a
I0623 09:45:02.954413  1897 net.cpp:367] res4a_branch2a_relu -> res4a_branch2a (in-place)
I0623 09:45:02.954437  1897 net.cpp:122] Setting up res4a_branch2a_relu
I0623 09:45:02.954455  1897 net.cpp:129] Top shape: 8 256 16 16 (524288)
I0623 09:45:02.954471  1897 net.cpp:137] Memory required for data: 1860173920
I0623 09:45:02.954488  1897 layer_factory.hpp:77] Creating layer res4a_branch2b
I0623 09:45:02.954507  1897 net.cpp:84] Creating Layer res4a_branch2b
I0623 09:45:02.954525  1897 net.cpp:406] res4a_branch2b <- res4a_branch2a
I0623 09:45:02.954545  1897 net.cpp:380] res4a_branch2b -> res4a_branch2b
I0623 09:45:02.955575  1897 net.cpp:122] Setting up res4a_branch2b
I0623 09:45:02.955605  1897 net.cpp:129] Top shape: 8 256 16 16 (524288)
I0623 09:45:02.955621  1897 net.cpp:137] Memory required for data: 1862271072
I0623 09:45:02.955641  1897 layer_factory.hpp:77] Creating layer bn4a_branch2b
I0623 09:45:02.955660  1897 net.cpp:84] Creating Layer bn4a_branch2b
I0623 09:45:02.955678  1897 net.cpp:406] bn4a_branch2b <- res4a_branch2b
I0623 09:45:02.955698  1897 net.cpp:367] bn4a_branch2b -> res4a_branch2b (in-place)
I0623 09:45:02.955730  1897 net.cpp:122] Setting up bn4a_branch2b
I0623 09:45:02.955751  1897 net.cpp:129] Top shape: 8 256 16 16 (524288)
I0623 09:45:02.955768  1897 net.cpp:137] Memory required for data: 1864368224
I0623 09:45:02.955790  1897 layer_factory.hpp:77] Creating layer scale4a_branch2b
I0623 09:45:02.955811  1897 net.cpp:84] Creating Layer scale4a_branch2b
I0623 09:45:02.955829  1897 net.cpp:406] scale4a_branch2b <- res4a_branch2b
I0623 09:45:02.955849  1897 net.cpp:367] scale4a_branch2b -> res4a_branch2b (in-place)
I0623 09:45:02.955878  1897 layer_factory.hpp:77] Creating layer scale4a_branch2b
I0623 09:45:02.955909  1897 net.cpp:122] Setting up scale4a_branch2b
I0623 09:45:02.955935  1897 net.cpp:129] Top shape: 8 256 16 16 (524288)
I0623 09:45:02.955952  1897 net.cpp:137] Memory required for data: 1866465376
I0623 09:45:02.955972  1897 layer_factory.hpp:77] Creating layer res4a_branch2b_relu
I0623 09:45:02.955993  1897 net.cpp:84] Creating Layer res4a_branch2b_relu
I0623 09:45:02.956012  1897 net.cpp:406] res4a_branch2b_relu <- res4a_branch2b
I0623 09:45:02.956029  1897 net.cpp:367] res4a_branch2b_relu -> res4a_branch2b (in-place)
I0623 09:45:02.956049  1897 net.cpp:122] Setting up res4a_branch2b_relu
I0623 09:45:02.956069  1897 net.cpp:129] Top shape: 8 256 16 16 (524288)
I0623 09:45:02.956085  1897 net.cpp:137] Memory required for data: 1868562528
I0623 09:45:02.956101  1897 layer_factory.hpp:77] Creating layer res4a_branch2c
I0623 09:45:02.956121  1897 net.cpp:84] Creating Layer res4a_branch2c
I0623 09:45:02.956137  1897 net.cpp:406] res4a_branch2c <- res4a_branch2b
I0623 09:45:02.956156  1897 net.cpp:380] res4a_branch2c -> res4a_branch2c
I0623 09:45:02.956629  1897 net.cpp:122] Setting up res4a_branch2c
I0623 09:45:02.956653  1897 net.cpp:129] Top shape: 8 1024 16 16 (2097152)
I0623 09:45:02.956670  1897 net.cpp:137] Memory required for data: 1876951136
I0623 09:45:02.956689  1897 layer_factory.hpp:77] Creating layer bn4a_branch2c
I0623 09:45:02.956708  1897 net.cpp:84] Creating Layer bn4a_branch2c
I0623 09:45:02.956725  1897 net.cpp:406] bn4a_branch2c <- res4a_branch2c
I0623 09:45:02.956748  1897 net.cpp:367] bn4a_branch2c -> res4a_branch2c (in-place)
I0623 09:45:02.956781  1897 net.cpp:122] Setting up bn4a_branch2c
I0623 09:45:02.956804  1897 net.cpp:129] Top shape: 8 1024 16 16 (2097152)
I0623 09:45:02.956820  1897 net.cpp:137] Memory required for data: 1885339744
I0623 09:45:02.956841  1897 layer_factory.hpp:77] Creating layer scale4a_branch2c
I0623 09:45:02.956863  1897 net.cpp:84] Creating Layer scale4a_branch2c
I0623 09:45:02.956882  1897 net.cpp:406] scale4a_branch2c <- res4a_branch2c
I0623 09:45:02.956902  1897 net.cpp:367] scale4a_branch2c -> res4a_branch2c (in-place)
I0623 09:45:02.956931  1897 layer_factory.hpp:77] Creating layer scale4a_branch2c
I0623 09:45:02.956964  1897 net.cpp:122] Setting up scale4a_branch2c
I0623 09:45:02.956987  1897 net.cpp:129] Top shape: 8 1024 16 16 (2097152)
I0623 09:45:02.957006  1897 net.cpp:137] Memory required for data: 1893728352
I0623 09:45:02.957027  1897 layer_factory.hpp:77] Creating layer res4a
I0623 09:45:02.957051  1897 net.cpp:84] Creating Layer res4a
I0623 09:45:02.957070  1897 net.cpp:406] res4a <- res4a_branch1
I0623 09:45:02.957088  1897 net.cpp:406] res4a <- res4a_branch2c
I0623 09:45:02.957108  1897 net.cpp:380] res4a -> res4a
I0623 09:45:02.957129  1897 net.cpp:122] Setting up res4a
I0623 09:45:02.957149  1897 net.cpp:129] Top shape: 8 1024 16 16 (2097152)
I0623 09:45:02.957165  1897 net.cpp:137] Memory required for data: 1902116960
I0623 09:45:02.957181  1897 layer_factory.hpp:77] Creating layer res4a_relu
I0623 09:45:02.957201  1897 net.cpp:84] Creating Layer res4a_relu
I0623 09:45:02.957218  1897 net.cpp:406] res4a_relu <- res4a
I0623 09:45:02.957238  1897 net.cpp:367] res4a_relu -> res4a (in-place)
I0623 09:45:02.957262  1897 net.cpp:122] Setting up res4a_relu
I0623 09:45:02.957291  1897 net.cpp:129] Top shape: 8 1024 16 16 (2097152)
I0623 09:45:02.957307  1897 net.cpp:137] Memory required for data: 1910505568
I0623 09:45:02.957324  1897 layer_factory.hpp:77] Creating layer res4a_res4a_relu_0_split
I0623 09:45:02.957357  1897 net.cpp:84] Creating Layer res4a_res4a_relu_0_split
I0623 09:45:02.957376  1897 net.cpp:406] res4a_res4a_relu_0_split <- res4a
I0623 09:45:02.957396  1897 net.cpp:380] res4a_res4a_relu_0_split -> res4a_res4a_relu_0_split_0
I0623 09:45:02.957418  1897 net.cpp:380] res4a_res4a_relu_0_split -> res4a_res4a_relu_0_split_1
I0623 09:45:02.957442  1897 net.cpp:122] Setting up res4a_res4a_relu_0_split
I0623 09:45:02.957463  1897 net.cpp:129] Top shape: 8 1024 16 16 (2097152)
I0623 09:45:02.957480  1897 net.cpp:129] Top shape: 8 1024 16 16 (2097152)
I0623 09:45:02.957495  1897 net.cpp:137] Memory required for data: 1927282784
I0623 09:45:02.957517  1897 layer_factory.hpp:77] Creating layer res4b_branch2a
I0623 09:45:02.957541  1897 net.cpp:84] Creating Layer res4b_branch2a
I0623 09:45:02.957559  1897 net.cpp:406] res4b_branch2a <- res4a_res4a_relu_0_split_0
I0623 09:45:02.957578  1897 net.cpp:380] res4b_branch2a -> res4b_branch2a
I0623 09:45:02.958048  1897 net.cpp:122] Setting up res4b_branch2a
I0623 09:45:02.958073  1897 net.cpp:129] Top shape: 8 256 16 16 (524288)
I0623 09:45:02.958089  1897 net.cpp:137] Memory required for data: 1929379936
I0623 09:45:02.958108  1897 layer_factory.hpp:77] Creating layer bn4b_branch2a
I0623 09:45:02.958129  1897 net.cpp:84] Creating Layer bn4b_branch2a
I0623 09:45:02.958148  1897 net.cpp:406] bn4b_branch2a <- res4b_branch2a
I0623 09:45:02.958165  1897 net.cpp:367] bn4b_branch2a -> res4b_branch2a (in-place)
I0623 09:45:02.958199  1897 net.cpp:122] Setting up bn4b_branch2a
I0623 09:45:02.958221  1897 net.cpp:129] Top shape: 8 256 16 16 (524288)
I0623 09:45:02.958237  1897 net.cpp:137] Memory required for data: 1931477088
I0623 09:45:02.958261  1897 layer_factory.hpp:77] Creating layer scale4b_branch2a
I0623 09:45:02.958281  1897 net.cpp:84] Creating Layer scale4b_branch2a
I0623 09:45:02.958297  1897 net.cpp:406] scale4b_branch2a <- res4b_branch2a
I0623 09:45:02.958315  1897 net.cpp:367] scale4b_branch2a -> res4b_branch2a (in-place)
I0623 09:45:02.958343  1897 layer_factory.hpp:77] Creating layer scale4b_branch2a
I0623 09:45:02.958375  1897 net.cpp:122] Setting up scale4b_branch2a
I0623 09:45:02.958397  1897 net.cpp:129] Top shape: 8 256 16 16 (524288)
I0623 09:45:02.958412  1897 net.cpp:137] Memory required for data: 1933574240
I0623 09:45:02.958433  1897 layer_factory.hpp:77] Creating layer res4b_branch2a_relu
I0623 09:45:02.958452  1897 net.cpp:84] Creating Layer res4b_branch2a_relu
I0623 09:45:02.958469  1897 net.cpp:406] res4b_branch2a_relu <- res4b_branch2a
I0623 09:45:02.958489  1897 net.cpp:367] res4b_branch2a_relu -> res4b_branch2a (in-place)
I0623 09:45:02.958510  1897 net.cpp:122] Setting up res4b_branch2a_relu
I0623 09:45:02.958530  1897 net.cpp:129] Top shape: 8 256 16 16 (524288)
I0623 09:45:02.958546  1897 net.cpp:137] Memory required for data: 1935671392
I0623 09:45:02.958562  1897 layer_factory.hpp:77] Creating layer res4b_branch2b
I0623 09:45:02.958582  1897 net.cpp:84] Creating Layer res4b_branch2b
I0623 09:45:02.958600  1897 net.cpp:406] res4b_branch2b <- res4b_branch2a
I0623 09:45:02.958618  1897 net.cpp:380] res4b_branch2b -> res4b_branch2b
I0623 09:45:02.990259  1897 net.cpp:122] Setting up res4b_branch2b
I0623 09:45:02.990334  1897 net.cpp:129] Top shape: 8 256 16 16 (524288)
I0623 09:45:02.990348  1897 net.cpp:137] Memory required for data: 1937768544
I0623 09:45:02.990368  1897 layer_factory.hpp:77] Creating layer bn4b_branch2b
I0623 09:45:02.990393  1897 net.cpp:84] Creating Layer bn4b_branch2b
I0623 09:45:02.990412  1897 net.cpp:406] bn4b_branch2b <- res4b_branch2b
I0623 09:45:02.990434  1897 net.cpp:367] bn4b_branch2b -> res4b_branch2b (in-place)
I0623 09:45:02.990468  1897 net.cpp:122] Setting up bn4b_branch2b
I0623 09:45:02.990494  1897 net.cpp:129] Top shape: 8 256 16 16 (524288)
I0623 09:45:02.990510  1897 net.cpp:137] Memory required for data: 1939865696
I0623 09:45:02.990532  1897 layer_factory.hpp:77] Creating layer scale4b_branch2b
I0623 09:45:02.990555  1897 net.cpp:84] Creating Layer scale4b_branch2b
I0623 09:45:02.990571  1897 net.cpp:406] scale4b_branch2b <- res4b_branch2b
I0623 09:45:02.990591  1897 net.cpp:367] scale4b_branch2b -> res4b_branch2b (in-place)
I0623 09:45:02.990620  1897 layer_factory.hpp:77] Creating layer scale4b_branch2b
I0623 09:45:02.990654  1897 net.cpp:122] Setting up scale4b_branch2b
I0623 09:45:02.990681  1897 net.cpp:129] Top shape: 8 256 16 16 (524288)
I0623 09:45:02.990700  1897 net.cpp:137] Memory required for data: 1941962848
I0623 09:45:02.990720  1897 layer_factory.hpp:77] Creating layer res4b_branch2b_relu
I0623 09:45:02.990741  1897 net.cpp:84] Creating Layer res4b_branch2b_relu
I0623 09:45:02.990767  1897 net.cpp:406] res4b_branch2b_relu <- res4b_branch2b
I0623 09:45:02.990787  1897 net.cpp:367] res4b_branch2b_relu -> res4b_branch2b (in-place)
I0623 09:45:02.990808  1897 net.cpp:122] Setting up res4b_branch2b_relu
I0623 09:45:02.990828  1897 net.cpp:129] Top shape: 8 256 16 16 (524288)
I0623 09:45:02.990844  1897 net.cpp:137] Memory required for data: 1944060000
I0623 09:45:02.990859  1897 layer_factory.hpp:77] Creating layer res4b_branch2c
I0623 09:45:02.990881  1897 net.cpp:84] Creating Layer res4b_branch2c
I0623 09:45:02.990898  1897 net.cpp:406] res4b_branch2c <- res4b_branch2b
I0623 09:45:02.990918  1897 net.cpp:380] res4b_branch2c -> res4b_branch2c
I0623 09:45:02.991420  1897 net.cpp:122] Setting up res4b_branch2c
I0623 09:45:02.991447  1897 net.cpp:129] Top shape: 8 1024 16 16 (2097152)
I0623 09:45:02.991464  1897 net.cpp:137] Memory required for data: 1952448608
I0623 09:45:02.991483  1897 layer_factory.hpp:77] Creating layer bn4b_branch2c
I0623 09:45:02.991503  1897 net.cpp:84] Creating Layer bn4b_branch2c
I0623 09:45:02.991520  1897 net.cpp:406] bn4b_branch2c <- res4b_branch2c
I0623 09:45:02.991538  1897 net.cpp:367] bn4b_branch2c -> res4b_branch2c (in-place)
I0623 09:45:02.991570  1897 net.cpp:122] Setting up bn4b_branch2c
I0623 09:45:02.991591  1897 net.cpp:129] Top shape: 8 1024 16 16 (2097152)
I0623 09:45:02.991610  1897 net.cpp:137] Memory required for data: 1960837216
I0623 09:45:02.991632  1897 layer_factory.hpp:77] Creating layer scale4b_branch2c
I0623 09:45:02.991654  1897 net.cpp:84] Creating Layer scale4b_branch2c
I0623 09:45:02.991672  1897 net.cpp:406] scale4b_branch2c <- res4b_branch2c
I0623 09:45:02.991691  1897 net.cpp:367] scale4b_branch2c -> res4b_branch2c (in-place)
I0623 09:45:02.991724  1897 layer_factory.hpp:77] Creating layer scale4b_branch2c
I0623 09:45:02.991755  1897 net.cpp:122] Setting up scale4b_branch2c
I0623 09:45:02.991776  1897 net.cpp:129] Top shape: 8 1024 16 16 (2097152)
I0623 09:45:02.991791  1897 net.cpp:137] Memory required for data: 1969225824
I0623 09:45:02.991811  1897 layer_factory.hpp:77] Creating layer res4b
I0623 09:45:02.991832  1897 net.cpp:84] Creating Layer res4b
I0623 09:45:02.991848  1897 net.cpp:406] res4b <- res4a_res4a_relu_0_split_1
I0623 09:45:02.991868  1897 net.cpp:406] res4b <- res4b_branch2c
I0623 09:45:02.991889  1897 net.cpp:380] res4b -> res4b
I0623 09:45:02.991914  1897 net.cpp:122] Setting up res4b
I0623 09:45:02.991935  1897 net.cpp:129] Top shape: 8 1024 16 16 (2097152)
I0623 09:45:02.991951  1897 net.cpp:137] Memory required for data: 1977614432
I0623 09:45:02.991967  1897 layer_factory.hpp:77] Creating layer res4b_relu
I0623 09:45:02.991986  1897 net.cpp:84] Creating Layer res4b_relu
I0623 09:45:02.992005  1897 net.cpp:406] res4b_relu <- res4b
I0623 09:45:02.992023  1897 net.cpp:367] res4b_relu -> res4b (in-place)
I0623 09:45:02.992043  1897 net.cpp:122] Setting up res4b_relu
I0623 09:45:02.992061  1897 net.cpp:129] Top shape: 8 1024 16 16 (2097152)
I0623 09:45:02.992077  1897 net.cpp:137] Memory required for data: 1986003040
I0623 09:45:02.992094  1897 layer_factory.hpp:77] Creating layer res4b_res4b_relu_0_split
I0623 09:45:02.992112  1897 net.cpp:84] Creating Layer res4b_res4b_relu_0_split
I0623 09:45:02.992128  1897 net.cpp:406] res4b_res4b_relu_0_split <- res4b
I0623 09:45:02.992146  1897 net.cpp:380] res4b_res4b_relu_0_split -> res4b_res4b_relu_0_split_0
I0623 09:45:02.992167  1897 net.cpp:380] res4b_res4b_relu_0_split -> res4b_res4b_relu_0_split_1
I0623 09:45:02.992204  1897 net.cpp:122] Setting up res4b_res4b_relu_0_split
I0623 09:45:02.992228  1897 net.cpp:129] Top shape: 8 1024 16 16 (2097152)
I0623 09:45:02.992247  1897 net.cpp:129] Top shape: 8 1024 16 16 (2097152)
I0623 09:45:02.992264  1897 net.cpp:137] Memory required for data: 2002780256
I0623 09:45:02.992280  1897 layer_factory.hpp:77] Creating layer res4c_branch2a
I0623 09:45:02.992301  1897 net.cpp:84] Creating Layer res4c_branch2a
I0623 09:45:02.992318  1897 net.cpp:406] res4c_branch2a <- res4b_res4b_relu_0_split_0
I0623 09:45:02.992341  1897 net.cpp:380] res4c_branch2a -> res4c_branch2a
I0623 09:45:02.992831  1897 net.cpp:122] Setting up res4c_branch2a
I0623 09:45:02.992859  1897 net.cpp:129] Top shape: 8 256 16 16 (524288)
I0623 09:45:02.992877  1897 net.cpp:137] Memory required for data: 2004877408
I0623 09:45:02.992898  1897 layer_factory.hpp:77] Creating layer bn4c_branch2a
I0623 09:45:02.992921  1897 net.cpp:84] Creating Layer bn4c_branch2a
I0623 09:45:02.992939  1897 net.cpp:406] bn4c_branch2a <- res4c_branch2a
I0623 09:45:02.992959  1897 net.cpp:367] bn4c_branch2a -> res4c_branch2a (in-place)
I0623 09:45:02.992988  1897 net.cpp:122] Setting up bn4c_branch2a
I0623 09:45:02.993010  1897 net.cpp:129] Top shape: 8 256 16 16 (524288)
I0623 09:45:02.993026  1897 net.cpp:137] Memory required for data: 2006974560
I0623 09:45:02.993047  1897 layer_factory.hpp:77] Creating layer scale4c_branch2a
I0623 09:45:02.993072  1897 net.cpp:84] Creating Layer scale4c_branch2a
I0623 09:45:02.993090  1897 net.cpp:406] scale4c_branch2a <- res4c_branch2a
I0623 09:45:02.993109  1897 net.cpp:367] scale4c_branch2a -> res4c_branch2a (in-place)
I0623 09:45:02.993139  1897 layer_factory.hpp:77] Creating layer scale4c_branch2a
I0623 09:45:02.993170  1897 net.cpp:122] Setting up scale4c_branch2a
I0623 09:45:02.993191  1897 net.cpp:129] Top shape: 8 256 16 16 (524288)
I0623 09:45:02.993208  1897 net.cpp:137] Memory required for data: 2009071712
I0623 09:45:02.993228  1897 layer_factory.hpp:77] Creating layer res4c_branch2a_relu
I0623 09:45:02.993247  1897 net.cpp:84] Creating Layer res4c_branch2a_relu
I0623 09:45:02.993263  1897 net.cpp:406] res4c_branch2a_relu <- res4c_branch2a
I0623 09:45:02.993283  1897 net.cpp:367] res4c_branch2a_relu -> res4c_branch2a (in-place)
I0623 09:45:02.993302  1897 net.cpp:122] Setting up res4c_branch2a_relu
I0623 09:45:02.993322  1897 net.cpp:129] Top shape: 8 256 16 16 (524288)
I0623 09:45:02.993338  1897 net.cpp:137] Memory required for data: 2011168864
I0623 09:45:02.993355  1897 layer_factory.hpp:77] Creating layer res4c_branch2b
I0623 09:45:02.993374  1897 net.cpp:84] Creating Layer res4c_branch2b
I0623 09:45:02.993392  1897 net.cpp:406] res4c_branch2b <- res4c_branch2a
I0623 09:45:02.993414  1897 net.cpp:380] res4c_branch2b -> res4c_branch2b
I0623 09:45:02.994462  1897 net.cpp:122] Setting up res4c_branch2b
I0623 09:45:02.994489  1897 net.cpp:129] Top shape: 8 256 16 16 (524288)
I0623 09:45:02.994505  1897 net.cpp:137] Memory required for data: 2013266016
I0623 09:45:02.994524  1897 layer_factory.hpp:77] Creating layer bn4c_branch2b
I0623 09:45:02.994546  1897 net.cpp:84] Creating Layer bn4c_branch2b
I0623 09:45:02.994565  1897 net.cpp:406] bn4c_branch2b <- res4c_branch2b
I0623 09:45:02.994582  1897 net.cpp:367] bn4c_branch2b -> res4c_branch2b (in-place)
I0623 09:45:02.994611  1897 net.cpp:122] Setting up bn4c_branch2b
I0623 09:45:02.994632  1897 net.cpp:129] Top shape: 8 256 16 16 (524288)
I0623 09:45:02.994648  1897 net.cpp:137] Memory required for data: 2015363168
I0623 09:45:02.994673  1897 layer_factory.hpp:77] Creating layer scale4c_branch2b
I0623 09:45:02.994699  1897 net.cpp:84] Creating Layer scale4c_branch2b
I0623 09:45:02.994717  1897 net.cpp:406] scale4c_branch2b <- res4c_branch2b
I0623 09:45:02.994736  1897 net.cpp:367] scale4c_branch2b -> res4c_branch2b (in-place)
I0623 09:45:02.994761  1897 layer_factory.hpp:77] Creating layer scale4c_branch2b
I0623 09:45:02.994792  1897 net.cpp:122] Setting up scale4c_branch2b
I0623 09:45:02.994812  1897 net.cpp:129] Top shape: 8 256 16 16 (524288)
I0623 09:45:02.994828  1897 net.cpp:137] Memory required for data: 2017460320
I0623 09:45:02.994848  1897 layer_factory.hpp:77] Creating layer res4c_branch2b_relu
I0623 09:45:02.994868  1897 net.cpp:84] Creating Layer res4c_branch2b_relu
I0623 09:45:02.994884  1897 net.cpp:406] res4c_branch2b_relu <- res4c_branch2b
I0623 09:45:02.994904  1897 net.cpp:367] res4c_branch2b_relu -> res4c_branch2b (in-place)
I0623 09:45:02.994926  1897 net.cpp:122] Setting up res4c_branch2b_relu
I0623 09:45:02.994946  1897 net.cpp:129] Top shape: 8 256 16 16 (524288)
I0623 09:45:02.994966  1897 net.cpp:137] Memory required for data: 2019557472
I0623 09:45:02.994983  1897 layer_factory.hpp:77] Creating layer res4c_branch2c
I0623 09:45:02.995004  1897 net.cpp:84] Creating Layer res4c_branch2c
I0623 09:45:02.995020  1897 net.cpp:406] res4c_branch2c <- res4c_branch2b
I0623 09:45:02.995043  1897 net.cpp:380] res4c_branch2c -> res4c_branch2c
I0623 09:45:02.995522  1897 net.cpp:122] Setting up res4c_branch2c
I0623 09:45:02.995549  1897 net.cpp:129] Top shape: 8 1024 16 16 (2097152)
I0623 09:45:02.995568  1897 net.cpp:137] Memory required for data: 2027946080
I0623 09:45:02.995586  1897 layer_factory.hpp:77] Creating layer bn4c_branch2c
I0623 09:45:02.995611  1897 net.cpp:84] Creating Layer bn4c_branch2c
I0623 09:45:02.995630  1897 net.cpp:406] bn4c_branch2c <- res4c_branch2c
I0623 09:45:02.995649  1897 net.cpp:367] bn4c_branch2c -> res4c_branch2c (in-place)
I0623 09:45:02.995679  1897 net.cpp:122] Setting up bn4c_branch2c
I0623 09:45:02.995699  1897 net.cpp:129] Top shape: 8 1024 16 16 (2097152)
I0623 09:45:02.995715  1897 net.cpp:137] Memory required for data: 2036334688
I0623 09:45:02.995736  1897 layer_factory.hpp:77] Creating layer scale4c_branch2c
I0623 09:45:02.995755  1897 net.cpp:84] Creating Layer scale4c_branch2c
I0623 09:45:02.995772  1897 net.cpp:406] scale4c_branch2c <- res4c_branch2c
I0623 09:45:02.995791  1897 net.cpp:367] scale4c_branch2c -> res4c_branch2c (in-place)
I0623 09:45:02.995822  1897 layer_factory.hpp:77] Creating layer scale4c_branch2c
I0623 09:45:02.995856  1897 net.cpp:122] Setting up scale4c_branch2c
I0623 09:45:02.995877  1897 net.cpp:129] Top shape: 8 1024 16 16 (2097152)
I0623 09:45:02.995893  1897 net.cpp:137] Memory required for data: 2044723296
I0623 09:45:02.995914  1897 layer_factory.hpp:77] Creating layer res4c
I0623 09:45:02.995934  1897 net.cpp:84] Creating Layer res4c
I0623 09:45:02.995950  1897 net.cpp:406] res4c <- res4b_res4b_relu_0_split_1
I0623 09:45:02.995968  1897 net.cpp:406] res4c <- res4c_branch2c
I0623 09:45:02.995987  1897 net.cpp:380] res4c -> res4c
I0623 09:45:02.996008  1897 net.cpp:122] Setting up res4c
I0623 09:45:02.996028  1897 net.cpp:129] Top shape: 8 1024 16 16 (2097152)
I0623 09:45:02.996044  1897 net.cpp:137] Memory required for data: 2053111904
I0623 09:45:02.996060  1897 layer_factory.hpp:77] Creating layer res4c_relu
I0623 09:45:02.996078  1897 net.cpp:84] Creating Layer res4c_relu
I0623 09:45:02.996098  1897 net.cpp:406] res4c_relu <- res4c
I0623 09:45:02.996121  1897 net.cpp:367] res4c_relu -> res4c (in-place)
I0623 09:45:02.996143  1897 net.cpp:122] Setting up res4c_relu
I0623 09:45:02.996162  1897 net.cpp:129] Top shape: 8 1024 16 16 (2097152)
I0623 09:45:02.996179  1897 net.cpp:137] Memory required for data: 2061500512
I0623 09:45:02.996196  1897 layer_factory.hpp:77] Creating layer res4c_res4c_relu_0_split
I0623 09:45:02.996217  1897 net.cpp:84] Creating Layer res4c_res4c_relu_0_split
I0623 09:45:02.996233  1897 net.cpp:406] res4c_res4c_relu_0_split <- res4c
I0623 09:45:02.996251  1897 net.cpp:380] res4c_res4c_relu_0_split -> res4c_res4c_relu_0_split_0
I0623 09:45:02.996273  1897 net.cpp:380] res4c_res4c_relu_0_split -> res4c_res4c_relu_0_split_1
I0623 09:45:02.996294  1897 net.cpp:122] Setting up res4c_res4c_relu_0_split
I0623 09:45:02.996316  1897 net.cpp:129] Top shape: 8 1024 16 16 (2097152)
I0623 09:45:02.996335  1897 net.cpp:129] Top shape: 8 1024 16 16 (2097152)
I0623 09:45:02.996351  1897 net.cpp:137] Memory required for data: 2078277728
I0623 09:45:02.996366  1897 layer_factory.hpp:77] Creating layer res4d_branch2a
I0623 09:45:02.996388  1897 net.cpp:84] Creating Layer res4d_branch2a
I0623 09:45:02.996407  1897 net.cpp:406] res4d_branch2a <- res4c_res4c_relu_0_split_0
I0623 09:45:02.996429  1897 net.cpp:380] res4d_branch2a -> res4d_branch2a
I0623 09:45:02.996912  1897 net.cpp:122] Setting up res4d_branch2a
I0623 09:45:02.996937  1897 net.cpp:129] Top shape: 8 256 16 16 (524288)
I0623 09:45:02.996955  1897 net.cpp:137] Memory required for data: 2080374880
I0623 09:45:02.996978  1897 layer_factory.hpp:77] Creating layer bn4d_branch2a
I0623 09:45:02.997005  1897 net.cpp:84] Creating Layer bn4d_branch2a
I0623 09:45:02.997023  1897 net.cpp:406] bn4d_branch2a <- res4d_branch2a
I0623 09:45:02.997042  1897 net.cpp:367] bn4d_branch2a -> res4d_branch2a (in-place)
I0623 09:45:02.997071  1897 net.cpp:122] Setting up bn4d_branch2a
I0623 09:45:02.997092  1897 net.cpp:129] Top shape: 8 256 16 16 (524288)
I0623 09:45:02.997110  1897 net.cpp:137] Memory required for data: 2082472032
I0623 09:45:02.997133  1897 layer_factory.hpp:77] Creating layer scale4d_branch2a
I0623 09:45:02.997154  1897 net.cpp:84] Creating Layer scale4d_branch2a
I0623 09:45:02.997172  1897 net.cpp:406] scale4d_branch2a <- res4d_branch2a
I0623 09:45:02.997190  1897 net.cpp:367] scale4d_branch2a -> res4d_branch2a (in-place)
I0623 09:45:02.997217  1897 layer_factory.hpp:77] Creating layer scale4d_branch2a
I0623 09:45:02.997252  1897 net.cpp:122] Setting up scale4d_branch2a
I0623 09:45:02.997275  1897 net.cpp:129] Top shape: 8 256 16 16 (524288)
I0623 09:45:02.997292  1897 net.cpp:137] Memory required for data: 2084569184
I0623 09:45:02.997311  1897 layer_factory.hpp:77] Creating layer res4d_branch2a_relu
I0623 09:45:02.997331  1897 net.cpp:84] Creating Layer res4d_branch2a_relu
I0623 09:45:02.997349  1897 net.cpp:406] res4d_branch2a_relu <- res4d_branch2a
I0623 09:45:02.997367  1897 net.cpp:367] res4d_branch2a_relu -> res4d_branch2a (in-place)
I0623 09:45:02.997387  1897 net.cpp:122] Setting up res4d_branch2a_relu
I0623 09:45:02.997406  1897 net.cpp:129] Top shape: 8 256 16 16 (524288)
I0623 09:45:02.997422  1897 net.cpp:137] Memory required for data: 2086666336
I0623 09:45:02.997438  1897 layer_factory.hpp:77] Creating layer res4d_branch2b
I0623 09:45:02.997458  1897 net.cpp:84] Creating Layer res4d_branch2b
I0623 09:45:02.997475  1897 net.cpp:406] res4d_branch2b <- res4d_branch2a
I0623 09:45:02.997496  1897 net.cpp:380] res4d_branch2b -> res4d_branch2b
I0623 09:45:02.998519  1897 net.cpp:122] Setting up res4d_branch2b
I0623 09:45:02.998545  1897 net.cpp:129] Top shape: 8 256 16 16 (524288)
I0623 09:45:02.998563  1897 net.cpp:137] Memory required for data: 2088763488
I0623 09:45:02.998580  1897 layer_factory.hpp:77] Creating layer bn4d_branch2b
I0623 09:45:02.998602  1897 net.cpp:84] Creating Layer bn4d_branch2b
I0623 09:45:02.998620  1897 net.cpp:406] bn4d_branch2b <- res4d_branch2b
I0623 09:45:02.998639  1897 net.cpp:367] bn4d_branch2b -> res4d_branch2b (in-place)
I0623 09:45:02.998672  1897 net.cpp:122] Setting up bn4d_branch2b
I0623 09:45:02.998695  1897 net.cpp:129] Top shape: 8 256 16 16 (524288)
I0623 09:45:02.998711  1897 net.cpp:137] Memory required for data: 2090860640
I0623 09:45:02.998733  1897 layer_factory.hpp:77] Creating layer scale4d_branch2b
I0623 09:45:02.998754  1897 net.cpp:84] Creating Layer scale4d_branch2b
I0623 09:45:02.998772  1897 net.cpp:406] scale4d_branch2b <- res4d_branch2b
I0623 09:45:02.998790  1897 net.cpp:367] scale4d_branch2b -> res4d_branch2b (in-place)
I0623 09:45:02.998817  1897 layer_factory.hpp:77] Creating layer scale4d_branch2b
I0623 09:45:02.998848  1897 net.cpp:122] Setting up scale4d_branch2b
I0623 09:45:02.998869  1897 net.cpp:129] Top shape: 8 256 16 16 (524288)
I0623 09:45:02.998885  1897 net.cpp:137] Memory required for data: 2092957792
I0623 09:45:02.998904  1897 layer_factory.hpp:77] Creating layer res4d_branch2b_relu
I0623 09:45:02.998924  1897 net.cpp:84] Creating Layer res4d_branch2b_relu
I0623 09:45:02.998941  1897 net.cpp:406] res4d_branch2b_relu <- res4d_branch2b
I0623 09:45:02.998961  1897 net.cpp:367] res4d_branch2b_relu -> res4d_branch2b (in-place)
I0623 09:45:02.998981  1897 net.cpp:122] Setting up res4d_branch2b_relu
I0623 09:45:02.999001  1897 net.cpp:129] Top shape: 8 256 16 16 (524288)
I0623 09:45:02.999017  1897 net.cpp:137] Memory required for data: 2095054944
I0623 09:45:02.999032  1897 layer_factory.hpp:77] Creating layer res4d_branch2c
I0623 09:45:02.999053  1897 net.cpp:84] Creating Layer res4d_branch2c
I0623 09:45:02.999070  1897 net.cpp:406] res4d_branch2c <- res4d_branch2b
I0623 09:45:02.999091  1897 net.cpp:380] res4d_branch2c -> res4d_branch2c
I0623 09:45:02.999568  1897 net.cpp:122] Setting up res4d_branch2c
I0623 09:45:02.999593  1897 net.cpp:129] Top shape: 8 1024 16 16 (2097152)
I0623 09:45:02.999610  1897 net.cpp:137] Memory required for data: 2103443552
I0623 09:45:02.999629  1897 layer_factory.hpp:77] Creating layer bn4d_branch2c
I0623 09:45:02.999650  1897 net.cpp:84] Creating Layer bn4d_branch2c
I0623 09:45:02.999670  1897 net.cpp:406] bn4d_branch2c <- res4d_branch2c
I0623 09:45:02.999688  1897 net.cpp:367] bn4d_branch2c -> res4d_branch2c (in-place)
I0623 09:45:02.999717  1897 net.cpp:122] Setting up bn4d_branch2c
I0623 09:45:02.999740  1897 net.cpp:129] Top shape: 8 1024 16 16 (2097152)
I0623 09:45:02.999758  1897 net.cpp:137] Memory required for data: 2111832160
I0623 09:45:02.999779  1897 layer_factory.hpp:77] Creating layer scale4d_branch2c
I0623 09:45:02.999799  1897 net.cpp:84] Creating Layer scale4d_branch2c
I0623 09:45:02.999816  1897 net.cpp:406] scale4d_branch2c <- res4d_branch2c
I0623 09:45:02.999835  1897 net.cpp:367] scale4d_branch2c -> res4d_branch2c (in-place)
I0623 09:45:02.999864  1897 layer_factory.hpp:77] Creating layer scale4d_branch2c
I0623 09:45:02.999897  1897 net.cpp:122] Setting up scale4d_branch2c
I0623 09:45:02.999918  1897 net.cpp:129] Top shape: 8 1024 16 16 (2097152)
I0623 09:45:02.999934  1897 net.cpp:137] Memory required for data: 2120220768
I0623 09:45:02.999954  1897 layer_factory.hpp:77] Creating layer res4d
I0623 09:45:02.999974  1897 net.cpp:84] Creating Layer res4d
I0623 09:45:02.999991  1897 net.cpp:406] res4d <- res4c_res4c_relu_0_split_1
I0623 09:45:03.000010  1897 net.cpp:406] res4d <- res4d_branch2c
I0623 09:45:03.000030  1897 net.cpp:380] res4d -> res4d
I0623 09:45:03.000061  1897 net.cpp:122] Setting up res4d
I0623 09:45:03.000080  1897 net.cpp:129] Top shape: 8 1024 16 16 (2097152)
I0623 09:45:03.000097  1897 net.cpp:137] Memory required for data: 2128609376
I0623 09:45:03.000113  1897 layer_factory.hpp:77] Creating layer res4d_relu
I0623 09:45:03.000133  1897 net.cpp:84] Creating Layer res4d_relu
I0623 09:45:03.000150  1897 net.cpp:406] res4d_relu <- res4d
I0623 09:45:03.000171  1897 net.cpp:367] res4d_relu -> res4d (in-place)
I0623 09:45:03.000191  1897 net.cpp:122] Setting up res4d_relu
I0623 09:45:03.000211  1897 net.cpp:129] Top shape: 8 1024 16 16 (2097152)
I0623 09:45:03.000226  1897 net.cpp:137] Memory required for data: 2136997984
I0623 09:45:03.000242  1897 layer_factory.hpp:77] Creating layer res4d_res4d_relu_0_split
I0623 09:45:03.000262  1897 net.cpp:84] Creating Layer res4d_res4d_relu_0_split
I0623 09:45:03.000278  1897 net.cpp:406] res4d_res4d_relu_0_split <- res4d
I0623 09:45:03.000296  1897 net.cpp:380] res4d_res4d_relu_0_split -> res4d_res4d_relu_0_split_0
I0623 09:45:03.000320  1897 net.cpp:380] res4d_res4d_relu_0_split -> res4d_res4d_relu_0_split_1
I0623 09:45:03.000344  1897 net.cpp:122] Setting up res4d_res4d_relu_0_split
I0623 09:45:03.000366  1897 net.cpp:129] Top shape: 8 1024 16 16 (2097152)
I0623 09:45:03.000385  1897 net.cpp:129] Top shape: 8 1024 16 16 (2097152)
I0623 09:45:03.000401  1897 net.cpp:137] Memory required for data: 2153775200
I0623 09:45:03.000416  1897 layer_factory.hpp:77] Creating layer res4e_branch2a
I0623 09:45:03.000437  1897 net.cpp:84] Creating Layer res4e_branch2a
I0623 09:45:03.000455  1897 net.cpp:406] res4e_branch2a <- res4d_res4d_relu_0_split_0
I0623 09:45:03.000476  1897 net.cpp:380] res4e_branch2a -> res4e_branch2a
I0623 09:45:03.000948  1897 net.cpp:122] Setting up res4e_branch2a
I0623 09:45:03.000974  1897 net.cpp:129] Top shape: 8 256 16 16 (524288)
I0623 09:45:03.000991  1897 net.cpp:137] Memory required for data: 2155872352
I0623 09:45:03.001009  1897 layer_factory.hpp:77] Creating layer bn4e_branch2a
I0623 09:45:03.001031  1897 net.cpp:84] Creating Layer bn4e_branch2a
I0623 09:45:03.001049  1897 net.cpp:406] bn4e_branch2a <- res4e_branch2a
I0623 09:45:03.001068  1897 net.cpp:367] bn4e_branch2a -> res4e_branch2a (in-place)
I0623 09:45:03.001101  1897 net.cpp:122] Setting up bn4e_branch2a
I0623 09:45:03.001121  1897 net.cpp:129] Top shape: 8 256 16 16 (524288)
I0623 09:45:03.001143  1897 net.cpp:137] Memory required for data: 2157969504
I0623 09:45:03.001165  1897 layer_factory.hpp:77] Creating layer scale4e_branch2a
I0623 09:45:03.001189  1897 net.cpp:84] Creating Layer scale4e_branch2a
I0623 09:45:03.001209  1897 net.cpp:406] scale4e_branch2a <- res4e_branch2a
I0623 09:45:03.001227  1897 net.cpp:367] scale4e_branch2a -> res4e_branch2a (in-place)
I0623 09:45:03.001255  1897 layer_factory.hpp:77] Creating layer scale4e_branch2a
I0623 09:45:03.001286  1897 net.cpp:122] Setting up scale4e_branch2a
I0623 09:45:03.001308  1897 net.cpp:129] Top shape: 8 256 16 16 (524288)
I0623 09:45:03.001324  1897 net.cpp:137] Memory required for data: 2160066656
I0623 09:45:03.001343  1897 layer_factory.hpp:77] Creating layer res4e_branch2a_relu
I0623 09:45:03.001363  1897 net.cpp:84] Creating Layer res4e_branch2a_relu
I0623 09:45:03.001379  1897 net.cpp:406] res4e_branch2a_relu <- res4e_branch2a
I0623 09:45:03.001396  1897 net.cpp:367] res4e_branch2a_relu -> res4e_branch2a (in-place)
I0623 09:45:03.001416  1897 net.cpp:122] Setting up res4e_branch2a_relu
I0623 09:45:03.001435  1897 net.cpp:129] Top shape: 8 256 16 16 (524288)
I0623 09:45:03.001452  1897 net.cpp:137] Memory required for data: 2162163808
I0623 09:45:03.001471  1897 layer_factory.hpp:77] Creating layer res4e_branch2b
I0623 09:45:03.001492  1897 net.cpp:84] Creating Layer res4e_branch2b
I0623 09:45:03.001509  1897 net.cpp:406] res4e_branch2b <- res4e_branch2a
I0623 09:45:03.001530  1897 net.cpp:380] res4e_branch2b -> res4e_branch2b
I0623 09:45:03.157510  1897 net.cpp:122] Setting up res4e_branch2b
I0623 09:45:03.157589  1897 net.cpp:129] Top shape: 8 256 16 16 (524288)
I0623 09:45:03.157605  1897 net.cpp:137] Memory required for data: 2164260960
I0623 09:45:03.157625  1897 layer_factory.hpp:77] Creating layer bn4e_branch2b
I0623 09:45:03.157654  1897 net.cpp:84] Creating Layer bn4e_branch2b
I0623 09:45:03.157675  1897 net.cpp:406] bn4e_branch2b <- res4e_branch2b
I0623 09:45:03.157696  1897 net.cpp:367] bn4e_branch2b -> res4e_branch2b (in-place)
I0623 09:45:03.157730  1897 net.cpp:122] Setting up bn4e_branch2b
I0623 09:45:03.157752  1897 net.cpp:129] Top shape: 8 256 16 16 (524288)
I0623 09:45:03.157768  1897 net.cpp:137] Memory required for data: 2166358112
I0623 09:45:03.157790  1897 layer_factory.hpp:77] Creating layer scale4e_branch2b
I0623 09:45:03.157814  1897 net.cpp:84] Creating Layer scale4e_branch2b
I0623 09:45:03.157831  1897 net.cpp:406] scale4e_branch2b <- res4e_branch2b
I0623 09:45:03.157850  1897 net.cpp:367] scale4e_branch2b -> res4e_branch2b (in-place)
I0623 09:45:03.157877  1897 layer_factory.hpp:77] Creating layer scale4e_branch2b
I0623 09:45:03.157912  1897 net.cpp:122] Setting up scale4e_branch2b
I0623 09:45:03.157932  1897 net.cpp:129] Top shape: 8 256 16 16 (524288)
I0623 09:45:03.157948  1897 net.cpp:137] Memory required for data: 2168455264
I0623 09:45:03.157968  1897 layer_factory.hpp:77] Creating layer res4e_branch2b_relu
I0623 09:45:03.157990  1897 net.cpp:84] Creating Layer res4e_branch2b_relu
I0623 09:45:03.158007  1897 net.cpp:406] res4e_branch2b_relu <- res4e_branch2b
I0623 09:45:03.158028  1897 net.cpp:367] res4e_branch2b_relu -> res4e_branch2b (in-place)
I0623 09:45:03.158049  1897 net.cpp:122] Setting up res4e_branch2b_relu
I0623 09:45:03.158068  1897 net.cpp:129] Top shape: 8 256 16 16 (524288)
I0623 09:45:03.158083  1897 net.cpp:137] Memory required for data: 2170552416
I0623 09:45:03.158099  1897 layer_factory.hpp:77] Creating layer res4e_branch2c
I0623 09:45:03.158121  1897 net.cpp:84] Creating Layer res4e_branch2c
I0623 09:45:03.158138  1897 net.cpp:406] res4e_branch2c <- res4e_branch2b
I0623 09:45:03.158160  1897 net.cpp:380] res4e_branch2c -> res4e_branch2c
I0623 09:45:03.158648  1897 net.cpp:122] Setting up res4e_branch2c
I0623 09:45:03.158679  1897 net.cpp:129] Top shape: 8 1024 16 16 (2097152)
I0623 09:45:03.158699  1897 net.cpp:137] Memory required for data: 2178941024
I0623 09:45:03.158717  1897 layer_factory.hpp:77] Creating layer bn4e_branch2c
I0623 09:45:03.158749  1897 net.cpp:84] Creating Layer bn4e_branch2c
I0623 09:45:03.158768  1897 net.cpp:406] bn4e_branch2c <- res4e_branch2c
I0623 09:45:03.158787  1897 net.cpp:367] bn4e_branch2c -> res4e_branch2c (in-place)
I0623 09:45:03.158818  1897 net.cpp:122] Setting up bn4e_branch2c
I0623 09:45:03.158838  1897 net.cpp:129] Top shape: 8 1024 16 16 (2097152)
I0623 09:45:03.158854  1897 net.cpp:137] Memory required for data: 2187329632
I0623 09:45:03.158876  1897 layer_factory.hpp:77] Creating layer scale4e_branch2c
I0623 09:45:03.158897  1897 net.cpp:84] Creating Layer scale4e_branch2c
I0623 09:45:03.158915  1897 net.cpp:406] scale4e_branch2c <- res4e_branch2c
I0623 09:45:03.158933  1897 net.cpp:367] scale4e_branch2c -> res4e_branch2c (in-place)
I0623 09:45:03.158962  1897 layer_factory.hpp:77] Creating layer scale4e_branch2c
I0623 09:45:03.158994  1897 net.cpp:122] Setting up scale4e_branch2c
I0623 09:45:03.159015  1897 net.cpp:129] Top shape: 8 1024 16 16 (2097152)
I0623 09:45:03.159031  1897 net.cpp:137] Memory required for data: 2195718240
I0623 09:45:03.159050  1897 layer_factory.hpp:77] Creating layer res4e
I0623 09:45:03.159070  1897 net.cpp:84] Creating Layer res4e
I0623 09:45:03.159086  1897 net.cpp:406] res4e <- res4d_res4d_relu_0_split_1
I0623 09:45:03.159104  1897 net.cpp:406] res4e <- res4e_branch2c
I0623 09:45:03.159123  1897 net.cpp:380] res4e -> res4e
I0623 09:45:03.159147  1897 net.cpp:122] Setting up res4e
I0623 09:45:03.159165  1897 net.cpp:129] Top shape: 8 1024 16 16 (2097152)
I0623 09:45:03.159181  1897 net.cpp:137] Memory required for data: 2204106848
I0623 09:45:03.159196  1897 layer_factory.hpp:77] Creating layer res4e_relu
I0623 09:45:03.159215  1897 net.cpp:84] Creating Layer res4e_relu
I0623 09:45:03.159231  1897 net.cpp:406] res4e_relu <- res4e
I0623 09:45:03.159252  1897 net.cpp:367] res4e_relu -> res4e (in-place)
I0623 09:45:03.159274  1897 net.cpp:122] Setting up res4e_relu
I0623 09:45:03.159293  1897 net.cpp:129] Top shape: 8 1024 16 16 (2097152)
I0623 09:45:03.159309  1897 net.cpp:137] Memory required for data: 2212495456
I0623 09:45:03.159325  1897 layer_factory.hpp:77] Creating layer res4e_res4e_relu_0_split
I0623 09:45:03.159344  1897 net.cpp:84] Creating Layer res4e_res4e_relu_0_split
I0623 09:45:03.159361  1897 net.cpp:406] res4e_res4e_relu_0_split <- res4e
I0623 09:45:03.159380  1897 net.cpp:380] res4e_res4e_relu_0_split -> res4e_res4e_relu_0_split_0
I0623 09:45:03.159401  1897 net.cpp:380] res4e_res4e_relu_0_split -> res4e_res4e_relu_0_split_1
I0623 09:45:03.159423  1897 net.cpp:122] Setting up res4e_res4e_relu_0_split
I0623 09:45:03.159446  1897 net.cpp:129] Top shape: 8 1024 16 16 (2097152)
I0623 09:45:03.159463  1897 net.cpp:129] Top shape: 8 1024 16 16 (2097152)
I0623 09:45:03.159478  1897 net.cpp:137] Memory required for data: 2229272672
I0623 09:45:03.159494  1897 layer_factory.hpp:77] Creating layer res4f_branch2a
I0623 09:45:03.159515  1897 net.cpp:84] Creating Layer res4f_branch2a
I0623 09:45:03.159533  1897 net.cpp:406] res4f_branch2a <- res4e_res4e_relu_0_split_0
I0623 09:45:03.159554  1897 net.cpp:380] res4f_branch2a -> res4f_branch2a
I0623 09:45:03.160040  1897 net.cpp:122] Setting up res4f_branch2a
I0623 09:45:03.160066  1897 net.cpp:129] Top shape: 8 256 16 16 (524288)
I0623 09:45:03.160084  1897 net.cpp:137] Memory required for data: 2231369824
I0623 09:45:03.160102  1897 layer_factory.hpp:77] Creating layer bn4f_branch2a
I0623 09:45:03.160125  1897 net.cpp:84] Creating Layer bn4f_branch2a
I0623 09:45:03.160142  1897 net.cpp:406] bn4f_branch2a <- res4f_branch2a
I0623 09:45:03.160161  1897 net.cpp:367] bn4f_branch2a -> res4f_branch2a (in-place)
I0623 09:45:03.160190  1897 net.cpp:122] Setting up bn4f_branch2a
I0623 09:45:03.160210  1897 net.cpp:129] Top shape: 8 256 16 16 (524288)
I0623 09:45:03.160228  1897 net.cpp:137] Memory required for data: 2233466976
I0623 09:45:03.160248  1897 layer_factory.hpp:77] Creating layer scale4f_branch2a
I0623 09:45:03.160269  1897 net.cpp:84] Creating Layer scale4f_branch2a
I0623 09:45:03.160287  1897 net.cpp:406] scale4f_branch2a <- res4f_branch2a
I0623 09:45:03.160310  1897 net.cpp:367] scale4f_branch2a -> res4f_branch2a (in-place)
I0623 09:45:03.160337  1897 layer_factory.hpp:77] Creating layer scale4f_branch2a
I0623 09:45:03.160370  1897 net.cpp:122] Setting up scale4f_branch2a
I0623 09:45:03.160390  1897 net.cpp:129] Top shape: 8 256 16 16 (524288)
I0623 09:45:03.160408  1897 net.cpp:137] Memory required for data: 2235564128
I0623 09:45:03.160426  1897 layer_factory.hpp:77] Creating layer res4f_branch2a_relu
I0623 09:45:03.160445  1897 net.cpp:84] Creating Layer res4f_branch2a_relu
I0623 09:45:03.160464  1897 net.cpp:406] res4f_branch2a_relu <- res4f_branch2a
I0623 09:45:03.160482  1897 net.cpp:367] res4f_branch2a_relu -> res4f_branch2a (in-place)
I0623 09:45:03.160503  1897 net.cpp:122] Setting up res4f_branch2a_relu
I0623 09:45:03.160523  1897 net.cpp:129] Top shape: 8 256 16 16 (524288)
I0623 09:45:03.160539  1897 net.cpp:137] Memory required for data: 2237661280
I0623 09:45:03.160555  1897 layer_factory.hpp:77] Creating layer res4f_branch2b
I0623 09:45:03.160575  1897 net.cpp:84] Creating Layer res4f_branch2b
I0623 09:45:03.160593  1897 net.cpp:406] res4f_branch2b <- res4f_branch2a
I0623 09:45:03.160614  1897 net.cpp:380] res4f_branch2b -> res4f_branch2b
I0623 09:45:03.161654  1897 net.cpp:122] Setting up res4f_branch2b
I0623 09:45:03.161681  1897 net.cpp:129] Top shape: 8 256 16 16 (524288)
I0623 09:45:03.161697  1897 net.cpp:137] Memory required for data: 2239758432
I0623 09:45:03.161716  1897 layer_factory.hpp:77] Creating layer bn4f_branch2b
I0623 09:45:03.161738  1897 net.cpp:84] Creating Layer bn4f_branch2b
I0623 09:45:03.161756  1897 net.cpp:406] bn4f_branch2b <- res4f_branch2b
I0623 09:45:03.161775  1897 net.cpp:367] bn4f_branch2b -> res4f_branch2b (in-place)
I0623 09:45:03.161804  1897 net.cpp:122] Setting up bn4f_branch2b
I0623 09:45:03.161824  1897 net.cpp:129] Top shape: 8 256 16 16 (524288)
I0623 09:45:03.161840  1897 net.cpp:137] Memory required for data: 2241855584
I0623 09:45:03.161860  1897 layer_factory.hpp:77] Creating layer scale4f_branch2b
I0623 09:45:03.161881  1897 net.cpp:84] Creating Layer scale4f_branch2b
I0623 09:45:03.161900  1897 net.cpp:406] scale4f_branch2b <- res4f_branch2b
I0623 09:45:03.161918  1897 net.cpp:367] scale4f_branch2b -> res4f_branch2b (in-place)
I0623 09:45:03.161943  1897 layer_factory.hpp:77] Creating layer scale4f_branch2b
I0623 09:45:03.161974  1897 net.cpp:122] Setting up scale4f_branch2b
I0623 09:45:03.161996  1897 net.cpp:129] Top shape: 8 256 16 16 (524288)
I0623 09:45:03.162014  1897 net.cpp:137] Memory required for data: 2243952736
I0623 09:45:03.162032  1897 layer_factory.hpp:77] Creating layer res4f_branch2b_relu
I0623 09:45:03.162051  1897 net.cpp:84] Creating Layer res4f_branch2b_relu
I0623 09:45:03.162070  1897 net.cpp:406] res4f_branch2b_relu <- res4f_branch2b
I0623 09:45:03.162089  1897 net.cpp:367] res4f_branch2b_relu -> res4f_branch2b (in-place)
I0623 09:45:03.162109  1897 net.cpp:122] Setting up res4f_branch2b_relu
I0623 09:45:03.162128  1897 net.cpp:129] Top shape: 8 256 16 16 (524288)
I0623 09:45:03.162144  1897 net.cpp:137] Memory required for data: 2246049888
I0623 09:45:03.162160  1897 layer_factory.hpp:77] Creating layer res4f_branch2c
I0623 09:45:03.162180  1897 net.cpp:84] Creating Layer res4f_branch2c
I0623 09:45:03.162197  1897 net.cpp:406] res4f_branch2c <- res4f_branch2b
I0623 09:45:03.162219  1897 net.cpp:380] res4f_branch2c -> res4f_branch2c
I0623 09:45:03.162704  1897 net.cpp:122] Setting up res4f_branch2c
I0623 09:45:03.162731  1897 net.cpp:129] Top shape: 8 1024 16 16 (2097152)
I0623 09:45:03.162748  1897 net.cpp:137] Memory required for data: 2254438496
I0623 09:45:03.162767  1897 layer_factory.hpp:77] Creating layer bn4f_branch2c
I0623 09:45:03.162794  1897 net.cpp:84] Creating Layer bn4f_branch2c
I0623 09:45:03.162813  1897 net.cpp:406] bn4f_branch2c <- res4f_branch2c
I0623 09:45:03.162832  1897 net.cpp:367] bn4f_branch2c -> res4f_branch2c (in-place)
I0623 09:45:03.162863  1897 net.cpp:122] Setting up bn4f_branch2c
I0623 09:45:03.162883  1897 net.cpp:129] Top shape: 8 1024 16 16 (2097152)
I0623 09:45:03.162904  1897 net.cpp:137] Memory required for data: 2262827104
I0623 09:45:03.162957  1897 layer_factory.hpp:77] Creating layer scale4f_branch2c
I0623 09:45:03.162981  1897 net.cpp:84] Creating Layer scale4f_branch2c
I0623 09:45:03.162998  1897 net.cpp:406] scale4f_branch2c <- res4f_branch2c
I0623 09:45:03.163017  1897 net.cpp:367] scale4f_branch2c -> res4f_branch2c (in-place)
I0623 09:45:03.163046  1897 layer_factory.hpp:77] Creating layer scale4f_branch2c
I0623 09:45:03.163080  1897 net.cpp:122] Setting up scale4f_branch2c
I0623 09:45:03.163101  1897 net.cpp:129] Top shape: 8 1024 16 16 (2097152)
I0623 09:45:03.163117  1897 net.cpp:137] Memory required for data: 2271215712
I0623 09:45:03.163138  1897 layer_factory.hpp:77] Creating layer res4f
I0623 09:45:03.163159  1897 net.cpp:84] Creating Layer res4f
I0623 09:45:03.163177  1897 net.cpp:406] res4f <- res4e_res4e_relu_0_split_1
I0623 09:45:03.163195  1897 net.cpp:406] res4f <- res4f_branch2c
I0623 09:45:03.163216  1897 net.cpp:380] res4f -> res4f
I0623 09:45:03.163239  1897 net.cpp:122] Setting up res4f
I0623 09:45:03.163259  1897 net.cpp:129] Top shape: 8 1024 16 16 (2097152)
I0623 09:45:03.163275  1897 net.cpp:137] Memory required for data: 2279604320
I0623 09:45:03.163290  1897 layer_factory.hpp:77] Creating layer res4f_relu
I0623 09:45:03.163310  1897 net.cpp:84] Creating Layer res4f_relu
I0623 09:45:03.163326  1897 net.cpp:406] res4f_relu <- res4f
I0623 09:45:03.163347  1897 net.cpp:367] res4f_relu -> res4f (in-place)
I0623 09:45:03.163367  1897 net.cpp:122] Setting up res4f_relu
I0623 09:45:03.163385  1897 net.cpp:129] Top shape: 8 1024 16 16 (2097152)
I0623 09:45:03.163401  1897 net.cpp:137] Memory required for data: 2287992928
I0623 09:45:03.163417  1897 layer_factory.hpp:77] Creating layer res4f_res4f_relu_0_split
I0623 09:45:03.163436  1897 net.cpp:84] Creating Layer res4f_res4f_relu_0_split
I0623 09:45:03.163452  1897 net.cpp:406] res4f_res4f_relu_0_split <- res4f
I0623 09:45:03.163471  1897 net.cpp:380] res4f_res4f_relu_0_split -> res4f_res4f_relu_0_split_0
I0623 09:45:03.163492  1897 net.cpp:380] res4f_res4f_relu_0_split -> res4f_res4f_relu_0_split_1
I0623 09:45:03.163514  1897 net.cpp:122] Setting up res4f_res4f_relu_0_split
I0623 09:45:03.163533  1897 net.cpp:129] Top shape: 8 1024 16 16 (2097152)
I0623 09:45:03.163550  1897 net.cpp:129] Top shape: 8 1024 16 16 (2097152)
I0623 09:45:03.163566  1897 net.cpp:137] Memory required for data: 2304770144
I0623 09:45:03.163583  1897 layer_factory.hpp:77] Creating layer res5a_branch1
I0623 09:45:03.163604  1897 net.cpp:84] Creating Layer res5a_branch1
I0623 09:45:03.163622  1897 net.cpp:406] res5a_branch1 <- res4f_res4f_relu_0_split_0
I0623 09:45:03.163643  1897 net.cpp:380] res5a_branch1 -> res5a_branch1
I0623 09:45:03.325168  1897 net.cpp:122] Setting up res5a_branch1
I0623 09:45:03.325309  1897 net.cpp:129] Top shape: 8 2048 8 8 (1048576)
I0623 09:45:03.325342  1897 net.cpp:137] Memory required for data: 2308964448
I0623 09:45:03.325392  1897 layer_factory.hpp:77] Creating layer bn5a_branch1
I0623 09:45:03.325435  1897 net.cpp:84] Creating Layer bn5a_branch1
I0623 09:45:03.325469  1897 net.cpp:406] bn5a_branch1 <- res5a_branch1
I0623 09:45:03.325502  1897 net.cpp:367] bn5a_branch1 -> res5a_branch1 (in-place)
I0623 09:45:03.325552  1897 net.cpp:122] Setting up bn5a_branch1
I0623 09:45:03.325588  1897 net.cpp:129] Top shape: 8 2048 8 8 (1048576)
I0623 09:45:03.325618  1897 net.cpp:137] Memory required for data: 2313158752
I0623 09:45:03.325652  1897 layer_factory.hpp:77] Creating layer scale5a_branch1
I0623 09:45:03.325686  1897 net.cpp:84] Creating Layer scale5a_branch1
I0623 09:45:03.325717  1897 net.cpp:406] scale5a_branch1 <- res5a_branch1
I0623 09:45:03.325759  1897 net.cpp:367] scale5a_branch1 -> res5a_branch1 (in-place)
I0623 09:45:03.325806  1897 layer_factory.hpp:77] Creating layer scale5a_branch1
I0623 09:45:03.325860  1897 net.cpp:122] Setting up scale5a_branch1
I0623 09:45:03.325894  1897 net.cpp:129] Top shape: 8 2048 8 8 (1048576)
I0623 09:45:03.325932  1897 net.cpp:137] Memory required for data: 2317353056
I0623 09:45:03.325966  1897 layer_factory.hpp:77] Creating layer res5a_branch2a
I0623 09:45:03.326004  1897 net.cpp:84] Creating Layer res5a_branch2a
I0623 09:45:03.326036  1897 net.cpp:406] res5a_branch2a <- res4f_res4f_relu_0_split_1
I0623 09:45:03.326069  1897 net.cpp:380] res5a_branch2a -> res5a_branch2a
I0623 09:45:03.327066  1897 net.cpp:122] Setting up res5a_branch2a
I0623 09:45:03.327122  1897 net.cpp:129] Top shape: 8 512 8 8 (262144)
I0623 09:45:03.327152  1897 net.cpp:137] Memory required for data: 2318401632
I0623 09:45:03.327184  1897 layer_factory.hpp:77] Creating layer bn5a_branch2a
I0623 09:45:03.327217  1897 net.cpp:84] Creating Layer bn5a_branch2a
I0623 09:45:03.327249  1897 net.cpp:406] bn5a_branch2a <- res5a_branch2a
I0623 09:45:03.327280  1897 net.cpp:367] bn5a_branch2a -> res5a_branch2a (in-place)
I0623 09:45:03.327324  1897 net.cpp:122] Setting up bn5a_branch2a
I0623 09:45:03.327359  1897 net.cpp:129] Top shape: 8 512 8 8 (262144)
I0623 09:45:03.327389  1897 net.cpp:137] Memory required for data: 2319450208
I0623 09:45:03.327422  1897 layer_factory.hpp:77] Creating layer scale5a_branch2a
I0623 09:45:03.327466  1897 net.cpp:84] Creating Layer scale5a_branch2a
I0623 09:45:03.327498  1897 net.cpp:406] scale5a_branch2a <- res5a_branch2a
I0623 09:45:03.327530  1897 net.cpp:367] scale5a_branch2a -> res5a_branch2a (in-place)
I0623 09:45:03.327574  1897 layer_factory.hpp:77] Creating layer scale5a_branch2a
I0623 09:45:03.327633  1897 net.cpp:122] Setting up scale5a_branch2a
I0623 09:45:03.327671  1897 net.cpp:129] Top shape: 8 512 8 8 (262144)
I0623 09:45:03.327699  1897 net.cpp:137] Memory required for data: 2320498784
I0623 09:45:03.327733  1897 layer_factory.hpp:77] Creating layer res5a_branch2a_relu
I0623 09:45:03.327765  1897 net.cpp:84] Creating Layer res5a_branch2a_relu
I0623 09:45:03.327795  1897 net.cpp:406] res5a_branch2a_relu <- res5a_branch2a
I0623 09:45:03.327826  1897 net.cpp:367] res5a_branch2a_relu -> res5a_branch2a (in-place)
I0623 09:45:03.327859  1897 net.cpp:122] Setting up res5a_branch2a_relu
I0623 09:45:03.327891  1897 net.cpp:129] Top shape: 8 512 8 8 (262144)
I0623 09:45:03.327926  1897 net.cpp:137] Memory required for data: 2321547360
I0623 09:45:03.327958  1897 layer_factory.hpp:77] Creating layer res5a_branch2b
I0623 09:45:03.327991  1897 net.cpp:84] Creating Layer res5a_branch2b
I0623 09:45:03.328022  1897 net.cpp:406] res5a_branch2b <- res5a_branch2a
I0623 09:45:03.328057  1897 net.cpp:380] res5a_branch2b -> res5a_branch2b
I0623 09:45:03.468375  1897 net.cpp:122] Setting up res5a_branch2b
I0623 09:45:03.468407  1897 net.cpp:129] Top shape: 8 512 8 8 (262144)
I0623 09:45:03.468411  1897 net.cpp:137] Memory required for data: 2322595936
I0623 09:45:03.468420  1897 layer_factory.hpp:77] Creating layer bn5a_branch2b
I0623 09:45:03.468435  1897 net.cpp:84] Creating Layer bn5a_branch2b
I0623 09:45:03.468441  1897 net.cpp:406] bn5a_branch2b <- res5a_branch2b
I0623 09:45:03.468447  1897 net.cpp:367] bn5a_branch2b -> res5a_branch2b (in-place)
I0623 09:45:03.468475  1897 net.cpp:122] Setting up bn5a_branch2b
I0623 09:45:03.468483  1897 net.cpp:129] Top shape: 8 512 8 8 (262144)
I0623 09:45:03.468487  1897 net.cpp:137] Memory required for data: 2323644512
I0623 09:45:03.468495  1897 layer_factory.hpp:77] Creating layer scale5a_branch2b
I0623 09:45:03.468503  1897 net.cpp:84] Creating Layer scale5a_branch2b
I0623 09:45:03.468508  1897 net.cpp:406] scale5a_branch2b <- res5a_branch2b
I0623 09:45:03.468513  1897 net.cpp:367] scale5a_branch2b -> res5a_branch2b (in-place)
I0623 09:45:03.468530  1897 layer_factory.hpp:77] Creating layer scale5a_branch2b
I0623 09:45:03.468554  1897 net.cpp:122] Setting up scale5a_branch2b
I0623 09:45:03.468560  1897 net.cpp:129] Top shape: 8 512 8 8 (262144)
I0623 09:45:03.468564  1897 net.cpp:137] Memory required for data: 2324693088
I0623 09:45:03.468570  1897 layer_factory.hpp:77] Creating layer res5a_branch2b_relu
I0623 09:45:03.468577  1897 net.cpp:84] Creating Layer res5a_branch2b_relu
I0623 09:45:03.468581  1897 net.cpp:406] res5a_branch2b_relu <- res5a_branch2b
I0623 09:45:03.468588  1897 net.cpp:367] res5a_branch2b_relu -> res5a_branch2b (in-place)
I0623 09:45:03.468595  1897 net.cpp:122] Setting up res5a_branch2b_relu
I0623 09:45:03.468601  1897 net.cpp:129] Top shape: 8 512 8 8 (262144)
I0623 09:45:03.468605  1897 net.cpp:137] Memory required for data: 2325741664
I0623 09:45:03.468610  1897 layer_factory.hpp:77] Creating layer res5a_branch2c
I0623 09:45:03.468619  1897 net.cpp:84] Creating Layer res5a_branch2c
I0623 09:45:03.468624  1897 net.cpp:406] res5a_branch2c <- res5a_branch2b
I0623 09:45:03.468631  1897 net.cpp:380] res5a_branch2c -> res5a_branch2c
I0623 09:45:03.490643  1897 net.cpp:122] Setting up res5a_branch2c
I0623 09:45:03.490725  1897 net.cpp:129] Top shape: 8 2048 8 8 (1048576)
I0623 09:45:03.490741  1897 net.cpp:137] Memory required for data: 2329935968
I0623 09:45:03.490761  1897 layer_factory.hpp:77] Creating layer bn5a_branch2c
I0623 09:45:03.490788  1897 net.cpp:84] Creating Layer bn5a_branch2c
I0623 09:45:03.490808  1897 net.cpp:406] bn5a_branch2c <- res5a_branch2c
I0623 09:45:03.490829  1897 net.cpp:367] bn5a_branch2c -> res5a_branch2c (in-place)
I0623 09:45:03.490866  1897 net.cpp:122] Setting up bn5a_branch2c
I0623 09:45:03.490890  1897 net.cpp:129] Top shape: 8 2048 8 8 (1048576)
I0623 09:45:03.490906  1897 net.cpp:137] Memory required for data: 2334130272
I0623 09:45:03.490929  1897 layer_factory.hpp:77] Creating layer scale5a_branch2c
I0623 09:45:03.490952  1897 net.cpp:84] Creating Layer scale5a_branch2c
I0623 09:45:03.490970  1897 net.cpp:406] scale5a_branch2c <- res5a_branch2c
I0623 09:45:03.490989  1897 net.cpp:367] scale5a_branch2c -> res5a_branch2c (in-place)
I0623 09:45:03.491020  1897 layer_factory.hpp:77] Creating layer scale5a_branch2c
I0623 09:45:03.491060  1897 net.cpp:122] Setting up scale5a_branch2c
I0623 09:45:03.491081  1897 net.cpp:129] Top shape: 8 2048 8 8 (1048576)
I0623 09:45:03.491097  1897 net.cpp:137] Memory required for data: 2338324576
I0623 09:45:03.491117  1897 layer_factory.hpp:77] Creating layer res5a
I0623 09:45:03.491137  1897 net.cpp:84] Creating Layer res5a
I0623 09:45:03.491155  1897 net.cpp:406] res5a <- res5a_branch1
I0623 09:45:03.491174  1897 net.cpp:406] res5a <- res5a_branch2c
I0623 09:45:03.491197  1897 net.cpp:380] res5a -> res5a
I0623 09:45:03.491220  1897 net.cpp:122] Setting up res5a
I0623 09:45:03.491241  1897 net.cpp:129] Top shape: 8 2048 8 8 (1048576)
I0623 09:45:03.491257  1897 net.cpp:137] Memory required for data: 2342518880
I0623 09:45:03.491274  1897 layer_factory.hpp:77] Creating layer res5a_relu
I0623 09:45:03.491293  1897 net.cpp:84] Creating Layer res5a_relu
I0623 09:45:03.491310  1897 net.cpp:406] res5a_relu <- res5a
I0623 09:45:03.491329  1897 net.cpp:367] res5a_relu -> res5a (in-place)
I0623 09:45:03.491349  1897 net.cpp:122] Setting up res5a_relu
I0623 09:45:03.491369  1897 net.cpp:129] Top shape: 8 2048 8 8 (1048576)
I0623 09:45:03.491382  1897 net.cpp:137] Memory required for data: 2346713184
I0623 09:45:03.491399  1897 layer_factory.hpp:77] Creating layer res5a_res5a_relu_0_split
I0623 09:45:03.491420  1897 net.cpp:84] Creating Layer res5a_res5a_relu_0_split
I0623 09:45:03.491437  1897 net.cpp:406] res5a_res5a_relu_0_split <- res5a
I0623 09:45:03.491456  1897 net.cpp:380] res5a_res5a_relu_0_split -> res5a_res5a_relu_0_split_0
I0623 09:45:03.491478  1897 net.cpp:380] res5a_res5a_relu_0_split -> res5a_res5a_relu_0_split_1
I0623 09:45:03.491500  1897 net.cpp:122] Setting up res5a_res5a_relu_0_split
I0623 09:45:03.491520  1897 net.cpp:129] Top shape: 8 2048 8 8 (1048576)
I0623 09:45:03.491539  1897 net.cpp:129] Top shape: 8 2048 8 8 (1048576)
I0623 09:45:03.491554  1897 net.cpp:137] Memory required for data: 2355101792
I0623 09:45:03.491570  1897 layer_factory.hpp:77] Creating layer res5b_branch2a
I0623 09:45:03.491591  1897 net.cpp:84] Creating Layer res5b_branch2a
I0623 09:45:03.491610  1897 net.cpp:406] res5b_branch2a <- res5a_res5a_relu_0_split_0
I0623 09:45:03.491631  1897 net.cpp:380] res5b_branch2a -> res5b_branch2a
I0623 09:45:03.519232  1897 net.cpp:122] Setting up res5b_branch2a
I0623 09:45:03.519333  1897 net.cpp:129] Top shape: 8 512 8 8 (262144)
I0623 09:45:03.519351  1897 net.cpp:137] Memory required for data: 2356150368
I0623 09:45:03.519371  1897 layer_factory.hpp:77] Creating layer bn5b_branch2a
I0623 09:45:03.519398  1897 net.cpp:84] Creating Layer bn5b_branch2a
I0623 09:45:03.519423  1897 net.cpp:406] bn5b_branch2a <- res5b_branch2a
I0623 09:45:03.519455  1897 net.cpp:367] bn5b_branch2a -> res5b_branch2a (in-place)
I0623 09:45:03.519505  1897 net.cpp:122] Setting up bn5b_branch2a
I0623 09:45:03.519529  1897 net.cpp:129] Top shape: 8 512 8 8 (262144)
I0623 09:45:03.519549  1897 net.cpp:137] Memory required for data: 2357198944
I0623 09:45:03.519575  1897 layer_factory.hpp:77] Creating layer scale5b_branch2a
I0623 09:45:03.519604  1897 net.cpp:84] Creating Layer scale5b_branch2a
I0623 09:45:03.519625  1897 net.cpp:406] scale5b_branch2a <- res5b_branch2a
I0623 09:45:03.519647  1897 net.cpp:367] scale5b_branch2a -> res5b_branch2a (in-place)
I0623 09:45:03.519681  1897 layer_factory.hpp:77] Creating layer scale5b_branch2a
I0623 09:45:03.519719  1897 net.cpp:122] Setting up scale5b_branch2a
I0623 09:45:03.519740  1897 net.cpp:129] Top shape: 8 512 8 8 (262144)
I0623 09:45:03.519757  1897 net.cpp:137] Memory required for data: 2358247520
I0623 09:45:03.519778  1897 layer_factory.hpp:77] Creating layer res5b_branch2a_relu
I0623 09:45:03.519798  1897 net.cpp:84] Creating Layer res5b_branch2a_relu
I0623 09:45:03.519817  1897 net.cpp:406] res5b_branch2a_relu <- res5b_branch2a
I0623 09:45:03.519839  1897 net.cpp:367] res5b_branch2a_relu -> res5b_branch2a (in-place)
I0623 09:45:03.519862  1897 net.cpp:122] Setting up res5b_branch2a_relu
I0623 09:45:03.519886  1897 net.cpp:129] Top shape: 8 512 8 8 (262144)
I0623 09:45:03.519904  1897 net.cpp:137] Memory required for data: 2359296096
I0623 09:45:03.519923  1897 layer_factory.hpp:77] Creating layer res5b_branch2b
I0623 09:45:03.519951  1897 net.cpp:84] Creating Layer res5b_branch2b
I0623 09:45:03.519975  1897 net.cpp:406] res5b_branch2b <- res5b_branch2a
I0623 09:45:03.519999  1897 net.cpp:380] res5b_branch2b -> res5b_branch2b
I0623 09:45:03.672617  1897 net.cpp:122] Setting up res5b_branch2b
I0623 09:45:03.672765  1897 net.cpp:129] Top shape: 8 512 8 8 (262144)
I0623 09:45:03.672798  1897 net.cpp:137] Memory required for data: 2360344672
I0623 09:45:03.672848  1897 layer_factory.hpp:77] Creating layer bn5b_branch2b
I0623 09:45:03.672889  1897 net.cpp:84] Creating Layer bn5b_branch2b
I0623 09:45:03.672922  1897 net.cpp:406] bn5b_branch2b <- res5b_branch2b
I0623 09:45:03.672957  1897 net.cpp:367] bn5b_branch2b -> res5b_branch2b (in-place)
I0623 09:45:03.673010  1897 net.cpp:122] Setting up bn5b_branch2b
I0623 09:45:03.673046  1897 net.cpp:129] Top shape: 8 512 8 8 (262144)
I0623 09:45:03.673076  1897 net.cpp:137] Memory required for data: 2361393248
I0623 09:45:03.673112  1897 layer_factory.hpp:77] Creating layer scale5b_branch2b
I0623 09:45:03.673147  1897 net.cpp:84] Creating Layer scale5b_branch2b
I0623 09:45:03.673179  1897 net.cpp:406] scale5b_branch2b <- res5b_branch2b
I0623 09:45:03.673228  1897 net.cpp:367] scale5b_branch2b -> res5b_branch2b (in-place)
I0623 09:45:03.673280  1897 layer_factory.hpp:77] Creating layer scale5b_branch2b
I0623 09:45:03.673333  1897 net.cpp:122] Setting up scale5b_branch2b
I0623 09:45:03.673370  1897 net.cpp:129] Top shape: 8 512 8 8 (262144)
I0623 09:45:03.673400  1897 net.cpp:137] Memory required for data: 2362441824
I0623 09:45:03.673434  1897 layer_factory.hpp:77] Creating layer res5b_branch2b_relu
I0623 09:45:03.673468  1897 net.cpp:84] Creating Layer res5b_branch2b_relu
I0623 09:45:03.673499  1897 net.cpp:406] res5b_branch2b_relu <- res5b_branch2b
I0623 09:45:03.673532  1897 net.cpp:367] res5b_branch2b_relu -> res5b_branch2b (in-place)
I0623 09:45:03.673564  1897 net.cpp:122] Setting up res5b_branch2b_relu
I0623 09:45:03.673598  1897 net.cpp:129] Top shape: 8 512 8 8 (262144)
I0623 09:45:03.673629  1897 net.cpp:137] Memory required for data: 2363490400
I0623 09:45:03.673666  1897 layer_factory.hpp:77] Creating layer res5b_branch2c
I0623 09:45:03.673702  1897 net.cpp:84] Creating Layer res5b_branch2c
I0623 09:45:03.673759  1897 net.cpp:406] res5b_branch2c <- res5b_branch2b
I0623 09:45:03.673794  1897 net.cpp:380] res5b_branch2c -> res5b_branch2c
I0623 09:45:03.725167  1897 net.cpp:122] Setting up res5b_branch2c
I0623 09:45:03.725303  1897 net.cpp:129] Top shape: 8 2048 8 8 (1048576)
I0623 09:45:03.725337  1897 net.cpp:137] Memory required for data: 2367684704
I0623 09:45:03.725384  1897 layer_factory.hpp:77] Creating layer bn5b_branch2c
I0623 09:45:03.725425  1897 net.cpp:84] Creating Layer bn5b_branch2c
I0623 09:45:03.725458  1897 net.cpp:406] bn5b_branch2c <- res5b_branch2c
I0623 09:45:03.725494  1897 net.cpp:367] bn5b_branch2c -> res5b_branch2c (in-place)
I0623 09:45:03.725555  1897 net.cpp:122] Setting up bn5b_branch2c
I0623 09:45:03.725592  1897 net.cpp:129] Top shape: 8 2048 8 8 (1048576)
I0623 09:45:03.725622  1897 net.cpp:137] Memory required for data: 2371879008
I0623 09:45:03.725659  1897 layer_factory.hpp:77] Creating layer scale5b_branch2c
I0623 09:45:03.725706  1897 net.cpp:84] Creating Layer scale5b_branch2c
I0623 09:45:03.725739  1897 net.cpp:406] scale5b_branch2c <- res5b_branch2c
I0623 09:45:03.725771  1897 net.cpp:367] scale5b_branch2c -> res5b_branch2c (in-place)
I0623 09:45:03.725817  1897 layer_factory.hpp:77] Creating layer scale5b_branch2c
I0623 09:45:03.725870  1897 net.cpp:122] Setting up scale5b_branch2c
I0623 09:45:03.725906  1897 net.cpp:129] Top shape: 8 2048 8 8 (1048576)
I0623 09:45:03.725965  1897 net.cpp:137] Memory required for data: 2376073312
I0623 09:45:03.725998  1897 layer_factory.hpp:77] Creating layer res5b
I0623 09:45:03.726033  1897 net.cpp:84] Creating Layer res5b
I0623 09:45:03.726064  1897 net.cpp:406] res5b <- res5a_res5a_relu_0_split_1
I0623 09:45:03.726096  1897 net.cpp:406] res5b <- res5b_branch2c
I0623 09:45:03.726128  1897 net.cpp:380] res5b -> res5b
I0623 09:45:03.726166  1897 net.cpp:122] Setting up res5b
I0623 09:45:03.726215  1897 net.cpp:129] Top shape: 8 2048 8 8 (1048576)
I0623 09:45:03.726249  1897 net.cpp:137] Memory required for data: 2380267616
I0623 09:45:03.726284  1897 layer_factory.hpp:77] Creating layer res5b_relu
I0623 09:45:03.726321  1897 net.cpp:84] Creating Layer res5b_relu
I0623 09:45:03.726359  1897 net.cpp:406] res5b_relu <- res5b
I0623 09:45:03.726393  1897 net.cpp:367] res5b_relu -> res5b (in-place)
I0623 09:45:03.726434  1897 net.cpp:122] Setting up res5b_relu
I0623 09:45:03.726487  1897 net.cpp:129] Top shape: 8 2048 8 8 (1048576)
I0623 09:45:03.726523  1897 net.cpp:137] Memory required for data: 2384461920
I0623 09:45:03.726557  1897 layer_factory.hpp:77] Creating layer res5b_res5b_relu_0_split
I0623 09:45:03.726595  1897 net.cpp:84] Creating Layer res5b_res5b_relu_0_split
I0623 09:45:03.726629  1897 net.cpp:406] res5b_res5b_relu_0_split <- res5b
I0623 09:45:03.726675  1897 net.cpp:380] res5b_res5b_relu_0_split -> res5b_res5b_relu_0_split_0
I0623 09:45:03.726717  1897 net.cpp:380] res5b_res5b_relu_0_split -> res5b_res5b_relu_0_split_1
I0623 09:45:03.726758  1897 net.cpp:122] Setting up res5b_res5b_relu_0_split
I0623 09:45:03.726809  1897 net.cpp:129] Top shape: 8 2048 8 8 (1048576)
I0623 09:45:03.726845  1897 net.cpp:129] Top shape: 8 2048 8 8 (1048576)
I0623 09:45:03.726881  1897 net.cpp:137] Memory required for data: 2392850528
I0623 09:45:03.726917  1897 layer_factory.hpp:77] Creating layer res5c_branch2a
I0623 09:45:03.726956  1897 net.cpp:84] Creating Layer res5c_branch2a
I0623 09:45:03.726992  1897 net.cpp:406] res5c_branch2a <- res5b_res5b_relu_0_split_0
I0623 09:45:03.727028  1897 net.cpp:380] res5c_branch2a -> res5c_branch2a
I0623 09:45:03.772361  1897 net.cpp:122] Setting up res5c_branch2a
I0623 09:45:03.772495  1897 net.cpp:129] Top shape: 8 512 8 8 (262144)
I0623 09:45:03.772528  1897 net.cpp:137] Memory required for data: 2393899104
I0623 09:45:03.772577  1897 layer_factory.hpp:77] Creating layer bn5c_branch2a
I0623 09:45:03.772622  1897 net.cpp:84] Creating Layer bn5c_branch2a
I0623 09:45:03.772666  1897 net.cpp:406] bn5c_branch2a <- res5c_branch2a
I0623 09:45:03.772703  1897 net.cpp:367] bn5c_branch2a -> res5c_branch2a (in-place)
I0623 09:45:03.772754  1897 net.cpp:122] Setting up bn5c_branch2a
I0623 09:45:03.772791  1897 net.cpp:129] Top shape: 8 512 8 8 (262144)
I0623 09:45:03.772822  1897 net.cpp:137] Memory required for data: 2394947680
I0623 09:45:03.772858  1897 layer_factory.hpp:77] Creating layer scale5c_branch2a
I0623 09:45:03.772894  1897 net.cpp:84] Creating Layer scale5c_branch2a
I0623 09:45:03.772925  1897 net.cpp:406] scale5c_branch2a <- res5c_branch2a
I0623 09:45:03.772967  1897 net.cpp:367] scale5c_branch2a -> res5c_branch2a (in-place)
I0623 09:45:03.773021  1897 layer_factory.hpp:77] Creating layer scale5c_branch2a
I0623 09:45:03.773074  1897 net.cpp:122] Setting up scale5c_branch2a
I0623 09:45:03.773110  1897 net.cpp:129] Top shape: 8 512 8 8 (262144)
I0623 09:45:03.773140  1897 net.cpp:137] Memory required for data: 2395996256
I0623 09:45:03.773174  1897 layer_factory.hpp:77] Creating layer res5c_branch2a_relu
I0623 09:45:03.773208  1897 net.cpp:84] Creating Layer res5c_branch2a_relu
I0623 09:45:03.773239  1897 net.cpp:406] res5c_branch2a_relu <- res5c_branch2a
I0623 09:45:03.773272  1897 net.cpp:367] res5c_branch2a_relu -> res5c_branch2a (in-place)
I0623 09:45:03.773305  1897 net.cpp:122] Setting up res5c_branch2a_relu
I0623 09:45:03.773337  1897 net.cpp:129] Top shape: 8 512 8 8 (262144)
I0623 09:45:03.773367  1897 net.cpp:137] Memory required for data: 2397044832
I0623 09:45:03.773397  1897 layer_factory.hpp:77] Creating layer res5c_branch2b
I0623 09:45:03.773434  1897 net.cpp:84] Creating Layer res5c_branch2b
I0623 09:45:03.773500  1897 net.cpp:406] res5c_branch2b <- res5c_branch2a
I0623 09:45:03.773543  1897 net.cpp:380] res5c_branch2b -> res5c_branch2b
I0623 09:45:03.860416  1897 net.cpp:122] Setting up res5c_branch2b
I0623 09:45:03.860450  1897 net.cpp:129] Top shape: 8 512 8 8 (262144)
I0623 09:45:03.860455  1897 net.cpp:137] Memory required for data: 2398093408
I0623 09:45:03.860463  1897 layer_factory.hpp:77] Creating layer bn5c_branch2b
I0623 09:45:03.860476  1897 net.cpp:84] Creating Layer bn5c_branch2b
I0623 09:45:03.860481  1897 net.cpp:406] bn5c_branch2b <- res5c_branch2b
I0623 09:45:03.860487  1897 net.cpp:367] bn5c_branch2b -> res5c_branch2b (in-place)
I0623 09:45:03.860508  1897 net.cpp:122] Setting up bn5c_branch2b
I0623 09:45:03.860514  1897 net.cpp:129] Top shape: 8 512 8 8 (262144)
I0623 09:45:03.860518  1897 net.cpp:137] Memory required for data: 2399141984
I0623 09:45:03.860527  1897 layer_factory.hpp:77] Creating layer scale5c_branch2b
I0623 09:45:03.860536  1897 net.cpp:84] Creating Layer scale5c_branch2b
I0623 09:45:03.860540  1897 net.cpp:406] scale5c_branch2b <- res5c_branch2b
I0623 09:45:03.860545  1897 net.cpp:367] scale5c_branch2b -> res5c_branch2b (in-place)
I0623 09:45:03.860558  1897 layer_factory.hpp:77] Creating layer scale5c_branch2b
I0623 09:45:03.860579  1897 net.cpp:122] Setting up scale5c_branch2b
I0623 09:45:03.860585  1897 net.cpp:129] Top shape: 8 512 8 8 (262144)
I0623 09:45:03.860589  1897 net.cpp:137] Memory required for data: 2400190560
I0623 09:45:03.860596  1897 layer_factory.hpp:77] Creating layer res5c_branch2b_relu
I0623 09:45:03.860605  1897 net.cpp:84] Creating Layer res5c_branch2b_relu
I0623 09:45:03.860608  1897 net.cpp:406] res5c_branch2b_relu <- res5c_branch2b
I0623 09:45:03.860615  1897 net.cpp:367] res5c_branch2b_relu -> res5c_branch2b (in-place)
I0623 09:45:03.860620  1897 net.cpp:122] Setting up res5c_branch2b_relu
I0623 09:45:03.860625  1897 net.cpp:129] Top shape: 8 512 8 8 (262144)
I0623 09:45:03.860628  1897 net.cpp:137] Memory required for data: 2401239136
I0623 09:45:03.860632  1897 layer_factory.hpp:77] Creating layer res5c_branch2c
I0623 09:45:03.860643  1897 net.cpp:84] Creating Layer res5c_branch2c
I0623 09:45:03.860649  1897 net.cpp:406] res5c_branch2c <- res5c_branch2b
I0623 09:45:03.860656  1897 net.cpp:380] res5c_branch2c -> res5c_branch2c
I0623 09:45:03.919432  1897 net.cpp:122] Setting up res5c_branch2c
I0623 09:45:03.919463  1897 net.cpp:129] Top shape: 8 2048 8 8 (1048576)
I0623 09:45:03.919468  1897 net.cpp:137] Memory required for data: 2405433440
I0623 09:45:03.919476  1897 layer_factory.hpp:77] Creating layer bn5c_branch2c
I0623 09:45:03.919489  1897 net.cpp:84] Creating Layer bn5c_branch2c
I0623 09:45:03.919497  1897 net.cpp:406] bn5c_branch2c <- res5c_branch2c
I0623 09:45:03.919519  1897 net.cpp:367] bn5c_branch2c -> res5c_branch2c (in-place)
I0623 09:45:03.919556  1897 net.cpp:122] Setting up bn5c_branch2c
I0623 09:45:03.919584  1897 net.cpp:129] Top shape: 8 2048 8 8 (1048576)
I0623 09:45:03.919589  1897 net.cpp:137] Memory required for data: 2409627744
I0623 09:45:03.919598  1897 layer_factory.hpp:77] Creating layer scale5c_branch2c
I0623 09:45:03.919617  1897 net.cpp:84] Creating Layer scale5c_branch2c
I0623 09:45:03.919625  1897 net.cpp:406] scale5c_branch2c <- res5c_branch2c
I0623 09:45:03.919631  1897 net.cpp:367] scale5c_branch2c -> res5c_branch2c (in-place)
I0623 09:45:03.919649  1897 layer_factory.hpp:77] Creating layer scale5c_branch2c
I0623 09:45:03.919677  1897 net.cpp:122] Setting up scale5c_branch2c
I0623 09:45:03.919687  1897 net.cpp:129] Top shape: 8 2048 8 8 (1048576)
I0623 09:45:03.919692  1897 net.cpp:137] Memory required for data: 2413822048
I0623 09:45:03.919699  1897 layer_factory.hpp:77] Creating layer res5c
I0623 09:45:03.919708  1897 net.cpp:84] Creating Layer res5c
I0623 09:45:03.919713  1897 net.cpp:406] res5c <- res5b_res5b_relu_0_split_1
I0623 09:45:03.919728  1897 net.cpp:406] res5c <- res5c_branch2c
I0623 09:45:03.919739  1897 net.cpp:380] res5c -> res5c
I0623 09:45:03.919749  1897 net.cpp:122] Setting up res5c
I0623 09:45:03.919757  1897 net.cpp:129] Top shape: 8 2048 8 8 (1048576)
I0623 09:45:03.919761  1897 net.cpp:137] Memory required for data: 2418016352
I0623 09:45:03.919765  1897 layer_factory.hpp:77] Creating layer res5c_relu
I0623 09:45:03.919773  1897 net.cpp:84] Creating Layer res5c_relu
I0623 09:45:03.919780  1897 net.cpp:406] res5c_relu <- res5c
I0623 09:45:03.919786  1897 net.cpp:367] res5c_relu -> res5c (in-place)
I0623 09:45:03.919795  1897 net.cpp:122] Setting up res5c_relu
I0623 09:45:03.919800  1897 net.cpp:129] Top shape: 8 2048 8 8 (1048576)
I0623 09:45:03.919806  1897 net.cpp:137] Memory required for data: 2422210656
I0623 09:45:03.919809  1897 layer_factory.hpp:77] Creating layer pool5
I0623 09:45:03.919816  1897 net.cpp:84] Creating Layer pool5
I0623 09:45:03.919821  1897 net.cpp:406] pool5 <- res5c
I0623 09:45:03.919827  1897 net.cpp:380] pool5 -> pool5
I0623 09:45:03.919837  1897 net.cpp:122] Setting up pool5
I0623 09:45:03.919844  1897 net.cpp:129] Top shape: 8 2048 1 1 (16384)
I0623 09:45:03.919849  1897 net.cpp:137] Memory required for data: 2422276192
I0623 09:45:03.919853  1897 layer_factory.hpp:77] Creating layer fc1000
I0623 09:45:03.919862  1897 net.cpp:84] Creating Layer fc1000
I0623 09:45:03.919868  1897 net.cpp:406] fc1000 <- pool5
I0623 09:45:03.919875  1897 net.cpp:380] fc1000 -> fc1000
I0623 09:45:03.988543  1897 net.cpp:122] Setting up fc1000
I0623 09:45:03.988616  1897 net.cpp:129] Top shape: 8 1000 (8000)
I0623 09:45:03.988628  1897 net.cpp:137] Memory required for data: 2422308192
I0623 09:45:03.988647  1897 layer_factory.hpp:77] Creating layer prob
I0623 09:45:03.988665  1897 net.cpp:84] Creating Layer prob
I0623 09:45:03.988677  1897 net.cpp:406] prob <- fc1000
I0623 09:45:03.988694  1897 net.cpp:380] prob -> prob
I0623 09:45:03.988715  1897 net.cpp:122] Setting up prob
I0623 09:45:03.988729  1897 net.cpp:129] Top shape: 8 1000 (8000)
I0623 09:45:03.988739  1897 net.cpp:137] Memory required for data: 2422340192
I0623 09:45:03.988749  1897 layer_factory.hpp:77] Creating layer prob_prob_0_split
I0623 09:45:03.988761  1897 net.cpp:84] Creating Layer prob_prob_0_split
I0623 09:45:03.988772  1897 net.cpp:406] prob_prob_0_split <- prob
I0623 09:45:03.988783  1897 net.cpp:380] prob_prob_0_split -> prob_prob_0_split_0
I0623 09:45:03.988797  1897 net.cpp:380] prob_prob_0_split -> prob_prob_0_split_1
I0623 09:45:03.988821  1897 net.cpp:122] Setting up prob_prob_0_split
I0623 09:45:03.988833  1897 net.cpp:129] Top shape: 8 1000 (8000)
I0623 09:45:03.988843  1897 net.cpp:129] Top shape: 8 1000 (8000)
I0623 09:45:03.988853  1897 net.cpp:137] Memory required for data: 2422404192
I0623 09:45:03.988862  1897 layer_factory.hpp:77] Creating layer accuracy/top1
I0623 09:45:03.988885  1897 net.cpp:84] Creating Layer accuracy/top1
I0623 09:45:03.988896  1897 net.cpp:406] accuracy/top1 <- prob_prob_0_split_0
I0623 09:45:03.988907  1897 net.cpp:406] accuracy/top1 <- label_data_1_split_0
I0623 09:45:03.988919  1897 net.cpp:380] accuracy/top1 -> accuracy@1
I0623 09:45:03.988934  1897 net.cpp:122] Setting up accuracy/top1
I0623 09:45:03.988945  1897 net.cpp:129] Top shape: (1)
I0623 09:45:03.988955  1897 net.cpp:137] Memory required for data: 2422404196
I0623 09:45:03.988965  1897 layer_factory.hpp:77] Creating layer accuracy/top5
I0623 09:45:03.988977  1897 net.cpp:84] Creating Layer accuracy/top5
I0623 09:45:03.988988  1897 net.cpp:406] accuracy/top5 <- prob_prob_0_split_1
I0623 09:45:03.988999  1897 net.cpp:406] accuracy/top5 <- label_data_1_split_1
I0623 09:45:03.989011  1897 net.cpp:380] accuracy/top5 -> accuracy@5
I0623 09:45:03.989023  1897 net.cpp:122] Setting up accuracy/top5
I0623 09:45:03.989035  1897 net.cpp:129] Top shape: (1)
I0623 09:45:03.989044  1897 net.cpp:137] Memory required for data: 2422404200
I0623 09:45:03.989054  1897 net.cpp:200] accuracy/top5 does not need backward computation.
I0623 09:45:03.989065  1897 net.cpp:200] accuracy/top1 does not need backward computation.
I0623 09:45:03.989075  1897 net.cpp:200] prob_prob_0_split does not need backward computation.
I0623 09:45:03.989085  1897 net.cpp:200] prob does not need backward computation.
I0623 09:45:03.989095  1897 net.cpp:200] fc1000 does not need backward computation.
I0623 09:45:03.989105  1897 net.cpp:200] pool5 does not need backward computation.
I0623 09:45:03.989116  1897 net.cpp:200] res5c_relu does not need backward computation.
I0623 09:45:03.989126  1897 net.cpp:200] res5c does not need backward computation.
I0623 09:45:03.989136  1897 net.cpp:200] scale5c_branch2c does not need backward computation.
I0623 09:45:03.989147  1897 net.cpp:200] bn5c_branch2c does not need backward computation.
I0623 09:45:03.989157  1897 net.cpp:200] res5c_branch2c does not need backward computation.
I0623 09:45:03.989167  1897 net.cpp:200] res5c_branch2b_relu does not need backward computation.
I0623 09:45:03.989177  1897 net.cpp:200] scale5c_branch2b does not need backward computation.
I0623 09:45:03.989187  1897 net.cpp:200] bn5c_branch2b does not need backward computation.
I0623 09:45:03.989197  1897 net.cpp:200] res5c_branch2b does not need backward computation.
I0623 09:45:03.989208  1897 net.cpp:200] res5c_branch2a_relu does not need backward computation.
I0623 09:45:03.989218  1897 net.cpp:200] scale5c_branch2a does not need backward computation.
I0623 09:45:03.989228  1897 net.cpp:200] bn5c_branch2a does not need backward computation.
I0623 09:45:03.989238  1897 net.cpp:200] res5c_branch2a does not need backward computation.
I0623 09:45:03.989248  1897 net.cpp:200] res5b_res5b_relu_0_split does not need backward computation.
I0623 09:45:03.989259  1897 net.cpp:200] res5b_relu does not need backward computation.
I0623 09:45:03.989269  1897 net.cpp:200] res5b does not need backward computation.
I0623 09:45:03.989280  1897 net.cpp:200] scale5b_branch2c does not need backward computation.
I0623 09:45:03.989290  1897 net.cpp:200] bn5b_branch2c does not need backward computation.
I0623 09:45:03.989300  1897 net.cpp:200] res5b_branch2c does not need backward computation.
I0623 09:45:03.989310  1897 net.cpp:200] res5b_branch2b_relu does not need backward computation.
I0623 09:45:03.989320  1897 net.cpp:200] scale5b_branch2b does not need backward computation.
I0623 09:45:03.989331  1897 net.cpp:200] bn5b_branch2b does not need backward computation.
I0623 09:45:03.989341  1897 net.cpp:200] res5b_branch2b does not need backward computation.
I0623 09:45:03.989351  1897 net.cpp:200] res5b_branch2a_relu does not need backward computation.
I0623 09:45:03.989365  1897 net.cpp:200] scale5b_branch2a does not need backward computation.
I0623 09:45:03.989377  1897 net.cpp:200] bn5b_branch2a does not need backward computation.
I0623 09:45:03.989385  1897 net.cpp:200] res5b_branch2a does not need backward computation.
I0623 09:45:03.989397  1897 net.cpp:200] res5a_res5a_relu_0_split does not need backward computation.
I0623 09:45:03.989406  1897 net.cpp:200] res5a_relu does not need backward computation.
I0623 09:45:03.989416  1897 net.cpp:200] res5a does not need backward computation.
I0623 09:45:03.989428  1897 net.cpp:200] scale5a_branch2c does not need backward computation.
I0623 09:45:03.989437  1897 net.cpp:200] bn5a_branch2c does not need backward computation.
I0623 09:45:03.989447  1897 net.cpp:200] res5a_branch2c does not need backward computation.
I0623 09:45:03.989457  1897 net.cpp:200] res5a_branch2b_relu does not need backward computation.
I0623 09:45:03.989467  1897 net.cpp:200] scale5a_branch2b does not need backward computation.
I0623 09:45:03.989477  1897 net.cpp:200] bn5a_branch2b does not need backward computation.
I0623 09:45:03.989487  1897 net.cpp:200] res5a_branch2b does not need backward computation.
I0623 09:45:03.989497  1897 net.cpp:200] res5a_branch2a_relu does not need backward computation.
I0623 09:45:03.989507  1897 net.cpp:200] scale5a_branch2a does not need backward computation.
I0623 09:45:03.989517  1897 net.cpp:200] bn5a_branch2a does not need backward computation.
I0623 09:45:03.989526  1897 net.cpp:200] res5a_branch2a does not need backward computation.
I0623 09:45:03.989537  1897 net.cpp:200] scale5a_branch1 does not need backward computation.
I0623 09:45:03.989547  1897 net.cpp:200] bn5a_branch1 does not need backward computation.
I0623 09:45:03.989557  1897 net.cpp:200] res5a_branch1 does not need backward computation.
I0623 09:45:03.989568  1897 net.cpp:200] res4f_res4f_relu_0_split does not need backward computation.
I0623 09:45:03.989578  1897 net.cpp:200] res4f_relu does not need backward computation.
I0623 09:45:03.989588  1897 net.cpp:200] res4f does not need backward computation.
I0623 09:45:03.989599  1897 net.cpp:200] scale4f_branch2c does not need backward computation.
I0623 09:45:03.989610  1897 net.cpp:200] bn4f_branch2c does not need backward computation.
I0623 09:45:03.989620  1897 net.cpp:200] res4f_branch2c does not need backward computation.
I0623 09:45:03.989629  1897 net.cpp:200] res4f_branch2b_relu does not need backward computation.
I0623 09:45:03.989639  1897 net.cpp:200] scale4f_branch2b does not need backward computation.
I0623 09:45:03.989650  1897 net.cpp:200] bn4f_branch2b does not need backward computation.
I0623 09:45:03.989660  1897 net.cpp:200] res4f_branch2b does not need backward computation.
I0623 09:45:03.989670  1897 net.cpp:200] res4f_branch2a_relu does not need backward computation.
I0623 09:45:03.989681  1897 net.cpp:200] scale4f_branch2a does not need backward computation.
I0623 09:45:03.989689  1897 net.cpp:200] bn4f_branch2a does not need backward computation.
I0623 09:45:03.989699  1897 net.cpp:200] res4f_branch2a does not need backward computation.
I0623 09:45:03.989709  1897 net.cpp:200] res4e_res4e_relu_0_split does not need backward computation.
I0623 09:45:03.989720  1897 net.cpp:200] res4e_relu does not need backward computation.
I0623 09:45:03.989729  1897 net.cpp:200] res4e does not need backward computation.
I0623 09:45:03.989740  1897 net.cpp:200] scale4e_branch2c does not need backward computation.
I0623 09:45:03.989750  1897 net.cpp:200] bn4e_branch2c does not need backward computation.
I0623 09:45:03.989760  1897 net.cpp:200] res4e_branch2c does not need backward computation.
I0623 09:45:03.989771  1897 net.cpp:200] res4e_branch2b_relu does not need backward computation.
I0623 09:45:03.989781  1897 net.cpp:200] scale4e_branch2b does not need backward computation.
I0623 09:45:03.989791  1897 net.cpp:200] bn4e_branch2b does not need backward computation.
I0623 09:45:03.989801  1897 net.cpp:200] res4e_branch2b does not need backward computation.
I0623 09:45:03.989816  1897 net.cpp:200] res4e_branch2a_relu does not need backward computation.
I0623 09:45:03.989827  1897 net.cpp:200] scale4e_branch2a does not need backward computation.
I0623 09:45:03.989836  1897 net.cpp:200] bn4e_branch2a does not need backward computation.
I0623 09:45:03.989846  1897 net.cpp:200] res4e_branch2a does not need backward computation.
I0623 09:45:03.989857  1897 net.cpp:200] res4d_res4d_relu_0_split does not need backward computation.
I0623 09:45:03.989867  1897 net.cpp:200] res4d_relu does not need backward computation.
I0623 09:45:03.989877  1897 net.cpp:200] res4d does not need backward computation.
I0623 09:45:03.989888  1897 net.cpp:200] scale4d_branch2c does not need backward computation.
I0623 09:45:03.989898  1897 net.cpp:200] bn4d_branch2c does not need backward computation.
I0623 09:45:03.989907  1897 net.cpp:200] res4d_branch2c does not need backward computation.
I0623 09:45:03.989918  1897 net.cpp:200] res4d_branch2b_relu does not need backward computation.
I0623 09:45:03.989928  1897 net.cpp:200] scale4d_branch2b does not need backward computation.
I0623 09:45:03.989938  1897 net.cpp:200] bn4d_branch2b does not need backward computation.
I0623 09:45:03.989948  1897 net.cpp:200] res4d_branch2b does not need backward computation.
I0623 09:45:03.989959  1897 net.cpp:200] res4d_branch2a_relu does not need backward computation.
I0623 09:45:03.989969  1897 net.cpp:200] scale4d_branch2a does not need backward computation.
I0623 09:45:03.989979  1897 net.cpp:200] bn4d_branch2a does not need backward computation.
I0623 09:45:03.989989  1897 net.cpp:200] res4d_branch2a does not need backward computation.
I0623 09:45:03.990000  1897 net.cpp:200] res4c_res4c_relu_0_split does not need backward computation.
I0623 09:45:03.990010  1897 net.cpp:200] res4c_relu does not need backward computation.
I0623 09:45:03.990020  1897 net.cpp:200] res4c does not need backward computation.
I0623 09:45:03.990031  1897 net.cpp:200] scale4c_branch2c does not need backward computation.
I0623 09:45:03.990041  1897 net.cpp:200] bn4c_branch2c does not need backward computation.
I0623 09:45:03.990051  1897 net.cpp:200] res4c_branch2c does not need backward computation.
I0623 09:45:03.990061  1897 net.cpp:200] res4c_branch2b_relu does not need backward computation.
I0623 09:45:03.990070  1897 net.cpp:200] scale4c_branch2b does not need backward computation.
I0623 09:45:03.990080  1897 net.cpp:200] bn4c_branch2b does not need backward computation.
I0623 09:45:03.990090  1897 net.cpp:200] res4c_branch2b does not need backward computation.
I0623 09:45:03.990100  1897 net.cpp:200] res4c_branch2a_relu does not need backward computation.
I0623 09:45:03.990110  1897 net.cpp:200] scale4c_branch2a does not need backward computation.
I0623 09:45:03.990120  1897 net.cpp:200] bn4c_branch2a does not need backward computation.
I0623 09:45:03.990130  1897 net.cpp:200] res4c_branch2a does not need backward computation.
I0623 09:45:03.990141  1897 net.cpp:200] res4b_res4b_relu_0_split does not need backward computation.
I0623 09:45:03.990151  1897 net.cpp:200] res4b_relu does not need backward computation.
I0623 09:45:03.990161  1897 net.cpp:200] res4b does not need backward computation.
I0623 09:45:03.990172  1897 net.cpp:200] scale4b_branch2c does not need backward computation.
I0623 09:45:03.990182  1897 net.cpp:200] bn4b_branch2c does not need backward computation.
I0623 09:45:03.990192  1897 net.cpp:200] res4b_branch2c does not need backward computation.
I0623 09:45:03.990203  1897 net.cpp:200] res4b_branch2b_relu does not need backward computation.
I0623 09:45:03.990213  1897 net.cpp:200] scale4b_branch2b does not need backward computation.
I0623 09:45:03.990222  1897 net.cpp:200] bn4b_branch2b does not need backward computation.
I0623 09:45:03.990232  1897 net.cpp:200] res4b_branch2b does not need backward computation.
I0623 09:45:03.990243  1897 net.cpp:200] res4b_branch2a_relu does not need backward computation.
I0623 09:45:03.990253  1897 net.cpp:200] scale4b_branch2a does not need backward computation.
I0623 09:45:03.990267  1897 net.cpp:200] bn4b_branch2a does not need backward computation.
I0623 09:45:03.990276  1897 net.cpp:200] res4b_branch2a does not need backward computation.
I0623 09:45:03.990286  1897 net.cpp:200] res4a_res4a_relu_0_split does not need backward computation.
I0623 09:45:03.990298  1897 net.cpp:200] res4a_relu does not need backward computation.
I0623 09:45:03.990306  1897 net.cpp:200] res4a does not need backward computation.
I0623 09:45:03.990317  1897 net.cpp:200] scale4a_branch2c does not need backward computation.
I0623 09:45:03.990327  1897 net.cpp:200] bn4a_branch2c does not need backward computation.
I0623 09:45:03.990336  1897 net.cpp:200] res4a_branch2c does not need backward computation.
I0623 09:45:03.990341  1897 net.cpp:200] res4a_branch2b_relu does not need backward computation.
I0623 09:45:03.990345  1897 net.cpp:200] scale4a_branch2b does not need backward computation.
I0623 09:45:03.990348  1897 net.cpp:200] bn4a_branch2b does not need backward computation.
I0623 09:45:03.990352  1897 net.cpp:200] res4a_branch2b does not need backward computation.
I0623 09:45:03.990356  1897 net.cpp:200] res4a_branch2a_relu does not need backward computation.
I0623 09:45:03.990360  1897 net.cpp:200] scale4a_branch2a does not need backward computation.
I0623 09:45:03.990365  1897 net.cpp:200] bn4a_branch2a does not need backward computation.
I0623 09:45:03.990368  1897 net.cpp:200] res4a_branch2a does not need backward computation.
I0623 09:45:03.990373  1897 net.cpp:200] scale4a_branch1 does not need backward computation.
I0623 09:45:03.990376  1897 net.cpp:200] bn4a_branch1 does not need backward computation.
I0623 09:45:03.990381  1897 net.cpp:200] res4a_branch1 does not need backward computation.
I0623 09:45:03.990384  1897 net.cpp:200] res3d_res3d_relu_0_split does not need backward computation.
I0623 09:45:03.990388  1897 net.cpp:200] res3d_relu does not need backward computation.
I0623 09:45:03.990392  1897 net.cpp:200] res3d does not need backward computation.
I0623 09:45:03.990397  1897 net.cpp:200] scale3d_branch2c does not need backward computation.
I0623 09:45:03.990401  1897 net.cpp:200] bn3d_branch2c does not need backward computation.
I0623 09:45:03.990406  1897 net.cpp:200] res3d_branch2c does not need backward computation.
I0623 09:45:03.990409  1897 net.cpp:200] res3d_branch2b_relu does not need backward computation.
I0623 09:45:03.990412  1897 net.cpp:200] scale3d_branch2b does not need backward computation.
I0623 09:45:03.990417  1897 net.cpp:200] bn3d_branch2b does not need backward computation.
I0623 09:45:03.990420  1897 net.cpp:200] res3d_branch2b does not need backward computation.
I0623 09:45:03.990424  1897 net.cpp:200] res3d_branch2a_relu does not need backward computation.
I0623 09:45:03.990428  1897 net.cpp:200] scale3d_branch2a does not need backward computation.
I0623 09:45:03.990432  1897 net.cpp:200] bn3d_branch2a does not need backward computation.
I0623 09:45:03.990435  1897 net.cpp:200] res3d_branch2a does not need backward computation.
I0623 09:45:03.990439  1897 net.cpp:200] res3c_res3c_relu_0_split does not need backward computation.
I0623 09:45:03.990444  1897 net.cpp:200] res3c_relu does not need backward computation.
I0623 09:45:03.990447  1897 net.cpp:200] res3c does not need backward computation.
I0623 09:45:03.990453  1897 net.cpp:200] scale3c_branch2c does not need backward computation.
I0623 09:45:03.990455  1897 net.cpp:200] bn3c_branch2c does not need backward computation.
I0623 09:45:03.990459  1897 net.cpp:200] res3c_branch2c does not need backward computation.
I0623 09:45:03.990463  1897 net.cpp:200] res3c_branch2b_relu does not need backward computation.
I0623 09:45:03.990468  1897 net.cpp:200] scale3c_branch2b does not need backward computation.
I0623 09:45:03.990471  1897 net.cpp:200] bn3c_branch2b does not need backward computation.
I0623 09:45:03.990474  1897 net.cpp:200] res3c_branch2b does not need backward computation.
I0623 09:45:03.990478  1897 net.cpp:200] res3c_branch2a_relu does not need backward computation.
I0623 09:45:03.990483  1897 net.cpp:200] scale3c_branch2a does not need backward computation.
I0623 09:45:03.990485  1897 net.cpp:200] bn3c_branch2a does not need backward computation.
I0623 09:45:03.990489  1897 net.cpp:200] res3c_branch2a does not need backward computation.
I0623 09:45:03.990494  1897 net.cpp:200] res3b_res3b_relu_0_split does not need backward computation.
I0623 09:45:03.990497  1897 net.cpp:200] res3b_relu does not need backward computation.
I0623 09:45:03.990501  1897 net.cpp:200] res3b does not need backward computation.
I0623 09:45:03.990505  1897 net.cpp:200] scale3b_branch2c does not need backward computation.
I0623 09:45:03.990509  1897 net.cpp:200] bn3b_branch2c does not need backward computation.
I0623 09:45:03.990514  1897 net.cpp:200] res3b_branch2c does not need backward computation.
I0623 09:45:03.990517  1897 net.cpp:200] res3b_branch2b_relu does not need backward computation.
I0623 09:45:03.990521  1897 net.cpp:200] scale3b_branch2b does not need backward computation.
I0623 09:45:03.990525  1897 net.cpp:200] bn3b_branch2b does not need backward computation.
I0623 09:45:03.990530  1897 net.cpp:200] res3b_branch2b does not need backward computation.
I0623 09:45:03.990533  1897 net.cpp:200] res3b_branch2a_relu does not need backward computation.
I0623 09:45:03.990537  1897 net.cpp:200] scale3b_branch2a does not need backward computation.
I0623 09:45:03.990540  1897 net.cpp:200] bn3b_branch2a does not need backward computation.
I0623 09:45:03.990545  1897 net.cpp:200] res3b_branch2a does not need backward computation.
I0623 09:45:03.990548  1897 net.cpp:200] res3a_res3a_relu_0_split does not need backward computation.
I0623 09:45:03.990552  1897 net.cpp:200] res3a_relu does not need backward computation.
I0623 09:45:03.990556  1897 net.cpp:200] res3a does not need backward computation.
I0623 09:45:03.990561  1897 net.cpp:200] scale3a_branch2c does not need backward computation.
I0623 09:45:03.990566  1897 net.cpp:200] bn3a_branch2c does not need backward computation.
I0623 09:45:03.990568  1897 net.cpp:200] res3a_branch2c does not need backward computation.
I0623 09:45:03.990572  1897 net.cpp:200] res3a_branch2b_relu does not need backward computation.
I0623 09:45:03.990576  1897 net.cpp:200] scale3a_branch2b does not need backward computation.
I0623 09:45:03.990579  1897 net.cpp:200] bn3a_branch2b does not need backward computation.
I0623 09:45:03.990583  1897 net.cpp:200] res3a_branch2b does not need backward computation.
I0623 09:45:03.990587  1897 net.cpp:200] res3a_branch2a_relu does not need backward computation.
I0623 09:45:03.990592  1897 net.cpp:200] scale3a_branch2a does not need backward computation.
I0623 09:45:03.990595  1897 net.cpp:200] bn3a_branch2a does not need backward computation.
I0623 09:45:03.990599  1897 net.cpp:200] res3a_branch2a does not need backward computation.
I0623 09:45:03.990603  1897 net.cpp:200] scale3a_branch1 does not need backward computation.
I0623 09:45:03.990607  1897 net.cpp:200] bn3a_branch1 does not need backward computation.
I0623 09:45:03.990610  1897 net.cpp:200] res3a_branch1 does not need backward computation.
I0623 09:45:03.990615  1897 net.cpp:200] res2c_res2c_relu_0_split does not need backward computation.
I0623 09:45:03.990619  1897 net.cpp:200] res2c_relu does not need backward computation.
I0623 09:45:03.990623  1897 net.cpp:200] res2c does not need backward computation.
I0623 09:45:03.990628  1897 net.cpp:200] scale2c_branch2c does not need backward computation.
I0623 09:45:03.990631  1897 net.cpp:200] bn2c_branch2c does not need backward computation.
I0623 09:45:03.990635  1897 net.cpp:200] res2c_branch2c does not need backward computation.
I0623 09:45:03.990639  1897 net.cpp:200] res2c_branch2b_relu does not need backward computation.
I0623 09:45:03.990643  1897 net.cpp:200] scale2c_branch2b does not need backward computation.
I0623 09:45:03.990646  1897 net.cpp:200] bn2c_branch2b does not need backward computation.
I0623 09:45:03.990650  1897 net.cpp:200] res2c_branch2b does not need backward computation.
I0623 09:45:03.990654  1897 net.cpp:200] res2c_branch2a_relu does not need backward computation.
I0623 09:45:03.990658  1897 net.cpp:200] scale2c_branch2a does not need backward computation.
I0623 09:45:03.990661  1897 net.cpp:200] bn2c_branch2a does not need backward computation.
I0623 09:45:03.990665  1897 net.cpp:200] res2c_branch2a does not need backward computation.
I0623 09:45:03.990674  1897 net.cpp:200] res2b_res2b_relu_0_split does not need backward computation.
I0623 09:45:03.990679  1897 net.cpp:200] res2b_relu does not need backward computation.
I0623 09:45:03.990684  1897 net.cpp:200] res2b does not need backward computation.
I0623 09:45:03.990687  1897 net.cpp:200] scale2b_branch2c does not need backward computation.
I0623 09:45:03.990691  1897 net.cpp:200] bn2b_branch2c does not need backward computation.
I0623 09:45:03.990695  1897 net.cpp:200] res2b_branch2c does not need backward computation.
I0623 09:45:03.990700  1897 net.cpp:200] res2b_branch2b_relu does not need backward computation.
I0623 09:45:03.990703  1897 net.cpp:200] scale2b_branch2b does not need backward computation.
I0623 09:45:03.990707  1897 net.cpp:200] bn2b_branch2b does not need backward computation.
I0623 09:45:03.990711  1897 net.cpp:200] res2b_branch2b does not need backward computation.
I0623 09:45:03.990715  1897 net.cpp:200] res2b_branch2a_relu does not need backward computation.
I0623 09:45:03.990720  1897 net.cpp:200] scale2b_branch2a does not need backward computation.
I0623 09:45:03.990723  1897 net.cpp:200] bn2b_branch2a does not need backward computation.
I0623 09:45:03.990726  1897 net.cpp:200] res2b_branch2a does not need backward computation.
I0623 09:45:03.990731  1897 net.cpp:200] res2a_res2a_relu_0_split does not need backward computation.
I0623 09:45:03.990736  1897 net.cpp:200] res2a_relu does not need backward computation.
I0623 09:45:03.990738  1897 net.cpp:200] res2a does not need backward computation.
I0623 09:45:03.990743  1897 net.cpp:200] scale2a_branch2c does not need backward computation.
I0623 09:45:03.990747  1897 net.cpp:200] bn2a_branch2c does not need backward computation.
I0623 09:45:03.990751  1897 net.cpp:200] res2a_branch2c does not need backward computation.
I0623 09:45:03.990756  1897 net.cpp:200] res2a_branch2b_relu does not need backward computation.
I0623 09:45:03.990758  1897 net.cpp:200] scale2a_branch2b does not need backward computation.
I0623 09:45:03.990762  1897 net.cpp:200] bn2a_branch2b does not need backward computation.
I0623 09:45:03.990767  1897 net.cpp:200] res2a_branch2b does not need backward computation.
I0623 09:45:03.990770  1897 net.cpp:200] res2a_branch2a_relu does not need backward computation.
I0623 09:45:03.990773  1897 net.cpp:200] scale2a_branch2a does not need backward computation.
I0623 09:45:03.990777  1897 net.cpp:200] bn2a_branch2a does not need backward computation.
I0623 09:45:03.990782  1897 net.cpp:200] res2a_branch2a does not need backward computation.
I0623 09:45:03.990785  1897 net.cpp:200] scale2a_branch1 does not need backward computation.
I0623 09:45:03.990789  1897 net.cpp:200] bn2a_branch1 does not need backward computation.
I0623 09:45:03.990793  1897 net.cpp:200] res2a_branch1 does not need backward computation.
I0623 09:45:03.990798  1897 net.cpp:200] pool1_pool1_0_split does not need backward computation.
I0623 09:45:03.990803  1897 net.cpp:200] pool1 does not need backward computation.
I0623 09:45:03.990806  1897 net.cpp:200] conv1_relu does not need backward computation.
I0623 09:45:03.990809  1897 net.cpp:200] scale_conv1 does not need backward computation.
I0623 09:45:03.990813  1897 net.cpp:200] bn_conv1 does not need backward computation.
I0623 09:45:03.990818  1897 net.cpp:200] conv1 does not need backward computation.
I0623 09:45:03.990821  1897 net.cpp:200] label_data_1_split does not need backward computation.
I0623 09:45:03.990825  1897 net.cpp:200] data does not need backward computation.
I0623 09:45:03.990828  1897 net.cpp:242] This network produces output accuracy@1
I0623 09:45:03.990833  1897 net.cpp:242] This network produces output accuracy@5
I0623 09:45:03.990945  1897 net.cpp:255] Network initialization done.
I0623 09:45:04.964076  1897 upgrade_proto.cpp:67] Attempting to upgrade input file specified using deprecated input fields: /home/eikan/dezhi/caffe/models/ResNet-50/ResNet-50-model.caffemodel
I0623 09:45:04.964107  1897 upgrade_proto.cpp:70] Successfully upgraded file specified using deprecated input fields.
W0623 09:45:04.964112  1897 upgrade_proto.cpp:72] Note that future Caffe releases will only support input layers and not input fields.
output: /home/eikan/dezhi/caffe/models/ResNet-50/resnet50zip.npz
new_weights: /home/eikan/dezhi/caffe/models/ResNet-50/resnet50_xx.caffemodel
compressing layer conv1
vec_length 9408
[quantize] count:9408
[quantize] float src:	
max:0.704324	min:0.000001	diff:0
scale:7.000000	pow2_scale:128.000000
python scale [140144782868487]
compressing layer bn_conv1
vec_length 64
[quantize] count:64
[quantize] float src:	
max:3.537402	min:0.005598	diff:0
scale:5.000000	pow2_scale:32.000000
python scale [140144782868485]
compressing layer scale_conv1
vec_length 64
[quantize] count:64
[quantize] float src:	
max:2.668587	min:0.512643	diff:0
scale:5.000000	pow2_scale:32.000000
python scale [5]
compressing layer res2a_branch1
vec_length 16384
[quantize] count:16384
[quantize] float src:	
max:0.900367	min:0.000000	diff:0
scale:7.000000	pow2_scale:128.000000
python scale [140144782868487]
compressing layer bn2a_branch1
vec_length 256
[quantize] count:256
[quantize] float src:	
max:9.714517	min:0.002699	diff:0
scale:3.000000	pow2_scale:8.000000
python scale [140144782868483]
compressing layer scale2a_branch1
vec_length 256
[quantize] count:256
[quantize] float src:	
max:3.064375	min:0.004353	diff:0
scale:5.000000	pow2_scale:32.000000
python scale [140144782868485]
compressing layer res2a_branch2a
vec_length 4096
[quantize] count:4096
[quantize] float src:	
max:0.717496	min:0.000001	diff:0
scale:7.000000	pow2_scale:128.000000
python scale [140144782868487]
compressing layer bn2a_branch2a
vec_length 64
[quantize] count:64
[quantize] float src:	
max:7.615551	min:0.276527	diff:0
scale:4.000000	pow2_scale:16.000000
python scale [140144782868484]
compressing layer scale2a_branch2a
vec_length 64
[quantize] count:64
[quantize] float src:	
max:2.066087	min:0.509218	diff:0
scale:5.000000	pow2_scale:32.000000
python scale [5]
compressing layer res2a_branch2b
vec_length 36864
[quantize] count:36864
[quantize] float src:	
max:0.390040	min:0.000000	diff:0
scale:8.000000	pow2_scale:256.000000
python scale [140144782868488]
compressing layer bn2a_branch2b
vec_length 64
[quantize] count:64
[quantize] float src:	
max:4.011371	min:0.008868	diff:0
scale:4.000000	pow2_scale:16.000000
python scale [140144782868484]
compressing layer scale2a_branch2b
vec_length 64
[quantize] count:64
[quantize] float src:	
max:2.529534	min:0.420426	diff:0
scale:5.000000	pow2_scale:32.000000
python scale [5]
compressing layer res2a_branch2c
vec_length 16384
[quantize] count:16384
[quantize] float src:	
max:0.397442	min:0.000000	diff:0
scale:8.000000	pow2_scale:256.000000
python scale [140144782868488]
compressing layer bn2a_branch2c
vec_length 256
[quantize] count:256
[quantize] float src:	
max:2.008285	min:0.000910	diff:0
scale:5.000000	pow2_scale:32.000000
python scale [140144782868485]
compressing layer scale2a_branch2c
vec_length 256
[quantize] count:256
[quantize] float src:	
max:2.819955	min:0.011003	diff:0
scale:5.000000	pow2_scale:32.000000
python scale [140144782868485]
compressing layer res2b_branch2a
vec_length 16384
[quantize] count:16384
[quantize] float src:	
max:0.296858	min:0.000000	diff:0
scale:8.000000	pow2_scale:256.000000
python scale [140144782868488]
compressing layer bn2b_branch2a
vec_length 64
[quantize] count:64
[quantize] float src:	
max:2.512779	min:0.010715	diff:0
scale:5.000000	pow2_scale:32.000000
python scale [140144782868485]
compressing layer scale2b_branch2a
vec_length 64
[quantize] count:64
[quantize] float src:	
max:1.949030	min:0.746197	diff:0
scale:6.000000	pow2_scale:64.000000
python scale [6]
compressing layer res2b_branch2b
vec_length 36864
[quantize] count:36864
[quantize] float src:	
max:0.318288	min:0.000001	diff:0
scale:8.000000	pow2_scale:256.000000
python scale [140144782868488]
compressing layer bn2b_branch2b
vec_length 64
[quantize] count:64
[quantize] float src:	
max:1.338304	min:0.029214	diff:0
scale:6.000000	pow2_scale:64.000000
python scale [140144782868486]
compressing layer scale2b_branch2b
vec_length 64
[quantize] count:64
[quantize] float src:	
max:1.617719	min:0.620510	diff:0
scale:6.000000	pow2_scale:64.000000
python scale [6]
compressing layer res2b_branch2c
vec_length 16384
[quantize] count:16384
[quantize] float src:	
max:0.279571	min:0.000000	diff:0
scale:8.000000	pow2_scale:256.000000
python scale [140144782868488]
compressing layer bn2b_branch2c
vec_length 256
[quantize] count:256
[quantize] float src:	
max:1.090107	min:0.000525	diff:0
scale:6.000000	pow2_scale:64.000000
python scale [140144782868486]
compressing layer scale2b_branch2c
vec_length 256
[quantize] count:256
[quantize] float src:	
max:2.130081	min:0.000230	diff:0
scale:5.000000	pow2_scale:32.000000
python scale [140144782868485]
compressing layer res2c_branch2a
vec_length 16384
[quantize] count:16384
[quantize] float src:	
max:0.263710	min:0.000000	diff:0
scale:8.000000	pow2_scale:256.000000
python scale [140144782868488]
compressing layer bn2c_branch2a
vec_length 64
[quantize] count:64
[quantize] float src:	
max:1.988319	min:0.003882	diff:0
scale:6.000000	pow2_scale:64.000000
python scale [140144782868486]
compressing layer scale2c_branch2a
vec_length 64
[quantize] count:64
[quantize] float src:	
max:1.688044	min:0.574069	diff:0
scale:6.000000	pow2_scale:64.000000
python scale [6]
compressing layer res2c_branch2b
vec_length 36864
[quantize] count:36864
[quantize] float src:	
max:0.217954	min:0.000000	diff:0
scale:9.000000	pow2_scale:512.000000
python scale [140144782868489]
compressing layer bn2c_branch2b
vec_length 64
[quantize] count:64
[quantize] float src:	
max:1.346063	min:0.002165	diff:0
scale:6.000000	pow2_scale:64.000000
python scale [140144782868486]
compressing layer scale2c_branch2b
vec_length 64
[quantize] count:64
[quantize] float src:	
max:1.649279	min:0.757045	diff:0
scale:6.000000	pow2_scale:64.000000
python scale [6]
compressing layer res2c_branch2c
vec_length 16384
[quantize] count:16384
[quantize] float src:	
max:0.349984	min:0.000002	diff:0
scale:8.000000	pow2_scale:256.000000
python scale [140144782868488]
compressing layer bn2c_branch2c
vec_length 256
[quantize] count:256
[quantize] float src:	
max:1.083904	min:0.000554	diff:0
scale:6.000000	pow2_scale:64.000000
python scale [140144782868486]
compressing layer scale2c_branch2c
vec_length 256
[quantize] count:256
[quantize] float src:	
max:2.153982	min:0.000221	diff:0
scale:5.000000	pow2_scale:32.000000
python scale [140144782868485]
compressing layer res3a_branch1
vec_length 131072
[quantize] count:131072
[quantize] float src:	
max:0.642471	min:0.000000	diff:0
scale:7.000000	pow2_scale:128.000000
python scale [140144782868487]
compressing layer bn3a_branch1
vec_length 512
[quantize] count:512
[quantize] float src:	
max:2.735132	min:0.001346	diff:0
scale:5.000000	pow2_scale:32.000000
python scale [140144782868485]
compressing layer scale3a_branch1
vec_length 512
[quantize] count:512
[quantize] float src:	
max:2.551902	min:0.005531	diff:0
scale:5.000000	pow2_scale:32.000000
python scale [140144782868485]
compressing layer res3a_branch2a
vec_length 32768
[quantize] count:32768
[quantize] float src:	
max:0.333935	min:0.000001	diff:0
scale:8.000000	pow2_scale:256.000000
python scale [140144782868488]
compressing layer bn3a_branch2a
vec_length 128
[quantize] count:128
[quantize] float src:	
max:2.941627	min:0.018914	diff:0
scale:5.000000	pow2_scale:32.000000
python scale [140144782868485]
compressing layer scale3a_branch2a
vec_length 128
[quantize] count:128
[quantize] float src:	
max:1.642389	min:0.610337	diff:0
scale:6.000000	pow2_scale:64.000000
python scale [6]
compressing layer res3a_branch2b
vec_length 147456
[quantize] count:147456
[quantize] float src:	
max:0.383694	min:0.000000	diff:0
scale:8.000000	pow2_scale:256.000000
python scale [140144782868488]
compressing layer bn3a_branch2b
vec_length 128
[quantize] count:128
[quantize] float src:	
max:4.093867	min:0.002008	diff:0
scale:4.000000	pow2_scale:16.000000
python scale [140144782868484]
compressing layer scale3a_branch2b
vec_length 128
[quantize] count:128
[quantize] float src:	
max:1.621626	min:0.604892	diff:0
scale:6.000000	pow2_scale:64.000000
python scale [6]
compressing layer res3a_branch2c
vec_length 65536
[quantize] count:65536
[quantize] float src:	
max:0.434352	min:0.000000	diff:0
scale:8.000000	pow2_scale:256.000000
python scale [140144782868488]
compressing layer bn3a_branch2c
vec_length 512
[quantize] count:512
[quantize] float src:	
max:1.075805	min:0.000137	diff:0
scale:6.000000	pow2_scale:64.000000
python scale [140144782868486]
compressing layer scale3a_branch2c
vec_length 512
[quantize] count:512
[quantize] float src:	
max:2.729879	min:0.000944	diff:0
scale:5.000000	pow2_scale:32.000000
python scale [140144782868485]
compressing layer res3b_branch2a
vec_length 65536
[quantize] count:65536
[quantize] float src:	
max:0.194702	min:0.000000	diff:0
scale:9.000000	pow2_scale:512.000000
python scale [140144782868489]
compressing layer bn3b_branch2a
vec_length 128
[quantize] count:128
[quantize] float src:	
max:2.095689	min:0.003190	diff:0
scale:5.000000	pow2_scale:32.000000
python scale [140144782868485]
compressing layer scale3b_branch2a
vec_length 128
[quantize] count:128
[quantize] float src:	
max:1.428775	min:0.578484	diff:0
scale:6.000000	pow2_scale:64.000000
python scale [6]
compressing layer res3b_branch2b
vec_length 147456
[quantize] count:147456
[quantize] float src:	
max:0.177218	min:0.000000	diff:0
scale:9.000000	pow2_scale:512.000000
python scale [140144782868489]
compressing layer bn3b_branch2b
vec_length 128
[quantize] count:128
[quantize] float src:	
max:1.425480	min:0.006235	diff:0
scale:6.000000	pow2_scale:64.000000
python scale [140144782868486]
compressing layer scale3b_branch2b
vec_length 128
[quantize] count:128
[quantize] float src:	
max:1.794162	min:0.510786	diff:0
scale:6.000000	pow2_scale:64.000000
python scale [6]
compressing layer res3b_branch2c
vec_length 65536
[quantize] count:65536
[quantize] float src:	
max:0.344258	min:0.000000	diff:0
scale:8.000000	pow2_scale:256.000000
python scale [140144782868488]
compressing layer bn3b_branch2c
vec_length 512
[quantize] count:512
[quantize] float src:	
max:0.625331	min:0.001038	diff:0
scale:7.000000	pow2_scale:128.000000
python scale [140144782868487]
compressing layer scale3b_branch2c
vec_length 512
[quantize] count:512
[quantize] float src:	
max:2.121532	min:0.000069	diff:0
scale:5.000000	pow2_scale:32.000000
python scale [140144782868485]
compressing layer res3c_branch2a
vec_length 65536
[quantize] count:65536
[quantize] float src:	
max:0.368505	min:0.000001	diff:0
scale:8.000000	pow2_scale:256.000000
python scale [140144782868488]
compressing layer bn3c_branch2a
vec_length 128
[quantize] count:128
[quantize] float src:	
max:1.866740	min:0.007868	diff:0
scale:6.000000	pow2_scale:64.000000
python scale [140144782868486]
compressing layer scale3c_branch2a
vec_length 128
[quantize] count:128
[quantize] float src:	
max:1.695590	min:0.406000	diff:0
scale:6.000000	pow2_scale:64.000000
python scale [6]
compressing layer res3c_branch2b
vec_length 147456
[quantize] count:147456
[quantize] float src:	
max:0.373646	min:0.000000	diff:0
scale:8.000000	pow2_scale:256.000000
python scale [140144782868488]
compressing layer bn3c_branch2b
vec_length 128
[quantize] count:128
[quantize] float src:	
max:1.739012	min:0.002158	diff:0
scale:6.000000	pow2_scale:64.000000
python scale [140144782868486]
compressing layer scale3c_branch2b
vec_length 128
[quantize] count:128
[quantize] float src:	
max:2.178780	min:0.460057	diff:0
scale:5.000000	pow2_scale:32.000000
python scale [5]
compressing layer res3c_branch2c
vec_length 65536
[quantize] count:65536
[quantize] float src:	
max:0.287551	min:0.000000	diff:0
scale:8.000000	pow2_scale:256.000000
python scale [140144782868488]
compressing layer bn3c_branch2c
vec_length 512
[quantize] count:512
[quantize] float src:	
max:0.523285	min:0.000125	diff:0
scale:7.000000	pow2_scale:128.000000
python scale [140144782868487]
compressing layer scale3c_branch2c
vec_length 512
[quantize] count:512
[quantize] float src:	
max:3.042613	min:0.000119	diff:0
scale:5.000000	pow2_scale:32.000000
python scale [140144782868485]
compressing layer res3d_branch2a
vec_length 65536
[quantize] count:65536
[quantize] float src:	
max:0.346265	min:0.000000	diff:0
scale:8.000000	pow2_scale:256.000000
python scale [140144782868488]
compressing layer bn3d_branch2a
vec_length 128
[quantize] count:128
[quantize] float src:	
max:1.513273	min:0.018681	diff:0
scale:6.000000	pow2_scale:64.000000
python scale [140144782868486]
compressing layer scale3d_branch2a
vec_length 128
[quantize] count:128
[quantize] float src:	
max:2.394452	min:0.735502	diff:0
scale:5.000000	pow2_scale:32.000000
python scale [5]
compressing layer res3d_branch2b
vec_length 147456
[quantize] count:147456
[quantize] float src:	
max:0.272210	min:0.000000	diff:0
scale:8.000000	pow2_scale:256.000000
python scale [140144782868488]
compressing layer bn3d_branch2b
vec_length 128
[quantize] count:128
[quantize] float src:	
max:1.623106	min:0.004108	diff:0
scale:6.000000	pow2_scale:64.000000
python scale [140144782868486]
compressing layer scale3d_branch2b
vec_length 128
[quantize] count:128
[quantize] float src:	
max:1.694472	min:0.681690	diff:0
scale:6.000000	pow2_scale:64.000000
python scale [6]
compressing layer res3d_branch2c
vec_length 65536
[quantize] count:65536
[quantize] float src:	
max:0.280830	min:0.000000	diff:0
scale:8.000000	pow2_scale:256.000000
python scale [140144782868488]
compressing layer bn3d_branch2c
vec_length 512
[quantize] count:512
[quantize] float src:	
max:1.031248	min:0.001369	diff:0
scale:6.000000	pow2_scale:64.000000
python scale [140144782868486]
compressing layer scale3d_branch2c
vec_length 512
[quantize] count:512
[quantize] float src:	
max:1.720947	min:0.000063	diff:0
scale:6.000000	pow2_scale:64.000000
python scale [140144782868486]
compressing layer res4a_branch1
vec_length 524288
[quantize] count:524288
[quantize] float src:	
max:0.420744	min:0.000000	diff:0
scale:8.000000	pow2_scale:256.000000
python scale [140144782868488]
compressing layer bn4a_branch1
vec_length 1024
[quantize] count:1024
[quantize] float src:	
max:2.176449	min:0.001389	diff:0
scale:5.000000	pow2_scale:32.000000
python scale [140144782868485]
compressing layer scale4a_branch1
vec_length 1024
[quantize] count:1024
[quantize] float src:	
max:2.779192	min:0.033980	diff:0
scale:5.000000	pow2_scale:32.000000
python scale [140144782868485]
compressing layer res4a_branch2a
vec_length 131072
[quantize] count:131072
[quantize] float src:	
max:0.340799	min:0.000000	diff:0
scale:8.000000	pow2_scale:256.000000
python scale [140144782868488]
compressing layer bn4a_branch2a
vec_length 256
[quantize] count:256
[quantize] float src:	
max:1.799395	min:0.012472	diff:0
scale:6.000000	pow2_scale:64.000000
python scale [140144782868486]
compressing layer scale4a_branch2a
vec_length 256
[quantize] count:256
[quantize] float src:	
max:1.636373	min:0.621344	diff:0
scale:6.000000	pow2_scale:64.000000
python scale [140144782868486]
compressing layer res4a_branch2b
vec_length 589824
[quantize] count:589824
[quantize] float src:	
max:0.267294	min:0.000000	diff:0
scale:8.000000	pow2_scale:256.000000
python scale [140144782868488]
compressing layer bn4a_branch2b
vec_length 256
[quantize] count:256
[quantize] float src:	
max:4.123749	min:0.005275	diff:0
scale:4.000000	pow2_scale:16.000000
python scale [140144782868484]
compressing layer scale4a_branch2b
vec_length 256
[quantize] count:256
[quantize] float src:	
max:1.749166	min:0.585478	diff:0
scale:6.000000	pow2_scale:64.000000
python scale [140144782868486]
compressing layer res4a_branch2c
vec_length 262144
[quantize] count:262144
[quantize] float src:	
max:0.384191	min:0.000000	diff:0
scale:8.000000	pow2_scale:256.000000
python scale [140144782868488]
compressing layer bn4a_branch2c
vec_length 1024
[quantize] count:1024
[quantize] float src:	
max:0.733779	min:0.000207	diff:0
scale:7.000000	pow2_scale:128.000000
python scale [140144782868487]
compressing layer scale4a_branch2c
vec_length 1024
[quantize] count:1024
[quantize] float src:	
max:2.366837	min:0.071134	diff:0
scale:5.000000	pow2_scale:32.000000
python scale [140144782868485]
compressing layer res4b_branch2a
vec_length 262144
[quantize] count:262144
[quantize] float src:	
max:0.235930	min:0.000000	diff:0
scale:9.000000	pow2_scale:512.000000
python scale [140144782868489]
compressing layer bn4b_branch2a
vec_length 256
[quantize] count:256
[quantize] float src:	
max:5.858453	min:0.006560	diff:0
scale:4.000000	pow2_scale:16.000000
python scale [140144782868484]
compressing layer scale4b_branch2a
vec_length 256
[quantize] count:256
[quantize] float src:	
max:1.743358	min:0.565506	diff:0
scale:6.000000	pow2_scale:64.000000
python scale [140144782868486]
compressing layer res4b_branch2b
vec_length 589824
[quantize] count:589824
[quantize] float src:	
max:0.436288	min:0.000000	diff:0
scale:8.000000	pow2_scale:256.000000
python scale [140144782868488]
compressing layer bn4b_branch2b
vec_length 256
[quantize] count:256
[quantize] float src:	
max:2.382958	min:0.004087	diff:0
scale:5.000000	pow2_scale:32.000000
python scale [140144782868485]
compressing layer scale4b_branch2b
vec_length 256
[quantize] count:256
[quantize] float src:	
max:2.300741	min:0.514758	diff:0
scale:5.000000	pow2_scale:32.000000
python scale [140144782868485]
compressing layer res4b_branch2c
vec_length 262144
[quantize] count:262144
[quantize] float src:	
max:0.437614	min:0.000000	diff:0
scale:8.000000	pow2_scale:256.000000
python scale [140144782868488]
compressing layer bn4b_branch2c
vec_length 1024
[quantize] count:1024
[quantize] float src:	
max:0.431832	min:0.000105	diff:0
scale:8.000000	pow2_scale:256.000000
python scale [140144782868488]
compressing layer scale4b_branch2c
vec_length 1024
[quantize] count:1024
[quantize] float src:	
max:1.942971	min:0.054978	diff:0
scale:6.000000	pow2_scale:64.000000
python scale [140144782868486]
compressing layer res4c_branch2a
vec_length 262144
[quantize] count:262144
[quantize] float src:	
max:0.386906	min:0.000000	diff:0
scale:8.000000	pow2_scale:256.000000
python scale [140144782868488]
compressing layer bn4c_branch2a
vec_length 256
[quantize] count:256
[quantize] float src:	
max:2.171499	min:0.002985	diff:0
scale:5.000000	pow2_scale:32.000000
python scale [140144782868485]
compressing layer scale4c_branch2a
vec_length 256
[quantize] count:256
[quantize] float src:	
max:1.885679	min:0.462703	diff:0
scale:6.000000	pow2_scale:64.000000
python scale [140144782868486]
compressing layer res4c_branch2b
vec_length 589824
[quantize] count:589824
[quantize] float src:	
max:0.257589	min:0.000000	diff:0
scale:8.000000	pow2_scale:256.000000
python scale [140144782868488]
compressing layer bn4c_branch2b
vec_length 256
[quantize] count:256
[quantize] float src:	
max:0.957153	min:0.002709	diff:0
scale:7.000000	pow2_scale:128.000000
python scale [140144782868487]
compressing layer scale4c_branch2b
vec_length 256
[quantize] count:256
[quantize] float src:	
max:1.900555	min:0.555269	diff:0
scale:6.000000	pow2_scale:64.000000
python scale [140144782868486]
compressing layer res4c_branch2c
vec_length 262144
[quantize] count:262144
[quantize] float src:	
max:0.289744	min:0.000000	diff:0
scale:8.000000	pow2_scale:256.000000
python scale [140144782868488]
compressing layer bn4c_branch2c
vec_length 1024
[quantize] count:1024
[quantize] float src:	
max:0.342003	min:0.000063	diff:0
scale:8.000000	pow2_scale:256.000000
python scale [140144782868488]
compressing layer scale4c_branch2c
vec_length 1024
[quantize] count:1024
[quantize] float src:	
max:1.449706	min:0.048827	diff:0
scale:6.000000	pow2_scale:64.000000
python scale [140144782868486]
compressing layer res4d_branch2a
vec_length 262144
[quantize] count:262144
[quantize] float src:	
max:0.295404	min:0.000000	diff:0
scale:8.000000	pow2_scale:256.000000
python scale [140144782868488]
compressing layer bn4d_branch2a
vec_length 256
[quantize] count:256
[quantize] float src:	
max:1.941646	min:0.002175	diff:0
scale:6.000000	pow2_scale:64.000000
python scale [140144782868486]
compressing layer scale4d_branch2a
vec_length 256
[quantize] count:256
[quantize] float src:	
max:1.352728	min:0.442233	diff:0
scale:6.000000	pow2_scale:64.000000
python scale [140144782868486]
compressing layer res4d_branch2b
vec_length 589824
[quantize] count:589824
[quantize] float src:	
max:0.201440	min:0.000000	diff:0
scale:9.000000	pow2_scale:512.000000
python scale [140144782868489]
compressing layer bn4d_branch2b
vec_length 256
[quantize] count:256
[quantize] float src:	
max:1.118595	min:0.000866	diff:0
scale:6.000000	pow2_scale:64.000000
python scale [140144782868486]
compressing layer scale4d_branch2b
vec_length 256
[quantize] count:256
[quantize] float src:	
max:1.939181	min:0.529279	diff:0
scale:6.000000	pow2_scale:64.000000
python scale [140144782868486]
compressing layer res4d_branch2c
vec_length 262144
[quantize] count:262144
[quantize] float src:	
max:0.239456	min:0.000000	diff:0
scale:9.000000	pow2_scale:512.000000
python scale [140144782868489]
compressing layer bn4d_branch2c
vec_length 1024
[quantize] count:1024
[quantize] float src:	
max:0.395854	min:0.000081	diff:0
scale:8.000000	pow2_scale:256.000000
python scale [140144782868488]
compressing layer scale4d_branch2c
vec_length 1024
[quantize] count:1024
[quantize] float src:	
max:1.645641	min:0.002167	diff:0
scale:6.000000	pow2_scale:64.000000
python scale [140144782868486]
compressing layer res4e_branch2a
vec_length 262144
[quantize] count:262144
[quantize] float src:	
max:0.306106	min:0.000000	diff:0
scale:8.000000	pow2_scale:256.000000
python scale [140144782868488]
compressing layer bn4e_branch2a
vec_length 256
[quantize] count:256
[quantize] float src:	
max:2.570902	min:0.002239	diff:0
scale:5.000000	pow2_scale:32.000000
python scale [140144782868485]
compressing layer scale4e_branch2a
vec_length 256
[quantize] count:256
[quantize] float src:	
max:1.445796	min:0.438297	diff:0
scale:6.000000	pow2_scale:64.000000
python scale [140144782868486]
compressing layer res4e_branch2b
vec_length 589824
[quantize] count:589824
[quantize] float src:	
max:0.223091	min:0.000000	diff:0
scale:9.000000	pow2_scale:512.000000
python scale [140144782868489]
compressing layer bn4e_branch2b
vec_length 256
[quantize] count:256
[quantize] float src:	
max:0.492296	min:0.000202	diff:0
scale:8.000000	pow2_scale:256.000000
python scale [140144782868488]
compressing layer scale4e_branch2b
vec_length 256
[quantize] count:256
[quantize] float src:	
max:1.858094	min:0.650596	diff:0
scale:6.000000	pow2_scale:64.000000
python scale [140144782868486]
compressing layer res4e_branch2c
vec_length 262144
[quantize] count:262144
[quantize] float src:	
max:0.264964	min:0.000000	diff:0
scale:8.000000	pow2_scale:256.000000
python scale [140144782868488]
compressing layer bn4e_branch2c
vec_length 1024
[quantize] count:1024
[quantize] float src:	
max:1.071693	min:0.000292	diff:0
scale:6.000000	pow2_scale:64.000000
python scale [140144782868486]
compressing layer scale4e_branch2c
vec_length 1024
[quantize] count:1024
[quantize] float src:	
max:1.500544	min:0.000228	diff:0
scale:6.000000	pow2_scale:64.000000
python scale [140144782868486]
compressing layer res4f_branch2a
vec_length 262144
[quantize] count:262144
[quantize] float src:	
max:0.329696	min:0.000000	diff:0
scale:8.000000	pow2_scale:256.000000
python scale [140144782868488]
compressing layer bn4f_branch2a
vec_length 256
[quantize] count:256
[quantize] float src:	
max:1.156536	min:0.000549	diff:0
scale:6.000000	pow2_scale:64.000000
python scale [140144782868486]
compressing layer scale4f_branch2a
vec_length 256
[quantize] count:256
[quantize] float src:	
max:1.546676	min:0.425436	diff:0
scale:6.000000	pow2_scale:64.000000
python scale [140144782868486]
compressing layer res4f_branch2b
vec_length 589824
[quantize] count:589824
[quantize] float src:	
max:0.292706	min:0.000000	diff:0
scale:8.000000	pow2_scale:256.000000
python scale [140144782868488]
compressing layer bn4f_branch2b
vec_length 256
[quantize] count:256
[quantize] float src:	
max:0.900260	min:0.001268	diff:0
scale:7.000000	pow2_scale:128.000000
python scale [140144782868487]
compressing layer scale4f_branch2b
vec_length 256
[quantize] count:256
[quantize] float src:	
max:2.942218	min:0.649812	diff:0
scale:5.000000	pow2_scale:32.000000
python scale [140144782868485]
compressing layer res4f_branch2c
vec_length 262144
[quantize] count:262144
[quantize] float src:	
max:0.293546	min:0.000000	diff:0
scale:8.000000	pow2_scale:256.000000
python scale [140144782868488]
compressing layer bn4f_branch2c
vec_length 1024
[quantize] count:1024
[quantize] float src:	
max:0.620325	min:0.000262	diff:0
scale:7.000000	pow2_scale:128.000000
python scale [140144782868487]
compressing layer scale4f_branch2c
vec_length 1024
[quantize] count:1024
[quantize] float src:	
max:1.984313	min:0.004237	diff:0
scale:6.000000	pow2_scale:64.000000
python scale [140144782868486]
compressing layer res5a_branch1
vec_length 2097152
[quantize] count:2097152
[quantize] float src:	
max:0.622136	min:0.000000	diff:0
scale:7.000000	pow2_scale:128.000000
python scale [140144782868487]
compressing layer bn5a_branch1
vec_length 2048
[quantize] count:2048
[quantize] float src:	
max:2.380824	min:0.000147	diff:0
scale:5.000000	pow2_scale:32.000000
python scale [140144782868485]
compressing layer scale5a_branch1
vec_length 2048
[quantize] count:2048
[quantize] float src:	
max:4.574630	min:0.260868	diff:0
scale:4.000000	pow2_scale:16.000000
python scale [140144782868484]
compressing layer res5a_branch2a
vec_length 524288
[quantize] count:524288
[quantize] float src:	
max:0.330981	min:0.000000	diff:0
scale:8.000000	pow2_scale:256.000000
python scale [140144782868488]
compressing layer bn5a_branch2a
vec_length 512
[quantize] count:512
[quantize] float src:	
max:2.481642	min:0.005027	diff:0
scale:5.000000	pow2_scale:32.000000
python scale [140144782868485]
compressing layer scale5a_branch2a
vec_length 512
[quantize] count:512
[quantize] float src:	
max:1.594356	min:0.535333	diff:0
scale:6.000000	pow2_scale:64.000000
python scale [140144782868486]
compressing layer res5a_branch2b
vec_length 2359296
[quantize] count:2359296
[quantize] float src:	
max:0.271500	min:0.000000	diff:0
scale:8.000000	pow2_scale:256.000000
python scale [140144782868488]
compressing layer bn5a_branch2b
vec_length 512
[quantize] count:512
[quantize] float src:	
max:2.402111	min:0.002672	diff:0
scale:5.000000	pow2_scale:32.000000
python scale [140144782868485]
compressing layer scale5a_branch2b
vec_length 512
[quantize] count:512
[quantize] float src:	
max:1.542043	min:0.455758	diff:0
scale:6.000000	pow2_scale:64.000000
python scale [140144782868486]
compressing layer res5a_branch2c
vec_length 1048576
[quantize] count:1048576
[quantize] float src:	
max:0.431766	min:0.000000	diff:0
scale:8.000000	pow2_scale:256.000000
python scale [140144782868488]
compressing layer bn5a_branch2c
vec_length 2048
[quantize] count:2048
[quantize] float src:	
max:0.686632	min:0.000032	diff:0
scale:7.000000	pow2_scale:128.000000
python scale [140144782868487]
compressing layer scale5a_branch2c
vec_length 2048
[quantize] count:2048
[quantize] float src:	
max:3.492254	min:0.888443	diff:0
scale:5.000000	pow2_scale:32.000000
python scale [140144782868485]
compressing layer res5b_branch2a
vec_length 1048576
[quantize] count:1048576
[quantize] float src:	
max:0.576673	min:0.000000	diff:0
scale:7.000000	pow2_scale:128.000000
python scale [140144782868487]
compressing layer bn5b_branch2a
vec_length 512
[quantize] count:512
[quantize] float src:	
max:4.969906	min:0.109607	diff:0
scale:4.000000	pow2_scale:16.000000
python scale [140144782868484]
compressing layer scale5b_branch2a
vec_length 512
[quantize] count:512
[quantize] float src:	
max:1.429125	min:0.397740	diff:0
scale:6.000000	pow2_scale:64.000000
python scale [140144782868486]
compressing layer res5b_branch2b
vec_length 2359296
[quantize] count:2359296
[quantize] float src:	
max:0.283863	min:0.000000	diff:0
scale:8.000000	pow2_scale:256.000000
python scale [140144782868488]
compressing layer bn5b_branch2b
vec_length 512
[quantize] count:512
[quantize] float src:	
max:1.218354	min:0.007542	diff:0
scale:6.000000	pow2_scale:64.000000
python scale [140144782868486]
compressing layer scale5b_branch2b
vec_length 512
[quantize] count:512
[quantize] float src:	
max:1.549806	min:0.349432	diff:0
scale:6.000000	pow2_scale:64.000000
python scale [140144782868486]
compressing layer res5b_branch2c
vec_length 1048576
[quantize] count:1048576
[quantize] float src:	
max:0.276730	min:0.000000	diff:0
scale:8.000000	pow2_scale:256.000000I0623 09:45:07.982105  1897 net.cpp:294] The NetState phase (1) differed from the phase (0) specified by a rule in layer data
I0623 09:45:07.983423  1897 net.cpp:51] Initializing net from parameters: 
name: "ResNet-50"
state {
  phase: TEST
  level: 0
}
layer {
  name: "data"
  type: "Data"
  top: "data"
  top: "label"
  include {
    phase: TEST
  }
  transform_param {
    mean_value: 104
    mean_value: 117
    mean_value: 123
  }
  data_param {
    source: "/home/eikan/dezhi/caffe/examples/imagenet/ilsvrc12_val_lmdb"
    batch_size: 8
    crop_size: 224
    backend: LMDB
  }
}
layer {
  name: "conv1"
  type: "Convolution"
  bottom: "data"
  top: "conv1"
  convolution_param {
    num_output: 64
    pad: 3
    kernel_size: 7
    stride: 2
  }
}
layer {
  name: "bn_conv1"
  type: "BatchNorm"
  bottom: "conv1"
  top: "conv1"
  batch_norm_param {
    use_global_stats: true
  }
}
layer {
  name: "scale_conv1"
  type: "Scale"
  bottom: "conv1"
  top: "conv1"
  scale_param {
    bias_term: true
  }
}
layer {
  name: "conv1_relu"
  type: "ReLU"
  bottom: "conv1"
  top: "conv1"
}
layer {
  name: "pool1"
  type: "Pooling"
  bottom: "conv1"
  top: "pool1"
  pooling_param {
    pool: MAX
    kernel_size: 3
    stride: 2
  }
}
layer {
  name: "res2a_branch1"
  type: "Convolution"
  bottom: "pool1"
  top: "res2a_branch1"
  convolution_param {
    num_output: 256
    bias_term: false
    pad: 0
    kernel_size: 1
    stride: 1
  }
}
layer {
  name: "bn2a_branch1"
  type: "BatchNorm"
  bottom: "res2a_branch1"
  top: "res2a_branch1"
  batch_norm_param {
    use_global_stats: true
  }
}
layer {
  name: "scale2a_branch1"
  type: "Scale"
  bottom: "res2a_branch1"
  top: "res2a_branch1"
  scale_param {
    bias_term: true
  }
}
layer {
  name: "res2a_branch2a"
  type: "Convolution"
  bottom: "pool1"
  top: "res2a_branch2a"
  convolution_param {
    num_output: 64
    bias_term: false
    pad: 0
    kernel_size: 1
    stride: 1
  }
}
layer {
  name: "bn2a_branch2a"
  type: "BatchNorm"
  bottom: "res2a_branch2a"
  top: "res2a_branch2a"
  batch_norm_param {
    use_global_stats: true
  }
}
layer {
  name: "scale2a_branch2a"
  type: "Scale"
  bottom: "res2a_branch2a"
  top: "res2a_branch2a"
  scale_param {
    bias_term: true
  }
}
layer {
  name: "res2a_branch2a_relu"
  type: "ReLU"
  bottom: "res2a_branch2a"
  top: "res2a_branch2a"
}
layer {
  name: "res2a_branch2b"
  type: "Convolution"
  bottom: "res2a_branch2a"
  top: "res2a_branch2b"
  convolution_param {
    num_output: 64
    bias_term: false
    pad: 1
    kernel_size: 3
    stride: 1
  }
}
layer {
  name: "bn2a_branch2b"
  type: "BatchNorm"
  bottom: "res2a_branch2b"
  top: "res2a_branch2b"
  batch_norm_param {
    use_global_stats: true
  }
}
layer {
  name: "scale2a_branch2b"
  type: "Scale"
  bottom: "res2a_branch2b"
  top: "res2a_branch2b"
  scale_param {
    bias_term: true
  }
}
layer {
  name: "res2a_branch2b_relu"
  type: "ReLU"
  bottom: "res2a_branch2b"
  top: "res2a_branch2b"
}
layer {
  name: "res2a_branch2c"
  type: "Convolution"
  bottom: "res2a_branch2b"
  top: "res2a_branch2c"
  convolution_param {
    num_output: 256
    bias_term: false
    pad: 0
    kernel_size: 1
    stride: 1
  }
}
layer {
  name: "bn2a_branch2c"
  type: "BatchNorm"
  bottom: "res2a_branch2c"
  top: "res2a_branch2c"
  batch_norm_param {
    use_global_stats: true
  }
}
layer {
  name: "scale2a_branch2c"
  type: "Scale"
  bottom: "res2a_branch2c"
  top: "res2a_branch2c"
  scale_param {
    bias_term: true
  }
}
layer {
  name: "res2a"
  type: "Eltwise"
  bottom: "res2a_branch1"
  bottom: "res2a_branch2c"
  top: "res2a"
}
layer {
  name: "res2a_relu"
  type: "ReLU"
  bottom: "res2a"
  top: "res2a"
}
layer {
  name: "res2b_branch2a"
  type: "Convolution"
  bottom: "res2a"
  top: "res2b_branch2a"
  convolution_param {
    num_output: 64
    bias_term: false
    pad: 0
    kernel_size: 1
    stride: 1
  }
}
layer {
  name: "bn2b_branch2a"
  type: "BatchNorm"
  bottom: "res2b_branch2a"
  top: "res2b_branch2a"
  batch_norm_param {
    use_global_stats: true
  }
}
layer {
  name: "scale2b_branch2a"
  type: "Scale"
  bottom: "res2b_branch2a"
  top: "res2b_branch2a"
  scale_param {
    bias_term: true
  }
}
layer {
  name: "res2b_branch2a_relu"
  type: "ReLU"
  bottom: "res2b_branch2a"
  top: "res2b_branch2a"
}
layer {
  name: "res2b_branch2b"
  type: "Convolution"
  bottom: "res2b_branch2a"
  top: "res2b_branch2b"
  convolution_param {
    num_output: 64
    bias_term: false
    pad: 1
    kernel_size: 3
    stride: 1
  }
}
layer {
  name: "bn2b_branch2b"
  type: "BatchNorm"
  bottom: "res2b_branch2b"
  top: "res2b_branch2b"
  batch_norm_param {
    use_global_stats: true
  }
}
layer {
  name: "scale2b_branch2b"
  type: "Scale"
  bottom: "res2b_branch2b"
  top: "res2b_branch2b"
  scale_param {
    bias_term: true
  }
}
layer {
  name: "res2b_branch2b_relu"
  type: "ReLU"
  bottom: "res2b_branch2b"
  top: "res2b_branch2b"
}
layer {
  name: "res2b_branch2c"
  type: "Convolution"
  bottom: "res2b_branch2b"
  top: "res2b_branch2c"
  convolution_param {
    num_output: 256
    bias_term: false
    pad: 0
    kernel_size: 1
    stride: 1
  }
}
layer {
  name: "bn2b_branch2c"
  type: "BatchNorm"
  bottom: "res2b_branch2c"
  top: "res2b_branch2c"
  batch_norm_param {
    use_global_stats: true
  }
}
layer {
  name: "scale2b_branch2c"
  type: "Scale"
  bottom: "res2b_branch2c"
  top: "res2b_branch2c"
  scale_param {
    bias_term: true
  }
}
layer {
  name: "res2b"
  type: "Eltwise"
  bottom: "res2a"
  bottom: "res2b_branch2c"
  top: "res2b"
}
layer {
  name: "res2b_relu"
  type: "ReLU"
  bottom: "res2b"
  top: "res2b"
}
layer {
  name: "res2c_branch2a"
  type: "Convolution"
  bottom: "res2b"
  top: "res2c_branch2a"
  convolution_param {
    num_output: 64
    bias_term: false
    pad: 0
    kernel_size: 1
    stride: 1
  }
}
layer {
  name: "bn2c_branch2a"
  type: "BatchNorm"
  bottom: "res2c_branch2a"
  top: "res2c_branch2a"
  batch_norm_param {
    use_global_stats: true
  }
}
layer {
  name: "scale2c_branch2a"
  type: "Scale"
  bottom: "res2c_branch2a"
  top: "res2c_branch2a"
  scale_param {
    bias_term: true
  }
}
layer {
  name: "res2c_branch2a_relu"
  type: "ReLU"
  bottom: "res2c_branch2a"
  top: "res2c_branch2a"
}
layer {
  name: "res2c_branch2b"
  type: "Convolution"
  bottom: "res2c_branch2a"
  top: "res2c_branch2b"
  convolution_param {
    num_output: 64
    bias_term: false
    pad: 1
    kernel_size: 3
    stride: 1
  }
}
layer {
  name: "bn2c_branch2b"
  type: "BatchNorm"
  bottom: "res2c_branch2b"
  top: "res2c_branch2b"
  batch_norm_param {
    use_global_stats: true
  }
}
layer {
  name: "scale2c_branch2b"
  type: "Scale"
  bottom: "res2c_branch2b"
  top: "res2c_branch2b"
  scale_param {
    bias_term: true
  }
}
layer {
  name: "res2c_branch2b_relu"
  type: "ReLU"
  bottom: "res2c_branch2b"
  top: "res2c_branch2b"
}
layer {
  name: "res2c_branch2c"
  type: "Convolution"
  bottom: "res2c_branch2b"
  top: "res2c_branch2c"
  convolution_param {
    num_output: 256
    bias_term: false
    pad: 0
    kernel_size: 1
    stride: 1
  }
}
layer {
  name: "bn2c_branch2c"
  type: "BatchNorm"
  bottom: "res2c_branch2c"
  top: "res2c_branch2c"
  batch_norm_param {
    use_global_stats: true
  }
}
layer {
  name: "scale2c_branch2c"
  type: "Scale"
  bottom: "res2c_branch2c"
  top: "res2c_branch2c"
  scale_param {
    bias_term: true
  }
}
layer {
  name: "res2c"
  type: "Eltwise"
  bottom: "res2b"
  bottom: "res2c_branch2c"
  top: "res2c"
}
layer {
  name: "res2c_relu"
  type: "ReLU"
  bottom: "res2c"
  top: "res2c"
}
layer {
  name: "res3a_branch1"
  type: "Convolution"
  bottom: "res2c"
  top: "res3a_branch1"
  convolution_param {
    num_output: 512
    bias_term: false
    pad: 0
    kernel_size: 1
    stride: 2
  }
}
layer {
  name: "bn3a_branch1"
  type: "BatchNorm"
  bottom: "res3a_branch1"
  top: "res3a_branch1"
  batch_norm_param {
    use_global_stats: true
  }
}
layer {
  name: "scale3a_branch1"
  type: "Scale"
  bottom: "res3a_branch1"
  top: "res3a_branch1"
  scale_param {
    bias_term: true
  }
}
layer {
  name: "res3a_branch2a"
  type: "Convolution"
  bottom: "res2c"
  top: "res3a_branch2a"
  convolution_param {
    num_output: 128
    bias_term: false
    pad: 0
    kernel_size: 1
    stride: 2
  }
}
layer {
  name: "bn3a_branch2a"
  type: "BatchNorm"
  bottom: "res3a_branch2a"
  top: "res3a_branch2a"
  batch_norm_param {
    use_global_stats: true
  }
}
layer {
  name: "scale3a_branch2a"
  type: "Scale"
  bottom: "res3a_branch2a"
  top: "res3a_branch2a"
  scale_param {
    bias_term: true
  }
}
layer {
  name: "res3a_branch2a_relu"
  type: "ReLU"
  bottom: "res3a_branch2a"
  top: "res3a_branch2a"
}
layer {
  name: "res3a_branch2b"
  type: "Convolution"
  bottom: "res3a_branch2a"
  top: "res3a_branch2b"
  convolution_param {
    num_output: 128
    bias_term: false
    pad: 1
    kernel_size: 3
    stride: 1
  }
}
layer {
  name: "bn3a_branch2b"
  type: "BatchNorm"
  bottom: "res3a_branch2b"
  top: "res3a_branch2b"
  batch_norm_param {
    use_global_stats: true
  }
}
layer {
  name: "scale3a_branch2b"
  type: "Scale"
  bottom: "res3a_branch2b"
  top: "res3a_branch2b"
  scale_param {
    bias_term: true
  }
}
layer {
  name: "res3a_branch2b_relu"
  type: "ReLU"
  bottom: "res3a_branch2b"
  top: "res3a_branch2b"
}
layer {
  name: "res3a_branch2c"
  type: "Convolution"
  bottom: "res3a_branch2b"
  top: "res3a_branch2c"
  convolution_param {
    num_output: 512
    bias_term: false
    pad: 0
    kernel_size: 1
    stride: 1
  }
}
layer {
  name: "bn3a_branch2c"
  type: "BatchNorm"
  bottom: "res3a_branch2c"
  top: "res3a_branch2c"
  batch_norm_param {
    use_global_stats: true
  }
}
layer {
  name: "scale3a_branch2c"
  type: "Scale"
  bottom: "res3a_branch2c"
  top: "res3a_branch2c"
  scale_param {
    bias_term: true
  }
}
layer {
  name: "res3a"
  type: "Eltwise"
  bottom: "res3a_branch1"
  bottom: "res3a_branch2c"
  top: "res3a"
}
layer {
  name: "res3a_relu"
  type: "ReLU"
  bottom: "res3a"
  top: "res3a"
}
layer {
  name: "res3b_branch2a"
  type: "Convolution"
  bottom: "res3a"
  top: "res3b_branch2a"
  convolution_param {
    num_output: 128
    bias_term: false
    pad: 0
    kernel_size: 1
    stride: 1
  }
}
layer {
  name: "bn3b_branch2a"
  type: "BatchNorm"
  bottom: "res3b_branch2a"
  top: "res3b_branch2a"
  batch_norm_param {
    use_global_stats: true
  }
}
layer {
  name: "scale3b_branch2a"
  type: "Scale"
  bottom: "res3b_branch2a"
  top: "res3b_branch2a"
  scale_param {
    bias_term: true
  }
}
layer {
  name: "res3b_branch2a_relu"
  type: "ReLU"
  bottom: "res3b_branch2a"
  top: "res3b_branch2a"
}
layer {
  name: "res3b_branch2b"
  type: "Convolution"
  bottom: "res3b_branch2a"
  top: "res3b_branch2b"
  convolution_param {
    num_output: 128
    bias_term: false
    pad: 1
    kernel_size: 3
    stride: 1
  }
}
layer {
  name: "bn3b_branch2b"
  type: "BatchNorm"
  bottom: "res3b_branch2b"
  top: "res3b_branch2b"
  batch_norm_param {
    use_global_stats: true
  }
}
layer {
  name: "scale3b_branch2b"
  type: "Scale"
  bottom: "res3b_branch2b"
  top: "res3b_branch2b"
  scale_param {
    bias_term: true
  }
}
layer {
  name: "res3b_branch2b_relu"
  type: "ReLU"
  bottom: "res3b_branch2b"
  top: "res3b_branch2b"
}
layer {
  name: "res3b_branch2c"
  type: "Convolution"
  bottom: "res3b_branch2b"
  top: "res3b_branch2c"
  convolution_param {
    num_output: 512
    bias_term: false
    pad: 0
    kernel_size: 1
    stride: 1
  }
}
layer {
  name: "bn3b_branch2c"
  type: "BatchNorm"
  bottom: "res3b_branch2c"
  top: "res3b_branch2c"
  batch_norm_param {
    use_global_stats: true
  }
}
layer {
  name: "scale3b_branch2c"
  type: "Scale"
  bottom: "res3b_branch2c"
  top: "res3b_branch2c"
  scale_param {
    bias_term: true
  }
}
layer {
  name: "res3b"
  type: "Eltwise"
  bottom: "res3a"
  bottom: "res3b_branch2c"
  top: "res3b"
}
layer {
  name: "res3b_relu"
  type: "ReLU"
  bottom: "res3b"
  top: "res3b"
}
layer {
  name: "res3c_branch2a"
  type: "Convolution"
  bottom: "res3b"
  top: "res3c_branch2a"
  convolution_param {
    num_output: 128
    bias_term: false
    pad: 0
    kernel_size: 1
    stride: 1
  }
}
layer {
  name: "bn3c_branch2a"
  type: "BatchNorm"
  bottom: "res3c_branch2a"
  top: "res3c_branch2a"
  batch_norm_param {
    use_global_stats: true
  }
}
layer {
  name: "scale3c_branch2a"
  type: "Scale"
  bottom: "res3c_branch2a"
  top: "res3c_branch2a"
  scale_param {
    bias_term: true
  }
}
layer {
  name: "res3c_branch2a_relu"
  type: "ReLU"
  bottom: "res3c_branch2a"
  top: "res3c_branch2a"
}
layer {
  name: "res3c_branch2b"
  type: "Convolution"
  bottom: "res3c_branch2a"
  top: "res3c_branch2b"
  convolution_param {
    num_output: 128
    bias_term: false
    pad: 1
    kernel_size: 3
    stride: 1
  }
}
layer {
  name: "bn3c_branch2b"
  type: "BatchNorm"
  bottom: "res3c_branch2b"
  top: "res3c_branch2b"
  batch_norm_param {
    use_global_stats: true
  }
}
layer {
  name: "scale3c_branch2b"
  type: "Scale"
  bottom: "res3c_branch2b"
  top: "res3c_branch2b"
  scale_param {
    bias_term: true
  }
}
layer {
  name: "res3c_branch2b_relu"
  type: "ReLU"
  bottom: "res3c_branch2b"
  top: "res3c_branch2b"
}
layer {
  name: "res3c_branch2c"
  type: "Convolution"
  bottom: "res3c_branch2b"
  top: "res3c_branch2c"
  convolution_param {
    num_output: 512
    bias_term: false
    pad: 0
    kernel_size: 1
    stride: 1
  }
}
layer {
  name: "bn3c_branch2c"
  type: "BatchNorm"
  bottom: "res3c_branch2c"
  top: "res3c_branch2c"
  batch_norm_param {
    use_global_stats: true
  }
}
layer {
  name: "scale3c_branch2c"
  type: "Scale"
  bottom: "res3c_branch2c"
  top: "res3c_branch2c"
  scale_param {
    bias_term: true
  }
}
layer {
  name: "res3c"
  type: "Eltwise"
  bottom: "res3b"
  bottom: "res3c_branch2c"
  top: "res3c"
}
layer {
  name: "res3c_relu"
  type: "ReLU"
  bottom: "res3c"
  top: "res3c"
}
layer {
  name: "res3d_branch2a"
  type: "Convolution"
  bottom: "res3c"
  top: "res3d_branch2a"
  convolution_param {
    num_output: 128
    bias_term: false
    pad: 0
    kernel_size: 1
    stride: 1
  }
}
layer {
  name: "bn3d_branch2a"
  type: "BatchNorm"
  bottom: "res3d_branch2a"
  top: "res3d_branch2a"
  batch_norm_param {
    use_global_stats: true
  }
}
layer {
  name: "scale3d_branch2a"
  type: "Scale"
  bottom: "res3d_branch2a"
  top: "res3d_branch2a"
  scale_param {
    bias_term: true
  }
}
layer {
  name: "res3d_branch2a_relu"
  type: "ReLU"
  bottom: "res3d_branch2a"
  top: "res3d_branch2a"
}
layer {
  name: "res3d_branch2b"
  type: "Convolution"
  bottom: "res3d_branch2a"
  top: "res3d_branch2b"
  convolution_param {
    num_output: 128
    bias_term: false
    pad: 1
    kernel_size: 3
    stride: 1
  }
}
layer {
  name: "bn3d_branch2b"
  type: "BatchNorm"
  bottom: "res3d_branch2b"
  top: "res3d_branch2b"
  batch_norm_param {
    use_global_stats: true
  }
}
layer {
  name: "scale3d_branch2b"
  type: "Scale"
  bottom: "res3d_branch2b"
  top: "res3d_branch2b"
  scale_param {
    bias_term: true
  }
}
layer {
  name: "res3d_branch2b_relu"
  type: "ReLU"
  bottom: "res3d_branch2b"
  top: "res3d_branch2b"
}
layer {
  name: "res3d_branch2c"
  type: "Convolution"
  bottom: "res3d_branch2b"
  top: "res3d_branch2c"
  convolution_param {
    num_output: 512
    bias_term: false
    pad: 0
    kernel_size: 1
    stride: 1
  }
}
layer {
  name: "bn3d_branch2c"
  type: "BatchNorm"
  bottom: "res3d_branch2c"
  top: "res3d_branch2c"
  batch_norm_param {
    use_global_stats: true
  }
}
layer {
  name: "scale3d_branch2c"
  type: "Scale"
  bottom: "res3d_branch2c"
  top: "res3d_branch2c"
  scale_param {
    bias_term: true
  }
}
layer {
  name: "res3d"
  type: "Eltwise"
  bottom: "res3c"
  bottom: "res3d_branch2c"
  top: "res3d"
}
layer {
  name: "res3d_relu"
  type: "ReLU"
  bottom: "res3d"
  top: "res3d"
}
layer {
  name: "res4a_branch1"
  type: "Convolution"
  bottom: "res3d"
  top: "res4a_branch1"
  convolution_param {
    num_output: 1024
    bias_term: false
    pad: 0
    kernel_size: 1
    stride: 2
  }
}
layer {
  name: "bn4a_branch1"
  type: "BatchNorm"
  bottom: "res4a_branch1"
  top: "res4a_branch1"
  batch_norm_param {
    use_global_stats: true
  }
}
layer {
  name: "scale4a_branch1"
  type: "Scale"
  bottom: "res4a_branch1"
  top: "res4a_branch1"
  scale_param {
    bias_term: true
  }
}
layer {
  name: "res4a_branch2a"
  type: "Convolution"
  bottom: "res3d"
  top: "res4a_branch2a"
  convolution_param {
    num_output: 256
    bias_term: false
    pad: 0
    kernel_size: 1
    stride: 2
  }
}
layer {
  name: "bn4a_branch2a"
  type: "BatchNorm"
  bottom: "res4a_branch2a"
  top: "res4a_branch2a"
  batch_norm_param {
    use_global_stats: true
  }
}
layer {
  name: "scale4a_branch2a"
  type: "Scale"
  bottom: "res4a_branch2a"
  top: "res4a_branch2a"
  scale_param {
    bias_term: true
  }
}
layer {
  name: "res4a_branch2a_relu"
  type: "ReLU"
  bottom: "res4a_branch2a"
  top: "res4a_branch2a"
}
layer {
  name: "res4a_branch2b"
  type: "Convolution"
  bottom: "res4a_branch2a"
  top: "res4a_branch2b"
  convolution_param {
    num_output: 256
    bias_term: false
    pad: 1
    kernel_size: 3
    stride: 1
  }
}
layer {
  name: "bn4a_branch2b"
  type: "BatchNorm"
  bottom: "res4a_branch2b"
  top: "res4a_branch2b"
  batch_norm_param {
    use_global_stats: true
  }
}
layer {
  name: "scale4a_branch2b"
  type: "Scale"
  bottom: "res4a_branch2b"
  top: "res4a_branch2b"
  scale_param {
    bias_term: true
  }
}
layer {
  name: "res4a_branch2b_relu"
  type: "ReLU"
  bottom: "res4a_branch2b"
  top: "res4a_branch2b"
}
layer {
  name: "res4a_branch2c"
  type: "Convolution"
  bottom: "res4a_branch2b"
  top: "res4a_branch2c"
  convolution_param {
    num_output: 1024
    bias_term: false
    pad: 0
    kernel_size: 1
    stride: 1
  }
}
layer {
  name: "bn4a_branch2c"
  type: "BatchNorm"
  bottom: "res4a_branch2c"
  top: "res4a_branch2c"
  batch_norm_param {
    use_global_stats: true
  }
}
layer {
  name: "scale4a_branch2c"
  type: "Scale"
  bottom: "res4a_branch2c"
  top: "res4a_branch2c"
  scale_param {
    bias_term: true
  }
}
layer {
  name: "res4a"
  type: "Eltwise"
  bottom: "res4a_branch1"
  bottom: "res4a_branch2c"
  top: "res4a"
}
layer {
  name: "res4a_relu"
  type: "ReLU"
  bottom: "res4a"
  top: "res4a"
}
layer {
  name: "res4b_branch2a"
  type: "Convolution"
  bottom: "res4a"
  top: "res4b_branch2a"
  convolution_param {
    num_output: 256
    bias_term: false
    pad: 0
    kernel_size: 1
    stride: 1
  }
}
layer {
  name: "bn4b_branch2a"
  type: "BatchNorm"
  bottom: "res4b_branch2a"
  top: "res4b_branch2a"
  batch_norm_param {
    use_global_stats: true
  }
}
layer {
  name: "scale4b_branch2a"
  type: "Scale"
  bottom: "res4b_branch2a"
  top: "res4b_branch2a"
  scale_param {
    bias_term: true
  }
}
layer {
  name: "res4b_branch2a_relu"
  type: "ReLU"
  bottom: "res4b_branch2a"
  top: "res4b_branch2a"
}
layer {
  name: "res4b_branch2b"
  type: "Convolution"
  bottom: "res4b_branch2a"
  top: "res4b_branch2b"
  convolution_param {
    num_output: 256
    bias_term: false
    pad: 1
    kernel_size: 3
    stride: 1
  }
}
layer {
  name: "bn4b_branch2b"
  type: "BatchNorm"
  bottom: "res4b_branch2b"
  top: "res4b_branch2b"
  batch_norm_param {
    use_global_stats: true
  }
}
layer {
  name: "scale4b_branch2b"
  type: "Scale"
  bottom: "res4b_branch2b"
  top: "res4b_branch2b"
  scale_param {
    bias_term: true
  }
}
layer {
  name: "res4b_branch2b_relu"
  type: "ReLU"
  bottom: "res4b_branch2b"
  top: "res4b_branch2b"
}
layer {
  name: "res4b_branch2c"
  type: "Convolution"
  bottom: "res4b_branch2b"
  top: "res4b_branch2c"
  convolution_param {
    num_output: 1024
    bias_term: false
    pad: 0
    kernel_size: 1
    stride: 1
  }
}
layer {
  name: "bn4b_branch2c"
  type: "BatchNorm"
  bottom: "res4b_branch2c"
  top: "res4b_branch2c"
  batch_norm_param {
    use_global_stats: true
  }
}
layer {
  name: "scale4b_branch2c"
  type: "Scale"
  bottom: "res4b_branch2c"
  top: "res4b_branch2c"
  scale_param {
    bias_term: true
  }
}
layer {
  name: "res4b"
  type: "Eltwise"
  bottom: "res4a"
  bottom: "res4b_branch2c"
  top: "res4b"
}
layer {
  name: "res4b_relu"
  type: "ReLU"
  bottom: "res4b"
  top: "res4b"
}
layer {
  name: "res4c_branch2a"
  type: "Convolution"
  bottom: "res4b"
  top: "res4c_branch2a"
  convolution_param {
    num_output: 256
    bias_term: false
    pad: 0
    kernel_size: 1
    stride: 1
  }
}
layer {
  name: "bn4c_branch2a"
  type: "BatchNorm"
  bottom: "res4c_branch2a"
  top: "res4c_branch2a"
  batch_norm_param {
    use_global_stats: true
  }
}
layer {
  name: "scale4c_branch2a"
  type: "Scale"
  bottom: "res4c_branch2a"
  top: "res4c_branch2a"
  scale_param {
    bias_term: true
  }
}
layer {
  name: "res4c_branch2a_relu"
  type: "ReLU"
  bottom: "res4c_branch2a"
  top: "res4c_branch2a"
}
layer {
  name: "res4c_branch2b"
  type: "Convolution"
  bottom: "res4c_branch2a"
  top: "res4c_branch2b"
  convolution_param {
    num_output: 256
    bias_term: false
    pad: 1
    kernel_size: 3
    stride: 1
  }
}
layer {
  name: "bn4c_branch2b"
  type: "BatchNorm"
  bottom: "res4c_branch2b"
  top: "res4c_branch2b"
  batch_norm_param {
    use_global_stats: true
  }
}
layer {
  name: "scale4c_branch2b"
  type: "Scale"
  bottom: "res4c_branch2b"
  top: "res4c_branch2b"
  scale_param {
    bias_term: true
  }
}
layer {
  name: "res4c_branch2b_relu"
  type: "ReLU"
  bottom: "res4c_branch2b"
  top: "res4c_branch2b"
}
layer {
  name: "res4c_branch2c"
  type: "Convolution"
  bottom: "res4c_branch2b"
  top: "res4c_branch2c"
  convolution_param {
    num_output: 1024
    bias_term: false
    pad: 0
    kernel_size: 1
    stride: 1
  }
}
layer {
  name: "bn4c_branch2c"
  type: "BatchNorm"
  bottom: "res4c_branch2c"
  top: "res4c_branch2c"
  batch_norm_param {
    use_global_stats: true
  }
}
layer {
  name: "scale4c_branch2c"
  type: "Scale"
  bottom: "res4c_branch2c"
  top: "res4c_branch2c"
  scale_param {
    bias_term: true
  }
}
layer {
  name: "res4c"
  type: "Eltwise"
  bottom: "res4b"
  bottom: "res4c_branch2c"
  top: "res4c"
}
layer {
  name: "res4c_relu"
  type: "ReLU"
  bottom: "res4c"
  top: "res4c"
}
layer {
  name: "res4d_branch2a"
  type: "Convolution"
  bottom: "res4c"
  top: "res4d_branch2a"
  convolution_param {
    num_output: 256
    bias_term: false
    pad: 0
    kernel_size: 1
    stride: 1
  }
}
layer {
  name: "bn4d_branch2a"
  type: "BatchNorm"
  bottom: "res4d_branch2a"
  top: "res4d_branch2a"
  batch_norm_param {
    use_global_stats: true
  }
}
layer {
  name: "scale4d_branch2a"
  type: "Scale"
  bottom: "res4d_branch2a"
  top: "res4d_branch2a"
  scale_param {
    bias_term: true
  }
}
layer {
  name: "res4d_branch2a_relu"
  type: "ReLU"
  bottom: "res4d_branch2a"
  top: "res4d_branch2a"
}
layer {
  name: "res4d_branch2b"
  type: "Convolution"
  bottom: "res4d_branch2a"
  top: "res4d_branch2b"
  convolution_param {
    num_output: 256
    bias_term: false
    pad: 1
    kernel_size: 3
    stride: 1
  }
}
layer {
  name: "bn4d_branch2b"
  type: "BatchNorm"
  bottom: "res4d_branch2b"
  top: "res4d_branch2b"
  batch_norm_param {
    use_global_stats: true
  }
}
layer {
  name: "scale4d_branch2b"
  type: "Scale"
  bottom: "res4d_branch2b"
  top: "res4d_branch2b"
  scale_param {
    bias_term: true
  }
}
layer {
  name: "res4d_branch2b_relu"
  type: "ReLU"
  bottom: "res4d_branch2b"
  top: "res4d_branch2b"
}
layer {
  name: "res4d_branch2c"
  type: "Convolution"
  bottom: "res4d_branch2b"
  top: "res4d_branch2c"
  convolution_param {
    num_output: 1024
    bias_term: false
    pad: 0
    kernel_size: 1
    stride: 1
  }
}
layer {
  name: "bn4d_branch2c"
  type: "BatchNorm"
  bottom: "res4d_branch2c"
  top: "res4d_branch2c"
  batch_norm_param {
    use_global_stats: true
  }
}
layer {
  name: "scale4d_branch2c"
  type: "Scale"
  bottom: "res4d_branch2c"
  top: "res4d_branch2c"
  scale_param {
    bias_term: true
  }
}
layer {
  name: "res4d"
  type: "Eltwise"
  bottom: "res4c"
  bottom: "res4d_branch2c"
  top: "res4d"
}
layer {
  name: "res4d_relu"
  type: "ReLU"
  bottom: "res4d"
  top: "res4d"
}
layer {
  name: "res4e_branch2a"
  type: "Convolution"
  bottom: "res4d"
  top: "res4e_branch2a"
  convolution_param {
    num_output: 256
    bias_term: false
    pad: 0
    kernel_size: 1
    stride: 1
  }
}
layer {
  name: "bn4e_branch2a"
  type: "BatchNorm"
  bottom: "res4e_branch2a"
  top: "res4e_branch2a"
  batch_norm_param {
    use_global_stats: true
  }
}
layer {
  name: "scale4e_branch2a"
  type: "Scale"
  bottom: "res4e_branch2a"
  top: "res4e_branch2a"
  scale_param {
    bias_term: true
  }
}
layer {
  name: "res4e_branch2a_relu"
  type: "ReLU"
  bottom: "res4e_branch2a"
  top: "res4e_branch2a"
}
layer {
  name: "res4e_branch2b"
  type: "Convolution"
  bottom: "res4e_branch2a"
  top: "res4e_branch2b"
  convolution_param {
    num_output: 256
    bias_term: false
    pad: 1
    kernel_size: 3
    stride: 1
  }
}
layer {
  name: "bn4e_branch2b"
  type: "BatchNorm"
  bottom: "res4e_branch2b"
  top: "res4e_branch2b"
  batch_norm_param {
    use_global_stats: true
  }
}
layer {
  name: "scale4e_branch2b"
  type: "Scale"
  bottom: "res4e_branch2b"
  top: "res4e_branch2b"
  scale_param {
    bias_term: true
  }
}
layer {
  name: "res4e_branch2b_relu"
  type: "ReLU"
  bottom: "res4e_branch2b"
  top: "res4e_branch2b"
}
layer {
  name: "res4e_branch2c"
  type: "Convolution"
  bottom: "res4e_branch2b"
  top: "res4e_branch2c"
  convolution_param {
    num_output: 1024
    bias_term: false
    pad: 0
    kernel_size: 1
    stride: 1
  }
}
layer {
  name: "bn4e_branch2c"
  type: "BatchNorm"
  bottom: "res4e_branch2c"
  top: "res4e_branch2c"
  batch_norm_param {
    use_global_stats: true
  }
}
layer {
  name: "scale4e_branch2c"
  type: "Scale"
  bottom: "res4e_branch2c"
  top: "res4e_branch2c"
  scale_param {
    bias_term: true
  }
}
layer {
  name: "res4e"
  type: "Eltwise"
  bottom: "res4d"
  bottom: "res4e_branch2c"
  top: "res4e"
}
layer {
  name: "res4e_relu"
  type: "ReLU"
  bottom: "res4e"
  top: "res4e"
}
layer {
  name: "res4f_branch2a"
  type: "Convolution"
  bottom: "res4e"
  top: "res4f_branch2a"
  convolution_param {
    num_output: 256
    bias_term: false
    pad: 0
    kernel_size: 1
    stride: 1
  }
}
layer {
  name: "bn4f_branch2a"
  type: "BatchNorm"
  bottom: "res4f_branch2a"
  top: "res4f_branch2a"
  batch_norm_param {
    use_global_stats: true
  }
}
layer {
  name: "scale4f_branch2a"
  type: "Scale"
  bottom: "res4f_branch2a"
  top: "res4f_branch2a"
  scale_param {
    bias_term: true
  }
}
layer {
  name: "res4f_branch2a_relu"
  type: "ReLU"
  bottom: "res4f_branch2a"
  top: "res4f_branch2a"
}
layer {
  name: "res4f_branch2b"
  type: "Convolution"
  bottom: "res4f_branch2a"
  top: "res4f_branch2b"
  convolution_param {
    num_output: 256
    bias_term: false
    pad: 1
    kernel_size: 3
    stride: 1
  }
}
layer {
  name: "bn4f_branch2b"
  type: "BatchNorm"
  bottom: "res4f_branch2b"
  top: "res4f_branch2b"
  batch_norm_param {
    use_global_stats: true
  }
}
layer {
  name: "scale4f_branch2b"
  type: "Scale"
  bottom: "res4f_branch2b"
  top: "res4f_branch2b"
  scale_param {
    bias_term: true
  }
}
layer {
  name: "res4f_branch2b_relu"
  type: "ReLU"
  bottom: "res4f_branch2b"
  top: "res4f_branch2b"
}
layer {
  name: "res4f_branch2c"
  type: "Convolution"
  bottom: "res4f_branch2b"
  top: "res4f_branch2c"
  convolution_param {
    num_output: 1024
    bias_term: false
    pad: 0
    kernel_size: 1
    stride: 1
  }
}
layer {
  name: "bn4f_branch2c"
  type: "BatchNorm"
  bottom: "res4f_branch2c"
  top: "res4f_branch2c"
  batch_norm_param {
    use_global_stats: true
  }
}
layer {
  name: "scale4f_branch2c"
  type: "Scale"
  bottom: "res4f_branch2c"
  top: "res4f_branch2c"
  scale_param {
    bias_term: true
  }
}
layer {
  name: "res4f"
  type: "Eltwise"
  bottom: "res4e"
  bottom: "res4f_branch2c"
  top: "res4f"
}
layer {
  name: "res4f_relu"
  type: "ReLU"
  bottom: "res4f"
  top: "res4f"
}
layer {
  name: "res5a_branch1"
  type: "Convolution"
  bottom: "res4f"
  top: "res5a_branch1"
  convolution_param {
    num_output: 2048
    bias_term: false
    pad: 0
    kernel_size: 1
    stride: 2
  }
}
layer {
  name: "bn5a_branch1"
  type: "BatchNorm"
  bottom: "res5a_branch1"
  top: "res5a_branch1"
  batch_norm_param {
    use_global_stats: true
  }
}
layer {
  name: "scale5a_branch1"
  type: "Scale"
  bottom: "res5a_branch1"
  top: "res5a_branch1"
  scale_param {
    bias_term: true
  }
}
layer {
  name: "res5a_branch2a"
  type: "Convolution"
  bottom: "res4f"
  top: "res5a_branch2a"
  convolution_param {
    num_output: 512
    bias_term: false
    pad: 0
    kernel_size: 1
    stride: 2
  }
}
layer {
  name: "bn5a_branch2a"
  type: "BatchNorm"
  bottom: "res5a_branch2a"
  top: "res5a_branch2a"
  batch_norm_param {
    use_global_stats: true
  }
}
layer {
  name: "scale5a_branch2a"
  type: "Scale"
  bottom: "res5a_branch2a"
  top: "res5a_branch2a"
  scale_param {
    bias_term: true
  }
}
layer {
  name: "res5a_branch2a_relu"
  type: "ReLU"
  bottom: "res5a_branch2a"
  top: "res5a_branch2a"
}
layer {
  name: "res5a_branch2b"
  type: "Convolution"
  bottom: "res5a_branch2a"
  top: "res5a_branch2b"
  convolution_param {
    num_output: 512
    bias_term: false
    pad: 1
    kernel_size: 3
    stride: 1
  }
}
layer {
  name: "bn5a_branch2b"
  type: "BatchNorm"
  bottom: "res5a_branch2b"
  top: "res5a_branch2b"
  batch_norm_param {
    use_global_stats: true
  }
}
layer {
  name: "scale5a_branch2b"
  type: "Scale"
  bottom: "res5a_branch2b"
  top: "res5a_branch2b"
  scale_param {
    bias_term: true
  }
}
layer {
  name: "res5a_branch2b_relu"
  type: "ReLU"
  bottom: "res5a_branch2b"
  top: "res5a_branch2b"
}
layer {
  name: "res5a_branch2c"
  type: "Convolution"
  bottom: "res5a_branch2b"
  top: "res5a_branch2c"
  convolution_param {
    num_output: 2048
    bias_term: false
    pad: 0
    kernel_size: 1
    stride: 1
  }
}
layer {
  name: "bn5a_branch2c"
  type: "BatchNorm"
  bottom: "res5a_branch2c"
  top: "re
I0623 09:45:07.989269  1897 layer_factory.hpp:77] Creating layer data
I0623 09:45:07.989349  1897 db_lmdb.cpp:35] Opened lmdb /home/eikan/dezhi/caffe/examples/imagenet/ilsvrc12_val_lmdb
I0623 09:45:07.989392  1897 net.cpp:84] Creating Layer data
I0623 09:45:07.989411  1897 net.cpp:380] data -> data
I0623 09:45:07.989435  1897 net.cpp:380] data -> label
I0623 09:45:07.990315  1897 data_layer.cpp:45] output data size: 8,3,256,256
I0623 09:45:08.083770  1897 net.cpp:122] Setting up data
I0623 09:45:08.083809  1897 net.cpp:129] Top shape: 8 3 256 256 (1572864)
I0623 09:45:08.083817  1897 net.cpp:129] Top shape: 8 (8)
I0623 09:45:08.083822  1897 net.cpp:137] Memory required for data: 6291488
I0623 09:45:08.083829  1897 layer_factory.hpp:77] Creating layer label_data_1_split
I0623 09:45:08.083844  1897 net.cpp:84] Creating Layer label_data_1_split
I0623 09:45:08.083853  1897 net.cpp:406] label_data_1_split <- label
I0623 09:45:08.083860  1897 net.cpp:380] label_data_1_split -> label_data_1_split_0
I0623 09:45:08.083890  1897 net.cpp:380] label_data_1_split -> label_data_1_split_1
I0623 09:45:08.083909  1897 net.cpp:122] Setting up label_data_1_split
I0623 09:45:08.083923  1897 net.cpp:129] Top shape: 8 (8)
I0623 09:45:08.083935  1897 net.cpp:129] Top shape: 8 (8)
I0623 09:45:08.083945  1897 net.cpp:137] Memory required for data: 6291552
I0623 09:45:08.083955  1897 layer_factory.hpp:77] Creating layer conv1
I0623 09:45:08.083972  1897 net.cpp:84] Creating Layer conv1
I0623 09:45:08.083983  1897 net.cpp:406] conv1 <- data
I0623 09:45:08.083997  1897 net.cpp:380] conv1 -> conv1
I0623 09:45:08.084054  1897 net.cpp:122] Setting up conv1
I0623 09:45:08.084071  1897 net.cpp:129] Top shape: 8 64 128 128 (8388608)
I0623 09:45:08.084082  1897 net.cpp:137] Memory required for data: 39845984
I0623 09:45:08.084100  1897 layer_factory.hpp:77] Creating layer bn_conv1
I0623 09:45:08.084117  1897 net.cpp:84] Creating Layer bn_conv1
I0623 09:45:08.084128  1897 net.cpp:406] bn_conv1 <- conv1
I0623 09:45:08.084141  1897 net.cpp:367] bn_conv1 -> conv1 (in-place)
I0623 09:45:08.084177  1897 net.cpp:122] Setting up bn_conv1
I0623 09:45:08.084203  1897 net.cpp:129] Top shape: 8 64 128 128 (8388608)
I0623 09:45:08.084214  1897 net.cpp:137] Memory required for data: 73400416
I0623 09:45:08.084233  1897 layer_factory.hpp:77] Creating layer scale_conv1
I0623 09:45:08.084249  1897 net.cpp:84] Creating Layer scale_conv1
I0623 09:45:08.084261  1897 net.cpp:406] scale_conv1 <- conv1
I0623 09:45:08.084273  1897 net.cpp:367] scale_conv1 -> conv1 (in-place)
I0623 09:45:08.084292  1897 layer_factory.hpp:77] Creating layer scale_conv1
I0623 09:45:08.084343  1897 net.cpp:122] Setting up scale_conv1
I0623 09:45:08.084360  1897 net.cpp:129] Top shape: 8 64 128 128 (8388608)
I0623 09:45:08.084370  1897 net.cpp:137] Memory required for data: 106954848
I0623 09:45:08.084383  1897 layer_factory.hpp:77] Creating layer conv1_relu
I0623 09:45:08.084398  1897 net.cpp:84] Creating Layer conv1_relu
I0623 09:45:08.084409  1897 net.cpp:406] conv1_relu <- conv1
I0623 09:45:08.084421  1897 net.cpp:367] conv1_relu -> conv1 (in-place)
I0623 09:45:08.084434  1897 net.cpp:122] Setting up conv1_relu
I0623 09:45:08.084446  1897 net.cpp:129] Top shape: 8 64 128 128 (8388608)
I0623 09:45:08.084456  1897 net.cpp:137] Memory required for data: 140509280
I0623 09:45:08.084466  1897 layer_factory.hpp:77] Creating layer pool1
I0623 09:45:08.084481  1897 net.cpp:84] Creating Layer pool1
I0623 09:45:08.084491  1897 net.cpp:406] pool1 <- conv1
I0623 09:45:08.084503  1897 net.cpp:380] pool1 -> pool1
I0623 09:45:08.084520  1897 net.cpp:122] Setting up pool1
I0623 09:45:08.084533  1897 net.cpp:129] Top shape: 8 64 64 64 (2097152)
I0623 09:45:08.084543  1897 net.cpp:137] Memory required for data: 148897888
I0623 09:45:08.084553  1897 layer_factory.hpp:77] Creating layer pool1_pool1_0_split
I0623 09:45:08.084566  1897 net.cpp:84] Creating Layer pool1_pool1_0_split
I0623 09:45:08.084576  1897 net.cpp:406] pool1_pool1_0_split <- pool1
I0623 09:45:08.084589  1897 net.cpp:380] pool1_pool1_0_split -> pool1_pool1_0_split_0
I0623 09:45:08.084602  1897 net.cpp:380] pool1_pool1_0_split -> pool1_pool1_0_split_1
I0623 09:45:08.084616  1897 net.cpp:122] Setting up pool1_pool1_0_split
I0623 09:45:08.084630  1897 net.cpp:129] Top shape: 8 64 64 64 (2097152)
I0623 09:45:08.084640  1897 net.cpp:129] Top shape: 8 64 64 64 (2097152)
I0623 09:45:08.084650  1897 net.cpp:137] Memory required for data: 165675104
I0623 09:45:08.084661  1897 layer_factory.hpp:77] Creating layer res2a_branch1
I0623 09:45:08.084676  1897 net.cpp:84] Creating Layer res2a_branch1
I0623 09:45:08.084687  1897 net.cpp:406] res2a_branch1 <- pool1_pool1_0_split_0
I0623 09:45:08.084700  1897 net.cpp:380] res2a_branch1 -> res2a_branch1
I0623 09:45:08.084739  1897 net.cpp:122] Setting up res2a_branch1
I0623 09:45:08.084756  1897 net.cpp:129] Top shape: 8 256 64 64 (8388608)
I0623 09:45:08.084766  1897 net.cpp:137] Memory required for data: 199229536
I0623 09:45:08.084779  1897 layer_factory.hpp:77] Creating layer bn2a_branch1
I0623 09:45:08.084792  1897 net.cpp:84] Creating Layer bn2a_branch1
I0623 09:45:08.084803  1897 net.cpp:406] bn2a_branch1 <- res2a_branch1
I0623 09:45:08.084816  1897 net.cpp:367] bn2a_branch1 -> res2a_branch1 (in-place)
I0623 09:45:08.084841  1897 net.cpp:122] Setting up bn2a_branch1
I0623 09:45:08.084856  1897 net.cpp:129] Top shape: 8 256 64 64 (8388608)
I0623 09:45:08.084866  1897 net.cpp:137] Memory required for data: 232783968
I0623 09:45:08.084882  1897 layer_factory.hpp:77] Creating layer scale2a_branch1
I0623 09:45:08.084897  1897 net.cpp:84] Creating Layer scale2a_branch1
I0623 09:45:08.084908  1897 net.cpp:406] scale2a_branch1 <- res2a_branch1
I0623 09:45:08.084919  1897 net.cpp:367] scale2a_branch1 -> res2a_branch1 (in-place)
I0623 09:45:08.084936  1897 layer_factory.hpp:77] Creating layer scale2a_branch1
I0623 09:45:08.084990  1897 net.cpp:122] Setting up scale2a_branch1
I0623 09:45:08.085007  1897 net.cpp:129] Top shape: 8 256 64 64 (8388608)
I0623 09:45:08.085017  1897 net.cpp:137] Memory required for data: 266338400
I0623 09:45:08.085031  1897 layer_factory.hpp:77] Creating layer res2a_branch2a
I0623 09:45:08.085050  1897 net.cpp:84] Creating Layer res2a_branch2a
I0623 09:45:08.085062  1897 net.cpp:406] res2a_branch2a <- pool1_pool1_0_split_1
I0623 09:45:08.085075  1897 net.cpp:380] res2a_branch2a -> res2a_branch2a
I0623 09:45:08.085101  1897 net.cpp:122] Setting up res2a_branch2a
I0623 09:45:08.085116  1897 net.cpp:129] Top shape: 8 64 64 64 (2097152)
I0623 09:45:08.085126  1897 net.cpp:137] Memory required for data: 274727008
I0623 09:45:08.085139  1897 layer_factory.hpp:77] Creating layer bn2a_branch2a
I0623 09:45:08.085152  1897 net.cpp:84] Creating Layer bn2a_branch2a
I0623 09:45:08.085163  1897 net.cpp:406] bn2a_branch2a <- res2a_branch2a
I0623 09:45:08.085175  1897 net.cpp:367] bn2a_branch2a -> res2a_branch2a (in-place)
I0623 09:45:08.085198  1897 net.cpp:122] Setting up bn2a_branch2a
I0623 09:45:08.085212  1897 net.cpp:129] Top shape: 8 64 64 64 (2097152)
I0623 09:45:08.085223  1897 net.cpp:137] Memory required for data: 283115616
I0623 09:45:08.085240  1897 layer_factory.hpp:77] Creating layer scale2a_branch2a
I0623 09:45:08.085254  1897 net.cpp:84] Creating Layer scale2a_branch2a
I0623 09:45:08.085265  1897 net.cpp:406] scale2a_branch2a <- res2a_branch2a
I0623 09:45:08.085278  1897 net.cpp:367] scale2a_branch2a -> res2a_branch2a (in-place)
I0623 09:45:08.085294  1897 layer_factory.hpp:77] Creating layer scale2a_branch2a
I0623 09:45:08.085322  1897 net.cpp:122] Setting up scale2a_branch2a
I0623 09:45:08.085337  1897 net.cpp:129] Top shape: 8 64 64 64 (2097152)
I0623 09:45:08.085347  1897 net.cpp:137] Memory required for data: 291504224
I0623 09:45:08.085361  1897 layer_factory.hpp:77] Creating layer res2a_branch2a_relu
I0623 09:45:08.085373  1897 net.cpp:84] Creating Layer res2a_branch2a_relu
I0623 09:45:08.085384  1897 net.cpp:406] res2a_branch2a_relu <- res2a_branch2a
I0623 09:45:08.085397  1897 net.cpp:367] res2a_branch2a_relu -> res2a_branch2a (in-place)
I0623 09:45:08.085410  1897 net.cpp:122] Setting up res2a_branch2a_relu
I0623 09:45:08.085422  1897 net.cpp:129] Top shape: 8 64 64 64 (2097152)
I0623 09:45:08.085433  1897 net.cpp:137] Memory required for data: 299892832
I0623 09:45:08.085443  1897 layer_factory.hpp:77] Creating layer res2a_branch2b
I0623 09:45:08.085458  1897 net.cpp:84] Creating Layer res2a_branch2b
I0623 09:45:08.085469  1897 net.cpp:406] res2a_branch2b <- res2a_branch2a
I0623 09:45:08.085480  1897 net.cpp:380] res2a_branch2b -> res2a_branch2b
I0623 09:45:08.085536  1897 net.cpp:122] Setting up res2a_branch2b
I0623 09:45:08.085553  1897 net.cpp:129] Top shape: 8 64 64 64 (2097152)
I0623 09:45:08.085563  1897 net.cpp:137] Memory required for data: 308281440
I0623 09:45:08.085575  1897 layer_factory.hpp:77] Creating layer bn2a_branch2b
I0623 09:45:08.085592  1897 net.cpp:84] Creating Layer bn2a_branch2b
I0623 09:45:08.085602  1897 net.cpp:406] bn2a_branch2b <- res2a_branch2b
I0623 09:45:08.085614  1897 net.cpp:367] bn2a_branch2b -> res2a_branch2b (in-place)
I0623 09:45:08.085638  1897 net.cpp:122] Setting up bn2a_branch2b
I0623 09:45:08.085651  1897 net.cpp:129] Top shape: 8 64 64 64 (2097152)
I0623 09:45:08.085661  1897 net.cpp:137] Memory required for data: 316670048
I0623 09:45:08.085676  1897 layer_factory.hpp:77] Creating layer scale2a_branch2b
I0623 09:45:08.085690  1897 net.cpp:84] Creating Layer scale2a_branch2b
I0623 09:45:08.085700  1897 net.cpp:406] scale2a_branch2b <- res2a_branch2b
I0623 09:45:08.085712  1897 net.cpp:367] scale2a_branch2b -> res2a_branch2b (in-place)
I0623 09:45:08.085729  1897 layer_factory.hpp:77] Creating layer scale2a_branch2b
I0623 09:45:08.085757  1897 net.cpp:122] Setting up scale2a_branch2b
I0623 09:45:08.085770  1897 net.cpp:129] Top shape: 8 64 64 64 (2097152)
I0623 09:45:08.085782  1897 net.cpp:137] Memory required for data: 325058656
I0623 09:45:08.085794  1897 layer_factory.hpp:77] Creating layer res2a_branch2b_relu
I0623 09:45:08.085808  1897 net.cpp:84] Creating Layer res2a_branch2b_relu
I0623 09:45:08.085819  1897 net.cpp:406] res2a_branch2b_relu <- res2a_branch2b
I0623 09:45:08.085830  1897 net.cpp:367] res2a_branch2b_relu -> res2a_branch2b (in-place)
I0623 09:45:08.085849  1897 net.cpp:122] Setting up res2a_branch2b_relu
I0623 09:45:08.085861  1897 net.cpp:129] Top shape: 8 64 64 64 (2097152)
I0623 09:45:08.085871  1897 net.cpp:137] Memory required for data: 333447264
I0623 09:45:08.085881  1897 layer_factory.hpp:77] Creating layer res2a_branch2c
I0623 09:45:08.085896  1897 net.cpp:84] Creating Layer res2a_branch2c
I0623 09:45:08.085906  1897 net.cpp:406] res2a_branch2c <- res2a_branch2b
I0623 09:45:08.085919  1897 net.cpp:380] res2a_branch2c -> res2a_branch2c
I0623 09:45:08.085955  1897 net.cpp:122] Setting up res2a_branch2c
I0623 09:45:08.085970  1897 net.cpp:129] Top shape: 8 256 64 64 (8388608)
I0623 09:45:08.085980  1897 net.cpp:137] Memory required for data: 367001696
I0623 09:45:08.085992  1897 layer_factory.hpp:77] Creating layer bn2a_branch2c
I0623 09:45:08.086006  1897 net.cpp:84] Creating Layer bn2a_branch2c
I0623 09:45:08.086016  1897 net.cpp:406] bn2a_branch2c <- res2a_branch2c
I0623 09:45:08.086028  1897 net.cpp:367] bn2a_branch2c -> res2a_branch2c (in-place)
I0623 09:45:08.086052  1897 net.cpp:122] Setting up bn2a_branch2c
I0623 09:45:08.086066  1897 net.cpp:129] Top shape: 8 256 64 64 (8388608)
I0623 09:45:08.086076  1897 net.cpp:137] Memory required for data: 400556128
I0623 09:45:08.086091  1897 layer_factory.hpp:77] Creating layer scale2a_branch2c
I0623 09:45:08.086103  1897 net.cpp:84] Creating Layer scale2a_branch2c
I0623 09:45:08.086113  1897 net.cpp:406] scale2a_branch2c <- res2a_branch2c
I0623 09:45:08.086125  1897 net.cpp:367] scale2a_branch2c -> res2a_branch2c (in-place)
I0623 09:45:08.086143  1897 layer_factory.hpp:77] Creating layer scale2a_branch2c
I0623 09:45:08.086169  1897 net.cpp:122] Setting up scale2a_branch2c
I0623 09:45:08.086184  1897 net.cpp:129] Top shape: 8 256 64 64 (8388608)
I0623 09:45:08.086194  1897 net.cpp:137] Memory required for data: 434110560
I0623 09:45:08.086208  1897 layer_factory.hpp:77] Creating layer res2a
I0623 09:45:08.086221  1897 net.cpp:84] Creating Layer res2a
I0623 09:45:08.086233  1897 net.cpp:406] res2a <- res2a_branch1
I0623 09:45:08.086246  1897 net.cpp:406] res2a <- res2a_branch2c
I0623 09:45:08.086257  1897 net.cpp:380] res2a -> res2a
I0623 09:45:08.086272  1897 net.cpp:122] Setting up res2a
I0623 09:45:08.086285  1897 net.cpp:129] Top shape: 8 256 64 64 (8388608)
I0623 09:45:08.086295  1897 net.cpp:137] Memory required for data: 467664992
I0623 09:45:08.086305  1897 layer_factory.hpp:77] Creating layer res2a_relu
I0623 09:45:08.086318  1897 net.cpp:84] Creating Layer res2a_relu
I0623 09:45:08.086328  1897 net.cpp:406] res2a_relu <- res2a
I0623 09:45:08.086340  1897 net.cpp:367] res2a_relu -> res2a (in-place)
I0623 09:45:08.086354  1897 net.cpp:122] Setting up res2a_relu
I0623 09:45:08.086366  1897 net.cpp:129] Top shape: 8 256 64 64 (8388608)
I0623 09:45:08.086376  1897 net.cpp:137] Memory required for data: 501219424
I0623 09:45:08.086386  1897 layer_factory.hpp:77] Creating layer res2a_res2a_relu_0_split
I0623 09:45:08.086398  1897 net.cpp:84] Creating Layer res2a_res2a_relu_0_split
I0623 09:45:08.086408  1897 net.cpp:406] res2a_res2a_relu_0_split <- res2a
I0623 09:45:08.086421  1897 net.cpp:380] res2a_res2a_relu_0_split -> res2a_res2a_relu_0_split_0
I0623 09:45:08.086434  1897 net.cpp:380] res2a_res2a_relu_0_split -> res2a_res2a_relu_0_split_1
I0623 09:45:08.086449  1897 net.cpp:122] Setting up res2a_res2a_relu_0_split
I0623 09:45:08.086462  1897 net.cpp:129] Top shape: 8 256 64 64 (8388608)
I0623 09:45:08.086473  1897 net.cpp:129] Top shape: 8 256 64 64 (8388608)
I0623 09:45:08.086483  1897 net.cpp:137] Memory required for data: 568328288
I0623 09:45:08.086493  1897 layer_factory.hpp:77] Creating layer res2b_branch2a
I0623 09:45:08.086508  1897 net.cpp:84] Creating Layer res2b_branch2a
I0623 09:45:08.086519  1897 net.cpp:406] res2b_branch2a <- res2a_res2a_relu_0_split_0
I0623 09:45:08.086530  1897 net.cpp:380] res2b_branch2a -> res2b_branch2a
I0623 09:45:08.086566  1897 net.cpp:122] Setting up res2b_branch2a
I0623 09:45:08.086582  1897 net.cpp:129] Top shape: 8 64 64 64 (2097152)
I0623 09:45:08.086597  1897 net.cpp:137] Memory required for data: 576716896
I0623 09:45:08.086611  1897 layer_factory.hpp:77] Creating layer bn2b_branch2a
I0623 09:45:08.086623  1897 net.cpp:84] Creating Layer bn2b_branch2a
I0623 09:45:08.086634  1897 net.cpp:406] bn2b_branch2a <- res2b_branch2a
I0623 09:45:08.086647  1897 net.cpp:367] bn2b_branch2a -> res2b_branch2a (in-place)
I0623 09:45:08.086678  1897 net.cpp:122] Setting up bn2b_branch2a
I0623 09:45:08.086694  1897 net.cpp:129] Top shape: 8 64 64 64 (2097152)
I0623 09:45:08.086704  1897 net.cpp:137] Memory required for data: 585105504
I0623 09:45:08.086716  1897 layer_factory.hpp:77] Creating layer scale2b_branch2a
I0623 09:45:08.086724  1897 net.cpp:84] Creating Layer scale2b_branch2a
I0623 09:45:08.086727  1897 net.cpp:406] scale2b_branch2a <- res2b_branch2a
I0623 09:45:08.086732  1897 net.cpp:367] scale2b_branch2a -> res2b_branch2a (in-place)
I0623 09:45:08.086742  1897 layer_factory.hpp:77] Creating layer scale2b_branch2a
I0623 09:45:08.086761  1897 net.cpp:122] Setting up scale2b_branch2a
I0623 09:45:08.086767  1897 net.cpp:129] Top shape: 8 64 64 64 (2097152)
I0623 09:45:08.086771  1897 net.cpp:137] Memory required for data: 593494112
I0623 09:45:08.086777  1897 layer_factory.hpp:77] Creating layer res2b_branch2a_relu
I0623 09:45:08.086783  1897 net.cpp:84] Creating Layer res2b_branch2a_relu
I0623 09:45:08.086787  1897 net.cpp:406] res2b_branch2a_relu <- res2b_branch2a
I0623 09:45:08.086792  1897 net.cpp:367] res2b_branch2a_relu -> res2b_branch2a (in-place)
I0623 09:45:08.086797  1897 net.cpp:122] Setting up res2b_branch2a_relu
I0623 09:45:08.086802  1897 net.cpp:129] Top shape: 8 64 64 64 (2097152)
I0623 09:45:08.086807  1897 net.cpp:137] Memory required for data: 601882720
I0623 09:45:08.086809  1897 layer_factory.hpp:77] Creating layer res2b_branch2b
I0623 09:45:08.086817  1897 net.cpp:84] Creating Layer res2b_branch2b
I0623 09:45:08.086820  1897 net.cpp:406] res2b_branch2b <- res2b_branch2a
I0623 09:45:08.086827  1897 net.cpp:380] res2b_branch2b -> res2b_branch2b
I0623 09:45:08.086874  1897 net.cpp:122] Setting up res2b_branch2b
I0623 09:45:08.086880  1897 net.cpp:129] Top shape: 8 64 64 64 (2097152)
I0623 09:45:08.086884  1897 net.cpp:137] Memory required for data: 610271328
I0623 09:45:08.086889  1897 layer_factory.hpp:77] Creating layer bn2b_branch2b
I0623 09:45:08.086896  1897 net.cpp:84] Creating Layer bn2b_branch2b
I0623 09:45:08.086899  1897 net.cpp:406] bn2b_branch2b <- res2b_branch2b
I0623 09:45:08.086905  1897 net.cpp:367] bn2b_branch2b -> res2b_branch2b (in-place)
I0623 09:45:08.086920  1897 net.cpp:122] Setting up bn2b_branch2b
I0623 09:45:08.086926  1897 net.cpp:129] Top shape: 8 64 64 64 (2097152)
I0623 09:45:08.086930  1897 net.cpp:137] Memory required for data: 618659936
I0623 09:45:08.086937  1897 layer_factory.hpp:77] Creating layer scale2b_branch2b
I0623 09:45:08.086944  1897 net.cpp:84] Creating Layer scale2b_branch2b
I0623 09:45:08.086947  1897 net.cpp:406] scale2b_branch2b <- res2b_branch2b
I0623 09:45:08.086952  1897 net.cpp:367] scale2b_branch2b -> res2b_branch2b (in-place)
I0623 09:45:08.086961  1897 layer_factory.hpp:77] Creating layer scale2b_branch2b
I0623 09:45:08.086979  1897 net.cpp:122] Setting up scale2b_branch2b
I0623 09:45:08.086984  1897 net.cpp:129] Top shape: 8 64 64 64 (2097152)
I0623 09:45:08.086988  1897 net.cpp:137] Memory required for data: 627048544
I0623 09:45:08.086994  1897 layer_factory.hpp:77] Creating layer res2b_branch2b_relu
I0623 09:45:08.087002  1897 net.cpp:84] Creating Layer res2b_branch2b_relu
I0623 09:45:08.087007  1897 net.cpp:406] res2b_branch2b_relu <- res2b_branch2b
I0623 09:45:08.087011  1897 net.cpp:367] res2b_branch2b_relu -> res2b_branch2b (in-place)
I0623 09:45:08.087016  1897 net.cpp:122] Setting up res2b_branch2b_relu
I0623 09:45:08.087021  1897 net.cpp:129] Top shape: 8 64 64 64 (2097152)
I0623 09:45:08.087025  1897 net.cpp:137] Memory required for data: 635437152
I0623 09:45:08.087029  1897 layer_factory.hpp:77] Creating layer res2b_branch2c
I0623 09:45:08.087035  1897 net.cpp:84] Creating Layer res2b_branch2c
I0623 09:45:08.087039  1897 net.cpp:406] res2b_branch2c <- res2b_branch2b
I0623 09:45:08.087045  1897 net.cpp:380] res2b_branch2c -> res2b_branch2c
I0623 09:45:08.087072  1897 net.cpp:122] Setting up res2b_branch2c
I0623 09:45:08.087079  1897 net.cpp:129] Top shape: 8 256 64 64 (8388608)
I0623 09:45:08.087082  1897 net.cpp:137] Memory required for data: 668991584
I0623 09:45:08.087087  1897 layer_factory.hpp:77] Creating layer bn2b_branch2c
I0623 09:45:08.087093  1897 net.cpp:84] Creating Layer bn2b_branch2c
I0623 09:45:08.087098  1897 net.cpp:406] bn2b_branch2c <- res2b_branch2c
I0623 09:45:08.087103  1897 net.cpp:367] bn2b_branch2c -> res2b_branch2c (in-place)
I0623 09:45:08.087118  1897 net.cpp:122] Setting up bn2b_branch2c
I0623 09:45:08.087123  1897 net.cpp:129] Top shape: 8 256 64 64 (8388608)
I0623 09:45:08.087127  1897 net.cpp:137] Memory required for data: 702546016
I0623 09:45:08.087134  1897 layer_factory.hpp:77] Creating layer scale2b_branch2c
I0623 09:45:08.087141  1897 net.cpp:84] Creating Layer scale2b_branch2c
I0623 09:45:08.087144  1897 net.cpp:406] scale2b_branch2c <- res2b_branch2c
I0623 09:45:08.087149  1897 net.cpp:367] scale2b_branch2c -> res2b_branch2c (in-place)
I0623 09:45:08.087157  1897 layer_factory.hpp:77] Creating layer scale2b_branch2c
I0623 09:45:08.087177  1897 net.cpp:122] Setting up scale2b_branch2c
I0623 09:45:08.087182  1897 net.cpp:129] Top shape: 8 256 64 64 (8388608)
I0623 09:45:08.087185  1897 net.cpp:137] Memory required for data: 736100448
I0623 09:45:08.087193  1897 layer_factory.hpp:77] Creating layer res2b
I0623 09:45:08.087198  1897 net.cpp:84] Creating Layer res2b
I0623 09:45:08.087201  1897 net.cpp:406] res2b <- res2a_res2a_relu_0_split_1
I0623 09:45:08.087206  1897 net.cpp:406] res2b <- res2b_branch2c
I0623 09:45:08.087211  1897 net.cpp:380] res2b -> res2b
I0623 09:45:08.087218  1897 net.cpp:122] Setting up res2b
I0623 09:45:08.087224  1897 net.cpp:129] Top shape: 8 256 64 64 (8388608)
I0623 09:45:08.087227  1897 net.cpp:137] Memory required for data: 769654880
I0623 09:45:08.087230  1897 layer_factory.hpp:77] Creating layer res2b_relu
I0623 09:45:08.087236  1897 net.cpp:84] Creating Layer res2b_relu
I0623 09:45:08.087240  1897 net.cpp:406] res2b_relu <- res2b
I0623 09:45:08.087245  1897 net.cpp:367] res2b_relu -> res2b (in-place)
I0623 09:45:08.087250  1897 net.cpp:122] Setting up res2b_relu
I0623 09:45:08.087255  1897 net.cpp:129] Top shape: 8 256 64 64 (8388608)
I0623 09:45:08.087260  1897 net.cpp:137] Memory required for data: 803209312
I0623 09:45:08.087263  1897 layer_factory.hpp:77] Creating layer res2b_res2b_relu_0_split
I0623 09:45:08.087268  1897 net.cpp:84] Creating Layer res2b_res2b_relu_0_split
I0623 09:45:08.087271  1897 net.cpp:406] res2b_res2b_relu_0_split <- res2b
I0623 09:45:08.087276  1897 net.cpp:380] res2b_res2b_relu_0_split -> res2b_res2b_relu_0_split_0
I0623 09:45:08.087283  1897 net.cpp:380] res2b_res2b_relu_0_split -> res2b_res2b_relu_0_split_1
I0623 09:45:08.087290  1897 net.cpp:122] Setting up res2b_res2b_relu_0_split
I0623 09:45:08.087294  1897 net.cpp:129] Top shape: 8 256 64 64 (8388608)
I0623 09:45:08.087299  1897 net.cpp:129] Top shape: 8 256 64 64 (8388608)
I0623 09:45:08.087303  1897 net.cpp:137] Memory required for data: 870318176
I0623 09:45:08.087306  1897 layer_factory.hpp:77] Creating layer res2c_branch2a
I0623 09:45:08.087313  1897 net.cpp:84] Creating Layer res2c_branch2a
I0623 09:45:08.087317  1897 net.cpp:406] res2c_branch2a <- res2b_res2b_relu_0_split_0
I0623 09:45:08.087322  1897 net.cpp:380] res2c_branch2a -> res2c_branch2a
I0623 09:45:08.087349  1897 net.cpp:122] Setting up res2c_branch2a
I0623 09:45:08.087357  1897 net.cpp:129] Top shape: 8 64 64 64 (2097152)
I0623 09:45:08.087359  1897 net.cpp:137] Memory required for data: 878706784
I0623 09:45:08.087364  1897 layer_factory.hpp:77] Creating layer bn2c_branch2a
I0623 09:45:08.087370  1897 net.cpp:84] Creating Layer bn2c_branch2a
I0623 09:45:08.087374  1897 net.cpp:406] bn2c_branch2a <- res2c_branch2a
I0623 09:45:08.087379  1897 net.cpp:367] bn2c_branch2a -> res2c_branch2a (in-place)
I0623 09:45:08.087394  1897 net.cpp:122] Setting up bn2c_branch2a
I0623 09:45:08.087400  1897 net.cpp:129] Top shape: 8 64 64 64 (2097152)
I0623 09:45:08.087404  1897 net.cpp:137] Memory required for data: 887095392
I0623 09:45:08.087411  1897 layer_factory.hpp:77] Creating layer scale2c_branch2a
I0623 09:45:08.087417  1897 net.cpp:84] Creating Layer scale2c_branch2a
I0623 09:45:08.087420  1897 net.cpp:406] scale2c_branch2a <- res2c_branch2a
I0623 09:45:08.087426  1897 net.cpp:367] scale2c_branch2a -> res2c_branch2a (in-place)
I0623 09:45:08.087435  1897 layer_factory.hpp:77] Creating layer scale2c_branch2a
I0623 09:45:08.087453  1897 net.cpp:122] Setting up scale2c_branch2a
I0623 09:45:08.087460  1897 net.cpp:129] Top shape: 8 64 64 64 (2097152)
I0623 09:45:08.087462  1897 net.cpp:137] Memory required for data: 895484000
I0623 09:45:08.087469  1897 layer_factory.hpp:77] Creating layer res2c_branch2a_relu
I0623 09:45:08.087476  1897 net.cpp:84] Creating Layer res2c_branch2a_relu
I0623 09:45:08.087478  1897 net.cpp:406] res2c_branch2a_relu <- res2c_branch2a
I0623 09:45:08.087483  1897 net.cpp:367] res2c_branch2a_relu -> res2c_branch2a (in-place)
I0623 09:45:08.087489  1897 net.cpp:122] Setting up res2c_branch2a_relu
I0623 09:45:08.087494  1897 net.cpp:129] Top shape: 8 64 64 64 (2097152)
I0623 09:45:08.087497  1897 net.cpp:137] Memory required for data: 903872608
I0623 09:45:08.087504  1897 layer_factory.hpp:77] Creating layer res2c_branch2b
I0623 09:45:08.087541  1897 net.cpp:84] Creating Layer res2c_branch2b
I0623 09:45:08.087546  1897 net.cpp:406] res2c_branch2b <- res2c_branch2a
I0623 09:45:08.087551  1897 net.cpp:380] res2c_branch2b -> res2c_branch2b
I0623 09:45:08.087599  1897 net.cpp:122] Setting up res2c_branch2b
I0623 09:45:08.087605  1897 net.cpp:129] Top shape: 8 64 64 64 (2097152)
I0623 09:45:08.087610  1897 net.cpp:137] Memory required for data: 912261216
I0623 09:45:08.087615  1897 layer_factory.hpp:77] Creating layer bn2c_branch2b
I0623 09:45:08.087621  1897 net.cpp:84] Creating Layer bn2c_branch2b
I0623 09:45:08.087625  1897 net.cpp:406] bn2c_branch2b <- res2c_branch2b
I0623 09:45:08.087630  1897 net.cpp:367] bn2c_branch2b -> res2c_branch2b (in-place)
I0623 09:45:08.087646  1897 net.cpp:122] Setting up bn2c_branch2b
I0623 09:45:08.087651  1897 net.cpp:129] Top shape: 8 64 64 64 (2097152)
I0623 09:45:08.087654  1897 net.cpp:137] Memory required for data: 920649824
I0623 09:45:08.087662  1897 layer_factory.hpp:77] Creating layer scale2c_branch2b
I0623 09:45:08.087668  1897 net.cpp:84] Creating Layer scale2c_branch2b
I0623 09:45:08.087672  1897 net.cpp:406] scale2c_branch2b <- res2c_branch2b
I0623 09:45:08.087677  1897 net.cpp:367] scale2c_branch2b -> res2c_branch2b (in-place)
I0623 09:45:08.087685  1897 layer_factory.hpp:77] Creating layer scale2c_branch2b
I0623 09:45:08.087703  1897 net.cpp:122] Setting up scale2c_branch2b
I0623 09:45:08.087708  1897 net.cpp:129] Top shape: 8 64 64 64 (2097152)
I0623 09:45:08.087713  1897 net.cpp:137] Memory required for data: 929038432
I0623 09:45:08.087718  1897 layer_factory.hpp:77] Creating layer res2c_branch2b_relu
I0623 09:45:08.087723  1897 net.cpp:84] Creating Layer res2c_branch2b_relu
I0623 09:45:08.087728  1897 net.cpp:406] res2c_branch2b_relu <- res2c_branch2b
I0623 09:45:08.087733  1897 net.cpp:367] res2c_branch2b_relu -> res2c_branch2b (in-place)
I0623 09:45:08.087738  1897 net.cpp:122] Setting up res2c_branch2b_relu
I0623 09:45:08.087743  1897 net.cpp:129] Top shape: 8 64 64 64 (2097152)
I0623 09:45:08.087746  1897 net.cpp:137] Memory required for data: 937427040
I0623 09:45:08.087750  1897 layer_factory.hpp:77] Creating layer res2c_branch2c
I0623 09:45:08.087756  1897 net.cpp:84] Creating Layer res2c_branch2c
I0623 09:45:08.087760  1897 net.cpp:406] res2c_branch2c <- res2c_branch2b
I0623 09:45:08.087765  1897 net.cpp:380] res2c_branch2c -> res2c_branch2c
I0623 09:45:08.087795  1897 net.cpp:122] Setting up res2c_branch2c
I0623 09:45:08.087800  1897 net.cpp:129] Top shape: 8 256 64 64 (8388608)
I0623 09:45:08.087805  1897 net.cpp:137] Memory required for data: 970981472
I0623 09:45:08.087808  1897 layer_factory.hpp:77] Creating layer bn2c_branch2c
I0623 09:45:08.087815  1897 net.cpp:84] Creating Layer bn2c_branch2c
I0623 09:45:08.087818  1897 net.cpp:406] bn2c_branch2c <- res2c_branch2c
I0623 09:45:08.087823  1897 net.cpp:367] bn2c_branch2c -> res2c_branch2c (in-place)
I0623 09:45:08.087839  1897 net.cpp:122] Setting up bn2c_branch2c
I0623 09:45:08.087846  1897 net.cpp:129] Top shape: 8 256 64 64 (8388608)
I0623 09:45:08.087849  1897 net.cpp:137] Memory required for data: 1004535904
I0623 09:45:08.087863  1897 layer_factory.hpp:77] Creating layer scale2c_branch2c
I0623 09:45:08.087869  1897 net.cpp:84] Creating Layer scale2c_branch2c
I0623 09:45:08.087873  1897 net.cpp:406] scale2c_branch2c <- res2c_branch2c
I0623 09:45:08.087878  1897 net.cpp:367] scale2c_branch2c -> res2c_branch2c (in-place)
I0623 09:45:08.087887  1897 layer_factory.hpp:77] Creating layer scale2c_branch2c
I0623 09:45:08.087905  1897 net.cpp:122] Setting up scale2c_branch2c
I0623 09:45:08.087911  1897 net.cpp:129] Top shape: 8 256 64 64 (8388608)
I0623 09:45:08.087914  1897 net.cpp:137] Memory required for data: 1038090336
I0623 09:45:08.087921  1897 layer_factory.hpp:77] Creating layer res2c
I0623 09:45:08.087927  1897 net.cpp:84] Creating Layer res2c
I0623 09:45:08.087931  1897 net.cpp:406] res2c <- res2b_res2b_relu_0_split_1
I0623 09:45:08.087935  1897 net.cpp:406] res2c <- res2c_branch2c
I0623 09:45:08.087941  1897 net.cpp:380] res2c -> res2c
I0623 09:45:08.087947  1897 net.cpp:122] Setting up res2c
I0623 09:45:08.087952  1897 net.cpp:129] Top shape: 8 256 64 64 (8388608)
I0623 09:45:08.087956  1897 net.cpp:137] Memory required for data: 1071644768
I0623 09:45:08.087960  1897 layer_factory.hpp:77] Creating layer res2c_relu
I0623 09:45:08.087965  1897 net.cpp:84] Creating Layer res2c_relu
I0623 09:45:08.087970  1897 net.cpp:406] res2c_relu <- res2c
I0623 09:45:08.087975  1897 net.cpp:367] res2c_relu -> res2c (in-place)
I0623 09:45:08.087980  1897 net.cpp:122] Setting up res2c_relu
I0623 09:45:08.087985  1897 net.cpp:129] Top shape: 8 256 64 64 (8388608)
I0623 09:45:08.087987  1897 net.cpp:137] Memory required for data: 1105199200
I0623 09:45:08.087991  1897 layer_factory.hpp:77] Creating layer res2c_res2c_relu_0_split
I0623 09:45:08.087997  1897 net.cpp:84] Creating Layer res2c_res2c_relu_0_split
I0623 09:45:08.088001  1897 net.cpp:406] res2c_res2c_relu_0_split <- res2c
I0623 09:45:08.088006  1897 net.cpp:380] res2c_res2c_relu_0_split -> res2c_res2c_relu_0_split_0
I0623 09:45:08.088011  1897 net.cpp:380] res2c_res2c_relu_0_split -> res2c_res2c_relu_0_split_1
I0623 09:45:08.088018  1897 net.cpp:122] Setting up res2c_res2c_relu_0_split
I0623 09:45:08.088023  1897 net.cpp:129] Top shape: 8 256 64 64 (8388608)
I0623 09:45:08.088028  1897 net.cpp:129] Top shape: 8 256 64 64 (8388608)
I0623 09:45:08.088032  1897 net.cpp:137] Memory required for data: 1172308064
I0623 09:45:08.088035  1897 layer_factory.hpp:77] Creating layer res3a_branch1
I0623 09:45:08.088042  1897 net.cpp:84] Creating Layer res3a_branch1
I0623 09:45:08.088047  1897 net.cpp:406] res3a_branch1 <- res2c_res2c_relu_0_split_0
I0623 09:45:08.088052  1897 net.cpp:380] res3a_branch1 -> res3a_branch1
I0623 09:45:08.088177  1897 net.cpp:122] Setting up res3a_branch1
I0623 09:45:08.088186  1897 net.cpp:129] Top shape: 8 512 32 32 (4194304)
I0623 09:45:08.088189  1897 net.cpp:137] Memory required for data: 1189085280
I0623 09:45:08.088194  1897 layer_factory.hpp:77] Creating layer bn3a_branch1
I0623 09:45:08.088201  1897 net.cpp:84] Creating Layer bn3a_branch1
I0623 09:45:08.088204  1897 net.cpp:406] bn3a_branch1 <- res3a_branch1
I0623 09:45:08.088209  1897 net.cpp:367] bn3a_branch1 -> res3a_branch1 (in-place)
I0623 09:45:08.088224  1897 net.cpp:122] Setting up bn3a_branch1
I0623 09:45:08.088229  1897 net.cpp:129] Top shape: 8 512 32 32 (4194304)
I0623 09:45:08.088233  1897 net.cpp:137] Memory required for data: 1205862496
I0623 09:45:08.088240  1897 layer_factory.hpp:77] Creating layer scale3a_branch1
I0623 09:45:08.088246  1897 net.cpp:84] Creating Layer scale3a_branch1
I0623 09:45:08.088250  1897 net.cpp:406] scale3a_branch1 <- res3a_branch1
I0623 09:45:08.088255  1897 net.cpp:367] scale3a_branch1 -> res3a_branch1 (in-place)
I0623 09:45:08.088264  1897 layer_factory.hpp:77] Creating layer scale3a_branch1
I0623 09:45:08.088279  1897 net.cpp:122] Setting up scale3a_branch1
I0623 09:45:08.088284  1897 net.cpp:129] Top shape: 8 512 32 32 (4194304)
I0623 09:45:08.088289  1897 net.cpp:137] Memory required for data: 1222639712
I0623 09:45:08.088294  1897 layer_factory.hpp:77] Creating layer res3a_branch2a
I0623 09:45:08.088301  1897 net.cpp:84] Creating Layer res3a_branch2a
I0623 09:45:08.088305  1897 net.cpp:406] res3a_branch2a <- res2c_res2c_relu_0_split_1
I0623 09:45:08.088311  1897 net.cpp:380] res3a_branch2a -> res3a_branch2a
I0623 09:45:08.088353  1897 net.cpp:122] Setting up res3a_branch2a
I0623 09:45:08.088361  1897 net.cpp:129] Top shape: 8 128 32 32 (1048576)
I0623 09:45:08.088364  1897 net.cpp:137] Memory required for data: 1226834016
I0623 09:45:08.088369  1897 layer_factory.hpp:77] Creating layer bn3a_branch2a
I0623 09:45:08.088376  1897 net.cpp:84] Creating Layer bn3a_branch2a
I0623 09:45:08.088379  1897 net.cpp:406] bn3a_branch2a <- res3a_branch2a
I0623 09:45:08.088385  1897 net.cpp:367] bn3a_branch2a -> res3a_branch2a (in-place)
I0623 09:45:08.088397  1897 net.cpp:122] Setting up bn3a_branch2a
I0623 09:45:08.088402  1897 net.cpp:129] Top shape: 8 128 32 32 (1048576)
I0623 09:45:08.088407  1897 net.cpp:137] Memory required for data: 1231028320
I0623 09:45:08.088413  1897 layer_factory.hpp:77] Creating layer scale3a_branch2a
I0623 09:45:08.088419  1897 net.cpp:84] Creating Layer scale3a_branch2a
I0623 09:45:08.088423  1897 net.cpp:406] scale3a_branch2a <- res3a_branch2a
I0623 09:45:08.088428  1897 net.cpp:367] scale3a_branch2a -> res3a_branch2a (in-place)
I0623 09:45:08.088436  1897 layer_factory.hpp:77] Creating layer scale3a_branch2a
I0623 09:45:08.088449  1897 net.cpp:122] Setting up scale3a_branch2a
I0623 09:45:08.088455  1897 net.cpp:129] Top shape: 8 128 32 32 (1048576)
I0623 09:45:08.088459  1897 net.cpp:137] Memory required for data: 1235222624
I0623 09:45:08.088464  1897 layer_factory.hpp:77] Creating layer res3a_branch2a_relu
I0623 09:45:08.088469  1897 net.cpp:84] Creating Layer res3a_branch2a_relu
I0623 09:45:08.088474  1897 net.cpp:406] res3a_branch2a_relu <- res3a_branch2a
I0623 09:45:08.088479  1897 net.cpp:367] res3a_branch2a_relu -> res3a_branch2a (in-place)
I0623 09:45:08.088485  1897 net.cpp:122] Setting up res3a_branch2a_relu
I0623 09:45:08.088490  1897 net.cpp:129] Top shape: 8 128 32 32 (1048576)
I0623 09:45:08.088492  1897 net.cpp:137] Memory required for data: 1239416928
I0623 09:45:08.088496  1897 layer_factory.hpp:77] Creating layer res3a_branch2b
I0623 09:45:08.088503  1897 net.cpp:84] Creating Layer res3a_branch2b
I0623 09:45:08.088507  1897 net.cpp:406] res3a_branch2b <- res3a_branch2a
I0623 09:45:08.088512  1897 net.cpp:380] res3a_branch2b -> res3a_branch2b
I0623 09:45:08.088654  1897 net.cpp:122] Setting up res3a_branch2b
I0623 09:45:08.088661  1897 net.cpp:129] Top shape: 8 128 32 32 (1048576)
I0623 09:45:08.088665  1897 net.cpp:137] Memory required for data: 1243611232
I0623 09:45:08.088670  1897 layer_factory.hpp:77] Creating layer bn3a_branch2b
I0623 09:45:08.088677  1897 net.cpp:84] Creating Layer bn3a_branch2b
I0623 09:45:08.088681  1897 net.cpp:406] bn3a_branch2b <- res3a_branch2b
I0623 09:45:08.088686  1897 net.cpp:367] bn3a_branch2b -> res3a_branch2b (in-place)
I0623 09:45:08.088698  1897 net.cpp:122] Setting up bn3a_branch2b
I0623 09:45:08.088703  1897 net.cpp:129] Top shape: 8 128 32 32 (1048576)
I0623 09:45:08.088707  1897 net.cpp:137] Memory required for data: 1247805536
I0623 09:45:08.088714  1897 layer_factory.hpp:77] Creating layer scale3a_branch2b
I0623 09:45:08.088721  1897 net.cpp:84] Creating Layer scale3a_branch2b
I0623 09:45:08.088723  1897 net.cpp:406] scale3a_branch2b <- res3a_branch2b
I0623 09:45:08.088728  1897 net.cpp:367] scale3a_branch2b -> res3a_branch2b (in-place)
I0623 09:45:08.088737  1897 layer_factory.hpp:77] Creating layer scale3a_branch2b
I0623 09:45:08.088750  1897 net.cpp:122] Setting up scale3a_branch2b
I0623 09:45:08.088755  1897 net.cpp:129] Top shape: 8 128 32 32 (1048576)
I0623 09:45:08.088759  1897 net.cpp:137] Memory required for data: 1251999840
I0623 09:45:08.088766  1897 layer_factory.hpp:77] Creating layer res3a_branch2b_relu
I0623 09:45:08.088771  1897 net.cpp:84] Creating Layer res3a_branch2b_relu
I0623 09:45:08.088775  1897 net.cpp:406] res3a_branch2b_relu <- res3a_branch2b
I0623 09:45:08.088780  1897 net.cpp:367] res3a_branch2b_relu -> res3a_branch2b (in-place)
I0623 09:45:08.088786  1897 net.cpp:122] Setting up res3a_branch2b_relu
I0623 09:45:08.088791  1897 net.cpp:129] Top shape: 8 128 32 32 (1048576)
I0623 09:45:08.088795  1897 net.cpp:137] Memory required for data: 1256194144
I0623 09:45:08.088798  1897 layer_factory.hpp:77] Creating layer res3a_branch2c
I0623 09:45:08.088809  1897 net.cpp:84] Creating Layer res3a_branch2c
I0623 09:45:08.088814  1897 net.cpp:406] res3a_branch2c <- res3a_branch2b
I0623 09:45:08.088819  1897 net.cpp:380] res3a_branch2c -> res3a_branch2c
I0623 09:45:08.088891  1897 net.cpp:122] Setting up res3a_branch2c
I0623 09:45:08.088899  1897 net.cpp:129] Top shape: 8 512 32 32 (4194304)
I0623 09:45:08.088903  1897 net.cpp:137] Memory required for data: 1272971360
I0623 09:45:08.088909  1897 layer_factory.hpp:77] Creating layer bn3a_branch2c
I0623 09:45:08.088915  1897 net.cpp:84] Creating Layer bn3a_branch2c
I0623 09:45:08.088919  1897 net.cpp:406] bn3a_branch2c <- res3a_branch2c
I0623 09:45:08.088924  1897 net.cpp:367] bn3a_branch2c -> res3a_branch2c (in-place)
I0623 09:45:08.088937  1897 net.cpp:122] Setting up bn3a_branch2c
I0623 09:45:08.088943  1897 net.cpp:129] Top shape: 8 512 32 32 (4194304)
I0623 09:45:08.088946  1897 net.cpp:137] Memory required for data: 1289748576
I0623 09:45:08.088954  1897 layer_factory.hpp:77] Creating layer scale3a_branch2c
I0623 09:45:08.088959  1897 net.cpp:84] Creating Layer scale3a_branch2c
I0623 09:45:08.088963  1897 net.cpp:406] scale3a_branch2c <- res3a_branch2c
I0623 09:45:08.088968  1897 net.cpp:367] scale3a_branch2c -> res3a_branch2c (in-place)
I0623 09:45:08.088976  1897 layer_factory.hpp:77] Creating layer scale3a_branch2c
I0623 09:45:08.088990  1897 net.cpp:122] Setting up scale3a_branch2c
I0623 09:45:08.088995  1897 net.cpp:129] Top shape: 8 512 32 32 (4194304)
I0623 09:45:08.088999  1897 net.cpp:137] Memory required for data: 1306525792
I0623 09:45:08.089005  1897 layer_factory.hpp:77] Creating layer res3a
I0623 09:45:08.089011  1897 net.cpp:84] Creating Layer res3a
I0623 09:45:08.089015  1897 net.cpp:406] res3a <- res3a_branch1
I0623 09:45:08.089020  1897 net.cpp:406] res3a <- res3a_branch2c
I0623 09:45:08.089025  1897 net.cpp:380] res3a -> res3a
I0623 09:45:08.089031  1897 net.cpp:122] Setting up res3a
I0623 09:45:08.089036  1897 net.cpp:129] Top shape: 8 512 32 32 (4194304)
I0623 09:45:08.089040  1897 net.cpp:137] Memory required for data: 1323303008
I0623 09:45:08.089043  1897 layer_factory.hpp:77] Creating layer res3a_relu
I0623 09:45:08.089048  1897 net.cpp:84] Creating Layer res3a_relu
I0623 09:45:08.089052  1897 net.cpp:406] res3a_relu <- res3a
I0623 09:45:08.089057  1897 net.cpp:367] res3a_relu -> res3a (in-place)
I0623 09:45:08.089062  1897 net.cpp:122] Setting up res3a_relu
I0623 09:45:08.089067  1897 net.cpp:129] Top shape: 8 512 32 32 (4194304)
I0623 09:45:08.089071  1897 net.cpp:137] Memory required for data: 1340080224
I0623 09:45:08.089074  1897 layer_factory.hpp:77] Creating layer res3a_res3a_relu_0_split
I0623 09:45:08.089079  1897 net.cpp:84] Creating Layer res3a_res3a_relu_0_split
I0623 09:45:08.089083  1897 net.cpp:406] res3a_res3a_relu_0_split <- res3a
I0623 09:45:08.089088  1897 net.cpp:380] res3a_res3a_relu_0_split -> res3a_res3a_relu_0_split_0
I0623 09:45:08.089097  1897 net.cpp:380] res3a_res3a_relu_0_split -> res3a_res3a_relu_0_split_1
I0623 09:45:08.089103  1897 net.cpp:122] Setting up res3a_res3a_relu_0_split
I0623 09:45:08.089108  1897 net.cpp:129] Top shape: 8 512 32 32 (4194304)
I0623 09:45:08.089113  1897 net.cpp:129] Top shape: 8 512 32 32 (4194304)
I0623 09:45:08.089118  1897 net.cpp:137] Memory required for data: 1373634656
I0623 09:45:08.089120  1897 layer_factory.hpp:77] Creating layer res3b_branch2a
I0623 09:45:08.089128  1897 net.cpp:84] Creating Layer res3b_branch2a
I0623 09:45:08.089133  1897 net.cpp:406] res3b_branch2a <- res3a_res3a_relu_0_split_0
I0623 09:45:08.089138  1897 net.cpp:380] res3b_branch2a -> res3b_branch2a
I0623 09:45:08.089207  1897 net.cpp:122] Setting up res3b_branch2a
I0623 09:45:08.089215  1897 net.cpp:129] Top shape: 8 128 32 32 (1048576)
I0623 09:45:08.089220  1897 net.cpp:137] Memory required for data: 1377828960
I0623 09:45:08.089224  1897 layer_factory.hpp:77] Creating layer bn3b_branch2a
I0623 09:45:08.089231  1897 net.cpp:84] Creating Layer bn3b_branch2a
I0623 09:45:08.089234  1897 net.cpp:406] bn3b_branch2a <- res3b_branch2a
I0623 09:45:08.089239  1897 net.cpp:367] bn3b_branch2a -> res3b_branch2a (in-place)
I0623 09:45:08.089252  1897 net.cpp:122] Setting up bn3b_branch2a
I0623 09:45:08.089257  1897 net.cpp:129] Top shape: 8 128 32 32 (1048576)
I0623 09:45:08.089262  1897 net.cpp:137] Memory required for data: 1382023264
I0623 09:45:08.089268  1897 layer_factory.hpp:77] Creating layer scale3b_branch2a
I0623 09:45:08.089274  1897 net.cpp:84] Creating Layer scale3b_branch2a
I0623 09:45:08.089278  1897 net.cpp:406] scale3b_branch2a <- res3b_branch2a
I0623 09:45:08.089283  1897 net.cpp:367] scale3b_branch2a -> res3b_branch2a (in-place)
I0623 09:45:08.089292  1897 layer_factory.hpp:77] Creating layer scale3b_branch2a
I0623 09:45:08.089304  1897 net.cpp:122] Setting up scale3b_branch2a
I0623 09:45:08.089309  1897 net.cpp:129] Top shape: 8 128 32 32 (1048576)
I0623 09:45:08.089313  1897 net.cpp:137] Memory required for data: 1386217568
I0623 09:45:08.089319  1897 layer_factory.hpp:77] Creating layer res3b_branch2a_relu
I0623 09:45:08.089324  1897 net.cpp:84] Creating Layer res3b_branch2a_relu
I0623 09:45:08.089329  1897 net.cpp:406] res3b_branch2a_relu <- res3b_branch2a
I0623 09:45:08.089334  1897 net.cpp:367] res3b_branch2a_relu -> res3b_branch2a (in-place)
I0623 09:45:08.089339  1897 net.cpp:122] Setting up res3b_branch2a_relu
I0623 09:45:08.089344  1897 net.cpp:129] Top shape: 8 128 32 32 (1048576)
I0623 09:45:08.089347  1897 net.cpp:137] Memory required for data: 1390411872
I0623 09:45:08.089351  1897 layer_factory.hpp:77] Creating layer res3b_branch2b
I0623 09:45:08.089359  1897 net.cpp:84] Creating Layer res3b_branch2b
I0623 09:45:08.089362  1897 net.cpp:406] res3b_branch2b <- res3b_branch2a
I0623 09:45:08.089367  1897 net.cpp:380] res3b_branch2b -> res3b_branch2b
I0623 09:45:08.089509  1897 net.cpp:122] Setting up res3b_branch2b
I0623 09:45:08.089517  1897 net.cpp:129] Top shape: 8 128 32 32 (1048576)
I0623 09:45:08.089520  1897 net.cpp:137] Memory required for data: 1394606176
I0623 09:45:08.089525  1897 layer_factory.hpp:77] Creating layer bn3b_branch2b
I0623 09:45:08.089532  1897 net.cpp:84] Creating Layer bn3b_branch2b
I0623 09:45:08.089535  1897 net.cpp:406] bn3b_branch2b <- res3b_branch2b
I0623 09:45:08.089541  1897 net.cpp:367] bn3b_branch2b -> res3b_branch2b (in-place)
I0623 09:45:08.089553  1897 net.cpp:122] Setting up bn3b_branch2b
I0623 09:45:08.089558  1897 net.cpp:129] Top shape: 8 128 32 32 (1048576)
I0623 09:45:08.089561  1897 net.cpp:137] Memory required for data: 1398800480
I0623 09:45:08.089570  1897 layer_factory.hpp:77] Creating layer scale3b_branch2b
I0623 09:45:08.089576  1897 net.cpp:84] Creating Layer scale3b_branch2b
I0623 09:45:08.089578  1897 net.cpp:406] scale3b_branch2b <- res3b_branch2b
I0623 09:45:08.089583  1897 net.cpp:367] scale3b_branch2b -> res3b_branch2b (in-place)
I0623 09:45:08.089591  1897 layer_factory.hpp:77] Creating layer scale3b_branch2b
I0623 09:45:08.089606  1897 net.cpp:122] Setting up scale3b_branch2b
I0623 09:45:08.089610  1897 net.cpp:129] Top shape: 8 128 32 32 (1048576)
I0623 09:45:08.089614  1897 net.cpp:137] Memory required for data: 1402994784
I0623 09:45:08.089620  1897 layer_factory.hpp:77] Creating layer res3b_branch2b_relu
I0623 09:45:08.089625  1897 net.cpp:84] Creating Layer res3b_branch2b_relu
I0623 09:45:08.089629  1897 net.cpp:406] res3b_branch2b_relu <- res3b_branch2b
I0623 09:45:08.089634  1897 net.cpp:367] res3b_branch2b_relu -> res3b_branch2b (in-place)
I0623 09:45:08.089640  1897 net.cpp:122] Setting up res3b_branch2b_relu
I0623 09:45:08.089645  1897 net.cpp:129] Top shape: 8 128 32 32 (1048576)
I0623 09:45:08.089649  1897 net.cpp:137] Memory required for data: 1407189088
I0623 09:45:08.089653  1897 layer_factory.hpp:77] Creating layer res3b_branch2c
I0623 09:45:08.089659  1897 net.cpp:84] Creating Layer res3b_branch2c
I0623 09:45:08.089663  1897 net.cpp:406] res3b_branch2c <- res3b_branch2b
I0623 09:45:08.089668  1897 net.cpp:380] res3b_branch2c -> res3b_branch2c
I0623 09:45:08.089738  1897 net.cpp:122] Setting up res3b_branch2c
I0623 09:45:08.089746  1897 net.cpp:129] Top shape: 8 512 32 32 (4194304)
I0623 09:45:08.089751  1897 net.cpp:137] Memory required for data: 1423966304
I0623 09:45:08.089756  1897 layer_factory.hpp:77] Creating layer bn3b_branch2c
I0623 09:45:08.089761  1897 net.cpp:84] Creating Layer bn3b_branch2c
I0623 09:45:08.089766  1897 net.cpp:406] bn3b_branch2c <- res3b_branch2c
I0623 09:45:08.089771  1897 net.cpp:367] bn3b_branch2c -> res3b_branch2c (in-place)
I0623 09:45:08.089783  1897 net.cpp:122] Setting up bn3b_branch2c
I0623 09:45:08.089789  1897 net.cpp:129] Top shape: 8 512 32 32 (4194304)
I0623 09:45:08.089792  1897 net.cpp:137] Memory required for data: 1440743520
I0623 09:45:08.089800  1897 layer_factory.hpp:77] Creating layer scale3b_branch2c
I0623 09:45:08.089805  1897 net.cpp:84] Creating Layer scale3b_branch2c
I0623 09:45:08.089809  1897 net.cpp:406] scale3b_branch2c <- res3b_branch2c
I0623 09:45:08.089814  1897 net.cpp:367] scale3b_branch2c -> res3b_branch2c (in-place)
I0623 09:45:08.089823  1897 layer_factory.hpp:77] Creating layer scale3b_branch2c
I0623 09:45:08.089836  1897 net.cpp:122] Setting up scale3b_branch2c
I0623 09:45:08.089843  1897 net.cpp:129] Top shape: 8 512 32 32 (4194304)
I0623 09:45:08.089845  1897 net.cpp:137] Memory required for data: 1457520736
I0623 09:45:08.089853  1897 layer_factory.hpp:77] Creating layer res3b
I0623 09:45:08.089857  1897 net.cpp:84] Creating Layer res3b
I0623 09:45:08.089861  1897 net.cpp:406] res3b <- res3a_res3a_relu_0_split_1
I0623 09:45:08.089866  1897 net.cpp:406] res3b <- res3b_branch2c
I0623 09:45:08.089871  1897 net.cpp:380] res3b -> res3b
I0623 09:45:08.089877  1897 net.cpp:122] Setting up res3b
I0623 09:45:08.089884  1897 net.cpp:129] Top shape: 8 512 32 32 (4194304)
I0623 09:45:08.089886  1897 net.cpp:137] Memory required for data: 1474297952
I0623 09:45:08.089890  1897 layer_factory.hpp:77] Creating layer res3b_relu
I0623 09:45:08.089895  1897 net.cpp:84] Creating Layer res3b_relu
I0623 09:45:08.089900  1897 net.cpp:406] res3b_relu <- res3b
I0623 09:45:08.089905  1897 net.cpp:367] res3b_relu -> res3b (in-place)
I0623 09:45:08.089910  1897 net.cpp:122] Setting up res3b_relu
I0623 09:45:08.089915  1897 net.cpp:129] Top shape: 8 512 32 32 (4194304)
I0623 09:45:08.089918  1897 net.cpp:137] Memory required for data: 1491075168
I0623 09:45:08.089921  1897 layer_factory.hpp:77] Creating layer res3b_res3b_relu_0_split
I0623 09:45:08.089926  1897 net.cpp:84] Creating Layer res3b_res3b_relu_0_split
I0623 09:45:08.089931  1897 net.cpp:406] res3b_res3b_relu_0_split <- res3b
I0623 09:45:08.089936  1897 net.cpp:380] res3b_res3b_relu_0_split -> res3b_res3b_relu_0_split_0
I0623 09:45:08.089941  1897 net.cpp:380] res3b_res3b_relu_0_split -> res3b_res3b_relu_0_split_1
I0623 09:45:08.089948  1897 net.cpp:122] Setting up res3b_res3b_relu_0_split
I0623 09:45:08.089953  1897 net.cpp:129] Top shape: 8 512 32 32 (4194304)
I0623 09:45:08.089958  1897 net.cpp:129] Top shape: 8 512 32 32 (4194304)
I0623 09:45:08.089962  1897 net.cpp:137] Memory required for data: 1524629600
I0623 09:45:08.089965  1897 layer_factory.hpp:77] Creating layer res3c_branch2a
I0623 09:45:08.089972  1897 net.cpp:84] Creating Layer res3c_branch2a
I0623 09:45:08.089977  1897 net.cpp:406] res3c_branch2a <- res3b_res3b_relu_0_split_0
I0623 09:45:08.089982  1897 net.cpp:380] res3c_branch2a -> res3c_branch2a
I0623 09:45:08.090052  1897 net.cpp:122] Setting up res3c_branch2a
I0623 09:45:08.090060  1897 net.cpp:129] Top shape: 8 128 32 32 (1048576)
I0623 09:45:08.090065  1897 net.cpp:137] Memory required for data: 1528823904
I0623 09:45:08.090070  1897 layer_factory.hpp:77] Creating layer bn3c_branch2a
I0623 09:45:08.090075  1897 net.cpp:84] Creating Layer bn3c_branch2a
I0623 09:45:08.090080  1897 net.cpp:406] bn3c_branch2a <- res3c_branch2a
I0623 09:45:08.090085  1897 net.cpp:367] bn3c_branch2a -> res3c_branch2a (in-place)
I0623 09:45:08.090097  1897 net.cpp:122] Setting up bn3c_branch2a
I0623 09:45:08.090103  1897 net.cpp:129] Top shape: 8 128 32 32 (1048576)
I0623 09:45:08.090106  1897 net.cpp:137] Memory required for data: 1533018208
I0623 09:45:08.090114  1897 layer_factory.hpp:77] Creating layer scale3c_branch2a
I0623 09:45:08.090121  1897 net.cpp:84] Creating Layer scale3c_branch2a
I0623 09:45:08.090124  1897 net.cpp:406] scale3c_branch2a <- res3c_branch2a
I0623 09:45:08.090129  1897 net.cpp:367] scale3c_branch2a -> res3c_branch2a (in-place)
I0623 09:45:08.090137  1897 layer_factory.hpp:77] Creating layer scale3c_branch2a
I0623 09:45:08.090150  1897 net.cpp:122] Setting up scale3c_branch2a
I0623 09:45:08.090157  1897 net.cpp:129] Top shape: 8 128 32 32 (1048576)
I0623 09:45:08.090160  1897 net.cpp:137] Memory required for data: 1537212512
I0623 09:45:08.090167  1897 layer_factory.hpp:77] Creating layer res3c_branch2a_relu
I0623 09:45:08.090171  1897 net.cpp:84] Creating Layer res3c_branch2a_relu
I0623 09:45:08.090175  1897 net.cpp:406] res3c_branch2a_relu <- res3c_branch2a
I0623 09:45:08.090180  1897 net.cpp:367] res3c_branch2a_relu -> res3c_branch2a (in-place)
I0623 09:45:08.090185  1897 net.cpp:122] Setting up res3c_branch2a_relu
I0623 09:45:08.090190  1897 net.cpp:129] Top shape: 8 128 32 32 (1048576)
I0623 09:45:08.090194  1897 net.cpp:137] Memory required for data: 1541406816
I0623 09:45:08.090198  1897 layer_factory.hpp:77] Creating layer res3c_branch2b
I0623 09:45:08.090205  1897 net.cpp:84] Creating Layer res3c_branch2b
I0623 09:45:08.090209  1897 net.cpp:406] res3c_branch2b <- res3c_branch2a
I0623 09:45:08.090214  1897 net.cpp:380] res3c_branch2b -> res3c_branch2b
I0623 09:45:08.090358  1897 net.cpp:122] Setting up res3c_branch2b
I0623 09:45:08.090365  1897 net.cpp:129] Top shape: 8 128 32 32 (1048576)
I0623 09:45:08.090368  1897 net.cpp:137] Memory required for data: 1545601120
I0623 09:45:08.090374  1897 layer_factory.hpp:77] Creating layer bn3c_branch2b
I0623 09:45:08.090379  1897 net.cpp:84] Creating Layer bn3c_branch2b
I0623 09:45:08.090384  1897 net.cpp:406] bn3c_branch2b <- res3c_branch2b
I0623 09:45:08.090389  1897 net.cpp:367] bn3c_branch2b -> res3c_branch2b (in-place)
I0623 09:45:08.090401  1897 net.cpp:122] Setting up bn3c_branch2b
I0623 09:45:08.090407  1897 net.cpp:129] Top shape: 8 128 32 32 (1048576)
I0623 09:45:08.090410  1897 net.cpp:137] Memory required for data: 1549795424
I0623 09:45:08.090417  1897 layer_factory.hpp:77] Creating layer scale3c_branch2b
I0623 09:45:08.090423  1897 net.cpp:84] Creating Layer scale3c_branch2b
I0623 09:45:08.090427  1897 net.cpp:406] scale3c_branch2b <- res3c_branch2b
I0623 09:45:08.090431  1897 net.cpp:367] scale3c_branch2b -> res3c_branch2b (in-place)
I0623 09:45:08.090440  1897 layer_factory.hpp:77] Creating layer scale3c_branch2b
I0623 09:45:08.090452  1897 net.cpp:122] Setting up scale3c_branch2b
I0623 09:45:08.090457  1897 net.cpp:129] Top shape: 8 128 32 32 (1048576)
I0623 09:45:08.090461  1897 net.cpp:137] Memory required for data: 1553989728
I0623 09:45:08.090467  1897 layer_factory.hpp:77] Creating layer res3c_branch2b_relu
I0623 09:45:08.090472  1897 net.cpp:84] Creating Layer res3c_branch2b_relu
I0623 09:45:08.090476  1897 net.cpp:406] res3c_branch2b_relu <- res3c_branch2b
I0623 09:45:08.090481  1897 net.cpp:367] res3c_branch2b_relu -> res3c_branch2b (in-place)
I0623 09:45:08.090487  1897 net.cpp:122] Setting up res3c_branch2b_relu
I0623 09:45:08.090492  1897 net.cpp:129] Top shape: 8 128 32 32 (1048576)
I0623 09:45:08.090498  1897 net.cpp:137] Memory required for data: 1558184032
I0623 09:45:08.090508  1897 layer_factory.hpp:77] Creating layer res3c_branch2c
I0623 09:45:08.090515  1897 net.cpp:84] Creating Layer res3c_branch2c
I0623 09:45:08.092108  1897 net.cpp:406] res3c_branch2c <- res3c_branch2b
I0623 09:45:08.092128  1897 net.cpp:380] res3c_branch2c -> res3c_branch2c
I0623 09:45:08.092216  1897 net.cpp:122] Setting up res3c_branch2c
I0623 09:45:08.092241  1897 net.cpp:129] Top shape: 8 512 32 32 (4194304)
I0623 09:45:08.092257  1897 net.cpp:137] Memory required for data: 1574961248
I0623 09:45:08.092273  1897 layer_factory.hpp:77] Creating layer bn3c_branch2c
I0623 09:45:08.092293  1897 net.cpp:84] Creating Layer bn3c_branch2c
I0623 09:45:08.092308  1897 net.cpp:406] bn3c_branch2c <- res3c_branch2c
I0623 09:45:08.092326  1897 net.cpp:367] bn3c_branch2c -> res3c_branch2c (in-place)
I0623 09:45:08.092353  1897 net.cpp:122] Setting up bn3c_branch2c
I0623 09:45:08.092371  1897 net.cpp:129] Top shape: 8 512 32 32 (4194304)
I0623 09:45:08.092386  1897 net.cpp:137] Memory required for data: 1591738464
I0623 09:45:08.092406  1897 layer_factory.hpp:77] Creating layer scale3c_branch2c
I0623 09:45:08.092424  1897 net.cpp:84] Creating Layer scale3c_branch2c
I0623 09:45:08.092442  1897 net.cpp:406] scale3c_branch2c <- res3c_branch2c
I0623 09:45:08.092456  1897 net.cpp:367] scale3c_branch2c -> res3c_branch2c (in-place)
I0623 09:45:08.092479  1897 layer_factory.hpp:77] Creating layer scale3c_branch2c
I0623 09:45:08.092507  1897 net.cpp:122] Setting up scale3c_branch2c
I0623 09:45:08.092525  1897 net.cpp:129] Top shape: 8 512 32 32 (4194304)
I0623 09:45:08.092541  1897 net.cpp:137] Memory required for data: 1608515680
I0623 09:45:08.092559  1897 layer_factory.hpp:77] Creating layer res3c
I0623 09:45:08.092577  1897 net.cpp:84] Creating Layer res3c
I0623 09:45:08.092593  1897 net.cpp:406] res3c <- res3b_res3b_relu_0_split_1
I0623 09:45:08.092610  1897 net.cpp:406] res3c <- res3c_branch2c
I0623 09:45:08.092628  1897 net.cpp:380] res3c -> res3c
I0623 09:45:08.092648  1897 net.cpp:122] Setting up res3c
I0623 09:45:08.092665  1897 net.cpp:129] Top shape: 8 512 32 32 (4194304)
I0623 09:45:08.092680  1897 net.cpp:137] Memory required for data: 1625292896
I0623 09:45:08.092695  1897 layer_factory.hpp:77] Creating layer res3c_relu
I0623 09:45:08.092712  1897 net.cpp:84] Creating Layer res3c_relu
I0623 09:45:08.092728  1897 net.cpp:406] res3c_relu <- res3c
I0623 09:45:08.092746  1897 net.cpp:367] res3c_relu -> res3c (in-place)
I0623 09:45:08.092763  1897 net.cpp:122] Setting up res3c_relu
I0623 09:45:08.092782  1897 net.cpp:129] Top shape: 8 512 32 32 (4194304)
I0623 09:45:08.092797  1897 net.cpp:137] Memory required for data: 1642070112
I0623 09:45:08.092811  1897 layer_factory.hpp:77] Creating layer res3c_res3c_relu_0_split
I0623 09:45:08.092828  1897 net.cpp:84] Creating Layer res3c_res3c_relu_0_split
I0623 09:45:08.092842  1897 net.cpp:406] res3c_res3c_relu_0_split <- res3c
I0623 09:45:08.092859  1897 net.cpp:380] res3c_res3c_relu_0_split -> res3c_res3c_relu_0_split_0
I0623 09:45:08.092878  1897 net.cpp:380] res3c_res3c_relu_0_split -> res3c_res3c_relu_0_split_1
I0623 09:45:08.092898  1897 net.cpp:122] Setting up res3c_res3c_relu_0_split
I0623 09:45:08.092916  1897 net.cpp:129] Top shape: 8 512 32 32 (4194304)
I0623 09:45:08.092932  1897 net.cpp:129] Top shape: 8 512 32 32 (4194304)
I0623 09:45:08.092947  1897 net.cpp:137] Memory required for data: 1675624544
I0623 09:45:08.092962  1897 layer_factory.hpp:77] Creating layer res3d_branch2a
I0623 09:45:08.092981  1897 net.cpp:84] Creating Layer res3d_branch2a
I0623 09:45:08.092998  1897 net.cpp:406] res3d_branch2a <- res3c_res3c_relu_0_split_0
I0623 09:45:08.093015  1897 net.cpp:380] res3d_branch2a -> res3d_branch2a
I0623 09:45:08.093101  1897 net.cpp:122] Setting up res3d_branch2a
I0623 09:45:08.093123  1897 net.cpp:129] Top shape: 8 128 32 32 (1048576)
I0623 09:45:08.093139  1897 net.cpp:137] Memory required for data: 1679818848
I0623 09:45:08.093160  1897 layer_factory.hpp:77] Creating layer bn3d_branch2a
I0623 09:45:08.093179  1897 net.cpp:84] Creating Layer bn3d_branch2a
I0623 09:45:08.093196  1897 net.cpp:406] bn3d_branch2a <- res3d_branch2a
I0623 09:45:08.093214  1897 net.cpp:367] bn3d_branch2a -> res3d_branch2a (in-place)
I0623 09:45:08.093240  1897 net.cpp:122] Setting up bn3d_branch2a
I0623 09:45:08.093258  1897 net.cpp:129] Top shape: 8 128 32 32 (1048576)
I0623 09:45:08.093273  1897 net.cpp:137] Memory required for data: 1684013152
I0623 09:45:08.093305  1897 layer_factory.hpp:77] Creating layer scale3d_branch2a
I0623 09:45:08.093325  1897 net.cpp:84] Creating Layer scale3d_branch2a
I0623 09:45:08.093341  1897 net.cpp:406] scale3d_branch2a <- res3d_branch2a
I0623 09:45:08.093359  1897 net.cpp:367] scale3d_branch2a -> res3d_branch2a (in-place)
I0623 09:45:08.093381  1897 layer_factory.hpp:77] Creating layer scale3d_branch2a
I0623 09:45:08.093408  1897 net.cpp:122] Setting up scale3d_branch2a
I0623 09:45:08.093428  1897 net.cpp:129] Top shape: 8 128 32 32 (1048576)
I0623 09:45:08.093443  1897 net.cpp:137] Memory required for data: 1688207456
I0623 09:45:08.093461  1897 layer_factory.hpp:77] Creating layer res3d_branch2a_relu
I0623 09:45:08.093480  1897 net.cpp:84] Creating Layer res3d_branch2a_relu
I0623 09:45:08.093497  1897 net.cpp:406] res3d_branch2a_relu <- res3d_branch2a
I0623 09:45:08.093513  1897 net.cpp:367] res3d_branch2a_relu -> res3d_branch2a (in-place)
I0623 09:45:08.093531  1897 net.cpp:122] Setting up res3d_branch2a_relu
I0623 09:45:08.093549  1897 net.cpp:129] Top shape: 8 128 32 32 (1048576)
I0623 09:45:08.093564  1897 net.cpp:137] Memory required for data: 1692401760
I0623 09:45:08.093580  1897 layer_factory.hpp:77] Creating layer res3d_branch2b
I0623 09:45:08.093598  1897 net.cpp:84] Creating Layer res3d_branch2b
I0623 09:45:08.093614  1897 net.cpp:406] res3d_branch2b <- res3d_branch2a
I0623 09:45:08.093632  1897 net.cpp:380] res3d_branch2b -> res3d_branch2b
I0623 09:45:08.093791  1897 net.cpp:122] Setting up res3d_branch2b
I0623 09:45:08.093813  1897 net.cpp:129] Top shape: 8 128 32 32 (1048576)
I0623 09:45:08.093828  1897 net.cpp:137] Memory required for data: 1696596064
I0623 09:45:08.093847  1897 layer_factory.hpp:77] Creating layer bn3d_branch2b
I0623 09:45:08.093864  1897 net.cpp:84] Creating Layer bn3d_branch2b
I0623 09:45:08.093880  1897 net.cpp:406] bn3d_branch2b <- res3d_branch2b
I0623 09:45:08.093899  1897 net.cpp:367] bn3d_branch2b -> res3d_branch2b (in-place)
I0623 09:45:08.093924  1897 net.cpp:122] Setting up bn3d_branch2b
I0623 09:45:08.093942  1897 net.cpp:129] Top shape: 8 128 32 32 (1048576)
I0623 09:45:08.093958  1897 net.cpp:137] Memory required for data: 1700790368
I0623 09:45:08.093977  1897 layer_factory.hpp:77] Creating layer scale3d_branch2b
I0623 09:45:08.093997  1897 net.cpp:84] Creating Layer scale3d_branch2b
I0623 09:45:08.094012  1897 net.cpp:406] scale3d_branch2b <- res3d_branch2b
I0623 09:45:08.094029  1897 net.cpp:367] scale3d_branch2b -> res3d_branch2b (in-place)
I0623 09:45:08.094050  1897 layer_factory.hpp:77] Creating layer scale3d_branch2b
I0623 09:45:08.094079  1897 net.cpp:122] Setting up scale3d_branch2b
I0623 09:45:08.094096  1897 net.cpp:129] Top shape: 8 128 32 32 (1048576)
I0623 09:45:08.094111  1897 net.cpp:137] Memory required for data: 1704984672
I0623 09:45:08.094130  1897 layer_factory.hpp:77] Creating layer res3d_branch2b_relu
I0623 09:45:08.094148  1897 net.cpp:84] Creating Layer res3d_branch2b_relu
I0623 09:45:08.094162  1897 net.cpp:406] res3d_branch2b_relu <- res3d_branch2b
I0623 09:45:08.094180  1897 net.cpp:367] res3d_branch2b_relu -> res3d_branch2b (in-place)
I0623 09:45:08.094198  1897 net.cpp:122] Setting up res3d_branch2b_relu
I0623 09:45:08.094215  1897 net.cpp:129] Top shape: 8 128 32 32 (1048576)
I0623 09:45:08.094230  1897 net.cpp:137] Memory required for data: 1709178976
I0623 09:45:08.094246  1897 layer_factory.hpp:77] Creating layer res3d_branch2c
I0623 09:45:08.094265  1897 net.cpp:84] Creating Layer res3d_branch2c
I0623 09:45:08.094285  1897 net.cpp:406] res3d_branch2c <- res3d_branch2b
I0623 09:45:08.094303  1897 net.cpp:380] res3d_branch2c -> res3d_branch2c
I0623 09:45:08.094388  1897 net.cpp:122] Setting up res3d_branch2c
I0623 09:45:08.094411  1897 net.cpp:129] Top shape: 8 512 32 32 (4194304)
I0623 09:45:08.094426  1897 net.cpp:137] Memory required for data: 1725956192
I0623 09:45:08.094444  1897 layer_factory.hpp:77] Creating layer bn3d_branch2c
I0623 09:45:08.094462  1897 net.cpp:84] Creating Layer bn3d_branch2c
I0623 09:45:08.094478  1897 net.cpp:406] bn3d_branch2c <- res3d_branch2c
I0623 09:45:08.094496  1897 net.cpp:367] bn3d_branch2c -> res3d_branch2c (in-place)
I0623 09:45:08.094522  1897 net.cpp:122] Setting up bn3d_branch2c
I0623 09:45:08.094540  1897 net.cpp:129] Top shape: 8 512 32 32 (4194304)
I0623 09:45:08.094557  1897 net.cpp:137] Memory required for data: 1742733408
I0623 09:45:08.094575  1897 layer_factory.hpp:77] Creating layer scale3d_branch2c
I0623 09:45:08.094594  1897 net.cpp:84] Creating Layer scale3d_branch2c
I0623 09:45:08.094609  1897 net.cpp:406] scale3d_branch2c <- res3d_branch2c
I0623 09:45:08.094626  1897 net.cpp:367] scale3d_branch2c -> res3d_branch2c (in-place)
I0623 09:45:08.094650  1897 layer_factory.hpp:77] Creating layer scale3d_branch2c
I0623 09:45:08.094681  1897 net.cpp:122] Setting up scale3d_branch2c
I0623 09:45:08.094702  1897 net.cpp:129] Top shape: 8 512 32 32 (4194304)
I0623 09:45:08.094718  1897 net.cpp:137] Memory required for data: 1759510624
I0623 09:45:08.094736  1897 layer_factory.hpp:77] Creating layer res3d
I0623 09:45:08.094754  1897 net.cpp:84] Creating Layer res3d
I0623 09:45:08.094770  1897 net.cpp:406] res3d <- res3c_res3c_relu_0_split_1
I0623 09:45:08.094786  1897 net.cpp:406] res3d <- res3d_branch2c
I0623 09:45:08.094805  1897 net.cpp:380] res3d -> res3d
I0623 09:45:08.094823  1897 net.cpp:122] Setting up res3d
I0623 09:45:08.094841  1897 net.cpp:129] Top shape: 8 512 32 32 (4194304)
I0623 09:45:08.094857  1897 net.cpp:137] Memory required for data: 1776287840
I0623 09:45:08.094872  1897 layer_factory.hpp:77] Creating layer res3d_relu
I0623 09:45:08.094889  1897 net.cpp:84] Creating Layer res3d_relu
I0623 09:45:08.094905  1897 net.cpp:406] res3d_relu <- res3d
I0623 09:45:08.094923  1897 net.cpp:367] res3d_relu -> res3d (in-place)
I0623 09:45:08.094941  1897 net.cpp:122] Setting up res3d_relu
I0623 09:45:08.094959  1897 net.cpp:129] Top shape: 8 512 32 32 (4194304)
I0623 09:45:08.094974  1897 net.cpp:137] Memory required for data: 1793065056
I0623 09:45:08.094988  1897 layer_factory.hpp:77] Creating layer res3d_res3d_relu_0_split
I0623 09:45:08.095006  1897 net.cpp:84] Creating Layer res3d_res3d_relu_0_split
I0623 09:45:08.095021  1897 net.cpp:406] res3d_res3d_relu_0_split <- res3d
I0623 09:45:08.095038  1897 net.cpp:380] res3d_res3d_relu_0_split -> res3d_res3d_relu_0_split_0
I0623 09:45:08.095057  1897 net.cpp:380] res3d_res3d_relu_0_split -> res3d_res3d_relu_0_split_1
I0623 09:45:08.095077  1897 net.cpp:122] Setting up res3d_res3d_relu_0_split
I0623 09:45:08.095094  1897 net.cpp:129] Top shape: 8 512 32 32 (4194304)
I0623 09:45:08.095111  1897 net.cpp:129] Top shape: 8 512 32 32 (4194304)
I0623 09:45:08.095126  1897 net.cpp:137] Memory required for data: 1826619488
I0623 09:45:08.095141  1897 layer_factory.hpp:77] Creating layer res4a_branch1
I0623 09:45:08.095160  1897 net.cpp:84] Creating Layer res4a_branch1
I0623 09:45:08.095176  1897 net.cpp:406] res4a_branch1 <- res3d_res3d_relu_0_split_0
I0623 09:45:08.095192  1897 net.cpp:380] res4a_branch1 -> res4a_branch1
I0623 09:45:08.095696  1897 net.cpp:122] Setting up res4a_branch1
I0623 09:45:08.095721  1897 net.cpp:129] Top shape: 8 1024 16 16 (2097152)
I0623 09:45:08.095736  1897 net.cpp:137] Memory required for data: 1835008096
I0623 09:45:08.095752  1897 layer_factory.hpp:77] Creating layer bn4a_branch1
I0623 09:45:08.095772  1897 net.cpp:84] Creating Layer bn4a_branch1
I0623 09:45:08.095788  1897 net.cpp:406] bn4a_branch1 <- res4a_branch1
I0623 09:45:08.095804  1897 net.cpp:367] bn4a_branch1 -> res4a_branch1 (in-place)
I0623 09:45:08.095834  1897 net.cpp:122] Setting up bn4a_branch1
I0623 09:45:08.095854  1897 net.cpp:129] Top shape: 8 1024 16 16 (2097152)
I0623 09:45:08.095868  1897 net.cpp:137] Memory required for data: 1843396704
I0623 09:45:08.095890  1897 layer_factory.hpp:77] Creating layer scale4a_branch1
I0623 09:45:08.095907  1897 net.cpp:84] Creating Layer scale4a_branch1
I0623 09:45:08.095923  1897 net.cpp:406] scale4a_branch1 <- res4a_branch1
I0623 09:45:08.095940  1897 net.cpp:367] scale4a_branch1 -> res4a_branch1 (in-place)
I0623 09:45:08.095963  1897 layer_factory.hpp:77] Creating layer scale4a_branch1
I0623 09:45:08.095990  1897 net.cpp:122] Setting up scale4a_branch1
I0623 09:45:08.096009  1897 net.cpp:129] Top shape: 8 1024 16 16 (2097152)
I0623 09:45:08.096024  1897 net.cpp:137] Memory required for data: 1851785312
I0623 09:45:08.096043  1897 layer_factory.hpp:77] Creating layer res4a_branch2a
I0623 09:45:08.096062  1897 net.cpp:84] Creating Layer res4a_branch2a
I0623 09:45:08.096078  1897 net.cpp:406] res4a_branch2a <- res3d_res3d_relu_0_split_1
I0623 09:45:08.096097  1897 net.cpp:380] res4a_branch2a -> res4a_branch2a
I0623 09:45:08.096240  1897 net.cpp:122] Setting up res4a_branch2a
I0623 09:45:08.096263  1897 net.cpp:129] Top shape: 8 256 16 16 (524288)
I0623 09:45:08.096279  1897 net.cpp:137] Memory required for data: 1853882464
I0623 09:45:08.096297  1897 layer_factory.hpp:77] Creating layer bn4a_branch2a
I0623 09:45:08.096314  1897 net.cpp:84] Creating Layer bn4a_branch2a
I0623 09:45:08.096329  1897 net.cpp:406] bn4a_branch2a <- res4a_branch2a
I0623 09:45:08.096348  1897 net.cpp:367] bn4a_branch2a -> res4a_branch2a (in-place)
I0623 09:45:08.096374  1897 net.cpp:122] Setting up bn4a_branch2a
I0623 09:45:08.096391  1897 net.cpp:129] Top shape: 8 256 16 16 (524288)
I0623 09:45:08.096406  1897 net.cpp:137] Memory required for data: 1855979616
I0623 09:45:08.096426  1897 layer_factory.hpp:77] Creating layer scale4a_branch2a
I0623 09:45:08.096444  1897 net.cpp:84] Creating Layer scale4a_branch2a
I0623 09:45:08.096460  1897 net.cpp:406] scale4a_branch2a <- res4a_branch2a
I0623 09:45:08.096477  1897 net.cpp:367] scale4a_branch2a -> res4a_branch2a (in-place)
I0623 09:45:08.096499  1897 layer_factory.hpp:77] Creating layer scale4a_branch2a
I0623 09:45:08.096526  1897 net.cpp:122] Setting up scale4a_branch2a
I0623 09:45:08.096544  1897 net.cpp:129] Top shape: 8 256 16 16 (524288)
I0623 09:45:08.096560  1897 net.cpp:137] Memory required for data: 1858076768
I0623 09:45:08.096577  1897 layer_factory.hpp:77] Creating layer res4a_branch2a_relu
I0623 09:45:08.096596  1897 net.cpp:84] Creating Layer res4a_branch2a_relu
I0623 09:45:08.096611  1897 net.cpp:406] res4a_branch2a_relu <- res4a_branch2a
I0623 09:45:08.096628  1897 net.cpp:367] res4a_branch2a_relu -> res4a_branch2a (in-place)
I0623 09:45:08.096647  1897 net.cpp:122] Setting up res4a_branch2a_relu
I0623 09:45:08.096667  1897 net.cpp:129] Top shape: 8 256 16 16 (524288)
I0623 09:45:08.096681  1897 net.cpp:137] Memory required for data: 1860173920
I0623 09:45:08.096698  1897 layer_factory.hpp:77] Creating layer res4a_branch2b
I0623 09:45:08.096717  1897 net.cpp:84] Creating Layer res4a_branch2b
I0623 09:45:08.096734  1897 net.cpp:406] res4a_branch2b <- res4a_branch2a
I0623 09:45:08.096751  1897 net.cpp:380] res4a_branch2b -> res4a_branch2b
I0623 09:45:08.097317  1897 net.cpp:122] Setting up res4a_branch2b
I0623 09:45:08.097343  1897 net.cpp:129] Top shape: 8 256 16 16 (524288)
I0623 09:45:08.097359  1897 net.cpp:137] Memory required for data: 1862271072
I0623 09:45:08.097376  1897 layer_factory.hpp:77] Creating layer bn4a_branch2b
I0623 09:45:08.097394  1897 net.cpp:84] Creating Layer bn4a_branch2b
I0623 09:45:08.097410  1897 net.cpp:406] bn4a_branch2b <- res4a_branch2b
I0623 09:45:08.097427  1897 net.cpp:367] bn4a_branch2b -> res4a_branch2b (in-place)
I0623 09:45:08.097455  1897 net.cpp:122] Setting up bn4a_branch2b
I0623 09:45:08.097472  1897 net.cpp:129] Top shape: 8 256 16 16 (524288)
I0623 09:45:08.097488  1897 net.cpp:137] Memory required for data: 1864368224
I0623 09:45:08.097512  1897 layer_factory.hpp:77] Creating layer scale4a_branch2b
I0623 09:45:08.097530  1897 net.cpp:84] Creating Layer scale4a_branch2b
I0623 09:45:08.097546  1897 net.cpp:406] scale4a_branch2b <- res4a_branch2b
I0623 09:45:08.097563  1897 net.cpp:367] scale4a_branch2b -> res4a_branch2b (in-place)
I0623 09:45:08.097585  1897 layer_factory.hpp:77] Creating layer scale4a_branch2b
I0623 09:45:08.097612  1897 net.cpp:122] Setting up scale4a_branch2b
I0623 09:45:08.097632  1897 net.cpp:129] Top shape: 8 256 16 16 (524288)
I0623 09:45:08.097647  1897 net.cpp:137] Memory required for data: 1866465376
I0623 09:45:08.097666  1897 layer_factory.hpp:77] Creating layer res4a_branch2b_relu
I0623 09:45:08.097684  1897 net.cpp:84] Creating Layer res4a_branch2b_relu
I0623 09:45:08.097700  1897 net.cpp:406] res4a_branch2b_relu <- res4a_branch2b
I0623 09:45:08.097718  1897 net.cpp:367] res4a_branch2b_relu -> res4a_branch2b (in-place)
I0623 09:45:08.097735  1897 net.cpp:122] Setting up res4a_branch2b_relu
I0623 09:45:08.097754  1897 net.cpp:129] Top shape: 8 256 16 16 (524288)
I0623 09:45:08.097769  1897 net.cpp:137] Memory required for data: 1868562528
I0623 09:45:08.097784  1897 layer_factory.hpp:77] Creating layer res4a_branch2c
I0623 09:45:08.097802  1897 net.cpp:84] Creating Layer res4a_branch2c
I0623 09:45:08.097818  1897 net.cpp:406] res4a_branch2c <- res4a_branch2b
I0623 09:45:08.097836  1897 net.cpp:380] res4a_branch2c -> res4a_branch2c
I0623 09:45:08.098098  1897 net.cpp:122] Setting up res4a_branch2c
I0623 09:45:08.098122  1897 net.cpp:129] Top shape: 8 1024 16 16 (2097152)
I0623 09:45:08.098137  1897 net.cpp:137] Memory required for data: 1876951136
I0623 09:45:08.098155  1897 layer_factory.hpp:77] Creating layer bn4a_branch2c
I0623 09:45:08.098173  1897 net.cpp:84] Creating Layer bn4a_branch2c
I0623 09:45:08.098189  1897 net.cpp:406] bn4a_branch2c <- res4a_branch2c
I0623 09:45:08.098206  1897 net.cpp:367] bn4a_branch2c -> res4a_branch2c (in-place)
I0623 09:45:08.098232  1897 net.cpp:122] Setting up bn4a_branch2c
I0623 09:45:08.098250  1897 net.cpp:129] Top shape: 8 1024 16 16 (2097152)
I0623 09:45:08.098265  1897 net.cpp:137] Memory required for data: 1885339744
I0623 09:45:08.098284  1897 layer_factory.hpp:77] Creating layer scale4a_branch2c
I0623 09:45:08.098302  1897 net.cpp:84] Creating Layer scale4a_branch2c
I0623 09:45:08.098318  1897 net.cpp:406] scale4a_branch2c <- res4a_branch2c
I0623 09:45:08.098335  1897 net.cpp:367] scale4a_branch2c -> res4a_branch2c (in-place)
I0623 09:45:08.098358  1897 layer_factory.hpp:77] Creating layer scale4a_branch2c
I0623 09:45:08.098386  1897 net.cpp:122] Setting up scale4a_branch2c
I0623 09:45:08.098404  1897 net.cpp:129] Top shape: 8 1024 16 16 (2097152)
I0623 09:45:08.098419  1897 net.cpp:137] Memory required for data: 1893728352
I0623 09:45:08.098438  1897 layer_factory.hpp:77] Creating layer res4a
I0623 09:45:08.098455  1897 net.cpp:84] Creating Layer res4a
I0623 09:45:08.098471  1897 net.cpp:406] res4a <- res4a_branch1
I0623 09:45:08.098489  1897 net.cpp:406] res4a <- res4a_branch2c
I0623 09:45:08.098505  1897 net.cpp:380] res4a -> res4a
I0623 09:45:08.098526  1897 net.cpp:122] Setting up res4a
I0623 09:45:08.098542  1897 net.cpp:129] Top shape: 8 1024 16 16 (2097152)
I0623 09:45:08.098557  1897 net.cpp:137] Memory required for data: 1902116960
I0623 09:45:08.098572  1897 layer_factory.hpp:77] Creating layer res4a_relu
I0623 09:45:08.098590  1897 net.cpp:84] Creating Layer res4a_relu
I0623 09:45:08.098605  1897 net.cpp:406] res4a_relu <- res4a
I0623 09:45:08.098623  1897 net.cpp:367] res4a_relu -> res4a (in-place)
I0623 09:45:08.098640  1897 net.cpp:122] Setting up res4a_relu
I0623 09:45:08.098657  1897 net.cpp:129] Top shape: 8 1024 16 16 (2097152)
I0623 09:45:08.098680  1897 net.cpp:137] Memory required for data: 1910505568
I0623 09:45:08.098696  1897 layer_factory.hpp:77] Creating layer res4a_res4a_relu_0_split
I0623 09:45:08.098726  1897 net.cpp:84] Creating Layer res4a_res4a_relu_0_split
I0623 09:45:08.098743  1897 net.cpp:406] res4a_res4a_relu_0_split <- res4a
I0623 09:45:08.098765  1897 net.cpp:380] res4a_res4a_relu_0_split -> res4a_res4a_relu_0_split_0
I0623 09:45:08.098785  1897 net.cpp:380] res4a_res4a_relu_0_split -> res4a_res4a_relu_0_split_1
I0623 09:45:08.098806  1897 net.cpp:122] Setting up res4a_res4a_relu_0_split
I0623 09:45:08.098824  1897 net.cpp:129] Top shape: 8 1024 16 16 (2097152)
I0623 09:45:08.098840  1897 net.cpp:129] Top shape: 8 1024 16 16 (2097152)
I0623 09:45:08.098855  1897 net.cpp:137] Memory required for data: 1927282784
I0623 09:45:08.098871  1897 layer_factory.hpp:77] Creating layer res4b_branch2a
I0623 09:45:08.098891  1897 net.cpp:84] Creating Layer res4b_branch2a
I0623 09:45:08.098907  1897 net.cpp:406] res4b_branch2a <- res4a_res4a_relu_0_split_0
I0623 09:45:08.098925  1897 net.cpp:380] res4b_branch2a -> res4b_branch2a
I0623 09:45:08.099186  1897 net.cpp:122] Setting up res4b_branch2a
I0623 09:45:08.099210  1897 net.cpp:129] Top shape: 8 256 16 16 (524288)
I0623 09:45:08.099225  1897 net.cpp:137] Memory required for data: 1929379936
I0623 09:45:08.099243  1897 layer_factory.hpp:77] Creating layer bn4b_branch2a
I0623 09:45:08.099261  1897 net.cpp:84] Creating Layer bn4b_branch2a
I0623 09:45:08.099278  1897 net.cpp:406] bn4b_branch2a <- res4b_branch2a
I0623 09:45:08.099295  1897 net.cpp:367] bn4b_branch2a -> res4b_branch2a (in-place)
I0623 09:45:08.099321  1897 net.cpp:122] Setting up bn4b_branch2a
I0623 09:45:08.099339  1897 net.cpp:129] Top shape: 8 256 16 16 (524288)
I0623 09:45:08.099354  1897 net.cpp:137] Memory required for data: 1931477088
I0623 09:45:08.099375  1897 layer_factory.hpp:77] Creating layer scale4b_branch2a
I0623 09:45:08.099392  1897 net.cpp:84] Creating Layer scale4b_branch2a
I0623 09:45:08.099408  1897 net.cpp:406] scale4b_branch2a <- res4b_branch2a
I0623 09:45:08.099426  1897 net.cpp:367] scale4b_branch2a -> res4b_branch2a (in-place)
I0623 09:45:08.099447  1897 layer_factory.hpp:77] Creating layer scale4b_branch2a
I0623 09:45:08.099473  1897 net.cpp:122] Setting up scale4b_branch2a
I0623 09:45:08.099493  1897 net.cpp:129] Top shape: 8 256 16 16 (524288)
I0623 09:45:08.099508  1897 net.cpp:137] Memory required for data: 1933574240
I0623 09:45:08.099526  1897 layer_factory.hpp:77] Creating layer res4b_branch2a_relu
I0623 09:45:08.099544  1897 net.cpp:84] Creating Layer res4b_branch2a_relu
I0623 09:45:08.099560  1897 net.cpp:406] res4b_branch2a_relu <- res4b_branch2a
I0623 09:45:08.099576  1897 net.cpp:367] res4b_branch2a_relu -> res4b_branch2a (in-place)
I0623 09:45:08.099596  1897 net.cpp:122] Setting up res4b_branch2a_relu
I0623 09:45:08.099612  1897 net.cpp:129] Top shape: 8 256 16 16 (524288)
I0623 09:45:08.099627  1897 net.cpp:137] Memory required for data: 1935671392
I0623 09:45:08.099642  1897 layer_factory.hpp:77] Creating layer res4b_branch2b
I0623 09:45:08.099661  1897 net.cpp:84] Creating Layer res4b_branch2b
I0623 09:45:08.099678  1897 net.cpp:406] res4b_branch2b <- res4b_branch2a
I0623 09:45:08.099695  1897 net.cpp:380] res4b_branch2b -> res4b_branch2b
I0623 09:45:08.100248  1897 net.cpp:122] Setting up res4b_branch2b
I0623 09:45:08.100273  1897 net.cpp:129] Top shape: 8 256 16 16 (524288)
I0623 09:45:08.100289  1897 net.cpp:137] Memory required for data: 1937768544
I0623 09:45:08.100306  1897 layer_factory.hpp:77] Creating layer bn4b_branch2b
I0623 09:45:08.100324  1897 net.cpp:84] Creating Layer bn4b_branch2b
I0623 09:45:08.100340  1897 net.cpp:406] bn4b_branch2b <- res4b_branch2b
I0623 09:45:08.100358  1897 net.cpp:367] bn4b_branch2b -> res4b_branch2b (in-place)
I0623 09:45:08.100383  1897 net.cpp:122] Setting up bn4b_branch2b
I0623 09:45:08.100401  1897 net.cpp:129] Top shape: 8 256 16 16 (524288)
I0623 09:45:08.100417  1897 net.cpp:137] Memory required for data: 1939865696
I0623 09:45:08.100436  1897 layer_factory.hpp:77] Creating layer scale4b_branch2b
I0623 09:45:08.100455  1897 net.cpp:84] Creating Layer scale4b_branch2b
I0623 09:45:08.100471  1897 net.cpp:406] scale4b_branch2b <- res4b_branch2b
I0623 09:45:08.100488  1897 net.cpp:367] scale4b_branch2b -> res4b_branch2b (in-place)
I0623 09:45:08.100514  1897 layer_factory.hpp:77] Creating layer scale4b_branch2b
I0623 09:45:08.100541  1897 net.cpp:122] Setting up scale4b_branch2b
I0623 09:45:08.100560  1897 net.cpp:129] Top shape: 8 256 16 16 (524288)
I0623 09:45:08.100575  1897 net.cpp:137] Memory required for data: 1941962848
I0623 09:45:08.100594  1897 layer_factory.hpp:77] Creating layer res4b_branch2b_relu
I0623 09:45:08.100612  1897 net.cpp:84] Creating Layer res4b_branch2b_relu
I0623 09:45:08.100628  1897 net.cpp:406] res4b_branch2b_relu <- res4b_branch2b
I0623 09:45:08.100646  1897 net.cpp:367] res4b_branch2b_relu -> res4b_branch2b (in-place)
I0623 09:45:08.100664  1897 net.cpp:122] Setting up res4b_branch2b_relu
I0623 09:45:08.100682  1897 net.cpp:129] Top shape: 8 256 16 16 (524288)
I0623 09:45:08.100697  1897 net.cpp:137] Memory required for data: 1944060000
I0623 09:45:08.100713  1897 layer_factory.hpp:77] Creating layer res4b_branch2c
I0623 09:45:08.100731  1897 net.cpp:84] Creating Layer res4b_branch2c
I0623 09:45:08.100747  1897 net.cpp:406] res4b_branch2c <- res4b_branch2b
I0623 09:45:08.100764  1897 net.cpp:380] res4b_branch2c -> res4b_branch2c
I0623 09:45:08.101024  1897 net.cpp:122] Setting up res4b_branch2c
I0623 09:45:08.101047  1897 net.cpp:129] Top shape: 8 1024 16 16 (2097152)
I0623 09:45:08.101063  1897 net.cpp:137] Memory required for data: 1952448608
I0623 09:45:08.101080  1897 layer_factory.hpp:77] Creating layer bn4b_branch2c
I0623 09:45:08.101099  1897 net.cpp:84] Creating Layer bn4b_branch2c
I0623 09:45:08.101115  1897 net.cpp:406] bn4b_branch2c <- res4b_branch2c
I0623 09:45:08.101132  1897 net.cpp:367] bn4b_branch2c -> res4b_branch2c (in-place)
I0623 09:45:08.101158  1897 net.cpp:122] Setting up bn4b_branch2c
I0623 09:45:08.101177  1897 net.cpp:129] Top shape: 8 1024 16 16 (2097152)
I0623 09:45:08.101192  1897 net.cpp:137] Memory required for data: 1960837216
I0623 09:45:08.101212  1897 layer_factory.hpp:77] Creating layer scale4b_branch2c
I0623 09:45:08.101229  1897 net.cpp:84] Creating Layer scale4b_branch2c
I0623 09:45:08.101245  1897 net.cpp:406] scale4b_branch2c <- res4b_branch2c
I0623 09:45:08.101263  1897 net.cpp:367] scale4b_branch2c -> res4b_branch2c (in-place)
I0623 09:45:08.101285  1897 layer_factory.hpp:77] Creating layer scale4b_branch2c
I0623 09:45:08.101313  1897 net.cpp:122] Setting up scale4b_branch2c
I0623 09:45:08.101332  1897 net.cpp:129] Top shape: 8 1024 16 16 (2097152)
I0623 09:45:08.101347  1897 net.cpp:137] Memory required for data: 1969225824
I0623 09:45:08.101366  1897 layer_factory.hpp:77] Creating layer res4b
I0623 09:45:08.101383  1897 net.cpp:84] Creating Layer res4b
I0623 09:45:08.101400  1897 net.cpp:406] res4b <- res4a_res4a_relu_0_split_1
I0623 09:45:08.101416  1897 net.cpp:406] res4b <- res4b_branch2c
I0623 09:45:08.101434  1897 net.cpp:380] res4b -> res4b
I0623 09:45:08.101455  1897 net.cpp:122] Setting up res4b
I0623 09:45:08.101472  1897 net.cpp:129] Top shape: 8 1024 16 16 (2097152)
I0623 09:45:08.101487  1897 net.cpp:137] Memory required for data: 1977614432
I0623 09:45:08.101503  1897 layer_factory.hpp:77] Creating layer res4b_relu
I0623 09:45:08.101521  1897 net.cpp:84] Creating Layer res4b_relu
I0623 09:45:08.101536  1897 net.cpp:406] res4b_relu <- res4b
I0623 09:45:08.101553  1897 net.cpp:367] res4b_relu -> res4b (in-place)
I0623 09:45:08.101572  1897 net.cpp:122] Setting up res4b_relu
I0623 09:45:08.101588  1897 net.cpp:129] Top shape: 8 1024 16 16 (2097152)
I0623 09:45:08.101603  1897 net.cpp:137] Memory required for data: 1986003040
I0623 09:45:08.101619  1897 layer_factory.hpp:77] Creating layer res4b_res4b_relu_0_split
I0623 09:45:08.101635  1897 net.cpp:84] Creating Layer res4b_res4b_relu_0_split
I0623 09:45:08.101651  1897 net.cpp:406] res4b_res4b_relu_0_split <- res4b
I0623 09:45:08.101668  1897 net.cpp:380] res4b_res4b_relu_0_split -> res4b_res4b_relu_0_split_0
I0623 09:45:08.101687  1897 net.cpp:380] res4b_res4b_relu_0_split -> res4b_res4b_relu_0_split_1
I0623 09:45:08.101714  1897 net.cpp:122] Setting up res4b_res4b_relu_0_split
I0623 09:45:08.101733  1897 net.cpp:129] Top shape: 8 1024 16 16 (2097152)
I0623 09:45:08.101754  1897 net.cpp:129] Top shape: 8 1024 16 16 (2097152)
I0623 09:45:08.101770  1897 net.cpp:137] Memory required for data: 2002780256
I0623 09:45:08.101785  1897 layer_factory.hpp:77] Creating layer res4c_branch2a
I0623 09:45:08.101804  1897 net.cpp:84] Creating Layer res4c_branch2a
I0623 09:45:08.101821  1897 net.cpp:406] res4c_branch2a <- res4b_res4b_relu_0_split_0
I0623 09:45:08.101838  1897 net.cpp:380] res4c_branch2a -> res4c_branch2a
I0623 09:45:08.102100  1897 net.cpp:122] Setting up res4c_branch2a
I0623 09:45:08.102123  1897 net.cpp:129] Top shape: 8 256 16 16 (524288)
I0623 09:45:08.102138  1897 net.cpp:137] Memory required for data: 2004877408
I0623 09:45:08.102155  1897 layer_factory.hpp:77] Creating layer bn4c_branch2a
I0623 09:45:08.102174  1897 net.cpp:84] Creating Layer bn4c_branch2a
I0623 09:45:08.102190  1897 net.cpp:406] bn4c_branch2a <- res4c_branch2a
I0623 09:45:08.102207  1897 net.cpp:367] bn4c_branch2a -> res4c_branch2a (in-place)
I0623 09:45:08.102233  1897 net.cpp:122] Setting up bn4c_branch2a
I0623 09:45:08.102252  1897 net.cpp:129] Top shape: 8 256 16 16 (524288)
I0623 09:45:08.102267  1897 net.cpp:137] Memory required for data: 2006974560
I0623 09:45:08.102286  1897 layer_factory.hpp:77] Creating layer scale4c_branch2a
I0623 09:45:08.102304  1897 net.cpp:84] Creating Layer scale4c_branch2a
I0623 09:45:08.102320  1897 net.cpp:406] scale4c_branch2a <- res4c_branch2a
I0623 09:45:08.102337  1897 net.cpp:367] scale4c_branch2a -> res4c_branch2a (in-place)
I0623 09:45:08.102362  1897 layer_factory.hpp:77] Creating layer scale4c_branch2a
I0623 09:45:08.102391  1897 net.cpp:122] Setting up scale4c_branch2a
I0623 09:45:08.102409  1897 net.cpp:129] Top shape: 8 256 16 16 (524288)
I0623 09:45:08.102424  1897 net.cpp:137] Memory required for data: 2009071712
I0623 09:45:08.102442  1897 layer_factory.hpp:77] Creating layer res4c_branch2a_relu
I0623 09:45:08.102460  1897 net.cpp:84] Creating Layer res4c_branch2a_relu
I0623 09:45:08.102476  1897 net.cpp:406] res4c_branch2a_relu <- res4c_branch2a
I0623 09:45:08.102494  1897 net.cpp:367] res4c_branch2a_relu -> res4c_branch2a (in-place)
I0623 09:45:08.102511  1897 net.cpp:122] Setting up res4c_branch2a_relu
I0623 09:45:08.102529  1897 net.cpp:129] Top shape: 8 256 16 16 (524288)
I0623 09:45:08.102542  1897 net.cpp:137] Memory required for data: 2011168864
I0623 09:45:08.102557  1897 layer_factory.hpp:77] Creating layer res4c_branch2b
I0623 09:45:08.102577  1897 net.cpp:84] Creating Layer res4c_branch2b
I0623 09:45:08.102592  1897 net.cpp:406] res4c_branch2b <- res4c_branch2a
I0623 09:45:08.102610  1897 net.cpp:380] res4c_branch2b -> res4c_branch2b
I0623 09:45:08.103186  1897 net.cpp:122] Setting up res4c_branch2b
I0623 09:45:08.103214  1897 net.cpp:129] Top shape: 8 256 16 16 (524288)
I0623 09:45:08.103229  1897 net.cpp:137] Memory required for data: 2013266016
I0623 09:45:08.103246  1897 layer_factory.hpp:77] Creating layer bn4c_branch2b
I0623 09:45:08.103266  1897 net.cpp:84] Creating Layer bn4c_branch2b
I0623 09:45:08.103281  1897 net.cpp:406] bn4c_branch2b <- res4c_branch2b
I0623 09:45:08.103299  1897 net.cpp:367] bn4c_branch2b -> res4c_branch2b (in-place)
I0623 09:45:08.103324  1897 net.cpp:122] Setting up bn4c_branch2b
I0623 09:45:08.103343  1897 net.cpp:129] Top shape: 8 256 16 16 (524288)
I0623 09:45:08.103358  1897 net.cpp:137] Memory required for data: 2015363168
I0623 09:45:08.103376  1897 layer_factory.hpp:77] Creating layer scale4c_branch2b
I0623 09:45:08.103395  1897 net.cpp:84] Creating Layer scale4c_branch2b
I0623 09:45:08.103411  1897 net.cpp:406] scale4c_branch2b <- res4c_branch2b
I0623 09:45:08.103428  1897 net.cpp:367] scale4c_branch2b -> res4c_branch2b (in-place)
I0623 09:45:08.103449  1897 layer_factory.hpp:77] Creating layer scale4c_branch2b
I0623 09:45:08.103476  1897 net.cpp:122] Setting up scale4c_branch2b
I0623 09:45:08.103494  1897 net.cpp:129] Top shape: 8 256 16 16 (524288)
I0623 09:45:08.103509  1897 net.cpp:137] Memory required for data: 2017460320
I0623 09:45:08.103541  1897 layer_factory.hpp:77] Creating layer res4c_branch2b_relu
I0623 09:45:08.103564  1897 net.cpp:84] Creating Layer res4c_branch2b_relu
I0623 09:45:08.103581  1897 net.cpp:406] res4c_branch2b_relu <- res4c_branch2b
I0623 09:45:08.103598  1897 net.cpp:367] res4c_branch2b_relu -> res4c_branch2b (in-place)
I0623 09:45:08.103617  1897 net.cpp:122] Setting up res4c_branch2b_relu
I0623 09:45:08.103636  1897 net.cpp:129] Top shape: 8 256 16 16 (524288)
I0623 09:45:08.103651  1897 net.cpp:137] Memory required for data: 2019557472
I0623 09:45:08.103667  1897 layer_factory.hpp:77] Creating layer res4c_branch2c
I0623 09:45:08.103685  1897 net.cpp:84] Creating Layer res4c_branch2c
I0623 09:45:08.103701  1897 net.cpp:406] res4c_branch2c <- res4c_branch2b
I0623 09:45:08.103718  1897 net.cpp:380] res4c_branch2c -> res4c_branch2c
I0623 09:45:08.103986  1897 net.cpp:122] Setting up res4c_branch2c
I0623 09:45:08.104008  1897 net.cpp:129] Top shape: 8 1024 16 16 (2097152)
I0623 09:45:08.104023  1897 net.cpp:137] Memory required for data: 2027946080
I0623 09:45:08.104040  1897 layer_factory.hpp:77] Creating layer bn4c_branch2c
I0623 09:45:08.104059  1897 net.cpp:84] Creating Layer bn4c_branch2c
I0623 09:45:08.104075  1897 net.cpp:406] bn4c_branch2c <- res4c_branch2c
I0623 09:45:08.104094  1897 net.cpp:367] bn4c_branch2c -> res4c_branch2c (in-place)
I0623 09:45:08.104120  1897 net.cpp:122] Setting up bn4c_branch2c
I0623 09:45:08.104138  1897 net.cpp:129] Top shape: 8 1024 16 16 (2097152)
I0623 09:45:08.104154  1897 net.cpp:137] Memory required for data: 2036334688
I0623 09:45:08.104173  1897 layer_factory.hpp:77] Creating layer scale4c_branch2c
I0623 09:45:08.104192  1897 net.cpp:84] Creating Layer scale4c_branch2c
I0623 09:45:08.104208  1897 net.cpp:406] scale4c_branch2c <- res4c_branch2c
I0623 09:45:08.104225  1897 net.cpp:367] scale4c_branch2c -> res4c_branch2c (in-place)
I0623 09:45:08.104248  1897 layer_factory.hpp:77] Creating layer scale4c_branch2c
I0623 09:45:08.104275  1897 net.cpp:122] Setting up scale4c_branch2c
I0623 09:45:08.104295  1897 net.cpp:129] Top shape: 8 1024 16 16 (2097152)
I0623 09:45:08.104310  1897 net.cpp:137] Memory required for data: 2044723296
I0623 09:45:08.104327  1897 layer_factory.hpp:77] Creating layer res4c
I0623 09:45:08.104346  1897 net.cpp:84] Creating Layer res4c
I0623 09:45:08.104362  1897 net.cpp:406] res4c <- res4b_res4b_relu_0_split_1
I0623 09:45:08.104378  1897 net.cpp:406] res4c <- res4c_branch2c
I0623 09:45:08.104396  1897 net.cpp:380] res4c -> res4c
I0623 09:45:08.104416  1897 net.cpp:122] Setting up res4c
I0623 09:45:08.104434  1897 net.cpp:129] Top shape: 8 1024 16 16 (2097152)
I0623 09:45:08.104449  1897 net.cpp:137] Memory required for data: 2053111904
I0623 09:45:08.104465  1897 layer_factory.hpp:77] Creating layer res4c_relu
I0623 09:45:08.104481  1897 net.cpp:84] Creating Layer res4c_relu
I0623 09:45:08.104497  1897 net.cpp:406] res4c_relu <- res4c
I0623 09:45:08.104514  1897 net.cpp:367] res4c_relu -> res4c (in-place)
I0623 09:45:08.104532  1897 net.cpp:122] Setting up res4c_relu
I0623 09:45:08.104548  1897 net.cpp:129] Top shape: 8 1024 16 16 (2097152)
I0623 09:45:08.104564  1897 net.cpp:137] Memory required for data: 2061500512
I0623 09:45:08.104579  1897 layer_factory.hpp:77] Creating layer res4c_res4c_relu_0_split
I0623 09:45:08.104596  1897 net.cpp:84] Creating Layer res4c_res4c_relu_0_split
I0623 09:45:08.104612  1897 net.cpp:406] res4c_res4c_relu_0_split <- res4c
I0623 09:45:08.104630  1897 net.cpp:380] res4c_res4c_relu_0_split -> res4c_res4c_relu_0_split_0
I0623 09:45:08.104650  1897 net.cpp:380] res4c_res4c_relu_0_split -> res4c_res4c_relu_0_split_1
I0623 09:45:08.104668  1897 net.cpp:122] Setting up res4c_res4c_relu_0_split
I0623 09:45:08.104686  1897 net.cpp:129] Top shape: 8 1024 16 16 (2097152)
I0623 09:45:08.104702  1897 net.cpp:129] Top shape: 8 1024 16 16 (2097152)
I0623 09:45:08.104717  1897 net.cpp:137] Memory required for data: 2078277728
I0623 09:45:08.104733  1897 layer_factory.hpp:77] Creating layer res4d_branch2a
I0623 09:45:08.104753  1897 net.cpp:84] Creating Layer res4d_branch2a
I0623 09:45:08.104773  1897 net.cpp:406] res4d_branch2a <- res4c_res4c_relu_0_split_0
I0623 09:45:08.104791  1897 net.cpp:380] res4d_branch2a -> res4d_branch2a
I0623 09:45:08.105053  1897 net.cpp:122] Setting up res4d_branch2a
I0623 09:45:08.105077  1897 net.cpp:129] Top shape: 8 256 16 16 (524288)
I0623 09:45:08.105092  1897 net.cpp:137] Memory required for data: 2080374880
I0623 09:45:08.105108  1897 layer_factory.hpp:77] Creating layer bn4d_branch2a
I0623 09:45:08.105128  1897 net.cpp:84] Creating Layer bn4d_branch2a
I0623 09:45:08.105144  1897 net.cpp:406] bn4d_branch2a <- res4d_branch2a
I0623 09:45:08.105160  1897 net.cpp:367] bn4d_branch2a -> res4d_branch2a (in-place)
I0623 09:45:08.105186  1897 net.cpp:122] Setting up bn4d_branch2a
I0623 09:45:08.105204  1897 net.cpp:129] Top shape: 8 256 16 16 (524288)
I0623 09:45:08.105219  1897 net.cpp:137] Memory required for data: 2082472032
I0623 09:45:08.105239  1897 layer_factory.hpp:77] Creating layer scale4d_branch2a
I0623 09:45:08.105257  1897 net.cpp:84] Creating Layer scale4d_branch2a
I0623 09:45:08.105273  1897 net.cpp:406] scale4d_branch2a <- res4d_branch2a
I0623 09:45:08.105289  1897 net.cpp:367] scale4d_branch2a -> res4d_branch2a (in-place)
I0623 09:45:08.105311  1897 layer_factory.hpp:77] Creating layer scale4d_branch2a
I0623 09:45:08.105337  1897 net.cpp:122] Setting up scale4d_branch2a
I0623 09:45:08.105356  1897 net.cpp:129] Top shape: 8 256 16 16 (524288)
I0623 09:45:08.105371  1897 net.cpp:137] Memory required for data: 2084569184
I0623 09:45:08.105389  1897 layer_factory.hpp:77] Creating layer res4d_branch2a_relu
I0623 09:45:08.105407  1897 net.cpp:84] Creating Layer res4d_branch2a_relu
I0623 09:45:08.105423  1897 net.cpp:406] res4d_branch2a_relu <- res4d_branch2a
I0623 09:45:08.105440  1897 net.cpp:367] res4d_branch2a_relu -> res4d_branch2a (in-place)
I0623 09:45:08.105458  1897 net.cpp:122] Setting up res4d_branch2a_relu
I0623 09:45:08.105475  1897 net.cpp:129] Top shape: 8 256 16 16 (524288)
I0623 09:45:08.105490  1897 net.cpp:137] Memory required for data: 2086666336
I0623 09:45:08.105505  1897 layer_factory.hpp:77] Creating layer res4d_branch2b
I0623 09:45:08.105525  1897 net.cpp:84] Creating Layer res4d_branch2b
I0623 09:45:08.105540  1897 net.cpp:406] res4d_branch2b <- res4d_branch2a
I0623 09:45:08.105557  1897 net.cpp:380] res4d_branch2b -> res4d_branch2b
I0623 09:45:08.106590  1897 net.cpp:122] Setting up res4d_branch2b
I0623 09:45:08.106619  1897 net.cpp:129] Top shape: 8 256 16 16 (524288)
I0623 09:45:08.106636  1897 net.cpp:137] Memory required for data: 2088763488
I0623 09:45:08.106652  1897 layer_factory.hpp:77] Creating layer bn4d_branch2b
I0623 09:45:08.106678  1897 net.cpp:84] Creating Layer bn4d_branch2b
I0623 09:45:08.106698  1897 net.cpp:406] bn4d_branch2b <- res4d_branch2b
I0623 09:45:08.106715  1897 net.cpp:367] bn4d_branch2b -> res4d_branch2b (in-place)
I0623 09:45:08.106741  1897 net.cpp:122] Setting up bn4d_branch2b
I0623 09:45:08.106760  1897 net.cpp:129] Top shape: 8 256 16 16 (524288)
I0623 09:45:08.106775  1897 net.cpp:137] Memory required for data: 2090860640
I0623 09:45:08.106796  1897 layer_factory.hpp:77] Creating layer scale4d_branch2b
I0623 09:45:08.106814  1897 net.cpp:84] Creating Layer scale4d_branch2b
I0623 09:45:08.106830  1897 net.cpp:406] scale4d_branch2b <- res4d_branch2b
I0623 09:45:08.106848  1897 net.cpp:367] scale4d_branch2b -> res4d_branch2b (in-place)
I0623 09:45:08.106869  1897 layer_factory.hpp:77] Creating layer scale4d_branch2b
I0623 09:45:08.106895  1897 net.cpp:122] Setting up scale4d_branch2b
I0623 09:45:08.106914  1897 net.cpp:129] Top shape: 8 256 16 16 (524288)
I0623 09:45:08.106930  1897 net.cpp:137] Memory required for data: 2092957792
I0623 09:45:08.106947  1897 layer_factory.hpp:77] Creating layer res4d_branch2b_relu
I0623 09:45:08.106966  1897 net.cpp:84] Creating Layer res4d_branch2b_relu
I0623 09:45:08.106981  1897 net.cpp:406] res4d_branch2b_relu <- res4d_branch2b
I0623 09:45:08.106998  1897 net.cpp:367] res4d_branch2b_relu -> res4d_branch2b (in-place)
I0623 09:45:08.107017  1897 net.cpp:122] Setting up res4d_branch2b_relu
I0623 09:45:08.107038  1897 net.cpp:129] Top shape: 8 256 16 16 (524288)
I0623 09:45:08.107054  1897 net.cpp:137] Memory required for data: 2095054944
I0623 09:45:08.107069  1897 layer_factory.hpp:77] Creating layer res4d_branch2c
I0623 09:45:08.107089  1897 net.cpp:84] Creating Layer res4d_branch2c
I0623 09:45:08.107105  1897 net.cpp:406] res4d_branch2c <- res4d_branch2b
I0623 09:45:08.107121  1897 net.cpp:380] res4d_branch2c -> res4d_branch2c
I0623 09:45:08.107590  1897 net.cpp:122] Setting up res4d_branch2c
I0623 09:45:08.107615  1897 net.cpp:129] Top shape: 8 1024 16 16 (2097152)
I0623 09:45:08.107630  1897 net.cpp:137] Memory required for data: 2103443552
I0623 09:45:08.107647  1897 layer_factory.hpp:77] Creating layer bn4d_branch2c
I0623 09:45:08.107666  1897 net.cpp:84] Creating Layer bn4d_branch2c
I0623 09:45:08.107682  1897 net.cpp:406] bn4d_branch2c <- res4d_branch2c
I0623 09:45:08.107699  1897 net.cpp:367] bn4d_branch2c -> res4d_branch2c (in-place)
I0623 09:45:08.107727  1897 net.cpp:122] Setting up bn4d_branch2c
I0623 09:45:08.107744  1897 net.cpp:129] Top shape: 8 1024 16 16 (2097152)
I0623 09:45:08.107760  1897 net.cpp:137] Memory required for data: 2111832160
I0623 09:45:08.107779  1897 layer_factory.hpp:77] Creating layer scale4d_branch2c
I0623 09:45:08.107798  1897 net.cpp:84] Creating Layer scale4d_branch2c
I0623 09:45:08.107815  1897 net.cpp:406] scale4d_branch2c <- res4d_branch2c
I0623 09:45:08.107833  1897 net.cpp:367] scale4d_branch2c -> res4d_branch2c (in-place)
I0623 09:45:08.107856  1897 layer_factory.hpp:77] Creating layer scale4d_branch2c
I0623 09:45:08.107884  1897 net.cpp:122] Setting up scale4d_branch2c
I0623 09:45:08.107903  1897 net.cpp:129] Top shape: 8 1024 16 16 (2097152)
I0623 09:45:08.107918  1897 net.cpp:137] Memory required for data: 2120220768
I0623 09:45:08.107936  1897 layer_factory.hpp:77] Creating layer res4d
I0623 09:45:08.107955  1897 net.cpp:84] Creating Layer res4d
I0623 09:45:08.107971  1897 net.cpp:406] res4d <- res4c_res4c_relu_0_split_1
I0623 09:45:08.107987  1897 net.cpp:406] res4d <- res4d_branch2c
I0623 09:45:08.108006  1897 net.cpp:380] res4d -> res4d
I0623 09:45:08.108024  1897 net.cpp:122] Setting up res4d
I0623 09:45:08.108042  1897 net.cpp:129] Top shape: 8 1024 16 16 (2097152)
I0623 09:45:08.108058  1897 net.cpp:137] Memory required for data: 2128609376
I0623 09:45:08.108073  1897 layer_factory.hpp:77] Creating layer res4d_relu
I0623 09:45:08.108090  1897 net.cpp:84] Creating Layer res4d_relu
I0623 09:45:08.108106  1897 net.cpp:406] res4d_relu <- res4d
I0623 09:45:08.108124  1897 net.cpp:367] res4d_relu -> res4d (in-place)
I0623 09:45:08.108141  1897 net.cpp:122] Setting up res4d_relu
I0623 09:45:08.108160  1897 net.cpp:129] Top shape: 8 1024 16 16 (2097152)
I0623 09:45:08.108175  1897 net.cpp:137] Memory required for data: 2136997984
I0623 09:45:08.108189  1897 layer_factory.hpp:77] Creating layer res4d_res4d_relu_0_split
I0623 09:45:08.108207  1897 net.cpp:84] Creating Layer res4d_res4d_relu_0_split
I0623 09:45:08.108222  1897 net.cpp:406] res4d_res4d_relu_0_split <- res4d
I0623 09:45:08.108240  1897 net.cpp:380] res4d_res4d_relu_0_split -> res4d_res4d_relu_0_split_0
I0623 09:45:08.108259  1897 net.cpp:380] res4d_res4d_relu_0_split -> res4d_res4d_relu_0_split_1
I0623 09:45:08.108279  1897 net.cpp:122] Setting up res4d_res4d_relu_0_split
I0623 09:45:08.108296  1897 net.cpp:129] Top shape: 8 1024 16 16 (2097152)
I0623 09:45:08.108314  1897 net.cpp:129] Top shape: 8 1024 16 16 (2097152)
I0623 09:45:08.108328  1897 net.cpp:137] Memory required for data: 2153775200
I0623 09:45:08.108343  1897 layer_factory.hpp:77] Creating layer res4e_branch2a
I0623 09:45:08.108362  1897 net.cpp:84] Creating Layer res4e_branch2a
I0623 09:45:08.108379  1897 net.cpp:406] res4e_branch2a <- res4d_res4d_relu_0_split_0
I0623 09:45:08.108397  1897 net.cpp:380] res4e_branch2a -> res4e_branch2a
I0623 09:45:08.108865  1897 net.cpp:122] Setting up res4e_branch2a
I0623 09:45:08.108888  1897 net.cpp:129] Top shape: 8 256 16 16 (524288)
I0623 09:45:08.108907  1897 net.cpp:137] Memory required for data: 2155872352
I0623 09:45:08.108925  1897 layer_factory.hpp:77] Creating layer bn4e_branch2a
I0623 09:45:08.108944  1897 net.cpp:84] Creating Layer bn4e_branch2a
I0623 09:45:08.108960  1897 net.cpp:406] bn4e_branch2a <- res4e_branch2a
I0623 09:45:08.108978  1897 net.cpp:367] bn4e_branch2a -> res4e_branch2a (in-place)
I0623 09:45:08.109004  1897 net.cpp:122] Setting up bn4e_branch2a
I0623 09:45:08.109021  1897 net.cpp:129] Top shape: 8 256 16 16 (524288)
I0623 09:45:08.109036  1897 net.cpp:137] Memory required for data: 2157969504
I0623 09:45:08.109056  1897 layer_factory.hpp:77] Creating layer scale4e_branch2a
I0623 09:45:08.109074  1897 net.cpp:84] Creating Layer scale4e_branch2a
I0623 09:45:08.109091  1897 net.cpp:406] scale4e_branch2a <- res4e_branch2a
I0623 09:45:08.109107  1897 net.cpp:367] scale4e_branch2a -> res4e_branch2a (in-place)
I0623 09:45:08.109128  1897 layer_factory.hpp:77] Creating layer scale4e_branch2a
I0623 09:45:08.109155  1897 net.cpp:122] Setting up scale4e_branch2a
I0623 09:45:08.109174  1897 net.cpp:129] Top shape: 8 256 16 16 (524288)
I0623 09:45:08.109189  1897 net.cpp:137] Memory required for data: 2160066656
I0623 09:45:08.109208  1897 layer_factory.hpp:77] Creating layer res4e_branch2a_relu
I0623 09:45:08.109225  1897 net.cpp:84] Creating Layer res4e_branch2a_relu
I0623 09:45:08.109241  1897 net.cpp:406] res4e_branch2a_relu <- res4e_branch2a
I0623 09:45:08.109258  1897 net.cpp:367] res4e_branch2a_relu -> res4e_branch2a (in-place)
I0623 09:45:08.109277  1897 net.cpp:122] Setting up res4e_branch2a_relu
I0623 09:45:08.109294  1897 net.cpp:129] Top shape: 8 256 16 16 (524288)
I0623 09:45:08.109309  1897 net.cpp:137] Memory required for data: 2162163808
I0623 09:45:08.109324  1897 layer_factory.hpp:77] Creating layer res4e_branch2b
I0623 09:45:08.109344  1897 net.cpp:84] Creating Layer res4e_branch2b
I0623 09:45:08.109359  1897 net.cpp:406] res4e_branch2b <- res4e_branch2a
I0623 09:45:08.109377  1897 net.cpp:380] res4e_branch2b -> res4e_branch2b
I0623 09:45:08.110388  1897 net.cpp:122] Setting up res4e_branch2b
I0623 09:45:08.110417  1897 net.cpp:129] Top shape: 8 256 16 16 (524288)
I0623 09:45:08.110432  1897 net.cpp:137] Memory required for data: 2164260960
I0623 09:45:08.110450  1897 layer_factory.hpp:77] Creating layer bn4e_branch2b
I0623 09:45:08.110468  1897 net.cpp:84] Creating Layer bn4e_branch2b
I0623 09:45:08.110486  1897 net.cpp:406] bn4e_branch2b <- res4e_branch2b
I0623 09:45:08.110502  1897 net.cpp:367] bn4e_branch2b -> res4e_branch2b (in-place)
I0623 09:45:08.110528  1897 net.cpp:122] Setting up bn4e_branch2b
I0623 09:45:08.110546  1897 net.cpp:129] Top shape: 8 256 16 16 (524288)
I0623 09:45:08.110561  1897 net.cpp:137] Memory required for data: 2166358112
I0623 09:45:08.110581  1897 layer_factory.hpp:77] Creating layer scale4e_branch2b
I0623 09:45:08.110600  1897 net.cpp:84] Creating Layer scale4e_branch2b
I0623 09:45:08.110616  1897 net.cpp:406] scale4e_branch2b <- res4e_branch2b
I0623 09:45:08.110633  1897 net.cpp:367] scale4e_branch2b -> res4e_branch2b (in-place)
I0623 09:45:08.110656  1897 layer_factory.hpp:77] Creating layer scale4e_branch2b
I0623 09:45:08.110687  1897 net.cpp:122] Setting up scale4e_branch2b
I0623 09:45:08.110708  1897 net.cpp:129] Top shape: 8 256 16 16 (524288)
I0623 09:45:08.110723  1897 net.cpp:137] Memory required for data: 2168455264
I0623 09:45:08.110741  1897 layer_factory.hpp:77] Creating layer res4e_branch2b_relu
I0623 09:45:08.110759  1897 net.cpp:84] Creating Layer res4e_branch2b_relu
I0623 09:45:08.110774  1897 net.cpp:406] res4e_branch2b_relu <- res4e_branch2b
I0623 09:45:08.110791  1897 net.cpp:367] res4e_branch2b_relu -> res4e_branch2b (in-place)
I0623 09:45:08.110810  1897 net.cpp:122] Setting up res4e_branch2b_relu
I0623 09:45:08.110826  1897 net.cpp:129] Top shape: 8 256 16 16 (524288)
I0623 09:45:08.110841  1897 net.cpp:137] Memory required for data: 2170552416
I0623 09:45:08.110857  1897 layer_factory.hpp:77] Creating layer res4e_branch2c
I0623 09:45:08.110875  1897 net.cpp:84] Creating Layer res4e_branch2c
I0623 09:45:08.110895  1897 net.cpp:406] res4e_branch2c <- res4e_branch2b
I0623 09:45:08.110913  1897 net.cpp:380] res4e_branch2c -> res4e_branch2c
I0623 09:45:08.111379  1897 net.cpp:122] Setting up res4e_branch2c
I0623 09:45:08.111404  1897 net.cpp:129] Top shape: 8 1024 16 16 (2097152)
I0623 09:45:08.111419  1897 net.cpp:137] Memory required for data: 2178941024
I0623 09:45:08.111436  1897 layer_factory.hpp:77] Creating layer bn4e_branch2c
I0623 09:45:08.111454  1897 net.cpp:84] Creating Layer bn4e_branch2c
I0623 09:45:08.111469  1897 net.cpp:406] bn4e_branch2c <- res4e_branch2c
I0623 09:45:08.111486  1897 net.cpp:367] bn4e_branch2c -> res4e_branch2c (in-place)
I0623 09:45:08.111512  1897 net.cpp:122] Setting up bn4e_branch2c
I0623 09:45:08.111531  1897 net.cpp:129] Top shape: 8 1024 16 16 (2097152)
I0623 09:45:08.111544  1897 net.cpp:137] Memory required for data: 2187329632
I0623 09:45:08.111564  1897 layer_factory.hpp:77] Creating layer scale4e_branch2c
I0623 09:45:08.111582  1897 net.cpp:84] Creating Layer scale4e_branch2c
I0623 09:45:08.111599  1897 net.cpp:406] scale4e_branch2c <- res4e_branch2c
I0623 09:45:08.111626  1897 net.cpp:367] scale4e_branch2c -> res4e_branch2c (in-place)
I0623 09:45:08.111650  1897 layer_factory.hpp:77] Creating layer scale4e_branch2c
I0623 09:45:08.111677  1897 net.cpp:122] Setting up scale4e_branch2c
I0623 09:45:08.111696  1897 net.cpp:129] Top shape: 8 1024 16 16 (2097152)
I0623 09:45:08.111711  1897 net.cpp:137] Memory required for data: 2195718240
I0623 09:45:08.111729  1897 layer_factory.hpp:77] Creating layer res4e
I0623 09:45:08.111747  1897 net.cpp:84] Creating Layer res4e
I0623 09:45:08.111763  1897 net.cpp:406] res4e <- res4d_res4d_relu_0_split_1
I0623 09:45:08.111779  1897 net.cpp:406] res4e <- res4e_branch2c
I0623 09:45:08.111796  1897 net.cpp:380] res4e -> res4e
I0623 09:45:08.111815  1897 net.cpp:122] Setting up res4e
I0623 09:45:08.111834  1897 net.cpp:129] Top shape: 8 1024 16 16 (2097152)
I0623 09:45:08.111847  1897 net.cpp:137] Memory required for data: 2204106848
I0623 09:45:08.111862  1897 layer_factory.hpp:77] Creating layer res4e_relu
I0623 09:45:08.111879  1897 net.cpp:84] Creating Layer res4e_relu
I0623 09:45:08.111894  1897 net.cpp:406] res4e_relu <- res4e
I0623 09:45:08.111910  1897 net.cpp:367] res4e_relu -> res4e (in-place)
I0623 09:45:08.111928  1897 net.cpp:122] Setting up res4e_relu
I0623 09:45:08.111945  1897 net.cpp:129] Top shape: 8 1024 16 16 (2097152)
I0623 09:45:08.111959  1897 net.cpp:137] Memory required for data: 2212495456
I0623 09:45:08.111974  1897 layer_factory.hpp:77] Creating layer res4e_res4e_relu_0_split
I0623 09:45:08.111991  1897 net.cpp:84] Creating Layer res4e_res4e_relu_0_split
I0623 09:45:08.112006  1897 net.cpp:406] res4e_res4e_relu_0_split <- res4e
I0623 09:45:08.112023  1897 net.cpp:380] res4e_res4e_relu_0_split -> res4e_res4e_relu_0_split_0
I0623 09:45:08.112041  1897 net.cpp:380] res4e_res4e_relu_0_split -> res4e_res4e_relu_0_split_1
I0623 09:45:08.112061  1897 net.cpp:122] Setting up res4e_res4e_relu_0_split
I0623 09:45:08.112078  1897 net.cpp:129] Top shape: 8 1024 16 16 (2097152)
I0623 09:45:08.112094  1897 net.cpp:129] Top shape: 8 1024 16 16 (2097152)
I0623 09:45:08.112109  1897 net.cpp:137] Memory required for data: 2229272672
I0623 09:45:08.112124  1897 layer_factory.hpp:77] Creating layer res4f_branch2a
I0623 09:45:08.112143  1897 net.cpp:84] Creating Layer res4f_branch2a
I0623 09:45:08.112159  1897 net.cpp:406] res4f_branch2a <- res4e_res4e_relu_0_split_0
I0623 09:45:08.112176  1897 net.cpp:380] res4f_branch2a -> res4f_branch2a
I0623 09:45:08.112642  1897 net.cpp:122] Setting up res4f_branch2a
I0623 09:45:08.112665  1897 net.cpp:129] Top shape: 8 256 16 16 (524288)
I0623 09:45:08.112680  1897 net.cpp:137] Memory required for data: 2231369824
I0623 09:45:08.112697  1897 layer_factory.hpp:77] Creating layer bn4f_branch2a
I0623 09:45:08.112715  1897 net.cpp:84] Creating Layer bn4f_branch2a
I0623 09:45:08.112731  1897 net.cpp:406] bn4f_branch2a <- res4f_branch2a
I0623 09:45:08.112748  1897 net.cpp:367] bn4f_branch2a -> res4f_branch2a (in-place)
I0623 09:45:08.112778  1897 net.cpp:122] Setting up bn4f_branch2a
I0623 09:45:08.112797  1897 net.cpp:129] Top shape: 8 256 16 16 (524288)
I0623 09:45:08.112812  1897 net.cpp:137] Memory required for data: 2233466976
I0623 09:45:08.112831  1897 layer_factory.hpp:77] Creating layer scale4f_branch2a
I0623 09:45:08.112849  1897 net.cpp:84] Creating Layer scale4f_branch2a
I0623 09:45:08.112864  1897 net.cpp:406] scale4f_branch2a <- res4f_branch2a
I0623 09:45:08.112880  1897 net.cpp:367] scale4f_branch2a -> res4f_branch2a (in-place)
I0623 09:45:08.112902  1897 layer_factory.hpp:77] Creating layer scale4f_branch2a
I0623 09:45:08.112927  1897 net.cpp:122] Setting up scale4f_branch2a
I0623 09:45:08.112946  1897 net.cpp:129] Top shape: 8 256 16 16 (524288)
I0623 09:45:08.112960  1897 net.cpp:137] Memory required for data: 2235564128
I0623 09:45:08.112978  1897 layer_factory.hpp:77] Creating layer res4f_branch2a_relu
I0623 09:45:08.112995  1897 net.cpp:84] Creating Layer res4f_branch2a_relu
I0623 09:45:08.113010  1897 net.cpp:406] res4f_branch2a_relu <- res4f_branch2a
I0623 09:45:08.113028  1897 net.cpp:367] res4f_branch2a_relu -> res4f_branch2a (in-place)
I0623 09:45:08.113044  1897 net.cpp:122] Setting up res4f_branch2a_relu
I0623 09:45:08.113061  1897 net.cpp:129] Top shape: 8 256 16 16 (524288)
I0623 09:45:08.113076  1897 net.cpp:137] Memory required for data: 2237661280
I0623 09:45:08.113090  1897 layer_factory.hpp:77] Creating layer res4f_branch2b
I0623 09:45:08.113109  1897 net.cpp:84] Creating Layer res4f_branch2b
I0623 09:45:08.113124  1897 net.cpp:406] res4f_branch2b <- res4f_branch2a
I0623 09:45:08.113142  1897 net.cpp:380] res4f_branch2b -> res4f_branch2b
I0623 09:45:08.127765  1897 net.cpp:122] Setting up res4f_branch2b
I0623 09:45:08.127799  1897 net.cpp:129] Top shape: 8 256 16 16 (524288)
I0623 09:45:08.127804  1897 net.cpp:137] Memory required for data: 2239758432
I0623 09:45:08.127815  1897 layer_factory.hpp:77] Creating layer bn4f_branch2b
I0623 09:45:08.127826  1897 net.cpp:84] Creating Layer bn4f_branch2b
I0623 09:45:08.127837  1897 net.cpp:406] bn4f_branch2b <- res4f_branch2b
I0623 09:45:08.127846  1897 net.cpp:367] bn4f_branch2b -> res4f_branch2b (in-place)
I0623 09:45:08.127866  1897 net.cpp:122] Setting up bn4f_branch2b
I0623 09:45:08.127872  1897 net.cpp:129] Top shape: 8 256 16 16 (524288)
I0623 09:45:08.127876  1897 net.cpp:137] Memory required for data: 2241855584
I0623 09:45:08.127885  1897 layer_factory.hpp:77] Creating layer scale4f_branch2b
I0623 09:45:08.127894  1897 net.cpp:84] Creating Layer scale4f_branch2b
I0623 09:45:08.127898  1897 net.cpp:406] scale4f_branch2b <- res4f_branch2b
I0623 09:45:08.127903  1897 net.cpp:367] scale4f_branch2b -> res4f_branch2b (in-place)
I0623 09:45:08.127918  1897 layer_factory.hpp:77] Creating layer scale4f_branch2b
I0623 09:45:08.127935  1897 net.cpp:122] Setting up scale4f_branch2b
I0623 09:45:08.127943  1897 net.cpp:129] Top shape: 8 256 16 16 (524288)
I0623 09:45:08.127946  1897 net.cpp:137] Memory required for data: 2243952736
I0623 09:45:08.127952  1897 layer_factory.hpp:77] Creating layer res4f_branch2b_relu
I0623 09:45:08.127960  1897 net.cpp:84] Creating Layer res4f_branch2b_relu
I0623 09:45:08.127964  1897 net.cpp:406] res4f_branch2b_relu <- res4f_branch2b
I0623 09:45:08.127969  1897 net.cpp:367] res4f_branch2b_relu -> res4f_branch2b (in-place)
I0623 09:45:08.127975  1897 net.cpp:122] Setting up res4f_branch2b_relu
I0623 09:45:08.127981  1897 net.cpp:129] Top shape: 8 256 16 16 (524288)
I0623 09:45:08.127985  1897 net.cpp:137] Memory required for data: 2246049888
I0623 09:45:08.127990  1897 layer_factory.hpp:77] Creating layer res4f_branch2c
I0623 09:45:08.127998  1897 net.cpp:84] Creating Layer res4f_branch2c
I0623 09:45:08.128002  1897 net.cpp:406] res4f_branch2c <- res4f_branch2b
I0623 09:45:08.128008  1897 net.cpp:380] res4f_branch2c -> res4f_branch2c
I0623 09:45:08.128492  1897 net.cpp:122] Setting up res4f_branch2c
I0623 09:45:08.128504  1897 net.cpp:129] Top shape: 8 1024 16 16 (2097152)
I0623 09:45:08.128509  1897 net.cpp:137] Memory required for data: 2254438496
I0623 09:45:08.128513  1897 layer_factory.hpp:77] Creating layer bn4f_branch2c
I0623 09:45:08.128520  1897 net.cpp:84] Creating Layer bn4f_branch2c
I0623 09:45:08.128525  1897 net.cpp:406] bn4f_branch2c <- res4f_branch2c
I0623 09:45:08.128530  1897 net.cpp:367] bn4f_branch2c -> res4f_branch2c (in-place)
I0623 09:45:08.128545  1897 net.cpp:122] Setting up bn4f_branch2c
I0623 09:45:08.128552  1897 net.cpp:129] Top shape: 8 1024 16 16 (2097152)
I0623 09:45:08.128556  1897 net.cpp:137] Memory required for data: 2262827104
I0623 09:45:08.128593  1897 layer_factory.hpp:77] Creating layer scale4f_branch2c
I0623 09:45:08.128602  1897 net.cpp:84] Creating Layer scale4f_branch2c
I0623 09:45:08.128607  1897 net.cpp:406] scale4f_branch2c <- res4f_branch2c
I0623 09:45:08.128612  1897 net.cpp:367] scale4f_branch2c -> res4f_branch2c (in-place)
I0623 09:45:08.128623  1897 layer_factory.hpp:77] Creating layer scale4f_branch2c
I0623 09:45:08.128639  1897 net.cpp:122] Setting up scale4f_branch2c
I0623 09:45:08.128648  1897 net.cpp:129] Top shape: 8 1024 16 16 (2097152)
I0623 09:45:08.128651  1897 net.cpp:137] Memory required for data: 2271215712
I0623 09:45:08.128659  1897 layer_factory.hpp:77] Creating layer res4f
I0623 09:45:08.128665  1897 net.cpp:84] Creating Layer res4f
I0623 09:45:08.128670  1897 net.cpp:406] res4f <- res4e_res4e_relu_0_split_1
I0623 09:45:08.128675  1897 net.cpp:406] res4f <- res4f_branch2c
I0623 09:45:08.128680  1897 net.cpp:380] res4f -> res4f
I0623 09:45:08.128690  1897 net.cpp:122] Setting up res4f
I0623 09:45:08.128695  1897 net.cpp:129] Top shape: 8 1024 16 16 (2097152)
I0623 09:45:08.128700  1897 net.cpp:137] Memory required for data: 2279604320
I0623 09:45:08.128703  1897 layer_factory.hpp:77] Creating layer res4f_relu
I0623 09:45:08.128710  1897 net.cpp:84] Creating Layer res4f_relu
I0623 09:45:08.128713  1897 net.cpp:406] res4f_relu <- res4f
I0623 09:45:08.128718  1897 net.cpp:367] res4f_relu -> res4f (in-place)
I0623 09:45:08.128724  1897 net.cpp:122] Setting up res4f_relu
I0623 09:45:08.128731  1897 net.cpp:129] Top shape: 8 1024 16 16 (2097152)
I0623 09:45:08.128733  1897 net.cpp:137] Memory required for data: 2287992928
I0623 09:45:08.128737  1897 layer_factory.hpp:77] Creating layer res4f_res4f_relu_0_split
I0623 09:45:08.128743  1897 net.cpp:84] Creating Layer res4f_res4f_relu_0_split
I0623 09:45:08.128747  1897 net.cpp:406] res4f_res4f_relu_0_split <- res4f
I0623 09:45:08.128753  1897 net.cpp:380] res4f_res4f_relu_0_split -> res4f_res4f_relu_0_split_0
I0623 09:45:08.128759  1897 net.cpp:380] res4f_res4f_relu_0_split -> res4f_res4f_relu_0_split_1
I0623 09:45:08.128767  1897 net.cpp:122] Setting up res4f_res4f_relu_0_split
I0623 09:45:08.128772  1897 net.cpp:129] Top shape: 8 1024 16 16 (2097152)
I0623 09:45:08.128777  1897 net.cpp:129] Top shape: 8 1024 16 16 (2097152)
I0623 09:45:08.128782  1897 net.cpp:137] Memory required for data: 2304770144
I0623 09:45:08.128785  1897 layer_factory.hpp:77] Creating layer res5a_branch1
I0623 09:45:08.128793  1897 net.cpp:84] Creating Layer res5a_branch1
I0623 09:45:08.128798  1897 net.cpp:406] res5a_branch1 <- res4f_res4f_relu_0_split_0
I0623 09:45:08.128803  1897 net.cpp:380] res5a_branch1 -> res5a_branch1
I0623 09:45:08.152813  1897 net.cpp:122] Setting up res5a_branch1
I0623 09:45:08.152845  1897 net.cpp:129] Top shape: 8 2048 8 8 (1048576)
I0623 09:45:08.152850  1897 net.cpp:137] Memory required for data: 2308964448
I0623 09:45:08.152860  1897 layer_factory.hpp:77] Creating layer bn5a_branch1
I0623 09:45:08.152873  1897 net.cpp:84] Creating Layer bn5a_branch1
I0623 09:45:08.152884  1897 net.cpp:406] bn5a_branch1 <- res5a_branch1
I0623 09:45:08.152892  1897 net.cpp:367] bn5a_branch1 -> res5a_branch1 (in-place)
I0623 09:45:08.152915  1897 net.cpp:122] Setting up bn5a_branch1
I0623 09:45:08.152921  1897 net.cpp:129] Top shape: 8 2048 8 8 (1048576)
I0623 09:45:08.152925  1897 net.cpp:137] Memory required for data: 2313158752
I0623 09:45:08.152935  1897 layer_factory.hpp:77] Creating layer scale5a_branch1
I0623 09:45:08.152942  1897 net.cpp:84] Creating Layer scale5a_branch1
I0623 09:45:08.152947  1897 net.cpp:406] scale5a_branch1 <- res5a_branch1
I0623 09:45:08.152952  1897 net.cpp:367] scale5a_branch1 -> res5a_branch1 (in-place)
I0623 09:45:08.152966  1897 layer_factory.hpp:77] Creating layer scale5a_branch1
I0623 09:45:08.152984  1897 net.cpp:122] Setting up scale5a_branch1
I0623 09:45:08.152992  1897 net.cpp:129] Top shape: 8 2048 8 8 (1048576)
I0623 09:45:08.152997  1897 net.cpp:137] Memory required for data: 2317353056
I0623 09:45:08.153002  1897 layer_factory.hpp:77] Creating layer res5a_branch2a
I0623 09:45:08.153013  1897 net.cpp:84] Creating Layer res5a_branch2a
I0623 09:45:08.153019  1897 net.cpp:406] res5a_branch2a <- res4f_res4f_relu_0_split_1
I0623 09:45:08.153025  1897 net.cpp:380] res5a_branch2a -> res5a_branch2a
I0623 09:45:08.153980  1897 net.cpp:122] Setting up res5a_branch2a
I0623 09:45:08.153992  1897 net.cpp:129] Top shape: 8 512 8 8 (262144)
I0623 09:45:08.153996  1897 net.cpp:137] Memory required for data: 2318401632
I0623 09:45:08.154002  1897 layer_factory.hpp:77] Creating layer bn5a_branch2a
I0623 09:45:08.154011  1897 net.cpp:84] Creating Layer bn5a_branch2a
I0623 09:45:08.154016  1897 net.cpp:406] bn5a_branch2a <- res5a_branch2a
I0623 09:45:08.154021  1897 net.cpp:367] bn5a_branch2a -> res5a_branch2a (in-place)
I0623 09:45:08.154036  1897 net.cpp:122] Setting up bn5a_branch2a
I0623 09:45:08.154043  1897 net.cpp:129] Top shape: 8 512 8 8 (262144)
I0623 09:45:08.154047  1897 net.cpp:137] Memory required for data: 2319450208
I0623 09:45:08.154055  1897 layer_factory.hpp:77] Creating layer scale5a_branch2a
I0623 09:45:08.154062  1897 net.cpp:84] Creating Layer scale5a_branch2a
I0623 09:45:08.154067  1897 net.cpp:406] scale5a_branch2a <- res5a_branch2a
I0623 09:45:08.154072  1897 net.cpp:367] scale5a_branch2a -> res5a_branch2a (in-place)
I0623 09:45:08.154083  1897 layer_factory.hpp:77] Creating layer scale5a_branch2a
I0623 09:45:08.154098  1897 net.cpp:122] Setting up scale5a_branch2a
I0623 09:45:08.154103  1897 net.cpp:129] Top shape: 8 512 8 8 (262144)
I0623 09:45:08.154108  1897 net.cpp:137] Memory required for data: 2320498784
I0623 09:45:08.154114  1897 layer_factory.hpp:77] Creating layer res5a_branch2a_relu
I0623 09:45:08.154121  1897 net.cpp:84] Creating Layer res5a_branch2a_relu
I0623 09:45:08.154126  1897 net.cpp:406] res5a_branch2a_relu <- res5a_branch2a
I0623 09:45:08.154132  1897 net.cpp:367] res5a_branch2a_relu -> res5a_branch2a (in-place)
I0623 09:45:08.154139  1897 net.cpp:122] Setting up res5a_branch2a_relu
I0623 09:45:08.154145  1897 net.cpp:129] Top shape: 8 512 8 8 (262144)
I0623 09:45:08.154148  1897 net.cpp:137] Memory required for data: 2321547360
I0623 09:45:08.154152  1897 layer_factory.hpp:77] Creating layer res5a_branch2b
I0623 09:45:08.154160  1897 net.cpp:84] Creating Layer res5a_branch2b
I0623 09:45:08.154165  1897 net.cpp:406] res5a_branch2b <- res5a_branch2a
I0623 09:45:08.154170  1897 net.cpp:380] res5a_branch2b -> res5a_branch2b
I0623 09:45:08.217097  1897 net.cpp:122] Setting up res5a_branch2b
I0623 09:45:08.217171  1897 net.cpp:129] Top shape: 8 512 8 8 (262144)
I0623 09:45:08.217190  1897 net.cpp:137] Memory required for data: 2322595936
I0623 09:45:08.217208  1897 layer_factory.hpp:77] Creating layer bn5a_branch2b
I0623 09:45:08.217233  1897 net.cpp:84] Creating Layer bn5a_branch2b
I0623 09:45:08.217252  1897 net.cpp:406] bn5a_branch2b <- res5a_branch2b
I0623 09:45:08.217270  1897 net.cpp:367] bn5a_branch2b -> res5a_branch2b (in-place)
I0623 09:45:08.217301  1897 net.cpp:122] Setting up bn5a_branch2b
I0623 09:45:08.217319  1897 net.cpp:129] Top shape: 8 512 8 8 (262144)
I0623 09:45:08.217332  1897 net.cpp:137] Memory required for data: 2323644512
I0623 09:45:08.217351  1897 layer_factory.hpp:77] Creating layer scale5a_branch2b
I0623 09:45:08.217371  1897 net.cpp:84] Creating Layer scale5a_branch2b
I0623 09:45:08.217384  1897 net.cpp:406] scale5a_branch2b <- res5a_branch2b
I0623 09:45:08.217401  1897 net.cpp:367] scale5a_branch2b -> res5a_branch2b (in-place)
I0623 09:45:08.217437  1897 layer_factory.hpp:77] Creating layer scale5a_branch2b
I0623 09:45:08.217468  1897 net.cpp:122] Setting up scale5a_branch2b
I0623 09:45:08.217486  1897 net.cpp:129] Top shape: 8 512 8 8 (262144)
I0623 09:45:08.217500  1897 net.cpp:137] Memory required for data: 2324693088
I0623 09:45:08.217517  1897 layer_factory.hpp:77] Creating layer res5a_branch2b_relu
I0623 09:45:08.217535  1897 net.cpp:84] Creating Layer res5a_branch2b_relu
I0623 09:45:08.217550  1897 net.cpp:406] res5a_branch2b_relu <- res5a_branch2b
I0623 09:45:08.217564  1897 net.cpp:367] res5a_branch2b_relu -> res5a_branch2b (in-place)
I0623 09:45:08.217581  1897 net.cpp:122] Setting up res5a_branch2b_relu
I0623 09:45:08.217598  1897 net.cpp:129] Top shape: 8 512 8 8 (262144)
I0623 09:45:08.217612  1897 net.cpp:137] Memory required for data: 2325741664
I0623 09:45:08.217623  1897 layer_factory.hpp:77] Creating layer res5a_branch2c
I0623 09:45:08.217644  1897 net.cpp:84] Creating Layer res5a_branch2c
I0623 09:45:08.217658  1897 net.cpp:406] res5a_branch2c <- res5a_branch2b
I0623 09:45:08.217674  1897 net.cpp:380] res5a_branch2c -> res5a_branch2c
I0623 09:45:08.228549  1897 net.cpp:122] Setting up res5a_branch2c
I0623 09:45:08.228590  1897 net.cpp:129] Top shape: 8 2048 8 8 (1048576)
I0623 09:45:08.228595  1897 net.cpp:137] Memory required for data: 2329935968
I0623 09:45:08.228606  1897 layer_factory.hpp:77] Creating layer bn5a_branch2c
I0623 09:45:08.228621  1897 net.cpp:84] Creating Layer bn5a_branch2c
I0623 09:45:08.228629  1897 net.cpp:406] bn5a_branch2c <- res5a_branch2c
I0623 09:45:08.228670  1897 net.cpp:367] bn5a_branch2c -> res5a_branch2c (in-place)
I0623 09:45:08.228711  1897 net.cpp:122] Setting up bn5a_branch2c
I0623 09:45:08.228735  1897 net.cpp:129] Top shape: 8 2048 8 8 (1048576)
I0623 09:45:08.228754  1897 net.cpp:137] Memory required for data: 2334130272
I0623 09:45:08.228777  1897 layer_factory.hpp:77] Creating layer scale5a_branch2c
I0623 09:45:08.228801  1897 net.cpp:84] Creating Layer scale5a_branch2c
I0623 09:45:08.228821  1897 net.cpp:406] scale5a_branch2c <- res5a_branch2c
I0623 09:45:08.228840  1897 net.cpp:367] scale5a_branch2c -> res5a_branch2c (in-place)
I0623 09:45:08.228873  1897 layer_factory.hpp:77] Creating layer scale5a_branch2c
I0623 09:45:08.228907  1897 net.cpp:122] Setting up scale5a_branch2c
I0623 09:45:08.228929  1897 net.cpp:129] Top shape: 8 2048 8 8 (1048576)
I0623 09:45:08.228947  1897 net.cpp:137] Memory required for data: 2338324576
I0623 09:45:08.228970  1897 layer_factory.hpp:77] Creating layer res5a
I0623 09:45:08.228991  1897 net.cpp:84] Creating Layer res5a
I0623 09:45:08.229009  1897 net.cpp:406] res5a <- res5a_branch1
I0623 09:45:08.229028  1897 net.cpp:406] res5a <- res5a_branch2c
I0623 09:45:08.229050  1897 net.cpp:380] res5a -> res5a
I0623 09:45:08.229074  1897 net.cpp:122] Setting up res5a
I0623 09:45:08.229096  1897 net.cpp:129] Top shape: 8 2048 8 8 (1048576)
I0623 09:45:08.229113  1897 net.cpp:137] Memory required for data: 2342518880
I0623 09:45:08.229131  1897 layer_factory.hpp:77] Creating layer res5a_relu
I0623 09:45:08.229153  1897 net.cpp:84] Creating Layer res5a_relu
I0623 09:45:08.229171  1897 net.cpp:406] res5a_relu <- res5a
I0623 09:45:08.229192  1897 net.cpp:367] res5a_relu -> res5a (in-place)
I0623 09:45:08.229213  1897 net.cpp:122] Setting up res5a_relu
I0623 09:45:08.229234  1897 net.cpp:129] Top shape: 8 2048 8 8 (1048576)
I0623 09:45:08.229251  1897 net.cpp:137] Memory required for data: 2346713184
I0623 09:45:08.229269  1897 layer_factory.hpp:77] Creating layer res5a_res5a_relu_0_split
I0623 09:45:08.229290  1897 net.cpp:84] Creating Layer res5a_res5a_relu_0_split
I0623 09:45:08.229310  1897 net.cpp:406] res5a_res5a_relu_0_split <- res5a
I0623 09:45:08.229331  1897 net.cpp:380] res5a_res5a_relu_0_split -> res5a_res5a_relu_0_split_0
I0623 09:45:08.229353  1897 net.cpp:380] res5a_res5a_relu_0_split -> res5a_res5a_relu_0_split_1
I0623 09:45:08.229377  1897 net.cpp:122] Setting up res5a_res5a_relu_0_split
I0623 09:45:08.229398  1897 net.cpp:129] Top shape: 8 2048 8 8 (1048576)
I0623 09:45:08.229427  1897 net.cpp:129] Top shape: 8 2048 8 8 (1048576)
I0623 09:45:08.229446  1897 net.cpp:137] Memory required for data: 2355101792
I0623 09:45:08.229465  1897 layer_factory.hpp:77] Creating layer res5b_branch2a
I0623 09:45:08.229488  1897 net.cpp:84] Creating Layer res5b_branch2a
I0623 09:45:08.229508  1897 net.cpp:406] res5b_branch2a <- res5a_res5a_relu_0_split_0
I0623 09:45:08.229531  1897 net.cpp:380] res5b_branch2a -> res5b_branch2a
I0623 09:45:08.252588  1897 net.cpp:122] Setting up res5b_branch2a
I0623 09:45:08.252625  1897 net.cpp:129] Top shape: 8 512 8 8 (262144)
I0623 09:45:08.252630  1897 net.cpp:137] Memory required for data: 2356150368
I0623 09:45:08.252640  1897 layer_factory.hpp:77] Creating layer bn5b_branch2a
I0623 09:45:08.252651  1897 net.cpp:84] Creating Layer bn5b_branch2a
I0623 09:45:08.252660  1897 net.cpp:406] bn5b_branch2a <- res5b_branch2a
I0623 09:45:08.252667  1897 net.cpp:367] bn5b_branch2a -> res5b_branch2a (in-place)
I0623 09:45:08.252686  1897 net.cpp:122] Setting up bn5b_branch2a
I0623 09:45:08.252692  1897 net.cpp:129] Top shape: 8 512 8 8 (262144)
I0623 09:45:08.252696  1897 net.cpp:137] Memory required for data: 2357198944
I0623 09:45:08.252704  1897 layer_factory.hpp:77] Creating layer scale5b_branch2a
I0623 09:45:08.252712  1897 net.cpp:84] Creating Layer scale5b_branch2a
I0623 09:45:08.252717  1897 net.cpp:406] scale5b_branch2a <- res5b_branch2a
I0623 09:45:08.252723  1897 net.cpp:367] scale5b_branch2a -> res5b_branch2a (in-place)
I0623 09:45:08.252737  1897 layer_factory.hpp:77] Creating layer scale5b_branch2a
I0623 09:45:08.252755  1897 net.cpp:122] Setting up scale5b_branch2a
I0623 09:45:08.252763  1897 net.cpp:129] Top shape: 8 512 8 8 (262144)
I0623 09:45:08.252766  1897 net.cpp:137] Memory required for data: 2358247520
I0623 09:45:08.252773  1897 layer_factory.hpp:77] Creating layer res5b_branch2a_relu
I0623 09:45:08.252779  1897 net.cpp:84] Creating Layer res5b_branch2a_relu
I0623 09:45:08.252784  1897 net.cpp:406] res5b_branch2a_relu <- res5b_branch2a
I0623 09:45:08.252789  1897 net.cpp:367] res5b_branch2a_relu -> res5b_branch2a (in-place)
I0623 09:45:08.252796  1897 net.cpp:122] Setting up res5b_branch2a_relu
I0623 09:45:08.252804  1897 net.cpp:129] Top shape: 8 512 8 8 (262144)
I0623 09:45:08.252809  1897 net.cpp:137] Memory required for data: 2359296096
I0623 09:45:08.252812  1897 layer_factory.hpp:77] Creating layer res5b_branch2b
I0623 09:45:08.252821  1897 net.cpp:84] Creating Layer res5b_branch2b
I0623 09:45:08.252825  1897 net.cpp:406] res5b_branch2b <- res5b_branch2a
I0623 09:45:08.252831  1897 net.cpp:380] res5b_branch2b -> res5b_branch2b
I0623 09:45:08.337107  1897 net.cpp:122] Setting up res5b_branch2b
I0623 09:45:08.337213  1897 net.cpp:129] Top shape: 8 512 8 8 (262144)
I0623 09:45:08.337231  1897 net.cpp:137] Memory required for data: 2360344672
I0623 09:45:08.337252  1897 layer_factory.hpp:77] Creating layer bn5b_branch2b
I0623 09:45:08.337280  1897 net.cpp:84] Creating Layer bn5b_branch2b
I0623 09:45:08.337298  1897 net.cpp:406] bn5b_branch2b <- res5b_branch2b
I0623 09:45:08.337318  1897 net.cpp:367] bn5b_branch2b -> res5b_branch2b (in-place)
I0623 09:45:08.337349  1897 net.cpp:122] Setting up bn5b_branch2b
I0623 09:45:08.337368  1897 net.cpp:129] Top shape: 8 512 8 8 (262144)
I0623 09:45:08.337383  1897 net.cpp:137] Memory required for data: 2361393248
I0623 09:45:08.337402  1897 layer_factory.hpp:77] Creating layer scale5b_branch2b
I0623 09:45:08.337424  1897 net.cpp:84] Creating Layer scale5b_branch2b
I0623 09:45:08.337438  1897 net.cpp:406] scale5b_branch2b <- res5b_branch2b
I0623 09:45:08.337455  1897 net.cpp:367] scale5b_branch2b -> res5b_branch2b (in-place)
I0623 09:45:08.337481  1897 layer_factory.hpp:77] Creating layer scale5b_branch2b
I0623 09:45:08.337512  1897 net.cpp:122] Setting up scale5b_branch2b
I0623 09:45:08.337529  1897 net.cpp:129] Top shape: 8 512 8 8 (262144)
I0623 09:45:08.337544  1897 net.cpp:137] Memory required for data: 2362441824
I0623 09:45:08.337563  1897 layer_factory.hpp:77] Creating layer res5b_branch2b_relu
I0623 09:45:08.337591  1897 net.cpp:84] Creating Layer res5b_branch2b_relu
I0623 09:45:08.337607  1897 net.cpp:406] res5b_branch2b_relu <- res5b_branch2b
I0623 09:45:08.337625  1897 net.cpp:367] res5b_branch2b_relu -> res5b_branch2b (in-place)
I0623 09:45:08.337643  1897 net.cpp:122] Setting up res5b_branch2b_relu
I0623 09:45:08.337661  1897 net.cpp:129] Top shape: 8 512 8 8 (262144)
I0623 09:45:08.337676  1897 net.cpp:137] Memory required for data: 2363490400
I0623 09:45:08.337690  1897 layer_factory.hpp:77] Creating layer res5b_branch2c
I0623 09:45:08.337712  1897 net.cpp:84] Creating Layer res5b_branch2c
I0623 09:45:08.337726  1897 net.cpp:406] res5b_branch2c <- res5b_branch2b
I0623 09:45:08.337744  1897 net.cpp:380] res5b_branch2c -> res5b_branch2c
I0623 09:45:08.348171  1897 net.cpp:122] Setting up res5b_branch2c
I0623 09:45:08.348234  1897 net.cpp:129] Top shape: 8 2048 8 8 (1048576)
I0623 09:45:08.348249  1897 net.cpp:137] Memory required for data: 2367684704
I0623 09:45:08.348268  1897 layer_factory.hpp:77] Creating layer bn5b_branch2c
I0623 09:45:08.348291  1897 net.cpp:84] Creating Layer bn5b_branch2c
I0623 09:45:08.348309  1897 net.cpp:406] bn5b_branch2c <- res5b_branch2c
I0623 09:45:08.348328  1897 net.cpp:367] bn5b_branch2c -> res5b_branch2c (in-place)
I0623 09:45:08.348359  1897 net.cpp:122] Setting up bn5b_branch2c
I0623 09:45:08.348378  1897 net.cpp:129] Top shape: 8 2048 8 8 (1048576)
I0623 09:45:08.348393  1897 net.cpp:137] Memory required for data: 2371879008
I0623 09:45:08.348412  1897 layer_factory.hpp:77] Creating layer scale5b_branch2c
I0623 09:45:08.348431  1897 net.cpp:84] Creating Layer scale5b_branch2c
I0623 09:45:08.348446  1897 net.cpp:406] scale5b_branch2c <- res5b_branch2c
I0623 09:45:08.348464  1897 net.cpp:367] scale5b_branch2c -> res5b_branch2c (in-place)
I0623 09:45:08.348490  1897 layer_factory.hpp:77] Creating layer scale5b_branch2c
I0623 09:45:08.348520  1897 net.cpp:122] Setting up scale5b_branch2c
I0623 09:45:08.348539  1897 net.cpp:129] Top shape: 8 2048 8 8 (1048576)
I0623 09:45:08.348553  1897 net.cpp:137] Memory required for data: 2376073312
I0623 09:45:08.348572  1897 layer_factory.hpp:77] Creating layer res5b
I0623 09:45:08.348589  1897 net.cpp:84] Creating Layer res5b
I0623 09:45:08.348605  1897 net.cpp:406] res5b <- res5a_res5a_relu_0_split_1
I0623 09:45:08.348621  1897 net.cpp:406] res5b <- res5b_branch2c
I0623 09:45:08.348639  1897 net.cpp:380] res5b -> res5b
I0623 09:45:08.348659  1897 net.cpp:122] Setting up res5b
I0623 09:45:08.348676  1897 net.cpp:129] Top shape: 8 2048 8 8 (1048576)
I0623 09:45:08.348690  1897 net.cpp:137] Memory required for data: 2380267616
I0623 09:45:08.348706  1897 layer_factory.hpp:77] Creating layer res5b_relu
I0623 09:45:08.348723  1897 net.cpp:84] Creating Layer res5b_relu
I0623 09:45:08.348738  1897 net.cpp:406] res5b_relu <- res5b
I0623 09:45:08.348754  1897 net.cpp:367] res5b_relu -> res5b (in-place)
I0623 09:45:08.348773  1897 net.cpp:122] Setting up res5b_relu
I0623 09:45:08.348788  1897 net.cpp:129] Top shape: 8 2048 8 8 (1048576)
I0623 09:45:08.348803  1897 net.cpp:137] Memory required for data: 2384461920
I0623 09:45:08.348817  1897 layer_factory.hpp:77] Creating layer res5b_res5b_relu_0_split
I0623 09:45:08.348834  1897 net.cpp:84] Creating Layer res5b_res5b_relu_0_split
I0623 09:45:08.348850  1897 net.cpp:406] res5b_res5b_relu_0_split <- res5b
I0623 09:45:08.348866  1897 net.cpp:380] res5b_res5b_relu_0_split -> res5b_res5b_relu_0_split_0
I0623 09:45:08.348883  1897 net.cpp:380] res5b_res5b_relu_0_split -> res5b_res5b_relu_0_split_1
I0623 09:45:08.348903  1897 net.cpp:122] Setting up res5b_res5b_relu_0_split
I0623 09:45:08.348922  1897 net.cpp:129] Top shape: 8 2048 8 8 (1048576)
I0623 09:45:08.348937  1897 net.cpp:129] Top shape: 8 2048 8 8 (1048576)
I0623 09:45:08.348951  1897 net.cpp:137] Memory required for data: 2392850528
I0623 09:45:08.348965  1897 layer_factory.hpp:77] Creating layer res5c_branch2a
I0623 09:45:08.348985  1897 net.cpp:84] Creating Layer res5c_branch2a
I0623 09:45:08.349001  1897 net.cpp:406] res5c_branch2a <- res5b_res5b_relu_0_split_0
I0623 09:45:08.349027  1897 net.cpp:380] res5c_branch2a -> res5c_branch2a
I0623 09:45:08.360221  1897 net.cpp:122] Setting up res5c_branch2a
I0623 09:45:08.360260  1897 net.cpp:129] Top shape: 8 512 8 8 (262144)
I0623 09:45:08.360265  1897 net.cpp:137] Memory required for data: 2393899104
I0623 09:45:08.360275  1897 layer_factory.hpp:77] Creating layer bn5c_branch2a
I0623 09:45:08.360286  1897 net.cpp:84] Creating Layer bn5c_branch2a
I0623 09:45:08.360293  1897 net.cpp:406] bn5c_branch2a <- res5c_branch2a
I0623 09:45:08.360301  1897 net.cpp:367] bn5c_branch2a -> res5c_branch2a (in-place)
I0623 09:45:08.360323  1897 net.cpp:122] Setting up bn5c_branch2a
I0623 09:45:08.360330  1897 net.cpp:129] Top shape: 8 512 8 8 (262144)
I0623 09:45:08.360334  1897 net.cpp:137] Memory required for data: 2394947680
I0623 09:45:08.360342  1897 layer_factory.hpp:77] Creating layer scale5c_branch2a
I0623 09:45:08.360352  1897 net.cpp:84] Creating Layer scale5c_branch2a
I0623 09:45:08.360358  1897 net.cpp:406] scale5c_branch2a <- res5c_branch2a
I0623 09:45:08.360363  1897 net.cpp:367] scale5c_branch2a -> res5c_branch2a (in-place)
I0623 09:45:08.360376  1897 layer_factory.hpp:77] Creating layer scale5c_branch2a
I0623 09:45:08.360393  1897 net.cpp:122] Setting up scale5c_branch2a
I0623 09:45:08.360399  1897 net.cpp:129] Top shape: 8 512 8 8 (262144)
I0623 09:45:08.360404  1897 net.cpp:137] Memory required for data: 2395996256
I0623 09:45:08.360410  1897 layer_factory.hpp:77] Creating layer res5c_branch2a_relu
I0623 09:45:08.360417  1897 net.cpp:84] Creating Layer res5c_branch2a_relu
I0623 09:45:08.360421  1897 net.cpp:406] res5c_branch2a_relu <- res5c_branch2a
I0623 09:45:08.360426  1897 net.cpp:367] res5c_branch2a_relu -> res5c_branch2a (in-place)
I0623 09:45:08.360432  1897 net.cpp:122] Setting up res5c_branch2a_relu
I0623 09:45:08.360438  1897 net.cpp:129] Top shape: 8 512 8 8 (262144)
I0623 09:45:08.360441  1897 net.cpp:137] Memory required for data: 2397044832
I0623 09:45:08.360445  1897 layer_factory.hpp:77] Creating layer res5c_branch2b
I0623 09:45:08.360455  1897 net.cpp:84] Creating Layer res5c_branch2b
I0623 09:45:08.360460  1897 net.cpp:406] res5c_branch2b <- res5c_branch2a
I0623 09:45:08.360465  1897 net.cpp:380] res5c_branch2b -> res5c_branch2b
I0623 09:45:08.485235  1897 net.cpp:122] Setting up res5c_branch2b
I0623 09:45:08.485282  1897 net.cpp:129] Top shape: 8 512 8 8 (262144)
I0623 09:45:08.485290  1897 net.cpp:137] Memory required for data: 2398093408
I0623 09:45:08.485301  1897 layer_factory.hpp:77] Creating layer bn5c_branch2b
I0623 09:45:08.485313  1897 net.cpp:84] Creating Layer bn5c_branch2b
I0623 09:45:08.485338  1897 net.cpp:406] bn5c_branch2b <- res5c_branch2b
I0623 09:45:08.485361  1897 net.cpp:367] bn5c_branch2b -> res5c_branch2b (in-place)
I0623 09:45:08.485384  1897 net.cpp:122] Setting up bn5c_branch2b
I0623 09:45:08.485393  1897 net.cpp:129] Top shape: 8 512 8 8 (262144)
I0623 09:45:08.485397  1897 net.cpp:137] Memory required for data: 2399141984
I0623 09:45:08.485407  1897 layer_factory.hpp:77] Creating layer scale5c_branch2b
I0623 09:45:08.485420  1897 net.cpp:84] Creating Layer scale5c_branch2b
I0623 09:45:08.485427  1897 net.cpp:406] scale5c_branch2b <- res5c_branch2b
I0623 09:45:08.485433  1897 net.cpp:367] scale5c_branch2b -> res5c_branch2b (in-place)
I0623 09:45:08.485447  1897 layer_factory.hpp:77] Creating layer scale5c_branch2b
I0623 09:45:08.485466  1897 net.cpp:122] Setting up scale5c_branch2b
I0623 09:45:08.485486  1897 net.cpp:129] Top shape: 8 512 8 8 (262144)
I0623 09:45:08.485496  1897 net.cpp:137] Memory required for data: 2400190560
I0623 09:45:08.485510  1897 layer_factory.hpp:77] Creating layer res5c_branch2b_relu
I0623 09:45:08.485525  1897 net.cpp:84] Creating Layer res5c_branch2b_relu
I0623 09:45:08.485536  1897 net.cpp:406] res5c_branch2b_relu <- res5c_branch2b
I0623 09:45:08.485548  1897 net.cpp:367] res5c_branch2b_relu -> res5c_branch2b (in-place)
I0623 09:45:08.485561  1897 net.cpp:122] Setting up res5c_branch2b_relu
I0623 09:45:08.485584  1897 net.cpp:129] Top shape: 8 512 8 8 (262144)
I0623 09:45:08.485595  1897 net.cpp:137] Memory required for data: 2401239136
I0623 09:45:08.485606  1897 layer_factory.hpp:77] Creating layer res5c_branch2c
I0623 09:45:08.485622  1897 net.cpp:84] Creating Layer res5c_branch2c
I0623 09:45:08.485635  1897 net.cpp:406] res5c_branch2c <- res5c_branch2b
I0623 09:45:08.485647  1897 net.cpp:380] res5c_branch2c -> res5c_branch2c
I0623 09:45:08.588564  1897 net.cpp:122] Setting up res5c_branch2c
I0623 09:45:08.588604  1897 net.cpp:129] Top shape: 8 2048 8 8 (1048576)
I0623 09:45:08.588610  1897 net.cpp:137] Memory required for data: 2405433440
I0623 09:45:08.588619  1897 layer_factory.hpp:77] Creating layer bn5c_branch2c
I0623 09:45:08.588632  1897 net.cpp:84] Creating Layer bn5c_branch2c
I0623 09:45:08.588665  1897 net.cpp:406] bn5c_branch2c <- res5c_branch2c
I0623 09:45:08.588685  1897 net.cpp:367] bn5c_branch2c -> res5c_branch2c (in-place)
I0623 09:45:08.588717  1897 net.cpp:122] Setting up bn5c_branch2c
I0623 09:45:08.588737  1897 net.cpp:129] Top shape: 8 2048 8 8 (1048576)
I0623 09:45:08.588752  1897 net.cpp:137] Memory required for data: 2409627744
I0623 09:45:08.588773  1897 layer_factory.hpp:77] Creating layer scale5c_branch2c
I0623 09:45:08.588793  1897 net.cpp:84] Creating Layer scale5c_branch2c
I0623 09:45:08.588809  1897 net.cpp:406] scale5c_branch2c <- res5c_branch2c
I0623 09:45:08.588824  1897 net.cpp:367] scale5c_branch2c -> res5c_branch2c (in-place)
I0623 09:45:08.588852  1897 layer_factory.hpp:77] Creating layer scale5c_branch2c
I0623 09:45:08.588883  1897 net.cpp:122] Setting up scale5c_branch2c
I0623 09:45:08.588902  1897 net.cpp:129] Top shape: 8 2048 8 8 (1048576)
I0623 09:45:08.588917  1897 net.cpp:137] Memory required for data: 2413822048
I0623 09:45:08.588935  1897 layer_factory.hpp:77] Creating layer res5c
I0623 09:45:08.588953  1897 net.cpp:84] Creating Layer res5c
I0623 09:45:08.588969  1897 net.cpp:406] res5c <- res5b_res5b_relu_0_split_1
I0623 09:45:08.588986  1897 net.cpp:406] res5c <- res5c_branch2c
I0623 09:45:08.589004  1897 net.cpp:380] res5c -> res5c
I0623 09:45:08.589025  1897 net.cpp:122] Setting up res5c
I0623 09:45:08.589043  1897 net.cpp:129] Top shape: 8 2048 8 8 (1048576)
I0623 09:45:08.589058  1897 net.cpp:137] Memory required for data: 2418016352
I0623 09:45:08.589073  1897 layer_factory.hpp:77] Creating layer res5c_relu
I0623 09:45:08.589092  1897 net.cpp:84] Creating Layer res5c_relu
I0623 09:45:08.589107  1897 net.cpp:406] res5c_relu <- res5c
I0623 09:45:08.589123  1897 net.cpp:367] res5c_relu -> res5c (in-place)
I0623 09:45:08.589143  1897 net.cpp:122] Setting up res5c_relu
I0623 09:45:08.589159  1897 net.cpp:129] Top shape: 8 2048 8 8 (1048576)
I0623 09:45:08.589174  1897 net.cpp:137] Memory required for data: 2422210656
I0623 09:45:08.589188  1897 layer_factory.hpp:77] Creating layer pool5
I0623 09:45:08.589206  1897 net.cpp:84] Creating Layer pool5
I0623 09:45:08.589222  1897 net.cpp:406] pool5 <- res5c
I0623 09:45:08.589239  1897 net.cpp:380] pool5 -> pool5
I0623 09:45:08.589260  1897 net.cpp:122] Setting up pool5
I0623 09:45:08.589278  1897 net.cpp:129] Top shape: 8 2048 1 1 (16384)
I0623 09:45:08.589293  1897 net.cpp:137] Memory required for data: 2422276192
I0623 09:45:08.589308  1897 layer_factory.hpp:77] Creating layer fc1000
I0623 09:45:08.589325  1897 net.cpp:84] Creating Layer fc1000
I0623 09:45:08.589340  1897 net.cpp:406] fc1000 <- pool5
I0623 09:45:08.589357  1897 net.cpp:380] fc1000 -> fc1000
I0623 09:45:08.654570  1897 net.cpp:122] Setting up fc1000
I0623 09:45:08.654659  1897 net.cpp:129] Top shape: 8 1000 (8000)
I0623 09:45:08.654685  1897 net.cpp:137] Memory required for data: 2422308192
I0623 09:45:08.654709  1897 layer_factory.hpp:77] Creating layer prob
I0623 09:45:08.654733  1897 net.cpp:84] Creating Layer prob
I0623 09:45:08.654752  1897 net.cpp:406] prob <- fc1000
I0623 09:45:08.654772  1897 net.cpp:380] prob -> prob
I0623 09:45:08.654798  1897 net.cpp:122] Setting up prob
I0623 09:45:08.654817  1897 net.cpp:129] Top shape: 8 1000 (8000)
I0623 09:45:08.654844  1897 net.cpp:137] Memory required for data: 2422340192
I0623 09:45:08.654860  1897 layer_factory.hpp:77] Creating layer prob_prob_0_split
I0623 09:45:08.654876  1897 net.cpp:84] Creating Layer prob_prob_0_split
I0623 09:45:08.654892  1897 net.cpp:406] prob_prob_0_split <- prob
I0623 09:45:08.654909  1897 net.cpp:380] prob_prob_0_split -> prob_prob_0_split_0
I0623 09:45:08.654928  1897 net.cpp:380] prob_prob_0_split -> prob_prob_0_split_1
I0623 09:45:08.654948  1897 net.cpp:122] Setting up prob_prob_0_split
I0623 09:45:08.654965  1897 net.cpp:129] Top shape: 8 1000 (8000)
I0623 09:45:08.654981  1897 net.cpp:129] Top shape: 8 1000 (8000)
I0623 09:45:08.654996  1897 net.cpp:137] Memory required for data: 2422404192
I0623 09:45:08.655010  1897 layer_factory.hpp:77] Creating layer accuracy/top1
I0623 09:45:08.655030  1897 net.cpp:84] Creating Layer accuracy/top1
I0623 09:45:08.655045  1897 net.cpp:406] accuracy/top1 <- prob_prob_0_split_0
I0623 09:45:08.655061  1897 net.cpp:406] accuracy/top1 <- label_data_1_split_0
I0623 09:45:08.655077  1897 net.cpp:380] accuracy/top1 -> accuracy@1
I0623 09:45:08.655097  1897 net.cpp:122] Setting up accuracy/top1
I0623 09:45:08.655113  1897 net.cpp:129] Top shape: (1)
I0623 09:45:08.655128  1897 net.cpp:137] Memory required for data: 2422404196
I0623 09:45:08.655143  1897 layer_factory.hpp:77] Creating layer accuracy/top5
I0623 09:45:08.655160  1897 net.cpp:84] Creating Layer accuracy/top5
I0623 09:45:08.655175  1897 net.cpp:406] accuracy/top5 <- prob_prob_0_split_1
I0623 09:45:08.655191  1897 net.cpp:406] accuracy/top5 <- label_data_1_split_1
I0623 09:45:08.655207  1897 net.cpp:380] accuracy/top5 -> accuracy@5
I0623 09:45:08.655226  1897 net.cpp:122] Setting up accuracy/top5
I0623 09:45:08.655243  1897 net.cpp:129] Top shape: (1)
I0623 09:45:08.655257  1897 net.cpp:137] Memory required for data: 2422404200
I0623 09:45:08.655273  1897 net.cpp:200] accuracy/top5 does not need backward computation.
I0623 09:45:08.655287  1897 net.cpp:200] accuracy/top1 does not need backward computation.
I0623 09:45:08.655303  1897 net.cpp:200] prob_prob_0_split does not need backward computation.
I0623 09:45:08.655318  1897 net.cpp:200] prob does not need backward computation.
I0623 09:45:08.655333  1897 net.cpp:200] fc1000 does not need backward computation.
I0623 09:45:08.655347  1897 net.cpp:200] pool5 does not need backward computation.
I0623 09:45:08.655362  1897 net.cpp:200] res5c_relu does not need backward computation.
I0623 09:45:08.655377  1897 net.cpp:200] res5c does not need backward computation.
I0623 09:45:08.655393  1897 net.cpp:200] scale5c_branch2c does not need backward computation.
I0623 09:45:08.655408  1897 net.cpp:200] bn5c_branch2c does not need backward computation.
I0623 09:45:08.655423  1897 net.cpp:200] res5c_branch2c does not need backward computation.
I0623 09:45:08.655438  1897 net.cpp:200] res5c_branch2b_relu does not need backward computation.
I0623 09:45:08.655453  1897 net.cpp:200] scale5c_branch2b does not need backward computation.
I0623 09:45:08.655467  1897 net.cpp:200] bn5c_branch2b does not need backward computation.
I0623 09:45:08.655483  1897 net.cpp:200] res5c_branch2b does not need backward computation.
I0623 09:45:08.655498  1897 net.cpp:200] res5c_branch2a_relu does not need backward computation.
I0623 09:45:08.655513  1897 net.cpp:200] scale5c_branch2a does not need backward computation.
I0623 09:45:08.655526  1897 net.cpp:200] bn5c_branch2a does not need backward computation.
I0623 09:45:08.655541  1897 net.cpp:200] res5c_branch2a does not need backward computation.
I0623 09:45:08.655556  1897 net.cpp:200] res5b_res5b_relu_0_split does not need backward computation.
I0623 09:45:08.655572  1897 net.cpp:200] res5b_relu does not need backward computation.
I0623 09:45:08.655586  1897 net.cpp:200] res5b does not need backward computation.
I0623 09:45:08.655602  1897 net.cpp:200] scale5b_branch2c does not need backward computation.
I0623 09:45:08.655617  1897 net.cpp:200] bn5b_branch2c does not need backward computation.
I0623 09:45:08.655632  1897 net.cpp:200] res5b_branch2c does not need backward computation.
I0623 09:45:08.655653  1897 net.cpp:200] res5b_branch2b_relu does not need backward computation.
I0623 09:45:08.655669  1897 net.cpp:200] scale5b_branch2b does not need backward computation.
I0623 09:45:08.655683  1897 net.cpp:200] bn5b_branch2b does not need backward computation.
I0623 09:45:08.655699  1897 net.cpp:200] res5b_branch2b does not need backward computation.
I0623 09:45:08.655714  1897 net.cpp:200] res5b_branch2a_relu does not need backward computation.
I0623 09:45:08.655728  1897 net.cpp:200] scale5b_branch2a does not need backward computation.
I0623 09:45:08.655743  1897 net.cpp:200] bn5b_branch2a does not need backward computation.
I0623 09:45:08.655758  1897 net.cpp:200] res5b_branch2a does not need backward computation.
I0623 09:45:08.655773  1897 net.cpp:200] res5a_res5a_relu_0_split does not need backward computation.
I0623 09:45:08.655789  1897 net.cpp:200] res5a_relu does not need backward computation.
I0623 09:45:08.655803  1897 net.cpp:200] res5a does not need backward computation.
I0623 09:45:08.655819  1897 net.cpp:200] scale5a_branch2c does not need backward computation.
I0623 09:45:08.655834  1897 net.cpp:200] bn5a_branch2c does not need backward computation.
I0623 09:45:08.655848  1897 net.cpp:200] res5a_branch2c does not need backward computation.
I0623 09:45:08.655864  1897 net.cpp:200] res5a_branch2b_relu does not need backward computation.
I0623 09:45:08.655879  1897 net.cpp:200] scale5a_branch2b does not need backward computation.
I0623 09:45:08.655894  1897 net.cpp:200] bn5a_branch2b does not need backward computation.
I0623 09:45:08.655908  1897 net.cpp:200] res5a_branch2b does not need backward computation.
I0623 09:45:08.655923  1897 net.cpp:200] res5a_branch2a_relu does not need backward computation.
I0623 09:45:08.655939  1897 net.cpp:200] scale5a_branch2a does not need backward computation.
I0623 09:45:08.655953  1897 net.cpp:200] bn5a_branch2a does not need backward computation.
I0623 09:45:08.655968  1897 net.cpp:200] res5a_branch2a does not need backward computation.
I0623 09:45:08.655983  1897 net.cpp:200] scale5a_branch1 does not need backward computation.
I0623 09:45:08.655998  1897 net.cpp:200] bn5a_branch1 does not need backward computation.
I0623 09:45:08.656013  1897 net.cpp:200] res5a_branch1 does not need backward computation.
I0623 09:45:08.656028  1897 net.cpp:200] res4f_res4f_relu_0_split does not need backward computation.
I0623 09:45:08.656044  1897 net.cpp:200] res4f_relu does not need backward computation.
I0623 09:45:08.656059  1897 net.cpp:200] res4f does not need backward computation.
I0623 09:45:08.656074  1897 net.cpp:200] scale4f_branch2c does not need backward computation.
I0623 09:45:08.656088  1897 net.cpp:200] bn4f_branch2c does not need backward computation.
I0623 09:45:08.656103  1897 net.cpp:200] res4f_branch2c does not need backward computation.
I0623 09:45:08.656118  1897 net.cpp:200] res4f_branch2b_relu does not need backward computation.
I0623 09:45:08.656133  1897 net.cpp:200] scale4f_branch2b does not need backward computation.
I0623 09:45:08.656148  1897 net.cpp:200] bn4f_branch2b does not need backward computation.
I0623 09:45:08.656163  1897 net.cpp:200] res4f_branch2b does not need backward computation.
I0623 09:45:08.656178  1897 net.cpp:200] res4f_branch2a_relu does not need backward computation.
I0623 09:45:08.656193  1897 net.cpp:200] scale4f_branch2a does not need backward computation.
I0623 09:45:08.656208  1897 net.cpp:200] bn4f_branch2a does not need backward computation.
I0623 09:45:08.656224  1897 net.cpp:200] res4f_branch2a does not need backward computation.
I0623 09:45:08.656239  1897 net.cpp:200] res4e_res4e_relu_0_split does not need backward computation.
I0623 09:45:08.656253  1897 net.cpp:200] res4e_relu does not need backward computation.
I0623 09:45:08.656267  1897 net.cpp:200] res4e does not need backward computation.
I0623 09:45:08.656283  1897 net.cpp:200] scale4e_branch2c does not need backward computation.
I0623 09:45:08.656298  1897 net.cpp:200] bn4e_branch2c does not need backward computation.
I0623 09:45:08.656316  1897 net.cpp:200] res4e_branch2c does not need backward computation.
I0623 09:45:08.656332  1897 net.cpp:200] res4e_branch2b_relu does not need backward computation.
I0623 09:45:08.656347  1897 net.cpp:200] scale4e_branch2b does not need backward computation.
I0623 09:45:08.656363  1897 net.cpp:200] bn4e_branch2b does not need backward computation.
I0623 09:45:08.656378  1897 net.cpp:200] res4e_branch2b does not need backward computation.
I0623 09:45:08.656393  1897 net.cpp:200] res4e_branch2a_relu does not need backward computation.
I0623 09:45:08.656407  1897 net.cpp:200] scale4e_branch2a does not need backward computation.
I0623 09:45:08.656422  1897 net.cpp:200] bn4e_branch2a does not need backward computation.
I0623 09:45:08.656436  1897 net.cpp:200] res4e_branch2a does not need backward computation.
I0623 09:45:08.656451  1897 net.cpp:200] res4d_res4d_relu_0_split does not need backward computation.
I0623 09:45:08.656466  1897 net.cpp:200] res4d_relu does not need backward computation.
I0623 09:45:08.656481  1897 net.cpp:200] res4d does not need backward computation.
I0623 09:45:08.656497  1897 net.cpp:200] scale4d_branch2c does not need backward computation.
I0623 09:45:08.656512  1897 net.cpp:200] bn4d_branch2c does not need backward computation.
I0623 09:45:08.656527  1897 net.cpp:200] res4d_branch2c does not need backward computation.
I0623 09:45:08.656541  1897 net.cpp:200] res4d_branch2b_relu does not need backward computation.
I0623 09:45:08.656556  1897 net.cpp:200] scale4d_branch2b does not need backward computation.
I0623 09:45:08.656571  1897 net.cpp:200] bn4d_branch2b does not need backward computation.
I0623 09:45:08.656587  1897 net.cpp:200] res4d_branch2b does not need backward computation.
I0623 09:45:08.656602  1897 net.cpp:200] res4d_branch2a_relu does not need backward computation.
I0623 09:45:08.656617  1897 net.cpp:200] scale4d_branch2a does not need backward computation.
I0623 09:45:08.656632  1897 net.cpp:200] bn4d_branch2a does not need backward computation.
I0623 09:45:08.656646  1897 net.cpp:200] res4d_branch2a does not need backward computation.
I0623 09:45:08.656662  1897 net.cpp:200] res4c_res4c_relu_0_split does not need backward computation.
I0623 09:45:08.656677  1897 net.cpp:200] res4c_relu does not need backward computation.
I0623 09:45:08.656692  1897 net.cpp:200] res4c does not need backward computation.
I0623 09:45:08.656708  1897 net.cpp:200] scale4c_branch2c does not need backward computation.
I0623 09:45:08.656723  1897 net.cpp:200] bn4c_branch2c does not need backward computation.
I0623 09:45:08.656738  1897 net.cpp:200] res4c_branch2c does not need backward computation.
I0623 09:45:08.656754  1897 net.cpp:200] res4c_branch2b_relu does not need backward computation.
I0623 09:45:08.656769  1897 net.cpp:200] scale4c_branch2b does not need backward computation.
I0623 09:45:08.656783  1897 net.cpp:200] bn4c_branch2b does not need backward computation.
I0623 09:45:08.656796  1897 net.cpp:200] res4c_branch2b does not need backward computation.
I0623 09:45:08.656811  1897 net.cpp:200] res4c_branch2a_relu does not need backward computation.
I0623 09:45:08.656826  1897 net.cpp:200] scale4c_branch2a does not need backward computation.
I0623 09:45:08.656841  1897 net.cpp:200] bn4c_branch2a does not need backward computation.
I0623 09:45:08.656857  1897 net.cpp:200] res4c_branch2a does not need backward computation.
I0623 09:45:08.656872  1897 net.cpp:200] res4b_res4b_relu_0_split does not need backward computation.
I0623 09:45:08.656886  1897 net.cpp:200] res4b_relu does not need backward computation.
I0623 09:45:08.656901  1897 net.cpp:200] res4b does not need backward computation.
I0623 09:45:08.656918  1897 net.cpp:200] scale4b_branch2c does not need backward computation.
I0623 09:45:08.656932  1897 net.cpp:200] bn4b_branch2c does not need backward computation.
I0623 09:45:08.656947  1897 net.cpp:200] res4b_branch2c does not need backward computation.
I0623 09:45:08.656963  1897 net.cpp:200] res4b_branch2b_relu does not need backward computation.
I0623 09:45:08.656981  1897 net.cpp:200] scale4b_branch2b does not need backward computation.
I0623 09:45:08.656996  1897 net.cpp:200] bn4b_branch2b does not need backward computation.
I0623 09:45:08.657011  1897 net.cpp:200] res4b_branch2b does not need backward computation.
I0623 09:45:08.657027  1897 net.cpp:200] res4b_branch2a_relu does not need backward computation.
I0623 09:45:08.657042  1897 net.cpp:200] scale4b_branch2a does not need backward computation.
I0623 09:45:08.657058  1897 net.cpp:200] bn4b_branch2a does not need backward computation.
I0623 09:45:08.657073  1897 net.cpp:200] res4b_branch2a does not need backward computation.
I0623 09:45:08.657088  1897 net.cpp:200] res4a_res4a_relu_0_split does not need backward computation.
I0623 09:45:08.657104  1897 net.cpp:200] res4a_relu does not need backward computation.
I0623 09:45:08.657119  1897 net.cpp:200] res4a does not need backward computation.
I0623 09:45:08.657133  1897 net.cpp:200] scale4a_branch2c does not need backward computation.
I0623 09:45:08.657150  1897 net.cpp:200] bn4a_branch2c does not need backward computation.
I0623 09:45:08.657165  1897 net.cpp:200] res4a_branch2c does not need backward computation.
I0623 09:45:08.657179  1897 net.cpp:200] res4a_branch2b_relu does not need backward computation.
I0623 09:45:08.657194  1897 net.cpp:200] scale4a_branch2b does not need backward computation.
I0623 09:45:08.657209  1897 net.cpp:200] bn4a_branch2b does not need backward computation.
I0623 09:45:08.657224  1897 net.cpp:200] res4a_branch2b does not need backward computation.
I0623 09:45:08.657239  1897 net.cpp:200] res4a_branch2a_relu does not need backward computation.
I0623 09:45:08.657254  1897 net.cpp:200] scale4a_branch2a does not need backward computation.
I0623 09:45:08.657269  1897 net.cpp:200] bn4a_branch2a does not need backward computation.
I0623 09:45:08.657284  1897 net.cpp:200] res4a_branch2a does not need backward computation.
I0623 09:45:08.657300  1897 net.cpp:200] scale4a_branch1 does not need backward computation.
I0623 09:45:08.657315  1897 net.cpp:200] bn4a_branch1 does not need backward computation.
I0623 09:45:08.657330  1897 net.cpp:200] res4a_branch1 does not need backward computation.
I0623 09:45:08.657346  1897 net.cpp:200] res3d_res3d_relu_0_split does not need backward computation.
I0623 09:45:08.657361  1897 net.cpp:200] res3d_relu does not need backward computation.
I0623 09:45:08.657374  1897 net.cpp:200] res3d does not need backward computation.
I0623 09:45:08.657390  1897 net.cpp:200] scale3d_branch2c does not need backward computation.
I0623 09:45:08.657405  1897 net.cpp:200] bn3d_branch2c does not need backward computation.
I0623 09:45:08.657420  1897 net.cpp:200] res3d_branch2c does not need backward computation.
I0623 09:45:08.657435  1897 net.cpp:200] res3d_branch2b_relu does not need backward computation.
I0623 09:45:08.657450  1897 net.cpp:200] scale3d_branch2b does not need backward computation.
I0623 09:45:08.657464  1897 net.cpp:200] bn3d_branch2b does not need backward computation.
I0623 09:45:08.657480  1897 net.cpp:200] res3d_branch2b does not need backward computation.
I0623 09:45:08.657495  1897 net.cpp:200] res3d_branch2a_relu does not need backward computation.
I0623 09:45:08.657510  1897 net.cpp:200] scale3d_branch2a does not need backward computation.
I0623 09:45:08.657524  1897 net.cpp:200] bn3d_branch2a does not need backward computation.
I0623 09:45:08.657539  1897 net.cpp:200] res3d_branch2a does not need backward computation.
I0623 09:45:08.657554  1897 net.cpp:200] res3c_res3c_relu_0_split does not need backward computation.
I0623 09:45:08.657570  1897 net.cpp:200] res3c_relu does not need backward computation.
I0623 09:45:08.657585  1897 net.cpp:200] res3c does not need backward computation.
I0623 09:45:08.657600  1897 net.cpp:200] scale3c_branch2c does not need backward computation.
I0623 09:45:08.657615  1897 net.cpp:200] bn3c_branch2c does not need backward computation.
I0623 09:45:08.657630  1897 net.cpp:200] res3c_branch2c does not need backward computation.
I0623 09:45:08.657649  1897 net.cpp:200] res3c_branch2b_relu does not need backward computation.
I0623 09:45:08.657665  1897 net.cpp:200] scale3c_branch2b does not need backward computation.
I0623 09:45:08.657680  1897 net.cpp:200] bn3c_branch2b does not need backward computation.
I0623 09:45:08.657694  1897 net.cpp:200] res3c_branch2b does not need backward computation.
I0623 09:45:08.657709  1897 net.cpp:200] res3c_branch2a_relu does not need backward computation.
I0623 09:45:08.657724  1897 net.cpp:200] scale3c_branch2a does not need backward computation.
I0623 09:45:08.657739  1897 net.cpp:200] bn3c_branch2a does not need backward computation.
I0623 09:45:08.657753  1897 net.cpp:200] res3c_branch2a does not need backward computation.
I0623 09:45:08.657769  1897 net.cpp:200] res3b_res3b_relu_0_split does not need backward computation.
I0623 09:45:08.657784  1897 net.cpp:200] res3b_relu does not need backward computation.
I0623 09:45:08.657799  1897 net.cpp:200] res3b does not need backward computation.
I0623 09:45:08.657814  1897 net.cpp:200] scale3b_branch2c does not need backward computation.
I0623 09:45:08.657829  1897 net.cpp:200] bn3b_branch2c does not need backward computation.
I0623 09:45:08.657845  1897 net.cpp:200] res3b_branch2c does not need backward computation.
I0623 09:45:08.657860  1897 net.cpp:200] res3b_branch2b_relu does not need backward computation.
I0623 09:45:08.657874  1897 net.cpp:200] scale3b_branch2b does not need backward computation.
I0623 09:45:08.657889  1897 net.cpp:200] bn3b_branch2b does not need backward computation.
I0623 09:45:08.657903  1897 net.cpp:200] res3b_branch2b does not need backward computation.
I0623 09:45:08.657919  1897 net.cpp:200] res3b_branch2a_relu does not need backward computation.
I0623 09:45:08.657933  1897 net.cpp:200] scale3b_branch2a does not need backward computation.
I0623 09:45:08.657948  1897 net.cpp:200] bn3b_branch2a does not need backward computation.
I0623 09:45:08.657963  1897 net.cpp:200] res3b_branch2a does not need backward computation.
I0623 09:45:08.657977  1897 net.cpp:200] res3a_res3a_relu_0_split does not need backward computation.
I0623 09:45:08.657994  1897 net.cpp:200] res3a_relu does not need backward computation.
I0623 09:45:08.658007  1897 net.cpp:200] res3a does not need backward computation.
I0623 09:45:08.658023  1897 net.cpp:200] scale3a_branch2c does not need backward computation.
I0623 09:45:08.658038  1897 net.cpp:200] bn3a_branch2c does not need backward computation.
I0623 09:45:08.658053  1897 net.cpp:200] res3a_branch2c does not need backward computation.
I0623 09:45:08.658068  1897 net.cpp:200] res3a_branch2b_relu does not need backward computation.
I0623 09:45:08.658083  1897 net.cpp:200] scale3a_branch2b does not need backward computation.
I0623 09:45:08.658098  1897 net.cpp:200] bn3a_branch2b does not need backward computation.
I0623 09:45:08.658113  1897 net.cpp:200] res3a_branch2b does not need backward computation.
I0623 09:45:08.658128  1897 net.cpp:200] res3a_branch2a_relu does not need backward computation.
I0623 09:45:08.658143  1897 net.cpp:200] scale3a_branch2a does not need backward computation.
I0623 09:45:08.658157  1897 net.cpp:200] bn3a_branch2a does not need backward computation.
I0623 09:45:08.658172  1897 net.cpp:200] res3a_branch2a does not need backward computation.
I0623 09:45:08.658187  1897 net.cpp:200] scale3a_branch1 does not need backward computation.
I0623 09:45:08.658203  1897 net.cpp:200] bn3a_branch1 does not need backward computation.
I0623 09:45:08.658218  1897 net.cpp:200] res3a_branch1 does not need backward computation.
I0623 09:45:08.658233  1897 net.cpp:200] res2c_res2c_relu_0_split does not need backward computation.
I0623 09:45:08.658249  1897 net.cpp:200] res2c_relu does not need backward computation.
I0623 09:45:08.658263  1897 net.cpp:200] res2c does not need backward computation.
I0623 09:45:08.658279  1897 net.cpp:200] scale2c_branch2c does not need backward computation.
I0623 09:45:08.658294  1897 net.cpp:200] bn2c_branch2c does not need backward computation.
I0623 09:45:08.658309  1897 net.cpp:200] res2c_branch2c does not need backward computation.
I0623 09:45:08.658326  1897 net.cpp:200] res2c_branch2b_relu does not need backward computation.
I0623 09:45:08.658342  1897 net.cpp:200] scale2c_branch2b does not need backward computation.
I0623 09:45:08.658356  1897 net.cpp:200] bn2c_branch2b does not need backward computation.
I0623 09:45:08.658371  1897 net.cpp:200] res2c_branch2b does not need backward computation.
I0623 09:45:08.658386  1897 net.cpp:200] res2c_branch2a_relu does not need backward computation.
I0623 09:45:08.658401  1897 net.cpp:200] scale2c_branch2a does not need backward computation.
I0623 09:45:08.658416  1897 net.cpp:200] bn2c_branch2a does not need backward computation.
I0623 09:45:08.658432  1897 net.cpp:200] res2c_branch2a does not need backward computation.
I0623 09:45:08.658447  1897 net.cpp:200] res2b_res2b_relu_0_split does not need backward computation.
I0623 09:45:08.658462  1897 net.cpp:200] res2b_relu does not need backward computation.
I0623 09:45:08.658476  1897 net.cpp:200] res2b does not need backward computation.
I0623 09:45:08.658491  1897 net.cpp:200] scale2b_branch2c does not need backward computation.
I0623 09:45:08.658506  1897 net.cpp:200] bn2b_branch2c does not need backward computation.
I0623 09:45:08.658521  1897 net.cpp:200] res2b_branch2c does not need backward computation.
I0623 09:45:08.658536  1897 net.cpp:200] res2b_branch2b_relu does not need backward computation.
I0623 09:45:08.658551  1897 net.cpp:200] scale2b_branch2b does not need backward computation.
I0623 09:45:08.658565  1897 net.cpp:200] bn2b_branch2b does not need backward computation.
I0623 09:45:08.658581  1897 net.cpp:200] res2b_branch2b does not need backward computation.
I0623 09:45:08.658596  1897 net.cpp:200] res2b_branch2a_relu does not need backward computation.
I0623 09:45:08.658610  1897 net.cpp:200] scale2b_branch2a does not need backward computation.
I0623 09:45:08.658624  1897 net.cpp:200] bn2b_branch2a does not need backward computation.
I0623 09:45:08.658639  1897 net.cpp:200] res2b_branch2a does not need backward computation.
I0623 09:45:08.658655  1897 net.cpp:200] res2a_res2a_relu_0_split does not need backward computation.
I0623 09:45:08.658675  1897 net.cpp:200] res2a_relu does not need backward computation.
I0623 09:45:08.658692  1897 net.cpp:200] res2a does not need backward computation.
I0623 09:45:08.658709  1897 net.cpp:200] scale2a_branch2c does not need backward computation.
I0623 09:45:08.658723  1897 net.cpp:200] bn2a_branch2c does not need backward computation.
I0623 09:45:08.658737  1897 net.cpp:200] res2a_branch2c does not need backward computation.
I0623 09:45:08.658753  1897 net.cpp:200] res2a_branch2b_relu does not need backward computation.
I0623 09:45:08.658768  1897 net.cpp:200] scale2a_branch2b does not need backward computation.
I0623 09:45:08.658783  1897 net.cpp:200] bn2a_branch2b does not need backward computation.
I0623 09:45:08.658798  1897 net.cpp:200] res2a_branch2b does not need backward computation.
I0623 09:45:08.658813  1897 net.cpp:200] res2a_branch2a_relu does not need backward computation.
I0623 09:45:08.658828  1897 net.cpp:200] scale2a_branch2a does not need backward computation.
I0623 09:45:08.658843  1897 net.cpp:200] bn2a_branch2a does not need backward computation.
I0623 09:45:08.658857  1897 net.cpp:200] res2a_branch2a does not need backward computation.
I0623 09:45:08.658874  1897 net.cpp:200] scale2a_branch1 does not need backward computation.
I0623 09:45:08.658888  1897 net.cpp:200] bn2a_branch1 does not need backward computation.
I0623 09:45:08.658903  1897 net.cpp:200] res2a_branch1 does not need backward computation.
I0623 09:45:08.658920  1897 net.cpp:200] pool1_pool1_0_split does not need backward computation.
I0623 09:45:08.658934  1897 net.cpp:200] pool1 does not need backward computation.
I0623 09:45:08.658949  1897 net.cpp:200] conv1_relu does not need backward computation.
I0623 09:45:08.658964  1897 net.cpp:200] scale_conv1 does not need backward computation.
I0623 09:45:08.658979  1897 net.cpp:200] bn_conv1 does not need backward computation.
I0623 09:45:08.658998  1897 net.cpp:200] conv1 does not need backward computation.
I0623 09:45:08.659013  1897 net.cpp:200] label_data_1_split does not need backward computation.
I0623 09:45:08.659029  1897 net.cpp:200] data does not need backward computation.
I0623 09:45:08.659044  1897 net.cpp:242] This network produces output accuracy@1
I0623 09:45:08.659059  1897 net.cpp:242] This network produces output accuracy@5
I0623 09:45:08.659191  1897 net.cpp:255] Network initialization done.

python scale [140144782868488]
compressing layer bn5b_branch2c
vec_length 2048
[quantize] count:2048
[quantize] float src:	
max:0.718131	min:0.000057	diff:0
scale:7.000000	pow2_scale:128.000000
python scale [140144782868487]
compressing layer scale5b_branch2c
vec_length 2048
[quantize] count:2048
[quantize] float src:	
max:2.846558	min:0.573608	diff:0
scale:5.000000	pow2_scale:32.000000
python scale [140144782868485]
compressing layer res5c_branch2a
vec_length 1048576
[quantize] count:1048576
[quantize] float src:	
max:0.514462	min:0.000000	diff:0
scale:7.000000	pow2_scale:128.000000
python scale [140144782868487]
compressing layer bn5c_branch2a
vec_length 512
[quantize] count:512
[quantize] float src:	
max:5.327801	min:0.162666	diff:0
scale:4.000000	pow2_scale:16.000000
python scale [140144782868484]
compressing layer scale5c_branch2a
vec_length 512
[quantize] count:512
[quantize] float src:	
max:1.249171	min:0.366309	diff:0
scale:6.000000	pow2_scale:64.000000
python scale [140144782868486]
compressing layer res5c_branch2b
vec_length 2359296
[quantize] count:2359296
[quantize] float src:	
max:0.143758	min:0.000000	diff:0
scale:9.000000	pow2_scale:512.000000
python scale [140144782868489]
compressing layer bn5c_branch2b
vec_length 512
[quantize] count:512
[quantize] float src:	
max:0.634746	min:0.094139	diff:0
scale:7.000000	pow2_scale:128.000000
python scale [140144782868487]
compressing layer scale5c_branch2b
vec_length 512
[quantize] count:512
[quantize] float src:	
max:1.334668	min:0.516349	diff:0
scale:6.000000	pow2_scale:64.000000
python scale [140144782868486]
compressing layer res5c_branch2c
vec_length 1048576
[quantize] count:1048576
[quantize] float src:	
max:0.299967	min:0.000000	diff:0
scale:8.000000	pow2_scale:256.000000
python scale [140144782868488]
compressing layer bn5c_branch2c
vec_length 2048
[quantize] count:2048
[quantize] float src:	
max:0.245636	min:0.000220	diff:0
scale:9.000000	pow2_scale:512.000000
python scale [140144782868489]
compressing layer scale5c_branch2c
vec_length 2048
[quantize] count:2048
[quantize] float src:	
max:3.073178	min:0.434784	diff:0
scale:5.000000	pow2_scale:32.000000
python scale [140144782868485]
compressing layer fc1000
vec_length 2048000
[quantize] count:2048000
[quantize] float src:	
max:0.736159	min:0.000000	diff:0
scale:7.000000	pow2_scale:128.000000
python scale [140144782868487]
['res4a_branch2b_scale', 'res5a_branch2a_scale', 'scale2a_branch1_newweights', 'res4e_branch2c_newweights', 'bn3d_branch2a_scale', 'res3a_branch1_newweights', 'scale4d_branch2c_scale', 'bn4a_branch2a_bias', 'bn2c_branch2c_newweights', 'scale3b_branch2b_scale', 'bn2b_branch2a_scale', 'fc1000_newweights', 'res5b_branch2a_scale', 'scale4b_branch2b_newweights', 'res4f_branch2c_newweights', 'bn2b_branch2b_newweights', 'scale4f_branch2b_newweights', 'bn4a_branch1_bias', 'res3b_branch2c_newweights', 'res5b_branch2b_scale', 'res5a_branch2a_newweights', 'res2a_branch1_scale', 'conv1_bias', 'bn5b_branch2c_third', 'res5a_branch2b_newweights', 'bn5b_branch2c_newweights', 'res3b_branch2a_scale', 'bn4d_branch2a_third', 'bn2c_branch2c_bias', 'scale4c_branch2c_bias', 'res4b_branch2b_newweights', 'res2c_branch2b_newweights', 'fc1000_scale', 'bn2b_branch2a_third', 'bn3a_branch2a_scale', 'res4b_branch2a_newweights', 'bn5c_branch2a_scale', 'scale2a_branch2a_newweights', 'bn_conv1_third', 'scale4a_branch2b_scale', 'scale2b_branch2a_bias', 'scale2b_branch2b_bias', 'res4f_branch2c_scale', 'res5a_branch1_newweights', 'conv1_scale', 'bn3b_branch2b_newweights', 'scale2b_branch2c_scale', 'scale2a_branch2c_newweights', 'bn3a_branch1_bias', 'bn3a_branch2a_newweights', 'scale5a_branch2a_scale', 'res3b_branch2b_scale', 'res3d_branch2a_newweights', 'scale3a_branch2a_bias', 'bn5c_branch2a_bias', 'scale4e_branch2b_bias', 'bn3c_branch2c_scale', 'scale3d_branch2c_scale', 'bn4d_branch2b_third', 'scale5b_branch2a_newweights', 'scale4c_branch2c_scale', 'scale3b_branch2a_scale', 'bn5c_branch2b_third', 'bn4c_branch2a_newweights', 'res3a_branch1_scale', 'bn4a_branch2a_newweights', 'bn2b_branch2b_scale', 'scale4c_branch2b_scale', 'scale5a_branch2b_scale', 'bn3a_branch2b_third', 'res4b_branch2c_scale', 'scale4b_branch2b_scale', 'bn3a_branch2a_bias', 'scale4a_branch2a_scale', 'res4a_branch2c_scale', 'scale2c_branch2b_bias', 'bn4e_branch2c_scale', 'res2c_branch2c_newweights', 'bn4b_branch2a_scale', 'bn3b_branch2a_third', 'res3c_branch2a_newweights', 'scale5b_branch2a_bias', 'res2c_branch2a_newweights', 'bn2c_branch2b_scale', 'bn3c_branch2c_newweights', 'res3c_branch2c_newweights', 'bn3a_branch2b_newweights', 'scale3c_branch2b_bias', 'bn4a_branch1_newweights', 'bn5a_branch2a_third', 'bn4f_branch2b_third', 'bn2a_branch2b_scale', 'bn5b_branch2a_scale', 'scale_conv1_bias', 'bn2b_branch2c_newweights', 'bn5a_branch2a_newweights', 'res2c_branch2a_scale', 'scale4d_branch2b_scale', 'scale5a_branch2a_newweights', 'scale2c_branch2b_scale', 'bn2a_branch1_bias', 'bn5a_branch2c_scale', 'res3d_branch2a_scale', 'res2c_branch2b_scale', 'scale4a_branch2b_newweights', 'bn2a_branch2a_third', 'scale5a_branch1_scale', 'bn5c_branch2a_third', 'res3d_branch2b_scale', 'scale3d_branch2a_newweights', 'bn5b_branch2b_newweights', 'res4c_branch2b_scale', 'bn4d_branch2a_scale', 'bn5c_branch2c_scale', 'scale3a_branch2a_scale', 'scale2a_branch2b_scale', 'res5a_branch1_scale', 'scale3a_branch2b_scale', 'scale3b_branch2c_newweights', 'res5b_branch2c_newweights', 'res3a_branch2a_newweights', 'bn4d_branch2a_newweights', 'res4c_branch2b_newweights', 'bn2a_branch1_newweights', 'bn2a_branch2b_bias', 'res4e_branch2c_scale', 'scale5b_branch2c_scale', 'bn2c_branch2c_third', 'scale4c_branch2c_newweights', 'bn4a_branch2c_newweights', 'scale4f_branch2b_bias', 'bn4a_branch2b_scale', 'bn4e_branch2a_scale', 'bn5a_branch1_bias', 'res5c_branch2c_scale', 'scale4d_branch2c_newweights', 'scale2c_branch2c_newweights', 'bn5a_branch2b_newweights', 'scale4f_branch2a_newweights', 'bn4c_branch2c_third', 'scale4f_branch2a_bias', 'res4a_branch2c_newweights', 'res2b_branch2c_newweights', 'scale3b_branch2b_newweights', 'bn4a_branch2a_third', 'scale4c_branch2a_bias', 'res3a_branch2c_scale', 'scale2c_branch2a_scale', 'res5b_branch2b_newweights', 'scale4a_branch2b_bias', 'scale5b_branch2c_newweights', 'res4a_branch1_newweights', 'bn2b_branch2c_third', 'bn2a_branch2c_newweights', 'bn5a_branch2b_scale', 'scale4a_branch2a_bias', 'res4a_branch2a_newweights', 'scale3c_branch2a_newweights', 'scale4a_branch2c_newweights', 'res3d_branch2b_newweights', 'scale5c_branch2b_newweights', 'scale4f_branch2c_newweights', 'res2a_branch1_newweights', 'bn3d_branch2a_bias', 'scale4a_branch1_scale', 'bn5c_branch2b_bias', 'bn2c_branch2a_bias', 'bn2a_branch2c_scale', 'scale3c_branch2c_scale', 'bn4f_branch2c_bias', 'bn4e_branch2a_third', 'res3b_branch2c_scale', 'scale4d_branch2a_scale', 'bn4e_branch2a_newweights', 'bn4b_branch2c_third', 'scale5b_branch2b_newweights', 'scale2b_branch2a_newweights', 'bn5a_branch2a_bias', 'bn2b_branch2c_bias', 'bn5b_branch2a_third', 'res3d_branch2c_scale', 'fc1000_bias', 'bn4a_branch1_third', 'bn4e_branch2c_newweights', 'bn4d_branch2c_newweights', 'scale3c_branch2a_bias', 'res4b_branch2b_scale', 'scale2a_branch2b_newweights', 'bn2a_branch2c_third', 'res2b_branch2b_scale', 'scale2b_branch2b_scale', 'scale3a_branch1_newweights', 'scale5c_branch2c_scale', 'bn5b_branch2a_bias', 'bn5a_branch2b_third', 'scale4a_branch2a_newweights', 'bn3c_branch2c_third', 'scale2a_branch1_scale', 'scale3a_branch2c_newweights', 'scale3d_branch2a_scale', 'scale4b_branch2a_scale', 'scale3c_branch2b_newweights', 'scale5c_branch2b_bias', 'res4d_branch2a_scale', 'res4d_branch2c_scale', 'bn3c_branch2a_scale', 'bn2c_branch2a_third', 'bn3b_branch2c_bias', 'res5b_branch2a_newweights', 'scale5c_branch2c_newweights', 'bn4d_branch2c_third', 'bn3d_branch2b_third', 'res2b_branch2a_scale', 'res3b_branch2a_newweights', 'scale4d_branch2c_bias', 'bn2b_branch2a_newweights', 'res4f_branch2b_scale', 'res2b_branch2a_newweights', 'bn_conv1_scale', 'scale3a_branch1_scale', 'res4c_branch2a_newweights', 'bn4d_branch2b_newweights', 'scale5a_branch2c_scale', 'bn2b_branch2c_scale', 'bn3d_branch2a_newweights', 'scale2b_branch2b_newweights', 'bn3d_branch2c_newweights', 'scale5c_branch2c_bias', 'bn3a_branch2c_newweights', 'res4c_branch2c_newweights', 'scale3b_branch2c_scale', 'bn2a_branch2b_newweights', 'bn3c_branch2b_newweights', 'bn4f_branch2c_scale', 'scale4a_branch1_newweights', 'res4f_branch2a_newweights', 'bn3a_branch1_newweights', 'scale3c_branch2b_scale', 'bn3d_branch2a_third', 'res5a_branch2c_scale', 'bn3c_branch2b_third', 'scale2b_branch2a_scale', 'scale2a_branch1_bias', 'bn3c_branch2a_newweights', 'scale4b_branch2c_scale', 'bn3b_branch2a_bias', 'bn5a_branch2c_newweights', 'res4d_branch2c_newweights', 'scale2b_branch2c_bias', 'res2a_branch2a_newweights', 'bn4e_branch2b_third', 'scale5a_branch2b_newweights', 'bn4b_branch2b_scale', 'res3c_branch2a_scale', 'bn3a_branch2c_bias', 'res2b_branch2b_newweights', 'bn3b_branch2b_bias', 'res4e_branch2a_newweights', 'scale5b_branch2b_scale', 'res5a_branch2b_scale', 'bn3a_branch1_third', 'scale4e_branch2a_newweights', 'bn5c_branch2c_third', 'compz_info', 'bn4d_branch2b_bias', 'bn3b_branch2a_scale', 'res4d_branch2a_newweights', 'res4d_branch2b_newweights', 'scale4e_branch2b_newweights', 'scale4b_branch2b_bias', 'bn2a_branch2a_newweights', 'bn3b_branch2b_scale', 'bn2c_branch2a_newweights', 'scale5b_branch2a_scale', 'bn5a_branch1_third', 'res5c_branch2a_scale', 'bn3a_branch2c_scale', 'bn3d_branch2b_scale', 'bn5c_branch2a_newweights', 'res5c_branch2b_newweights', 'res4a_branch2b_newweights', 'bn2a_branch2b_third', 'bn4e_branch2a_bias', 'res2c_branch2c_scale', 'scale3a_branch2b_newweights', 'bn2a_branch1_third', 'bn4a_branch2c_third', 'bn3d_branch2c_scale', 'bn5b_branch2b_third', 'scale3d_branch2c_newweights', 'scale2b_branch2c_newweights', 'scale5c_branch2a_bias', 'res5c_branch2a_newweights', 'bn4b_branch2b_bias', 'scale5c_branch2a_scale', 'res4e_branch2b_scale', 'bn4b_branch2a_third', 'scale2c_branch2c_bias', 'bn3d_branch2b_newweights', 'scale5c_branch2a_newweights', 'scale5b_branch2c_bias', 'conv1_newweights', 'bn4c_branch2b_scale', 'bn4a_branch2c_scale', 'bn4e_branch2b_scale', 'scale3d_branch2b_newweights', 'bn5c_branch2b_scale', 'bn3d_branch2c_bias', 'bn5c_branch2c_bias', 'scale2c_branch2a_newweights', 'res4b_branch2c_newweights', 'bn4c_branch2a_third', 'bn_conv1_bias', 'scale4f_branch2a_scale', 'scale4f_branch2c_scale', 'scale4a_branch2c_scale', 'bn3d_branch2b_bias', 'bn4f_branch2a_newweights', 'bn3b_branch2c_newweights', 'scale4a_branch2c_bias', 'res5b_branch2c_scale', 'bn4c_branch2b_newweights', 'bn5a_branch1_scale', 'bn3c_branch2c_bias', 'bn3b_branch2a_newweights', 'scale_conv1_scale', 'res3c_branch2c_scale', 'bn2a_branch2a_bias', 'bn3b_branch2c_scale', 'bn4c_branch2a_scale', 'bn4e_branch2b_newweights', 'scale3b_branch2a_bias', 'scale2a_branch2c_scale', 'scale4b_branch2c_bias', 'res4c_branch2c_scale', 'bn4e_branch2c_third', 'bn4e_branch2b_bias', 'bn3c_branch2b_bias', 'scale3a_branch1_bias', 'res4a_branch1_scale', 'bn4e_branch2c_bias', 'bn4a_branch2b_third', 'res2a_branch2b_scale', 'bn5b_branch2c_bias', 'scale4c_branch2a_scale', 'scale3c_branch2c_newweights', 'bn5c_branch2b_newweights', 'scale4d_branch2a_newweights', 'bn2c_branch2b_third', 'bn5a_branch2a_scale', 'bn5b_branch2b_bias', 'scale3d_branch2b_scale', 'scale4e_branch2a_bias', 'bn5c_branch2c_newweights', 'bn4b_branch2c_newweights', 'bn2c_branch2a_scale', 'scale4a_branch1_bias', 'bn3a_branch2a_third', 'bn4d_branch2c_scale', 'scale4b_branch2a_newweights', 'bn2a_branch2a_scale', 'res5c_branch2b_scale', 'bn3a_branch2b_scale', 'scale4f_branch2c_bias', 'res3c_branch2b_scale', 'res5c_branch2c_newweights', 'scale3a_branch2a_newweights', 'scale4e_branch2c_newweights', 'bn4f_branch2b_newweights', 'scale4c_branch2b_bias', 'bn3a_branch2c_third', 'res3c_branch2b_newweights', 'res2a_branch2b_newweights', 'bn4b_branch2c_scale', 'bn4f_branch2c_third', 'bn4a_branch1_scale', 'bn3b_branch2c_third', 'bn5b_branch2b_scale', 'scale4c_branch2b_newweights', 'res3d_branch2c_newweights', 'bn_conv1_newweights', 'scale3c_branch2c_bias', 'res4c_branch2a_scale', 'bn4d_branch2b_scale', 'scale2a_branch2a_bias', 'bn4b_branch2a_newweights', 'bn4a_branch2b_newweights', 'bn4c_branch2a_bias', 'scale4d_branch2b_newweights', 'bn4c_branch2b_bias', 'scale3b_branch2b_bias', 'res3a_branch2b_scale', 'bn4b_branch2c_bias', 'bn5b_branch2c_scale', 'bn4f_branch2a_third', 'res3b_branch2b_newweights', 'scale5a_branch2a_bias', 'bn4d_branch2c_bias', 'scale2a_branch2a_scale', 'res3a_branch2c_newweights', 'bn4f_branch2b_scale', 'bn4a_branch2b_bias', 'scale5a_branch2c_newweights', 'scale3b_branch2a_newweights', 'res2a_branch2c_scale', 'bn3d_branch2c_third', 'bn3c_branch2a_bias', 'scale4f_branch2b_scale', 'scale5c_branch2b_scale', 'scale5a_branch2c_bias', 'res3a_branch2a_scale', 'scale4b_branch2c_newweights', 'scale3a_branch2c_scale', 'bn2b_branch2a_bias', 'scale4d_branch2a_bias', 'bn4c_branch2c_newweights', 'scale5a_branch1_newweights', 'bn2a_branch1_scale', 'res2a_branch2c_newweights', 'scale4e_branch2b_scale', 'scale4e_branch2c_bias', 'bn3a_branch1_scale', 'scale2c_branch2b_newweights', 'bn4f_branch2b_bias', 'bn4f_branch2a_bias', 'bn4b_branch2b_newweights', 'bn4b_branch2b_third', 'bn2c_branch2b_newweights', 'scale2c_branch2a_bias', 'scale5b_branch2b_bias', 'res2a_branch2a_scale', 'bn5a_branch1_newweights', 'bn4c_branch2b_third', 'scale3d_branch2c_bias', 'scale4d_branch2b_bias', 'res5a_branch2c_newweights', 'res4e_branch2b_newweights', 'bn2b_branch2b_bias', 'scale3d_branch2a_bias', 'res2b_branch2c_scale', 'bn5a_branch2c_third', 'bn4a_branch2a_scale', 'scale2a_branch2b_bias', 'scale3d_branch2b_bias', 'bn4c_branch2c_bias', 'bn3c_branch2a_third', 'res4f_branch2a_scale', 'scale2a_branch2c_bias', 'scale5a_branch2b_bias', 'bn2b_branch2b_third', 'res4d_branch2b_scale', 'bn2c_branch2c_scale', 'bn4d_branch2a_bias', 'scale2c_branch2c_scale', 'bn3a_branch2b_bias', 'scale4c_branch2a_newweights', 'res4e_branch2a_scale', 'scale_conv1_newweights', 'bn4b_branch2a_bias', 'bn5b_branch2a_newweights', 'res4b_branch2a_scale', 'bn3c_branch2b_scale', 'res4a_branch2a_scale', 'bn4c_branch2c_scale', 'scale4e_branch2c_scale', 'bn2c_branch2b_bias', 'bn2a_branch2c_bias', 'scale3b_branch2c_bias', 'scale4e_branch2a_scale', 'scale3a_branch2c_bias', 'bn4a_branch2c_bias', 'bn4f_branch2c_newweights', 'scale3c_branch2a_scale', 'bn5a_branch2b_bias', 'res4f_branch2b_newweights', 'res3a_branch2b_newweights', 'scale4b_branch2a_bias', 'bn4f_branch2a_scale', 'scale5a_branch1_bias', 'bn5a_branch2c_bias', 'scale3a_branch2b_bias', 'bn3b_branch2b_third']
[de_]count:9408
[de_]count:64
[de_]count:64
[de_]count:16384
[de_]count:256
[de_]count:256
[de_]count:4096
[de_]count:64
[de_]count:64
[de_]count:36864
[de_]count:64
[de_]count:64
[de_]count:16384
[de_]count:256
[de_]count:256
[de_]count:16384
[de_]count:64
[de_]count:64
[de_]count:36864
[de_]count:64
[de_]count:64
[de_]count:16384
[de_]count:256
[de_]count:256
[de_]count:16384
[de_]count:64
[de_]count:64
[de_]count:36864
[de_]count:64
[de_]count:64
[de_]count:16384
[de_]count:256
[de_]count:256
[de_]count:131072
[de_]count:512
[de_]count:512
[de_]count:32768
[de_]count:128
[de_]count:128
[de_]count:147456
[de_]count:128
[de_]count:128
[de_]count:65536
[de_]count:512
[de_]count:512
[de_]count:65536
[de_]count:128
[de_]count:128
[de_]count:147456
[de_]count:128
[de_]count:128
[de_]count:65536
[de_]count:512
[de_]count:512
[de_]count:65536
[de_]count:128
[de_]count:128
[de_]count:147456
[de_]count:128
[de_]count:128
[de_]count:65536
[de_]count:512
[de_]count:512
[de_]count:65536
[de_]count:128
[de_]count:128
[de_]count:147456
[de_]count:128
[de_]count:128
[de_]count:65536
[de_]count:512
[de_]count:512
[de_]count:524288
[de_]count:1024
[de_]count:1024
[de_]count:131072
[de_]count:256
[de_]count:256
[de_]count:589824
[de_]count:256
[de_]count:256
[de_]count:262144
[de_]count:1024
[de_]count:1024
[de_]count:262144
[de_]count:256
[de_]count:256
[de_]count:589824
[de_]count:256
[de_]count:256
[de_]count:262144
[de_]count:1024
[de_]count:1024
[de_]count:262144
[de_]count:256
[de_]count:256
[de_]count:589824
[de_]count:256
[de_]count:256
[de_]count:262144
[de_]count:1024
[de_]count:1024
[de_]count:262144
[de_]count:256
[de_]count:256
[de_]count:589824
[de_]count:256
[de_]count:256
[de_]count:262144
[de_]count:1024
[de_]count:1024
[de_]count:262144
[de_]count:256
[de_]count:256
[de_]count:589824
[de_]count:256
[de_]count:256
[de_]count:262144
[de_]count:1024
[de_]count:1024
[de_]count:262144
[de_]count:256
[de_]count:256
[de_]count:589824
[de_]count:256
[de_]count:256
[de_]count:262144
[de_]count:1024
[de_]count:1024
[de_]count:2097152
[de_]count:2048
[de_]count:2048
[de_]count:524288
[de_]count:512
[de_]count:512
[de_]count:2359296
[de_]count:512
[de_]count:512
[de_]count:1048576
[de_]count:2048
[de_]count:2048
[de_]count:1048576
[de_]count:512
[de_]count:512
[de_]count:2359296
[de_]count:512
[de_]count:512
[de_]count:1048576
[de_]count:2048
[de_]count:2048
[de_]count:1048576
[de_]count:512
[de_]count:512
[de_]count:2359296
[de_]count:512
[de_]count:512
[de_]count:1048576
[de_]count:2048
[de_]count:2048
[de_]count:2048000
Done
