import os

import matplotlib.pyplot as plt
import json

data ="""Epoch	Training Loss	Validation Loss	Accuracy	F1	Precision	Recall
1	1.792400    1.498574	0.396814	0.388814	0.409113	0.396814
2	1.270900	0.658220	0.779918	0.780841	0.801582	0.779918
3	0.659900	0.362332	0.883846	0.884224	0.892237	0.883846
4	0.293200	0.313446	0.901074	0.901968	0.911523	0.901074
5	0.239700	0.279805	0.912745	0.913621	0.921876	0.912745
6	0.212000	0.224497	0.924416	0.925485	0.932503	0.924416
7	0.173300	0.208804	0.930345	0.931681	0.938210	0.930345
8	0.161600	0.207165	0.930345	0.931593	0.938069	0.930345
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
plt.plot(epochs, training_loss, label='Training Loss', color='red')
plt.plot(epochs, validation_loss, label='Validation Loss', color='blue')
plt.legend()
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.title('Training and Validation Loss')
# plt.show()

# plot the f1, precision and recall
plt.figure(figsize=(10, 5))
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

for file in os.listdir(folder_path):
    with open(os.path.join(folder_path, file), 'r') as f:
        log_history = json.load(f)['log_history']

        for entry in log_history:
            if 'learning_rate' in entry:
                learning_rates.append(entry['learning_rate'])
                epochs.append(entry['epoch'])

plt.figure(figsize=(10, 5))
plt.plot(epochs, learning_rates, label='Learning Rate', color='blue')
plt.legend()
plt.xlabel('Epoch')
plt.ylabel('Learning Rate')
plt.title('Learning Rate')
plt.show()


