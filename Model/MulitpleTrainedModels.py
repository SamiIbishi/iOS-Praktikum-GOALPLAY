# Generated by https://quicktype.io

from typing import List, Any


class MultipleTrainedModelsEvaluation:
    train_acc: int
    test_acc: int

    def __init__(self, train_acc: int, test_acc: int) -> None:
        self.train_acc = train_acc
        self.test_acc = test_acc


class ParameterClass:
    pass

    def __init__(self, ) -> None:
        pass


class Model:
    modeltype: str
    parameter: ParameterClass
    evaluation: ParameterClass

    def __init__(self, modeltype: str, parameter: ParameterClass, evaluation: ParameterClass) -> None:
        self.modeltype = modeltype
        self.parameter = parameter
        self.evaluation = evaluation


class Models:
    model: List[Any]

    def __init__(self, model: List[Any]) -> None:
        self.model = model


class Parameter:
    init: str
    optim: str
    input_shape: str
    num_mem_units: int
    num_hidden_units: int
    learning_rate: int
    num_epochs: int
    batch_size: int
    dropout: bool
    batchnormalization: bool

    def __init__(self, init: str, optim: str, input_shape: str, num_mem_units: int, num_hidden_units: int, learning_rate: int, num_epochs: int, batch_size: int, dropout: bool, batchnormalization: bool) -> None:
        self.init = init
        self.optim = optim
        self.input_shape = input_shape
        self.num_mem_units = num_mem_units
        self.num_hidden_units = num_hidden_units
        self.learning_rate = learning_rate
        self.num_epochs = num_epochs
        self.batch_size = batch_size
        self.dropout = dropout
        self.batchnormalization = batchnormalization


class MultipleTrainedModels:
    parameter: Parameter
    evaluation: MultipleTrainedModelsEvaluation
    model: Model
    models: Models

    def __init__(self, parameter: Parameter, evaluation: MultipleTrainedModelsEvaluation, model: Model, models: Models) -> None:
        self.parameter = parameter
        self.evaluation = evaluation
        self.model = model
        self.models = models
