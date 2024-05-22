import os

import matplotlib.pyplot as plt
import json

#parou aqui e não gravou :(
data = """Epoch	Training Loss	Validation Loss	Accuracy	F1	Precision	Recall
1	0.492100	0.302145	0.898481	0.899887	0.908306	0.898481
2	0.284100	0.225925	0.912560	0.913835	0.920596	0.912560
3	0.225200	0.197282	0.921823	0.922810	0.928592	0.921823
4	0.153800	0.200277	0.927566	0.928696	0.934510	0.927566
5	0.136700	0.224338	0.930159	0.931254	0.937546	0.930159
6	0.118500	0.212462	0.934420	0.935457	0.940635	0.934420
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


