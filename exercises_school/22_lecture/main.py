import pickle
import pandas as pd


def predict(quality, area, date_built, date_sell) -> float:
    with open("muj_model.dat", "rb") as openfile:
        model = pickle.load(openfile)
    data = pd.DataFrame([[quality, area, date_built, date_sell]], columns=['kvalita', 'plocha', 'rok_stavby', 'rok_prodeje'])
    predicted_price = model.predict(data)
    return predicted_price[0]


def main():
    predicted_price = predict(8, 140, 2003, 2020)
    print(f"Predicted price: {predicted_price:.6f} million")


if __name__ == "__main__":
    main()

