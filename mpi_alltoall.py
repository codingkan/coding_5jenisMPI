# mpi_alltoall.py
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# Materi kuliah yang akan dibagikan (disesuaikan dengan jumlah proses)
materi_kuliah = [
    "Materi: Pemrograman Dasar",
    "Materi: Struktur Data",
    "Materi: Algoritma",
    "Materi: Basis Data"
]

# Setiap proses mengirimkan data sesuai dengan jumlah item yang diperlukan
# Pastikan data dikemas dalam bentuk list atau array
data = [materi_kuliah[rank]] * size  # Mengirimkan 4 item sesuai jumlah proses

# Semua proses akan mengirimkan data ke semua proses lain
recvbuf = comm.alltoall(data)

# Tampilkan hasil setelah menerima data
print(f"Proses {rank} menerima materi: {recvbuf}")
