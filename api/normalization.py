import pandas as pd
from sklearn.preprocessing import (StandardScaler)

extra_data = pd.read_csv("../data/train.csv")


def normalized_test_data(df):
    features = extra_data[
        ['MSSubClass', 'MSZoning', 'LotArea', 'Street', 'LotShape',
         'LandContour', 'Utilities', 'LotConfig', 'LandSlope', 'Neighborhood',
         'Condition1', 'Condition2', 'BldgType', 'HouseStyle', 'OverallQual',
         'OverallCond', 'YearBuilt', 'YearRemodAdd', 'RoofStyle', 'RoofMatl',
         'Exterior1st', 'Exterior2nd', 'ExterQual', 'ExterCond', 'Foundation',
         'BsmtFinSF1', 'BsmtFinSF2', 'BsmtUnfSF', 'TotalBsmtSF', 'Heating',
         'HeatingQC', 'CentralAir', '1stFlrSF', '2ndFlrSF',
         'LowQualFinSF', 'GrLivArea', 'BsmtFullBath', 'BsmtHalfBath', 'FullBath',
         'HalfBath', 'BedroomAbvGr', 'KitchenAbvGr', 'KitchenQual',
         'TotRmsAbvGrd', 'Functional', 'Fireplaces', 'GarageCars', 'GarageArea',
         'PavedDrive', 'WoodDeckSF', 'OpenPorchSF', 'EnclosedPorch', '3SsnPorch',
         'ScreenPorch', 'PoolArea', 'MiscVal', 'MoSold', 'YrSold', 'SaleType',
         'SaleCondition']]
    df.drop("Id", axis=1, inplace=True)

    testing = pd.get_dummies(features)

    s = StandardScaler()
    testing = s.fit_transform(testing)

    return testing
