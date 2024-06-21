import tkinter as tk
from tkinter import ttk
from testdata import load_data


class YoubikeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("全國ubike資料")

        # 載入 YouBike 資料
        self.ubike_data = load_data()

        # 設定 Treeview
        self.tree = ttk.Treeview(self.root, columns=('sna', 'sarea', 'ar', 'lng', 'lat', 'mday', 'updateTime', 'act', 'total', 'rent_bikes', 'return_bikes'), show='headings')
        self.tree.heading('sna', text='站名')
        self.tree.heading('sarea', text='區域')
        self.tree.heading('ar', text='地段')
        self.tree.heading('lng', text='經度')
        self.tree.heading('lat', text='緯度')
        self.tree.heading('mday', text='回傳時間')
        self.tree.heading('updateTime', text='接收時間')
        self.tree.heading('act', text='啟用狀態')
        self.tree.heading('total', text='總車位數')
        self.tree.heading('rent_bikes', text='可借車輛數')
        self.tree.heading('return_bikes', text='可還車輛數')

        self.populate_treeview()

        self.tree.pack(fill='both', expand=True, padx=10, pady=10)

    def populate_treeview(self):
        for item in self.ubike_data:
            values = (item.sna, item.sarea, item.ar, item.lng, item.lat, item.mday, item.updateTime, item.act, item.total, item.rent_bikes, item.return_bikes)
            self.tree.insert('', tk.END, values=values)


def main():
    root = tk.Tk()
    app = YoubikeApp(root)
    root.mainloop()


if __name__ == '__main__':
    main()
