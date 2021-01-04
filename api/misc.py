import pandas as pd
import numpy as np


selected_features = [
    'MSSubClass',
    'MSZoning',
    'LotFrontage',
    'LotArea',
    'Street',
    'Alley',
    'LotShape',
    'LandContour',
    'Utilities',
    'LotConfig',
    'LandSlope',
    'Neighborhood',
    'Condition1',
    'Condition2',
    'BldgType',
    'HouseStyle',
    'OverallQual',
    'OverallCond',
    'YearBuilt',
    'YearRemodAdd',
    'RoofStyle',
    'RoofMatl',
    'Exterior1st',
    'Exterior2nd',
    'MasVnrType',
    'MasVnrArea',
    'ExterQual',
    'ExterCond',
    'Foundation',
    'BsmtQual',
    'BsmtCond',
    'BsmtExposure',
    'BsmtFinType1',
    'BsmtFinSF1',
    'BsmtFinType2',
    'BsmtFinSF2',
    'BsmtUnfSF',
    'TotalBsmtSF',
    'Heating',
    'HeatingQC',
    'CentralAir',
    'Electrical',
    '1stFlrSF',
    '2ndFlrSF',
    'LowQualFinSF',
    'GrLivArea',
    'BsmtFullBath',
    'BsmtHalfBath',
    'FullBath',
    'HalfBath',
    'BedroomAbvGr',
    'KitchenAbvGr',
    'KitchenQual',
    'TotRmsAbvGrd',
    'Functional',
    'Fireplaces',
    'FireplaceQu',
    'GarageType',
    'GarageYrBlt',
    'GarageFinish',
    'GarageCars',
    'GarageArea',
    'GarageQual',
    'GarageCond',
    'PavedDrive',
    'WoodDeckSF',
    'OpenPorchSF',
    'EnclosedPorch',
    '3SsnPorch',
    'ScreenPorch',
    'PoolArea',
    'PoolQC',
    'Fence',
    'MiscFeature',
    'MiscVal',
    'MoSold',
    'YrSold',
    'SaleType',
    'SaleCondition'
]


def normalize(d: pd.DataFrame):
    df: pd.DataFrame = d.copy()
    df['MSZoning'].fillna('N')
    df['LotFrontage'].fillna(df['LotFrontage'].median(), inplace=True)
    df['Alley'].fillna('N')
    df['Exterior1st'].fillna('N')
    df['Exterior2nd'].fillna('N')
    df['Utilities'].fillna('N')
    df['MasVnrType'].fillna('N')
    df['BsmtFullBath'].fillna(0)
    df['BsmtHalfBath'].fillna(0)
    df['FullBath'].fillna(0)
    df['HalfBath'].fillna(0)
    df['KitchenQual'].fillna('N')
    df['Functional'].fillna('N')
    df['FireplaceQu'].fillna('N')
    df['GarageType'].fillna('N')
    df['GarageYrBlt'].fillna(0, inplace=True)
    df['GarageFinish'].fillna('N')
    df['GarageCars'].fillna(0)
    df['GarageArea'].fillna(0, inplace=True)
    df['GarageQual'].fillna('N')
    df['GarageCond'].fillna('N')
    df['BsmtFinSF2'].fillna(0, inplace=True)
    df['MasVnrArea'].fillna(0, inplace=True)
    df['BsmtFinSF1'].fillna(0, inplace=True)
    df['SaleType'].fillna('N')
    df['BsmtUnfSF'].fillna(0, inplace=True)
    df['TotalBsmtSF'].fillna(0, inplace=True)
    df['PoolQC'].fillna('N')
    df['Fence'].fillna('N')
    df['MiscFeature'].fillna('N')
    df['BsmtQual'].fillna('N')
    df['BsmtCond'].fillna('N')
    df['BsmtExposure'].fillna('N')
    df['BsmtFinType1'].fillna('N')
    df['BsmtFinType2'].fillna('N')
    df['Electrical'].fillna('N')
    df["AllSF"] = df["GrLivArea"] + df["TotalBsmtSF"]
    df['Area'] = df['LotArea'] * df['LotFrontage']
    df['Area_log'] = np.log1p(df['Area'])

    def Gar_category(cat):
        if cat <= 250:
            return 1
        elif 500 >= cat > 250:
            return 2
        elif 750 >= cat > 500:
            return 3
        elif 1000 >= cat > 750:
            return 4
        return 5

    df['GarageArea_cat'] = df['GarageArea'].apply(Gar_category)

    def Low_category(cat):
        if cat <= 1000:
            return 1
        elif 2000 >= cat > 1000:
            return 2
        elif 3000 >= cat > 2000:
            return 3
        return 4

    df['GrLivArea_cat'] = df['GrLivArea'].apply(Low_category)

    def fl1_category(cat):
        if cat <= 500:
            return 1
        elif 1000 >= cat > 500:
            return 2
        elif 1500 >= cat > 1000:
            return 3
        elif 2000 >= cat > 1500:
            return 4
        return 5

    df['1stFlrSF_cat'] = df['1stFlrSF'].apply(fl1_category)
    df['2ndFlrSF_cat'] = df['2ndFlrSF'].apply(fl1_category)

    def bsmtt_category(cat):
        if cat <= 500:
            return 1
        elif 1000 >= cat > 500:
            return 2
        elif 1500 >= cat > 1000:
            return 3
        elif 2000 >= cat > 1500:
            return 4
        return 5

    df['TotalBsmtSF_cat'] = df['TotalBsmtSF'].apply(bsmtt_category)

    def bsmt_category(cat):
        if cat <= 600:
            return 1
        elif 1000 >= cat > 600:
            return 2
        elif 1500 >= cat > 1000:
            return 3
        elif 2100 >= cat > 1500:
            return 4
        return 5

    df['BsmtUnfSF_cat'] = df['BsmtUnfSF'].apply(bsmt_category)

    def lot_category(cat):
        if cat <= 60:
            return 1
        elif 70 >= cat > 60:
            return 2
        elif 80 >= cat > 70:
            return 3
        return 4

    df['LotFrontage_cat'] = df['LotFrontage'].apply(lot_category)

    def lot_category1(cat):
        if cat <= 5000:
            return 1
        elif 10000 >= cat > 5000:
            return 2
        elif 15000 >= cat > 10000:
            return 3
        elif 20000 >= cat > 15000:
            return 4
        elif 25000 >= cat > 20000:
            return 5
        return 6

    df['LotArea_cat'] = df['LotArea'].apply(lot_category1)

    def year_category(yb):
        if yb <= 1910:
            return 1
        elif 1950 >= yb > 1910:
            return 2
        elif 1950 < yb < 1980:
            return 3
        elif 1980 <= yb < 2000:
            return 4
        return 5

    df['YearBuilt_cat'] = df['YearBuilt'].apply(year_category)
    df['YearRemodAdd_cat'] = df['YearRemodAdd'].apply(year_category)
    df['GarageYrBlt_cat'] = df['GarageYrBlt'].apply(year_category)

    def vnr_category(cat):
        if cat <= 250:
            return 1
        elif 500 >= cat > 250:
            return 2
        elif 750 >= cat > 500:
            return 3
        return 4

    df['MasVnrArea_cat'] = df['MasVnrArea'].apply(vnr_category)

    def allsf_category(yb):
        if yb <= 1000:
            return 1
        elif 2000 >= yb > 1000:
            return 2
        elif 3000 <= yb < 2000:
            return 3
        elif 4000 <= yb < 3000:
            return 4
        elif 5000 <= yb < 4000:
            return 5
        elif 6000 <= yb < 5000:
            return 6
        return 7

    df['AllSF_cat'] = df['AllSF'].apply(allsf_category)

    def OverallQual(yb):
        return yb

    df['OverallQual_cat'] = df['OverallQual'].apply(OverallQual)

    def sale_condition(cat):
        if cat == "Normal":
            return 1
        elif cat == "Abnorml":
            return 2
        elif cat == "AdjLand":
            return 3
        elif cat == "Alloca":
            return 4
        elif cat == "Family":
            return 5
        elif cat == "Partial":
            return 6
        return 7

    df['SaleCondition_cat'] = df['SaleCondition'].apply(sale_condition)

    def BsmtQual(cat):
        if cat == "NA":
            return 1
        elif cat == "Po":
            return 2
        elif cat == "Fa":
            return 3
        elif cat == "TA":
            return 4
        elif cat == "Gd":
            return 5
        elif cat == "Ex":
            return 6
        return 7

    df['BsmtQual_cat'] = df['BsmtQual'].apply(BsmtQual)

    def neighborhood(cat):
        if cat == "Blmngtn":
            return 1
        elif cat == "Blueste":
            return 2
        elif cat == "BrDale":
            return 3
        elif cat == "BrkSide":
            return 4
        elif cat == "ClearCr":
            return 5
        elif cat == "CollgCr":
            return 6
        elif cat == "Crawfor":
            return 7
        elif cat == "Edwards":
            return 8
        elif cat == "Gilbert":
            return 9
        elif cat == "IDOTRR":
            return 10
        elif cat == "MeadowV":
            return 11
        elif cat == "Mitchel":
            return 12
        elif cat == "Names":
            return 13
        elif cat == "NoRidge":
            return 14
        elif cat == "NPkVill":
            return 15
        elif cat == "NridgHt":
            return 16
        elif cat == "NWAmes":
            return 17
        elif cat == "OldTown":
            return 18
        elif cat == "SWISU":
            return 19
        elif cat == "Sawyer":
            return 20
        elif cat == "SawyerW":
            return 21
        elif cat == "Somerst":
            return 22
        elif cat == "StoneBr":
            return 23
        elif cat == "Timber":
            return 24
        elif cat == "Veenker":
            return 25
        return 26

    df['Neighborhood_cat'] = df['Neighborhood'].apply(neighborhood)
    remove_cols = ['SaleCondition', 'Neighborhood',
                   'OverallQual', 'BsmtQual', 'AllSF_cat',
                   'MiscVal', 'OverallCond', 'BsmtFinType2',
                   'SaleType', 'YrSold', 'MoSold', 'MiscFeature',
                   'Fence', 'PoolQC', 'PoolArea', 'PavedDrive',
                   'GarageCond', 'GarageQual', 'GarageArea_cat',
                   'GarageCars', 'GarageFinish', 'GarageType',
                   'FireplaceQu', 'Fireplaces', 'Functional',
                   'TotRmsAbvGrd', 'KitchenQual', 'KitchenAbvGr',
                   'BedroomAbvGr', 'HalfBath', 'FullBath',
                   'BsmtHalfBath', 'BsmtFullBath', 'GrLivArea_cat',
                   'MSSubClass', 'MSZoning', 'LotFrontage_cat',
                   'LotArea_cat', 'Street', 'Alley', 'LotShape',
                   'LandContour', 'Utilities', 'LotConfig',
                   'LandSlope', 'Condition1', 'Condition2',
                   'BldgType', 'HouseStyle', 'YearBuilt_cat',
                   'YearRemodAdd_cat', 'RoofStyle', 'RoofMatl', 'Exterior2nd',
                   'Exterior1st', 'MasVnrType', 'MasVnrArea_cat', 'ExterQual',
                   'ExterCond', 'Foundation', 'BsmtCond', 'BsmtExposure',
                   'BsmtFinType1', 'BsmtUnfSF_cat', 'TotalBsmtSF_cat',
                   'Heating',
                   'HeatingQC', 'CentralAir', 'Electrical', '1stFlrSF_cat',
                   '2ndFlrSF_cat']
    df = df.drop(remove_cols, 1)

    df['LotFrontage_log'] = np.log1p(df['LotFrontage'])
    df['LotArea_log'] = np.log1p(df['LotArea'])
    df['BsmtUnfSF_log'] = np.log1p(df['BsmtUnfSF'])

    df['Is_MasVnr'] = [1 if i != 0 else 0 for i in df['MasVnrArea']]
    df['Is_BsmtFinSF1'] = [1 if i != 0 else 0 for i in df['BsmtFinSF1']]
    df['Is_BsmtFinSF2'] = [1 if i != 0 else 0 for i in df['BsmtFinSF2']]
    df['Is_BsmtUnfSF'] = [1 if i != 0 else 0 for i in df['BsmtUnfSF']]
    df['Is_TotalBsmtSF'] = [1 if i != 0 else 0 for i in df['TotalBsmtSF']]
    df['Is_2ndFlrSF'] = [1 if i != 0 else 0 for i in df['2ndFlrSF']]
    df['Is_LowQualFinSF'] = [1 if i != 0 else 0 for i in df['LowQualFinSF']]
    df['Is_GarageArea'] = [1 if i != 0 else 0 for i in df['GarageArea']]
    df['Is_WoodDeckSF'] = [1 if i != 0 else 0 for i in df['WoodDeckSF']]
    df['Is_OpenPorchSF'] = [1 if i != 0 else 0 for i in df['OpenPorchSF']]
    df['Is_EnclosedPorch'] = [1 if i != 0 else 0 for i in df['EnclosedPorch']]
    df['Is_3SsnPorch'] = [1 if i != 0 else 0 for i in df['3SsnPorch']]
    df['Is_ScreenPorch'] = [1 if i != 0 else 0 for i in df['ScreenPorch']]
    return df


def prepare(d: dict):
    # for key in d.keys():
    #     if key not in selected_features:
    #         del d[key]
    # if any(k not in selected_features for k in d.keys()):
    #     raise ValueError("Wrong features specified, "
    #                      f"allowed features: {selected_features}")
    data = {
        'MSSubClass': [d.get("MSSubClass", 0.0)],
        'MSZoning': [d.get("MSZoning", None)],
        'LotFrontage': [d.get("LotFrontage", 0.0)],
        'LotArea': [d.get("LotArea", 0.0)],
        'Street': [d.get("Street", None)],
        'Alley': [d.get("Alley", None)],
        'LotShape': [d.get("LotShape", None)],
        'LandContour': [d.get("LandContour", None)],
        'Utilities': [d.get("Utilities", None)],
        'LotConfig': [d.get("LotConfig", None)],
        'LandSlope': [d.get("LandSlope", None)],
        'Neighborhood': [d.get("Neighborhood", None)],
        'Condition1': [d.get("Condition1", None)],
        'Condition2': [d.get("Condition2", None)],
        'BldgType': [d.get("BldgType", None)],
        'HouseStyle': [d.get("HouseStyle", None)],
        'OverallQual': [d.get("OverallQual", 0.0)],
        'OverallCond': [d.get("OverallCond", 0.0)],
        'YearBuilt': [d.get("YearBuilt", 0.0)],
        'YearRemodAdd': [d.get("YearRemodAdd", 0.0)],
        'RoofStyle': [d.get("RoofStyle", None)],
        'RoofMatl': [d.get("RoofMatl", None)],
        'Exterior1st': [d.get("Exterior1st", None)],
        'Exterior2nd': [d.get("Exterior2nd", None)],
        'MasVnrType': [d.get("MasVnrType", None)],
        'MasVnrArea': [d.get("MasVnrArea", 0.0)],
        'ExterQual': [d.get("ExterQual", None)],
        'ExterCond': [d.get("ExterCond", None)],
        'Foundation': [d.get("Foundation", None)],
        'BsmtQual': [d.get("BsmtQual", None)],
        'BsmtCond': [d.get("BsmtCond", None)],
        'BsmtExposure': [d.get("BsmtExposure", None)],
        'BsmtFinType1': [d.get("BsmtFinType1", None)],
        'BsmtFinSF1': [d.get("BsmtFinSF1", 0.0)],
        'BsmtFinType2': [d.get("BsmtFinType2", None)],
        'BsmtFinSF2': [d.get("BsmtFinSF2", 0.0)],
        'BsmtUnfSF': [d.get("BsmtUnfSF", 0.0)],
        'TotalBsmtSF': [d.get("TotalBsmtSF", 0.0)],
        'Heating': [d.get("Heating", None)],
        'HeatingQC': [d.get("HeatingQC", None)],
        'CentralAir': [d.get("CentralAir", None)],
        'Electrical': [d.get("Electrical", None)],
        '1stFlrSF': [d.get("1stFlrSF", 0.0)],
        '2ndFlrSF': [d.get("2ndFlrSF", 0.0)],
        'LowQualFinSF': [d.get("LowQualFinSF", 0.0)],
        'GrLivArea': [d.get("GrLivArea", 0.0)],
        'BsmtFullBath': [d.get("BsmtFullBath", 0.0)],
        'BsmtHalfBath': [d.get("BsmtHalfBath", 0.0)],
        'FullBath': [d.get("FullBath", 0.0)],
        'HalfBath': [d.get("HalfBath", 0.0)],
        'BedroomAbvGr': [d.get("BedroomAbvGr", 0.0)],
        'KitchenAbvGr': [d.get("KitchenAbvGr", 0.0)],
        'KitchenQual': [d.get("KitchenQual", None)],
        'TotRmsAbvGrd': [d.get("TotRmsAbvGrd", 0.0)],
        'Functional': [d.get("Functional", None)],
        'Fireplaces': [d.get("Fireplaces", 0.0)],
        'FireplaceQu': [d.get("FireplaceQu", None)],
        'GarageType': [d.get("GarageType", None)],
        'GarageYrBlt': [d.get("GarageYrBlt", 0.0)],
        'GarageFinish': [d.get("GarageFinish", None)],
        'GarageCars': [d.get("GarageCars", 0.0)],
        'GarageArea': [d.get("GarageArea", 0.0)],
        'GarageQual': [d.get("GarageQual", None)],
        'GarageCond': [d.get("GarageCond", None)],
        'PavedDrive': [d.get("PavedDrive", None)],
        'WoodDeckSF': [d.get("WoodDeckSF", 0.0)],
        'OpenPorchSF': [d.get("OpenPorchSF", 0.0)],
        'EnclosedPorch': [d.get("EnclosedPorch", 0.0)],
        '3SsnPorch': [d.get("3SsnPorch", 0.0)],
        'ScreenPorch': [d.get("ScreenPorch", 0.0)],
        'PoolArea': [d.get("PoolArea", 0.0)],
        'PoolQC': [d.get("PoolQC", None)],
        'Fence': [d.get("Fence", None)],
        'MiscFeature': [d.get("MiscFeature", None)],
        'MiscVal': [d.get("MiscVal", 0.0)],
        'MoSold': [d.get("MoSold", 0.0)],
        'YrSold': [d.get("YrSold", 0.0)],
        'SaleType': [d.get("SaleType", None)],
        'SaleCondition': [d.get("SaleCondition", None)]
    }
    return pd.DataFrame(data)
