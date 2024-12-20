# mpi_scatter-gather.py
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# Daftar tugas kuliah yang akan dibagikan (proses 0)
if rank == 0:
    daftar_tugas = [
        "Tugas 1: Membaca Bab 1-3",
        "Tugas 2: Menyusun laporan",
        "Tugas 3: Membuat presentasi",
        "Tugas 4: Diskusi kelompok"
    ]
else:
    daftar_tugas = None

# Scatter tugas kuliah ke semua mahasiswa
tugas_saya = comm.scatter(daftar_tugas, root=0)

print(f"Proses {rank} menerima tugas: {tugas_saya}")

# Setelah selesai, mengumpulkan hasil dari semua mahasiswa
hasil_tugas = comm.gather(tugas_saya, root=0)

if rank == 0:
    print(f"Semua tugas yang dikerjakan: {hasil_tugas}")
