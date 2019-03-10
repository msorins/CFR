from typing import List
import tensorflow as tf
import tensorflow_hub as hub
import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd
import re
import seaborn as sns

from CSVDataExtractor import CSVDataExtractor
from PDFDataExtractor import PDFDataExtractor


class Estimator:

    def __init__(self):
        negative = CSVDataExtractor().get_data()
        positive = PDFDataExtractor().get_data()
        # Combine and shuffle training set
        df = pd.concat([positive, negative], axis=1).sample(frac=1).reset_index(drop=True)
        self.split_dataset(df)
        self.prepare_data()
        # Apply BOW on data
        self.embedded_text_feature_column = hub.text_embedding_column(
            key="sentence",
            module_spec="https://tfhub.dev/google/nnlm-en-dim128/1"
        )

        self.estimator = tf.estimator.DNNClassifier(
            hidden_units=[500, 100],
            feature_columns=[self.embedded_text_feature_column],
            n_classes=2,
            optimizer=tf.train.AdagradOptimizer(learning_rate=0.003)
        )


    def split_dataset(self, df: pd.DataFrame):
        train_size = int(0.75 * len(df))
        self.train_df = df.iloc[:, :train_size]
        self.test_df = df.iloc[:, train_size:]


    def prepare_data(self):
        self.train_input_fn = tf.estimator.inputs.pandas_input_fn(
            self.train_df,
            self.train_df["polarity"],
            shuffle=True
        )

        self.predict_test_input_fn = tf.estimator.inputs.pandas_input_fn(
            self.test_df,
            self.test_df["polarity"],
            shuffle=False
        )


    def train_estimator(self):
        self.estimator.train(input_fn=self.train_input_fn, steps=1000)

        train_eval_result = estimator.evaluate(input_fn=self.predict_train_input_fn)
        test_eval_result = estimator.evaluate(input_fn=self.predict_test_input_fn)

        print("Training set accuracy: {accuracy}".format(**train_eval_result))
        print("Test set accuracy: {accuracy}".format(**test_eval_result))


    def get_predictions(estimator, label):
      return [x["class_ids"][0] for x in estimator.predict(input_fn=input_fn)]


    def predict(self, text: List[str]):
        return tf.estimator.inputs.pandas_input_fn()


Estimator().train_estimator()
