import os
import csv
file=os.path.join("Resources","election_data.csv")
with open (file,"r")as csv_file:
    csv_reader=csv.reader(csv_file,delimiter=",")
    csv_header=next(csv_reader)
    votes=0
    v_khan=0
    v_correy=0
    v_li=0
    v_otooley=0
    for row in csv_reader:
        #Total number of votes
        votes=votes+1
        #Candidates who received votes
        if row[2]=="Khan":
            v_khan=v_khan+1
        elif row[2]=="Correy":
            v_correy=v_correy+1
        elif row[2]=="Li":
            v_li=v_li+1
        else:
            v_otooley=v_otooley+1
        #Percentage of votes each candidate won
        p_khan=(v_khan/votes)*100
        p_khan_round=round(p_khan)
        p_correy=(v_correy/votes)*100
        p_correy_round=round(p_correy)
        p_li=(v_li/votes)*100
        p_li_round=round(p_li)
        p_otooley=(v_otooley/votes)*100
        p_otooley_round=round(p_otooley)
        #Winner of the Election 
        if v_khan>v_correy and v_khan>v_li and v_khan>v_otooley:
            winner="Khan"
        elif v_correy>v_khan and v_correy>v_li and v_correy>v_otooley:
            winner="Correy"
        elif v_li>v_correy and v_li>v_khan and v_li>v_otooley:
            winner="Li"
        else:
            winner="Otooley"
    #Output code
    output_data= f"""
    Election Resoults
    -----------------------------------------
    Total Votes : {votes}
    -----------------------------------------
    Khan : {p_khan_round:.3f}% ({v_khan})
    Correy : {p_correy_round:.3f}% ({v_correy})
    Li : {p_li_round:.3f}% ({v_li})
    O'Tooley : {p_otooley_round:.3f}% ({v_otooley})
    -----------------------------------------
    Winner: {winner}
    -----------------------------------------
    """
    output_txt="Analysis/Analysis.txt"
    with open(output_txt,"w")as file:
        file.write(output_data)
    print (output_data)

