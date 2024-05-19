import os

import matplotlib.pyplot as plt
import json

data = """Epoch	Training Loss	Validation Loss	Accuracy	F1	Precision	Recall
1	1.336500	0.672151	0.767877	0.768445	0.787636	0.767877
2	0.548200	0.361130	0.878659	0.879110	0.891628	0.878659
3	0.329000	0.286695	0.904965	0.905948	0.914898	0.904965
4	0.201300	0.279562	0.911634	0.912859	0.922509	0.911634
5	0.181000	0.241044	0.927381	0.928658	0.935803	0.927381
6	0.162400	0.238819	0.925713	0.926895	0.933919	0.925713
7	0.130700	0.229541	0.930530	0.931690	0.938167	0.930530
8	0.122100	0.218883	0.931827	0.932936	0.938747	0.931827
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


