import torch
import torch.nn as nn
import torch.nn.functional as F

class LSTM(nn.Module):
    def __init__(
        self,
        input_size=8,
        sequence_num=31,
        lstm_dim=128,
        num_layers=2,
        output_size=1
    ):
        super().__init__()
        
        self.lstm = nn.LSTM(
            input_size,
            lstm_dim,
            num_layers,
            batch_first=True,
            bidirectional=True
        )
        # 维度？
        self.bn1 = nn.BatchNorm1d(lstm_dim*sequence_num*2)
        self.linear1 = nn.Linear(lstm_dim*sequence_num*2, 1)
        

    def forward(self,x):
        # 层的输出，结果和损失
        lstm_out, _ = self.lstm(x)
        # 除了第一批维，其余 flatten
        x = lstm_out.reshape(lstm_out.shape[0], -1)
        # 线性层之前的批归一化
        x = self.linear1(self.bn1(x))
        return x

