import onnxruntime

onnx_path = './yolov5s.onnx'
onnxruntime.InferenceSession(onnx_path, providers=['CUDAExecutionProvider'])
