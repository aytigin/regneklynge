from regneklynge import Regneklynge
from rack import Rack
from node import Node


abel = Regneklynge(12)

for tall in range(650):
    abel.settInnNode(Node(64, 1))

for tall in range(16):
    abel.settInnNode(Node(1024, 2))

print("abel:")
print("Noder med minst 32 GB:", abel.noderMedNokMinne(32))
print("Noder med minst 64 GB:", abel.noderMedNokMinne(64))
print("Noder med minst 128 GB:", abel.noderMedNokMinne(128))
print()
print("Antall prosessorer:", abel.antProsessoreriRegneklynge())
print("Antall rack:", abel.antRacks())
