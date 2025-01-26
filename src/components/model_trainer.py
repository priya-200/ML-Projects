import os
import sys
from dataclasses import dataclass

from catboost import CatBoostRegressor
from sklearn.ensemble import (
    AdaBoostRegressor,
    GradientBoostingRegressor,
    RandomForestRegressor
)
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from xgboost import XGBRegressor

from src.exception import CustomeException
from src.logger import logging

from src.utils import save_object,evaluate_models

@dataclass
class ModelTrainerConfig:
    train_model_file_path = os.path.join('artifacts','model.pkl')

class ModelTrainer:
    def __init__(self):
        self.model_train_config = ModelTrainerConfig()
    
    def initate_model_trainer(self,train_arr,test_arr):
        try:
            logging.info("Spliting the train and test input data")
            X_train,X_test,y_train,y_test = (
                train_arr[:,:-1],
                test_arr[:,:-1],
                train_arr[:,-1],
                test_arr[:,-1]
            )

            models = {
                "Random Forest" : RandomForestRegressor(),
                "Decision Tree" : DecisionTreeRegressor(),
                "Gradient Boosting" : GradientBoostingRegressor(),
                "Linear Regressor" : LinearRegression(),
                "XGBClassifier" : XGBRegressor(),
                "K-neighbors Regressor" : KNeighborsRegressor(),
                "CatBoosting Regressor" : CatBoostRegressor(verbose=0),
                "AdaBoost Regressor": AdaBoostRegressor()
            }

            model_report:dict = evaluate_models(X_train=X_train,y_train = y_train,X_test = X_test,y_test = y_test,models = models)

            best_model_Score = max(sorted(model_report.values()))

            best_model_name = list(model_report.keys())[
                list(model_report.values()).index(best_model_Score)
            ]

            best_model = models[best_model_name]

            if best_model_Score < 0.6:
                raise CustomeException("No best model found")
            logging.info(f"Best model found on both traing and testing dataset")

            save_object(
                file_path = self.model_train_config.train_model_file_path,
                obj = best_model
            )

            predicted = best_model.predict(X_test)

            score = r2_score(y_test,predicted)
            return score
        except Exception as e:
            raise CustomeException(e,sys)