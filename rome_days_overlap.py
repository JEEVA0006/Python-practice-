months=[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
arriveAlice=input("Enter the arrival date of Alice in the format MM-DD:")
leaveAlice=input("Enter the leaving date of Alice in the format MM-DD:")
arriveBob=input("Enter the arrival date of Bob in the format MM-DD:")
leaveBob=input("Enter the leaving date of Bob in the format MM-DD:")
Alicearrivemonth,Alicearrivedate=map(int,arriveAlice.split('-'))
Bobarrivemonth,Bobarrivedate=map(int,arriveBob.split('-'))
Aliceleftmonth,Aliceleftdate=map(int,leaveAlice.split('-'))
Bobleftmonth,Bobleftdate=map(int,leaveBob.split('-'))
alicearrivecount=0
for i in range(Alicearrivemonth):
     alicearrivecount+=months[i]
alicearrivecount+=Alicearrivedate
aliceleftcount=0
for i in range(Aliceleftmonth):
     aliceleftcount+=months[i]
aliceleftcount+=Aliceleftdate
bobarrivecount=0
for i in range(Bobarrivemonth):
     bobarrivecount+=months[i]
bobarrivecount+=Bobarrivedate
bobleftcount=0
for i in range(Bobleftmonth):
     bobleftcount+=months[i]
bobleftcount+=Bobleftdate
later_arrival=max(alicearrivecount,bobarrivecount)
earlier_departure=min(aliceleftcount,bobleftcount)
if earlier_departure>=later_arrival:
    overlap_days=earlier_departure-later_arrival+1
else:
    overlap_days=0
print(overlap_days)