import torch
import torch.nn as nn
import torch.nn.functional as F


class Model(nn.Module):
    def __init__(self, encoder):
        super(Model, self).__init__()
        self.encoder = encoder

    def forward(self, input_ids=None, labels=None):
        logits = self.encoder(input_ids, attention_mask=input_ids.ne(1))[0]
        prob = F.softmax(logits, dim=-1)

        if labels is not None:
            labels = labels.long()
            loss = F.cross_entropy(logits, labels)

            return loss, logits
        else:
            return prob