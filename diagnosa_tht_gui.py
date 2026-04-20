import tkinter as tk
from tkinter import messagebox

gejala_dict = {
    "G1": "Nafas abnormal", "G2": "Suara serak", "G3": "Perubahan kulit",
    "G4": "Telinga penuh", "G5": "Nyeri bicara menelan", "G6": "Nyeri tenggorokan",
    "G7": "Nyeri leher", "G8": "Pendarahan hidung", "G9": "Telinga berdenging",
    "G10": "Airliur menetes", "G11": "Perubahan suara", "G12": "Sakit kepala",
    "G13": "Nyeri pinggir hidung", "G14": "Serangan vertigo", "G15": "Getah bening",
    "G16": "Leher bengkak", "G17": "Hidung tersumbat", "G18": "Infeksi sinus",
    "G19": "Beratbadan turun", "G20": "Nyeri telinga", "G21": "Selaput lendir merah",
    "G22": "Benjolan leher", "G23": "Tubuh tak seimbang", "G24": "Bolamata bergerak",
    "G25": "Nyeri wajah", "G26": "Dahi sakit", "G27": "Batuk", "G28": "Tumbuh dimulut",
    "G29": "Benjolan dileher", "G30": "Nyeri antara mata", "G31": "Radang gendang telinga",
    "G32": "Tenggorokan gatal", "G33": "Hidung meler", "G34": "Tuli", "G35": "Mual muntah",
    "G36": "Letih lesu", "G37": "Demam"
}

penyakit_dict = {
    "Tonsilitis": ["G37", "G12", "G5", "G27", "G6", "G21"],
    "Sinusitis Maksilaris": ["G37", "G12", "G27", "G17", "G33", "G36", "G29"],
    "Sinusitis Frontalis": ["G37", "G12", "G27", "G17", "G33", "G36", "G21", "G26"],
    "Sinusitis Edmoidalis": ["G37", "G12", "G27", "G17", "G33", "G36", "G21", "G30", "G13", "G26"],
    "Sinusitis Sfenoidalis": ["G37", "G12", "G27", "G17", "G33", "G36", "G29", "G7"],
    "Abses Peritonsiler": ["G37", "G12", "G6", "G15", "G2", "G29", "G10"],
    "Faringitis": ["G37", "G5", "G6", "G7", "G15"],
    "Kanker Laring": ["G5", "G27", "G6", "G15", "G2", "G19", "G1"],
    "Deviasi Septum": ["G37", "G17", "G20", "G8", "G18", "G25"],
    "Laringitis": ["G37", "G5", "G15", "G16", "G32"],
    "Kanker Leher & Kepala": ["G5", "G22", "G8", "G28", "G3", "G11"],
    "Otitis Media Akut": ["G37", "G20", "G35", "G31"],
    "Contact Ulcers": ["G5", "G2"],
    "Abses Parafaringeal": ["G5", "G16"],
    "Barotitis Media": ["G12", "G20"],
    "Kanker Nafasoring": ["G17", "G8"],
    "Kanker Tonsil": ["G6", "G29"],
    "Neuronitis Vestibularis": ["G35", "G24"],
    "Meniere": ["G20", "G35", "G14", "G4"],
    "Tumor Syaraf Pendengaran": ["G12", "G34", "G23"],
    "Kanker Leher Metastatik": ["G29"],
    "Osteosklerosis": ["G34", "G9"],
    "Vertigo Postular": ["G24"]
}

class SistemPakarTHT_GUI_Lengkap:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistem Pakar Diagnosa Penyakit THT")
        self.root.geometry("500x650")

        label_judul = tk.Label(root, text="Sistem Pakar Penyakit THT", font=("Helvetica", 14, "bold"))
        label_judul.pack(pady=10)
        
        label_petunjuk = tk.Label(root, text="Centang semua gejala yang Anda alami:", font=("Helvetica", 10))
        label_petunjuk.pack(pady=5)

        frame_utama = tk.Frame(root)
        frame_utama.pack(fill=tk.BOTH, expand=True, padx=20, pady=5)

        self.canvas = tk.Canvas(frame_utama)
        self.scrollbar = tk.Scrollbar(frame_utama, orient=tk.VERTICAL, command=self.canvas.yview)
        
        self.frame_gejala = tk.Frame(self.canvas)

        self.frame_gejala.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )
        self.canvas.create_window((0, 0), window=self.frame_gejala, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.gejala_vars = {}

        for kode, nama in gejala_dict.items():
            var = tk.BooleanVar()
            chk = tk.Checkbutton(self.frame_gejala, text=f"{kode} - {nama}", variable=var, font=("Helvetica", 10))
            chk.pack(anchor="w", pady=2)
            self.gejala_vars[kode] = var

        frame_tombol = tk.Frame(root)
        frame_tombol.pack(pady=15, fill=tk.X, padx=20)

        btn_reset = tk.Button(frame_tombol, text="Reset", font=("Helvetica", 12), bg="gray", fg="white", command=self.reset_gejala)
        btn_reset.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 5))

        btn_diagnosa = tk.Button(frame_tombol, text="Proses Diagnosa", font=("Helvetica", 12, "bold"), bg="blue", fg="white", command=self.proses_diagnosa)
        btn_diagnosa.pack(side=tk.RIGHT, fill=tk.X, expand=True, padx=(5, 0))

    def reset_gejala(self):
        for var in self.gejala_vars.values():
            var.set(False)

    def proses_diagnosa(self):
        gejala_user = set([kode for kode, var in self.gejala_vars.items() if var.get()])

        if not gejala_user:
            messagebox.showwarning("Peringatan", "Silakan centang minimal satu gejala terlebih dahulu!")
            return

        kemungkinan_penyakit = []
        for penyakit, gejala_penyakit in penyakit_dict.items():
            gejala_cocok = set(gejala_penyakit).intersection(gejala_user)
            
            if gejala_cocok:
                persentase = (len(gejala_cocok) / len(gejala_penyakit)) * 100
                kemungkinan_penyakit.append((penyakit, persentase))

        kemungkinan_penyakit.sort(key=lambda x: x[1], reverse=True)
        if kemungkinan_penyakit:
            hasil_teks = "Hasil diagnosa berdasarkan persentase kecocokan gejala:\n\n"
            penyakit_ditemukan = False
            
            for penyakit, persen in kemungkinan_penyakit:
                if persen >= 40:
                    hasil_teks += f"👉 {penyakit} ({persen:.0f}%)\n"
                    penyakit_ditemukan = True
            
            if not penyakit_ditemukan:
                 hasil_teks = "Gejala yang Anda alami tidak cukup kuat (di bawah 40% kecocokan) untuk merujuk pada penyakit THT tertentu di basis data kami."
        else:
            hasil_teks = "Tidak ditemukan penyakit yang sesuai dengan gejala tersebut di basis data kami."

        messagebox.showinfo("Hasil Diagnosa", hasil_teks)

if __name__ == "__main__":
    root = tk.Tk()
    app = SistemPakarTHT_GUI_Lengkap(root)
    root.mainloop()