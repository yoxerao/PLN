import os
import matplotlib.pyplot as plt
import json

data = """Epoch	Training Loss	Validation Loss	Accuracy	F1	Precision	Recall
1	1.269000	0.562304	0.774361	0.766643	0.810507	0.774361
2	0.440600	0.287722	0.902001	0.903461	0.912398	0.902001
3	0.277900	0.237038	0.908670	0.910416	0.919590	0.908670
4	0.188400	0.282705	0.915339	0.916925	0.925723	0.915339
5	0.169300	0.231759	0.918674	0.920026	0.926668	0.918674
6	0.152000	0.226495	0.921267	0.922394	0.928852	0.921267
7	0.117900	0.229088	0.924787	0.926034	0.932369	0.924787
8	0.112800    0.231639	0.925157	0.926313	0.932034	0.925157
"""
# plot the training and validation loss
epochs = []
training_loss = []
validation_loss = []
accuracy = []
f1 = []
precision = []
recall = []

for line in data.strip().split('\n')[1:]:
    epoch, training, validation, acc, f, p, r = line.split()
    epochs.append(int(epoch))
    training_loss.append(float(training))
    validation_loss.append(float(validation))
    accuracy.append(float(acc))
    f1.append(float(f))
    precision.append(float(p))
    recall.append(float(r))

plt.figure(figsize=(10, 5))
# start y axis on 0
plt.ylim(bottom=0, top=1.26)
plt.plot(epochs, training_loss, label='Training Loss', color='red')
plt.plot(epochs, validation_loss, label='Validation Loss', color='blue')
plt.legend()
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.title('Training and Validation Loss')

# plt.show()

# plot the f1, precision and recall
plt.figure(figsize=(10, 5))
plt.ylim(bottom=0.6)
plt.plot(epochs, f1, label='F1', color='green')
plt.plot(epochs, precision, label='Precision', color='blue')
plt.plot(epochs, recall, label='Recall', color='red')
plt.legend()
plt.xlabel('Epoch')
plt.ylabel('Score')
plt.title('F1, Precision and Recall')
# plt.show()

plt.show()


