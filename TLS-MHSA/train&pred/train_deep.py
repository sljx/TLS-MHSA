import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
from decimal import Decimal
import matplotlib.pyplot as plt 
from sklearn.metrics import confusion_matrix ,classification_report,precision_recall_fscore_support
from sklearn.preprocessing import label_binarize
import tensorflow as tf
from tensorflow import keras
from deeptables.models.deeptable import DeepTable, ModelConfig
from deeptables.models.deepnets import (DeepFM, fgcnn_dnn_nets,xDeepFM,DCN,PNN,WideDeep,AutoInt,AFM,FGCNN,FiBiNet)
from tensorflow.compat.v1.metrics import root_mean_squared_error

#config = deeptable.ModelConfig(nets =['linear','cin_nets','dnn_nets'],
#    stacking_op = 'add', earlystopping_patience=15, metrics=["RootMeanSquaredError"])

TRAIN_CSV_PATH="traindata.csv"
TEST_CSV_PATH="testdata.csv"


train = pd.read_csv(TRAIN_CSV_PATH)
test = pd.read_csv(TEST_CSV_PATH)

def rmse(predictions, targets):
    """Competition metric: difference in prediction and target squared and then square rooted and averaged"""
    return np.sqrt(((predictions - targets) ** 2).mean())

target=train['Label']
train = train[[col for col in train.columns.values if (col != 'target') & (col != 'date') & (col != 'source') & (col!='label')]]
test = test[[col for col in train.columns.values if (col != 'target') & (col != 'date') & (col != 'source') & (col!='lable') ]]
test_target=test['Label']
y_test=label_binarize(test_target, classes=[i for i in range(0,12)])
#conf = ModelConfig(nets=DCN, metrics=['RootMeanSquaredError'],auto_discrete=False,apply_gbm_features=True)

conf = ModelConfig(
    #nets=['fm_nets','linear','dnn_nets'],
    #nets=['dnn_nets','cin_nets','fm_nets'],
    #'opnn_nets','fg_nets','fgcnn_cin_nets'],
    #nets=['dnn_nets','opnn_nets'],
    #nets=['dnn_nets','dnn_nets','dnn_nets'],
    #nets=DCN,0.996
    #nets=WideDeep,0.91
    #nets=FibiNet,
    nets=['linear', 'dnn_nets'],#0.92,0.79
    #nets=DCN,0.995,0.912
    #nets=AutoInt,
    #nets=FiBiNet,
    #nets=['dnn_nets','autoint_nets'],
    #nets=['fgcnn_cin_nets'],#{'loss': 0.1498553454875946, 'auc': 0.9979644417762756, 'accuracy': 0.937749981880188, 'recall': 0.9375}
    metrics=['AUC','Recall','acc'],
    #auto_discrete=True
    #optimizer=keras.optimizers.RMSprop(),
)
dt = DeepTable(config=conf)
#conf = ModelConfig(nets=['dnn_nets'], optimizer=keras.optimizers.RMSprop())
#dt = DeepTable(config=conf)
# with tf.device('./gpu'):
#dt.fit_cross_validation(train, target, epochs=5,shuffle=True)
model, history =dt.fit(train,target,epochs=100)
#dt=DeepTable.load_deepmodel()

dt.save('./model/')
evaluate=dt.evaluate(test,test_target, batch_size=512, verbose=0)
print(evaluate)
predict= dt.predict(test)
#print(predict)
