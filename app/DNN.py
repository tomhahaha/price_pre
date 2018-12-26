import numpy as np
np.random.seed(1337)  # for reproducibility
from keras.datasets import mnist
from keras.utils import np_utils
from keras.models import Sequential
from keras.layers import Dense, Activation
from keras.optimizers import RMSprop
import app.data_extra as de
from keras.callbacks import Callback
from sklearn.metrics import f1_score, precision_score, recall_score


class Metrics(Callback):
    def on_train_begin(self, logs={}):
        self.val_f1s = []
        self.val_recalls = []
        self.val_precisions = []

    def on_epoch_end(self, epoch, logs={}):
        val_predict = (np.asarray(self.model.predict(
            self.validation_data[0]))).round()
        val_targ = self.validation_data[1]
        _val_f1 = f1_score(val_targ, val_predict)
        _val_recall = recall_score(val_targ, val_predict)
        _val_precision = precision_score(val_targ, val_predict)
        self.val_f1s.append(_val_f1)
        self.val_recalls.append(_val_recall)
        self.val_precisions.append(_val_precision)
        return
metrics = Metrics()
trX, trY,valX, valY=de.data_load()
model = Sequential([
    Dense(60, input_dim=30),
    Activation('relu'),
    Dense(3),
    Activation('softmax'),
])
rmsprop = RMSprop(lr=0.001, rho=0.9, epsilon=1e-08, decay=0.0)
model.compile(optimizer=rmsprop,
              loss='categorical_crossentropy',
              metrics=['accuracy'])
model.fit(trX, trY, epochs=1, batch_size=20,validation_data=(valX,valY),callbacks=[metrics])
print(metrics.val_precisions)
# print('\nTesting ------------')
# Evaluate the model with the metrics we defined earlier
# loss, accuracy = model.evaluate(valX, valY)
#
# print('test loss: ', loss)
# print('test accuracy: ', accuracy)