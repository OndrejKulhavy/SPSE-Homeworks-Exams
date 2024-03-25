import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error


def main():
    data = pd.read_csv(
        'https://raw.githubusercontent.com/mlcollege/ai-academy/main/06-Regrese/data/vypujcky_kol.csv',
        sep=','
    )

    input_features = [ 'rocni_obdobi', 'mesic', 'hodina', 'svatek', 'den_v_tydnu', 'pracovni_den', 'pocasi',
                      'teplota',]
    target_feature = 'pocet'

    X_train, X_test, y_train, y_test = train_test_split(data[input_features], data[target_feature], test_size=0.2)
    model = LinearRegression()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    mae = mean_absolute_error(y_test, y_pred)
    mse = mean_squared_error(y_test, y_pred, squared=False)
    print(mae)
    print(mse)


if __name__ == "__main__":
    main()
