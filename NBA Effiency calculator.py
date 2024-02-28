#Use season totals

def true_shooting_percentage(points:int, fga:int, fta:int)-> float:
    true_shooting = (points / (2 * (fga + 0.44 * fta))) * 100

    return true_shooting

def effective_fieldgoal_percentage(fgm:int, threes:int, fga:int)-> float:
    efg = (fgm + 0.5 * threes) / fga * 100

    return efg

def PER(fgm:int, fga:int, threes:int, ftm:int, fta:int, tos:int, mins:int, orebs:int, drebs:int, asts:int, 
        blocks:int , steals:int, fouls:int)->float:
    per=(fgm*85.910 + steals*53.897 + threes*51.757 + ftm*46.845 + blocks*39.190 + orebs*39.190 + asts*34.677 + drebs*14.707 
         - fouls*17.174 -(fta-ftm)*20.091 - (fga-fgm)*39.910 - tos*53.897)/mins
    
    return per

def effiency_calculator():
    name = input("Name: ")
    points = int(input("Points: "))
    fgm = int(input("Field Goals Made: "))
    fga= int(input("Field Goals Attempted: "))
    threes = int(input("3-Point Field Goals Made: "))
    fta = int(input("Free Throws Attempted: "))
    ts = true_shooting_percentage(points,fga,fta)

    efg = effective_fieldgoal_percentage(fgm,threes,fga)

    print(f"{name}: TS%: {ts:.1f} EFG%: {efg:.1f}")
    return name,ts,efg