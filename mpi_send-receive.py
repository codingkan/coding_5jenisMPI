# mpi_send-receive.py
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# Tugas yang dikirimkan oleh mahasiswa
if rank == 0:
    tugas = "Tugas: Laporan Pemrograman Dasar"
    comm.send(tugas, dest=1)
    print(f"Proses {rank} mengirimkan tugas: {tugas}")

# Dosen (proses 1) menerima tugas
elif rank == 1:
    tugas_diterima = comm.recv(source=0)
    print(f"Proses {rank} menerima tugas: {tugas_diterima}")
