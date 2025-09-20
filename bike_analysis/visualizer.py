import matplotlib.pyplot as plt

def plot_average_price(data):
    brands = list(data.keys())
    prices = list(data.values())
    plt.bar(brands, prices)
    plt.xticks(rotation=45)
    plt.title("Средняя цена по брендам")
    plt.xlabel("Бренд")
    plt.ylabel("Цена")
    plt.tight_layout()
    plt.show()

def plot_top_bikes(bikes, title, value_label):
    names = [f"{b.brand} {b.model}" for b in bikes]
    values = [b.price if value_label == "Цена" else b.km_driven for b in bikes]
    plt.figure(figsize=(10, 6))
    plt.barh(names, values, color="#4CAF50")
    plt.xlabel(value_label)
    plt.title(title)
    plt.gca().invert_yaxis()
    plt.tight_layout()
    plt.show()

def plot_best_bikes(bikes):
    names = [f"{b.brand} {b.model}" for b in bikes]
    prices = [b.price for b in bikes]
    plt.figure(figsize=(10, 6))
    plt.barh(names, prices, color="#009688")
    plt.xlabel("Цена")
    plt.title("Лучшие байки для покупки (низкая цена и пробег)")
    plt.gca().invert_yaxis()
    plt.tight_layout()
    plt.show()

def plot_brand_bikes(bikes, brand):
    models = [f"{b.model}" for b in bikes]
    prices = [b.price for b in bikes]
    kms = [b.km_driven for b in bikes]

    fig, ax1 = plt.subplots(figsize=(10, 6))

    ax1.barh(models, prices, color="#2196F3", label="Цена")
    ax1.set_xlabel("Цена")
    ax1.set_title(f"Байки бренда {brand}: цена и пробег")
    ax1.invert_yaxis()

    ax2 = ax1.twiny()
    ax2.plot(kms, models, "ro", label="Пробег")
    ax2.set_xlabel("Пробег (км)")

    plt.tight_layout()
    plt.show()
