import os
import urllib.request as request
from zipfile import ZipFile
import tensorflow as tf
import time
from cnnClassifier.entity.config_entity import TrainingConfig
from pathlib import Path
from tensorflow.keras.callbacks import ModelCheckpoint,ReduceLROnPlateau,EarlyStopping

class Training:
    def __init__(self, config: TrainingConfig):
        self.config = config
# CHECKPOINT_PATH = "/content/drive/MyDrive/kidney_checkpoints_4class/best_model.h5"
    
    def get_base_model(self):
        self.model = tf.keras.models.load_model(
        self.config.updated_base_model_path,
        compile=False
        )

        self.model.compile(
            optimizer=tf.keras.optimizers.SGD(
                learning_rate=self.config.params_learning_rate
            ),
            loss=tf.keras.losses.CategoricalCrossentropy(),
            metrics=["accuracy"]
        )

    def train_valid_generator(self):

        datagenerator_kwargs = dict(
            rescale = 1./255,
            validation_split=0.20
        )

        dataflow_kwargs = dict(
            target_size=self.config.params_image_size[:-1],
            batch_size=self.config.params_batch_size,
            interpolation="bilinear"
        )

        valid_datagenerator = tf.keras.preprocessing.image.ImageDataGenerator(
            **datagenerator_kwargs
        )

        self.valid_generator = valid_datagenerator.flow_from_directory(
            directory=self.config.training_data,
            subset="validation",
            shuffle=False,
            **dataflow_kwargs
        )

        if self.config.params_is_augmentation:
            train_datagenerator = tf.keras.preprocessing.image.ImageDataGenerator(
                rotation_range=40,
                horizontal_flip=True,
                width_shift_range=0.2,
                height_shift_range=0.2,
                shear_range=0.2,
                zoom_range=0.2,
                **datagenerator_kwargs
            )
        else:
            train_datagenerator = valid_datagenerator

        self.train_generator = train_datagenerator.flow_from_directory(
            directory=self.config.training_data,
            subset="training",
            shuffle=True,
            **dataflow_kwargs
        )

    
    @staticmethod
    def save_model(path: Path, model: tf.keras.Model):
        model.save(path)


    def train(self):
        checkpoint = ModelCheckpoint(
        filepath="/content/drive/MyDrive/kidney_checkpoints_4class/best_model.h5",
        monitor="val_accuracy",
        mode="max",
        save_best_only=True,
        verbose=1
    )

        early_stop=EarlyStopping(
        monitor="val_loss",
        patience=5,
        restore_best_weights=True
    )

        reduce_lr = ReduceLROnPlateau(
        monitor="val_loss",
        factor=0.5,
        patience=3,
        min_lr=1e-7,
        verbose=1
        )

        self.model.fit(
        self.train_generator,
        epochs=self.config.params_epochs,
        validation_data=self.valid_generator,
        callbacks=[checkpoint,reduce_lr ,early_stop]
        )

        self.save_model(
            path=self.config.trained_model_path,
            model=self.model
        )