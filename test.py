import torch
# Kiểm tra xem CUDA có sẵn không và thiết lập biến 'device'
print(torch.cuda.is_available())  # Nếu trả về True, bạn đã cài PyTorch với CUDA thành công.
   
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
print(device)
print(torch.version.cuda)
print(torch.__version__)
print(torch.cuda.get_device_name(0))

