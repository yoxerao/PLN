import os

import matplotlib.pyplot as plt
import json

old_data ="""Epoch	Training Loss	Validation Loss	Accuracy	F1	Precision	Recall
1	1.792400    1.498574	0.396814	0.388814	0.409113	0.396814
2	1.270900	0.658220	0.779918	0.780841	0.801582	0.779918
3	0.659900	0.362332	0.883846	0.884224	0.892237	0.883846
4	0.293200	0.313446	0.901074	0.901968	0.911523	0.901074
5	0.239700	0.279805	0.912745	0.913621	0.921876	0.912745
6	0.212000	0.224497	0.924416	0.925485	0.932503	0.924416
7	0.173300	0.208804	0.930345	0.931681	0.938210	0.930345
8	0.161600	0.207165	0.930345	0.931593	0.938069	0.930345
"""

# data = """Epoch	Training Loss	Validation Loss	Accuracy	F1	Precision	Recall
# 1	0.449700	0.166591	0.949611	0.950469	0.954403	0.949611
# 2	0.160000	0.107827	0.952390	0.952897	0.956051	0.952390
# 3	0.131700	0.113743	0.955169	0.955906	0.959301	0.955169
# 4	0.101000	0.129865	0.952019	0.952877	0.956753	0.952019
# 5	0.097900	0.119263	0.957577	0.958380	0.961923	0.957577
# 6	0.092200	0.114707	0.957947	0.958662	0.961988	0.957947
# """

data = """Epoch	Training Loss	Validation Loss
1	7.751300	7.137944
2	7.000600	7.044827
3	6.845000	6.594419
4	6.696100	6.694266
5	6.643300	6.694021
6	6.538800	6.579125
7	6.438000	6.578517
8	6.437300	6.363343
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
    epoch, training, validation = line.split()
    epochs.append(int(epoch))
    training_loss.append(float(training))
    validation_loss.append(float(validation))
    print(epoch, training, validation)
    # accuracy.append(float(acc))
    # f1.append(float(f))
    # precision.append(float(p))
    # recall.append(float(r))

plt.figure(figsize=(10, 5))
plt.ylim(bottom=0, top=7.8)
plt.plot(epochs, training_loss, label='Training Loss', color='red')
plt.plot(epochs, validation_loss, label='Validation Loss', color='blue')
plt.legend()
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.title('Training and Validation Loss')
plt.show()


