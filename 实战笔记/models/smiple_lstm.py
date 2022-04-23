
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
        self.linear1 = nn.Linear(lstm_dim*sequence_num*2, 1)
        self.bn1 = nn.BatchNorm1d(lstm_dim*sequence_num*2)

    def forward(self,x):
        lstm_out, _ = self.lstm(x)
        x = lstm_out.reshape(lstm_out.shape[0], -1)
        x = self.linear1(self.bn1(x))
        return x

