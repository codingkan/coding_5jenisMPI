# mpi_reduce.py
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# Nilai ujian yang diberikan oleh setiap mahasiswa
nilai_ujian = rank * 10  # Nilai ujian mahasiswa sesuai dengan rank-nya

# Menggunakan reduce untuk menghitung rata-rata nilai ujian dari semua mahasiswa
total_nilai = comm.reduce(nilai_ujian, op=MPI.SUM, root=0)

if rank == 0:
    rata_rata = total_nilai / size
    print(f"Rata-rata nilai ujian adalah: {rata_rata}")
