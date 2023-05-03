import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import confusion_matrix
 
# confusion = confusion_matrix(y_test, y_pred)
 
confusion = np.array([[106069,0,0,0,29,0,0,0,12,0,0],
[0,9109,0,0,0,0,0,0,1,0,0],
[2,0,10739,0,0,0,0,0,1,8,0],
[1,0,10248,1,0,0,0,0,1,0,0],
[51,0,3,0,11395,0,0,0,3,0,0],
[0,0,0,0,0,10672,0,0,0,0,0],
[3,0,2,0,2,0,6260,1,0,3,0],
[4,0,0,0,3,0,3,8860,0,0,0],
[40,0,0,0,3,1,1,0,10334,1,0],
[0,0,9,0,0,0,25,0,0,552,0],
[0,0,0,0,0,0,9,0,0,0,525]])
cm_normalized = confusion.astype('float') / confusion.sum(axis=1)[:, np.newaxis]
# 热度图，后面是指定的颜色块，cmap可设置其他的不同颜色
plt.imshow(confusion, cmap=plt.cm.Reds)
plt.colorbar()
 
# 第一个是迭代对象，表示坐标的显示顺序，第二个参数是坐标轴显示列表
indices = range(len(confusion))
classes=['normal', 'trickbot', 'ursnif', 'Artemis', 'sathurbot', 'dridex', 'hancitor', 'zeus', 'miuref', 'dreambot', 'gootkit']
plt.xticks(indices, classes, rotation=45) # 设置横坐标方向，rotation=45为45度倾斜
plt.yticks(indices, classes)
 
 
# plt.ylabel('True label')
# plt.xlabel('Predicted label')
# plt.title('Confusion matrix')
 
plt.ylabel('True label')
plt.xlabel('Predicted label')
plt.title('Normalized confusion matrix')
tick_marks = np.array(range(len(classes))) + 0.5
np.set_printoptions(precision=2)
plt.figure(figsize=(12, 8), dpi=150)
ind_array = np.arange(len(classes))
x, y = np.meshgrid(ind_array, ind_array)
for x_val, y_val in zip(x.flatten(), y.flatten()):
    c = cm_normalized[y_val][x_val]
    if c > 0.99:
        c=0.99
    plt.text(x_val, y_val, "%0.2f" % (c,), color='black', fontsize=10, va='center', ha='center')
        # offset the tick
            # offset the tick
plt.gca().set_xticks(tick_marks, minor=True)
plt.gca().set_yticks(tick_marks, minor=True)
plt.gca().xaxis.set_ticks_position('none')
plt.gca().yaxis.set_ticks_position('none')
plt.grid(True, which='minor', linestyle='-')
plt.gcf().subplots_adjust(bottom=0.15)
# 显示
def plot_confusion_matrix(labels,cm,title='Confusion Matrix',cmap=plt.cm.Reds):
    plt.imshow(cm,interpolation='nearest',cmap=cmap)
    plt.title(title)
    plt.colorbar()
    xlocations = np.array(range(len(labels)))
    plt.xticks(xlocations, labels, rotation=60)
    plt.yticks(xlocations, labels)
    plt.ylabel('True label')
    plt.xlabel('Predicted label')
plot_confusion_matrix(classes,cm_normalized, title='Normalized confusion matrix')
plt.show()