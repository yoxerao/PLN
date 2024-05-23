import os

import matplotlib.pyplot as plt
import json

data = """Epoch	Training Loss	Validation Loss	Accuracy	F1	Precision	Recall
1	0.485900	0.141322	0.952946	0.953695	0.957330	0.952946
2	0.143100	0.096835	0.953501	0.954109	0.957095	0.953501
3	0.115900	0.108076	0.956651	0.957385	0.960580	0.956651
4	0.086800	0.128395	0.954428	0.955187	0.958637	0.954428
5	0.081100	0.134938	0.957392	0.958137	0.961487	0.957392
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
plt.ylim(bottom=0)
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


folder_path = './logs'
learning_rates = []
epochs = []

#
# plt.figure(figsize=(10, 5))
# plt.plot(epochs, learning_rates, label='Learning Rate', color='blue')
# plt.legend()
# plt.xlabel('Epoch')
# plt.ylabel('Learning Rate')
# plt.title('Learning Rate')
plt.show()


