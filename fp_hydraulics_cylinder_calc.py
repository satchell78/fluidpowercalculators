from math import*

ef=float(input("Extend Force= "))
rf=float(input("Retract Force= "))

p=float(input("Design PSI= "))

s=float(input("Stroke= "))

print("1 for Time 2 for GPM")
tg=int(input("Time(1) or GPM(2)= "))

if tg==1:
    t=float(input("Time= "))
    
if tg==2:  
    g=float(input("GPM= "))

rpm=float(input("RPM= "))

bea=(ef/p)

bore=sqrt(bea/0.7854)

print("1 for Ind. 4-Tie Rod")
print("2 for Mobile")
print("3 for Ag 4-Tie Rod")
print("Include Over Size 1-7")
print("Example 23")
print("For Mobile & OS Rod 3")
tr=int(input("tr= "))
if tr==11 and bore<=1.5:
    bore=1.5
    rod=0.625
if tr==11 and bore<=2 and bore>1.5:
    bore=2
    rod=1
if tr==11 and bore<=2.5 and bore>2:
    bore=2.5
    rod=1
if tr==11 and bore<=3.25 and bore>2.5:
    bore=3.25
    rod=1.375
if tr==11 and bore<=4 and bore>3.25:
    bore=4
    rod=1.75
if tr==11 and bore<=5 and bore>4:
    bore=5
    rod=2
if tr==11 and bore<=6 and bore>5:
    bore=6
    rod=2.5
if tr==11 and bore<=7 and bore>6:
    bore=7
    rod=3
if tr==11 and bore<=8 and bore>7:
    bore=8
    rod=3.5
if tr==11 and bore<=10 and bore>8:
    bore=10
    rod=4.5
if tr==11 and bore<=12 and bore>10:
    bore=12
    rod=5.5
if tr==11 and bore<=14 and bore>12:
    bore=14
    rod=7 
    
if tr==12 and bore<=1.5:
    bore=1.5
    rod=1
if tr==12 and bore<=2 and bore>1.5:
    bore=2
    rod=1.375
if tr==12 and bore<=2.5 and bore>2:
    bore=2.5
    rod=1.375
if tr==12 and bore<=3.25 and bore>2.5:
    bore=3.25
    rod=1.75
if tr==12 and bore<=4 and bore>3.25:
    bore=4
    rod=2
if tr==12 and bore<=5 and bore>4:
    bore=5
    rod=2.5
if tr==12 and bore<=6 and bore>5:
    bore=6
    rod=3
if tr==12 and bore<=7 and bore>6:
    bore=7
    rod=4
if tr==12 and bore<=8 and bore>7:
    bore=8
    rod=4
if tr==12 and bore<=10 and bore>8:
    bore=10
    rod=5.5
if tr==12 and bore<=12 and bore>10:
    bore=12
    rod=7
if tr==12 and bore<=14 and bore>12:
    bore=14
    rod=8  

if tr==13 and bore<=2.5:
    bore=2.5
    rod=1.75
if tr==13 and bore<=3.25 and bore>2.5:
    bore=3.25
    rod=2
if tr==13 and bore<=4 and bore>3.25:
    bore=4
    rod=2.5
if tr==13 and bore<=5 and bore>4:
    bore=5
    rod=3
if tr==13 and bore<=6 and bore>5:
    bore=6
    rod=4
if tr==13 and bore<=7 and bore>6:
    bore=7
    rod=5
if tr==13 and bore<=8 and bore>7:
    bore=8
    rod=5.5
if tr==13 and bore<=10 and bore>8:
    bore=10
    rod=7
if tr==13 and bore<=12 and bore>10:
    bore=12
    rod=8
if tr==13 and bore<=14 and bore>12:
    bore=14
    rod=10
if tr==14 and bore<=5 and bore>4:
    bore=5
    rod=3.5


if tr==21 and bore<=2:
    bore=2
    rod=1
if tr==21 and bore<=2.5 and bore>2:
    bore=2.5
    rod=1
if tr==21 and bore<=3 and bore>2.5:
    bore=3
    rod=1
if tr==21 and bore<=3.25 and bore>3:
    bore=3.25
    rod=1.25
if tr==21 and bore<3.5 and bore>3.25:
    bore=3.5
    rod=1.25
if tr==21 and bore<=4 and bore>3.5:
    bore=4
    rod=1.375
if tr==21 and bore<=4.5 and bore>4:
    bore=4.5
    rod=1.75
if tr==21 and bore<=5 and bore>4.5:
    bore=5
    rod=2
if tr==21 and bore<=5.5 and bore>5:
    bore=5.5
    rod=2.5
if tr==21 and bore<=6 and bore>5.5:
    bore=6
    rod=2.5
if tr==21 and bore<=7 and bore>6:
    bore=7
    rod=2.5
if tr==21 and bore<=8 and bore>7:
    bore=8
    rod=3.5 
if tr==21 and bore<=10 and bore>8:
    bore=10
    rod=4
if tr==21 and bore<=12 and bore>10:
    bore=12
    rod=4.5 

if tr==22 and bore<=2:
    bore=2
    rod=1.125
if tr==22 and bore<=2.5 and bore>2:
    bore=2.5
    rod=1.125
if tr==22 and bore<=3 and bore>2.5:
    bore=3
    rod=1.125
if tr==22 and bore<=3.25 and bore>3:
    bore=3.25
    rod=1.375
if tr==22 and bore<3.5 and bore>3.25:
    bore=3.5
    rod=1.375
if tr==22 and bore<=4 and bore>3.5:
    bore=4
    rod=1.5
if tr==22 and bore<=4.5 and bore>4:
    bore=4.5
    rod=2
if tr==22 and bore<=5 and bore>4.5:
    bore=5
    rod=2.5
if tr==22 and bore<=5.5 and bore>5:
    bore=5.5
    rod=3
if tr==22 and bore<=6 and bore>5.5:
    bore=6
    rod=3
if tr==22 and bore<=7 and bore>6:
    bore=7
    rod=3
if tr==22 and bore<=8 and bore>7:
    bore=8
    rod=4
if tr==22 and bore<=10 and bore>8:
    bore=10
    rod=4.5
if tr==22 and bore<=12 and bore>10:
    bore=12
    rod=5  

if tr==23 and bore<=2:
    bore=2
    rod=1.25
if tr==23 and bore<=2.5 and bore>2:
    bore=2.5
    rod=1.25
if tr==23 and bore<=3 and bore>2.5:
    bore=3
    rod=1.25
if tr==23 and bore<=3.25 and bore>3:
    bore=3.25
    rod=1.5
if tr==23 and bore<3.5 and bore>3.25:
    bore=3.5
    rod=1.5
if tr==23 and bore<=4 and bore>3.5:
    bore=4
    rod=1.75
if tr==23 and bore<=4.5 and bore>4:
    bore=4.5
    rod=2.5
if tr==23 and bore<=5 and bore>4.5:
    bore=5
    rod=3
if tr==23 and bore<=5.5 and bore>5:
    bore=5.5
    rod=3.5
if tr==23 and bore<=6 and bore>5.5:
    bore=6
    rod=3.5
if tr==23 and bore<=7 and bore>6:
    bore=7
    rod=3.5
if tr==23 and bore<=8 and bore>7:
    bore=8
    rod=4.5
if tr==23 and bore<=10 and bore>8:
    bore=10
    rod=5
if tr==23 and bore<=12 and bore>10:
    bore=12
    rod=6  

if tr==24 and bore<=2.5:
    bore=2.5
    rod=1.375
if tr==24 and bore<=3 and bore>2.5:
    bore=3
    rod=1.375
if tr==24 and bore<=3.25 and bore>3:
    bore=3.25
    rod=1.75
if tr==24 and bore<3.5 and bore>3.25:
    bore=3.5
    rod=1.75
if tr==24 and bore<=4 and bore>3.5:
    bore=4
    rod=2
if tr==24 and bore<=4.5 and bore>4:
    bore=4.5
    rod=3
if tr==24 and bore<=5 and bore>4.5:
    bore=5
    rod=3.5
if tr==24 and bore<=5.5 and bore>5:
    bore=5.5
    rod=4
if tr==24 and bore<=6 and bore>5.5:
    bore=6
    rod=4
if tr==24 and bore<=7 and bore>6:
    bore=7
    rod=4
if tr==24 and bore<=10 and bore>7:
    bore=10
    rod=6
if tr==24 and bore<=12 and bore>10:
    bore=12
    rod=8  

if tr==25 and bore<=2.5:
    bore=2.5
    rod=1.5
if tr==25 and bore<=3 and bore>2.5:
    bore=3
    rod=1.5
if tr==25 and bore<=3.25 and bore>2.5:
    bore=3.25
    rod=2
if tr==25 and bore<3.5 and bore>3.25:
    bore=3.5
    rod=2
if tr==25 and bore<=4 and bore>3.5:
    bore=4
    rod=2.5
if tr==25 and bore<=4.5 and bore>4:
    bore=4.5
    rod=3.5
if tr==25 and bore<=5 and bore>4.5:
    bore=5
    rod=4
if tr==25 and bore<=5.5 and bore>5:
    bore=5.5
    rod=4.5
if tr==25 and bore<=6 and bore>5.5:
    bore=6
    rod=4.5
if tr==25 and bore<=7 and bore>6:
    bore=7
    rod=4.5  

if tr==26 and bore<=2.5:
    bore=2.5
    rod=1.75
if tr==26 and bore<=3 and bore>2.5:
    bore=3
    rod=1.75
if tr==26 and bore<3.5 and bore>3:
    bore=3.5
    rod=2.5
if tr==26 and bore<=4 and bore>3.5:
    bore=4
    rod=3
    
if tr==27 and bore<=3:
    bore=3
    rod=2

    
if tr==31 and bore<=2:
    bore=2
    rod=1.0625
if tr==31 and bore<=2.5 and bore>2:
    bore=2.5
    rod=1.25
if tr==31 and bore<=3 and bore>2.5:
    bore=3
    rod=1.5
if tr==31 and bore<=3.5 and bore>3:
    bore=3.5
    rod=2
if tr==31 and bore<4 and bore>3.5:
    bore=4
    rod=2
if tr==31 and bore<=5 and bore>4:
    bore=4
    rod=2
  
print("Bore and Rod", bore, rod)
bea=float((bore**2)*0.7854)

rea=float(((bore**2)-(rod**2))*0.7854)

ratio=(bea/rea)

evol=(bea*s)

rvol=(rea*s)

elpsi=(ef/bea)

rlpsi=(rf/rea)

comp=(elpsi*1.15)

rv=(elpsi*1.3225)

if tg==1:
    gpm=(evol/(t*3.85))
    exttime=t
    rettime=t
if tg==2:  
    exttime=(evol/(g*3.85))
    rettime=(rvol/(g*3.85))
    gpm=g

extipm=((gpm*231)/bea)
retipm=((gpm*231)/rea)
pumpcid=((gpm*231)/rpm)

bea=round(bea, 2)
rea=round(rea, 2)
ratio=round(ratio,2)
evol=round(evol,2)
rvol=round(rvol,2)
elpsi=round(elpsi,0)
rlpsi=round(rlpsi,0)
comp=round(comp,2)
rv=round(rv,2)
gpm=round(gpm,2)
exttime=round(exttime,2)
rettime=round(rettime,2)
extipm=round(extipm,2)
retipm=round(retipm,2)
pumpcid=round(pumpcid,2)

print("Actual BEA/REA",bea,rea)
print("Ratio",ratio)
print("Vol E/R",evol,rvol)
print("LPSI E/R",elpsi,rlpsi)
print("Comp",comp)
print("RV",rv)
print("Ext. Time",exttime,rettime)
print("IPM E/R",extipm,retipm)
print("Pump GPM",gpm)
print("Pump CID",pumpcid)



  
