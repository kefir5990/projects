import tkinter as tk
from tkinter import filedialog
from models.dataset import BikeDataset
from models.analyzer import Analyzer
from visualizer import plot_average_price

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Анализ байков")
        root.geometry("600x400")

        self.by_price = tk.BooleanVar()
        self.by_km = tk.BooleanVar()

        title_label = tk.Label(root, text="Информация по рынку мотоциклов",
                       font=("Helvetica", 16, "bold"), fg="#333")
        title_label.pack(pady=10)


        self.load_btn = tk.Button(root, text="Загрузить CSV", command=self.load_data,
                                  width=35, height=2, bg="#4CAF50", fg="white",
                                  activebackground="#45a049", activeforeground="white")
        self.load_btn.pack(pady=10)

        self.cheapest_btn = tk.Button(root, text="Топ-5 дешёвых байков", command=self.show_cheapest,
                              width=35, height=2, bg="#FF9800", fg="white",
                              activebackground="#FB8C00", activeforeground="white")
        self.cheapest_btn.pack(pady=5)

        self.lowest_km_btn = tk.Button(root, text="Топ-5 байков с минимальным пробегом", command=self.show_lowest_km,
                               width=35, height=2, bg="#9C27B0", fg="white",
                               activebackground="#7B1FA2", activeforeground="white")
        self.lowest_km_btn.pack(pady=5)

        self.best_btn = tk.Button(root, text="Лучшие байки для покупки", command=self.show_best_bikes,
                          width=35, height=2, bg="#009688", fg="white",
                          activebackground="#00796B", activeforeground="white")
        self.best_btn.pack(pady=10)

        self.brand_entry = tk.Entry(root, width=30)
        self.brand_entry.pack(pady=5)
        self.brand_entry.insert(0, "Введите бренд")

        self.brand_btn = tk.Button(root, text="Показать байки бренда", command=self.show_brand_bikes,
                           width=35, height=2, bg="#3F51B5", fg="white",
                           activebackground="#303F9F", activeforeground="white")
        self.brand_btn.pack(pady=5)


        self.dataset = None
        self.analyzer = None

    def load_data(self):
        path = filedialog.askopenfilename()
        self.dataset = BikeDataset(path)
        self.analyzer = Analyzer(self.dataset.bikes)
        result = self.analyzer.average_price_by_brand()
        plot_average_price(result)

    def show_top(self):
        if self.analyzer:
            by_price = self.by_price.get()
            by_km = self.by_km.get()

            if not (by_price or by_km):
                return  # ничего не выбрано

            bikes = self.analyzer.top_bikes(by_price=by_price, by_km=by_km)

            # Определим критерий для подписи графика
            if by_price and not by_km:
                criterion = "price"
            elif by_km and not by_price:
                criterion = "km"
            else:
                criterion = "price"  # по умолчанию, если оба выбраны

            from visualizer import plot_top_bikes
            plot_top_bikes(bikes, criterion)

    def show_cheapest(self):
        if self.analyzer:
            bikes = self.analyzer.cheapest_bikes()
            from visualizer import plot_top_bikes
            plot_top_bikes(bikes, "Топ-5 дешёвых байков", "Цена")

    def show_lowest_km(self):
        if self.analyzer:
            bikes = self.analyzer.lowest_km_bikes()
            from visualizer import plot_top_bikes
            plot_top_bikes(bikes, "Топ-5 байков с минимальным пробегом", "Пробег (км)")

    def show_best_bikes(self):
        if self.analyzer:
            bikes = self.analyzer.best_bikes_for_purchase()
            from visualizer import plot_best_bikes
            plot_best_bikes(bikes)

    def show_brand_bikes(self):
        if self.analyzer:
            brand = self.brand_entry.get().strip()
            bikes = self.analyzer.bikes_by_brand(brand)
            if bikes:
                from visualizer import plot_brand_bikes
                plot_brand_bikes(bikes, brand)
            else:
                tk.messagebox.showinfo("Результат", f"Байки бренда '{brand}' не найдены.")




root = tk.Tk()
app = App(root)
root.mainloop()
