import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
from decimal import Decimal
from sklearn.metrics import confusion_matrix ,classification_report,precision_recall_fscore_support
from sklearn.preprocessing import label_binarize
from deeptables.models.deeptable import DeepTable, ModelConfig
from deeptables.models import deeptable, deepnets
from deeptables.models.layers import dt_custom_objects
from tensorflow.keras.models import load_model 
import os,time
import matplotlib.pyplot as plt              # 绘图库
TRAIN_CSV_PATH="traindata.csv"
TEST_CSV_PATH="testdata.csv"
MODEL_PATH=os.path.join('./model')


class PlotConfusionMatrix:
    def plot_confusion_matrix(self,labels,cm,title='Confusion Matrix',cmap=plt.cm.Reds):
        plt.imshow(cm,interpolation='nearest',cmap=cmap)
        plt.title(title)
        plt.colorbar()
        xlocations = np.array(range(len(labels)))
        plt.xticks(xlocations, labels, rotation=60)
        plt.yticks(xlocations, labels)
        plt.ylabel('True label')
        plt.xlabel('Predicted label')
 
    def prepareWork(self,labels, y_true, y_pred):
        tick_marks = np.array(range(len(labels))) + 0.5
        cm = confusion_matrix(y_true, y_pred)
        np.set_printoptions(precision=2)
        cm_normalized = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
        plt.figure(figsize=(12, 8), dpi=150)
        ind_array = np.arange(len(labels))
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
        self.plot_confusion_matrix(labels,cm_normalized, title='Normalized confusion matrix')
        # show confusion matrix
        # plt.savefig('image/confusion_matrix.png', format='png')
        # plt.show()
 
# 绘制混淆矩阵
def plotMatrix(attacks, y_test, y_pred):
    # attacks是整个数据集的标签集合，但是切分测试集的时候，某些标签数量很少，可能会被去掉，这里要剔除掉这些标签
    y_test_set = set(y_test)
    y_test_list = list(y_test_set)
    attacks_test = []
    for i in range(0, len(y_test_set)):
        attacks_test.append(attacks[y_test_list[i]])
    p = PlotConfusionMatrix()
    p.prepareWork(attacks_test, y_test, y_pred)
index_list=['normal', 'trickbot', 'ursnif', 'Artemis', 'sathurbot', 'dridex', 'hancitor', 'zeus', 'miuref', 'dreambot', 'gootkit']


def predict_nclass():
    train = pd.read_csv(TRAIN_CSV_PATH)
    test = pd.read_csv(TEST_CSV_PATH)
    test=test.sample(frac=0.2)
    test_target=test['family']
    y_test=label_binarize(test_target, classes=[i for i in range(0,11)])
    #model = keras.models.load_model('/root/graduate/dt_output/dt_20210509 213746_dnn_nets/dnn_nets.h5',dt_custom_objects)
    #(col != 'family') & 
    test = test[[col for col in test.columns.values if (col != 'date') & (col != 'source') & (col!='label')] ]
    #test_target='family'
    #model=load_model('model', dt_custom_objects)
    #model=load_model(MODEL_PATH, dt_custom_objects)
    newdt = deeptable.DeepTable.load(MODEL_PATH)
    preds = newdt.predict(test)
    evdt  = newdt.evaluate(test,test_target,batch_size=128,verbose=0)
    plotMatrix(index_list,test_target,preds)
    timestr= time.strftime('%m-%d_%H-%M', time.localtime(time.time()))
    plt.savefig(f'./cm_img_Predict_{timestr}.png', format='png')

    #print('模型预测的准确度矩阵:\n{}'.format(np.transpose(classification_report(sub,predict))))
    #cm=confusion_matrix(predict, sub)
    #print('模型预测的混淆矩阵:\n{}'.format(cm))

    #print(preds)
    print (evdt)
    y_predict=label_binarize(preds, classes=[i for i in range(0,11)])
    #print(predict)
    from sklearn.metrics import roc_curve, auc
    # 为每个类别计算ROC曲线和AUC
    fpr = dict()
    tpr = dict()
    roc_auc = dict()
    n_classes=11
    csv_list=[{}]
    metrics=precision_recall_fscore_support(test_target,preds)
    predict_list=metrics[0]
    recall_list=metrics[1]
    f1score_list=metrics[2]
    support=metrics[3]
    name=['predict','recall','f1score','auc']
    for i in range(n_classes):
        dict_temp={}
        fpr[i], tpr[i], _ = roc_curve(y_test[:, i], y_predict[:, i])
        dict_temp['predict']=np.around(predict_list[i],4)
        dict_temp['recall']=np.around(recall_list[i],4)
        dict_temp['f1score']=np.around(f1score_list[i],4)
        dict_temp['auc'] = np.around(auc(fpr[i], tpr[i]),4)
        csv_list.append(dict_temp)
    csv_list.pop(0)
    csv_df=pd.DataFrame(csv_list,index=index_list)
    csv_df.to_csv('testmetrics.csv')
def predict_std(runs=10):
    metrics=dict()
    auc_list = np.zeros(runs)
    precision_list = np.zeros(runs)
    recall_list= np.zeros(runs)
    f1_list= np.zeros(runs)
    for i in range(0,runs):
        #train = pd.read_csv(TRAIN_CSV_PATH)
        test = pd.read_csv(TEST_CSV_PATH)
        test=test.sample(frac=0.5)
        test_target=test['family']
        #model = keras.models.load_model('/root/graduate/dt_output/dt_20210509 213746_dnn_nets/dnn_nets.h5',dt_custom_objects)
        #(col != 'family') & 
        test = test[[col for col in test.columns.values if (col != 'date') & (col != 'source') & (col!='label')] ]
        #test_target='family'
        #model=load_model('model', dt_custom_objects)
        #model=load_model(MODEL_PATH, dt_custom_objects)
        newdt = deeptable.DeepTable.load(MODEL_PATH)
        preds = newdt.predict(test)
        evdt  = newdt.evaluate(test,test_target,batch_size=512,verbose=0)
        auc_list[i] = evdt['auc']
        recall_list[i] = evdt['recall']
        precision_list[i] = evdt['acc']
        f1_list[i] =2*evdt['recall']*evdt['acc']/(evdt['recall']+evdt['acc'])
    metrics['avg_auc'] =np.around(np.mean(auc_list),4)
    metrics['avg_precision'] =np.around(np.mean(precision_list),4)
    metrics['avg_recall'] =np.around(np.mean(recall_list),4)
    metrics['avg_f1'] =np.around(np.mean(f1_list),4)
    metrics['std_auc'] =np.around(np.std(auc_list),4)
    metrics['std_precision'] =np.around(np.std(precision_list),4)
    metrics['std_recall'] =np.around(np.std(recall_list),4)
    metrics['std_f1'] =np.around(np.std(f1_list),4)
    metrics_df=pd.DataFrame.from_dict(metrics,orient='index')
    metrics_df.to_csv('testmetrics.csv')
predict_nclass()