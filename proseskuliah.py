from metaflow import FlowSpec, step

class ProsesKuliahFlow(FlowSpec):

    @step
    def start(self):
        """Memulai proses dengan pembayaran SPP."""
        print("Langkah 1: Membayar SPP.")
        self.next(self.krs)

    @step
    def krs(self):
        """Melakukan KRS."""
        print("Langkah 2: Melakukan KRS")
        self.next(self.cetak_jadwal)
    
    @step
    def cetak_jadwal(self):
        """Cetak Jadwal."""
        print("Langkah 3: Mencetak Jadwal")
        self.next(self.mengikuti_kuliah)

    @step
    def mengikuti_kuliah(self):
        """Mengikuti kuliah dan perkuliahan."""
        print("Langkah 4: Mengikuti kuliah dan perkuliahan.")
        self.next(self.mengumpulkan_tugas)

    @step
    def mengumpulkan_tugas(self):
        """Mengumpulkan tugas selama perkuliahan."""
        print("Langkah 5: Mengumpulkan tugas.")
        self.next(self.ujian_tengah_semester)

    @step
    def ujian_tengah_semester(self):
        """Mengikuti ujian tengah semester."""
        print("Langkah 6: Mengikuti ujian tengah semester.")
        self.next(self.ujian_akhir_semester)

    @step
    def ujian_akhir_semester(self):
        """Mengikuti ujian akhir semester."""
        print("Langkah 7: Mengikuti ujian akhir semester.")
        self.next(self.menerima_nilai_akhir)

    @step
    def menerima_nilai_akhir(self):
        """Menerima nilai akhir untuk mata kuliah."""
        print("Langkah 8: Menerima nilai akhir.")
        self.next(self.end)

    @step
    def end(self):
        """Akhir dari proses kuliah."""
        print("Proses selesai. Anda telah menerima nilai akhir.")

if __name__ == '__main__':
    ProsesKuliahFlow()