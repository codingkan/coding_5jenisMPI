# mpi_broadcast.py
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# Pengumuman dari dosen (proses 0)
if rank == 0:
    pengumuman = "Pengumuman: Ujian Tengah Semester minggu depan"
else:
    pengumuman = None

# Proses 0 mengirimkan pengumuman kepada semua mahasiswa
pengumuman = comm.bcast(pengumuman, root=0)

print(f"Proses {rank} menerima pengumuman: {pengumuman}")
