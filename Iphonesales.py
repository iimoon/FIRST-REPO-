import pandas as pd
import matplotlib.pyplot  as plt
import numpy as np
import time
print("\n")
print("\t\t************************************************")
print("\t\t*******APPLE SALES DATA- FEBRUARY 2021*******")
print("\t\t************************************************")
msg= '''  .:'
          __ :'__
       .'`__`-'__``.
      :__________.-'
      :_________:    Think Different
       :_________`-;
        `.__.-.__.  '                  

('/'*50)'''
msg1=''' Iphone 12 is the latest mobile device by our company, Providing fast performance with the brand new A14 Bionic
        Chip, An edge to edge OLED display. Ceramic sheild with four times better drop performance. And night mode on
        every camera! Iphone 12 has it all - in two perfect sizes! The dataset contains the data generated in  the  month  of  February  
        2021 and the data is  categorised in the different categories (State wise ). 
        
        In this project we are going to analyse the same dataset using Python Pandas on  windows  machine  but
        the project can  be  run  on any  machine  support  Python  and Pandas. Besides pandas , we  also used
        matplotlib python module for visualization of this dataset. 
        The   whole project  is divided  into three major parts ie Export/Import, analysis and visualization .
        All these parts are further divided into menus for easy navigation'''
for x in msg:
    print(x,end='')
    time.sleep(0.010)
for x in msg1:
    print(x,end='')
    time.sleep(0.010)

wait = input('\n\n\n\n\n\t\t\tHit any key to proceed.....')
print()
print("*******************************************************")
print()
#Read/Export data from CSV to Dataframe with index 1 to 14
while True:
        print("\t\t\t Welcome!")
        print("\t\t\tIphone 12 Sales report --- MENU")
        print("\t\t\tPlease select any of the following to continue")
        print("\t\t\t1.Export CSV to Dataframe")
        print("\t\t\t2.Data Analysis ")
        print("\t\t\t3.Data Visualisation(Line,bar)")
        print("\t\t\t4.Close")
        print("\n")
        print("\t\t\tEnter your choice:")
        ch=int(input())
        if ch==1:
                #Read/Export data from CSV to Dataframe with default index
                df=pd.read_csv("iphonesales-us.csv")
                df.index=np.arange(1,16)
                print("*******************************************************")
                print("Dataframe with Index:")
                print("*********************")
                print(df)
                print("*******************************************************")
                print()
                wait = input('Hit any key to continue.....')
                #Read/Export data from CSV to Dataframe with labelled index
                df=pd.read_csv("iphonesales-us.csv",index_col=0)
                print("\nDataframe with States Code as Labelled Index:\n")
                print("******************************")
                print(df)
                print("*******************************************************\n")
        elif ch==2:
                while True:
                        print("**********************")
                        print("APPLE SALES ANALYSIS MENU")
                        print("**********************")
                        print(">1.Sales analysis of specific States:<")
                        print(">2.Display top and bottom rows<")
                        print(">3.Show columns<")
                        print(">4.Add new Column<")
                        print(">5.Delete a Column<")
                        print(">6.Delete a Record<")
                        print(">7.Update a Record<")
                        print(">8.Sort Dataframe<")
                        print(">9.Access Specific Rows-Slicing<")
                        print(">10.Show Specific column(s)<")
                        print(">11.Iteration on Dataframe<")
                        print(">12.Export to CSV/Update CSV<")
                        print(">13.Display Complete DataFrame<")
                        print(">14.Exit<")
                        c=int(input("Enter your choice:"))
                        if c==1:
                                d=input("\nEnter the States code you want to Display: ")
                                print(df.loc[d])
                                print('\n\n\n Hit any key to continue....')
                                wait=input()
                        elif c==2:
                                n = int(input('Enter Total number of top rows you want to show :'))
                                print(df.head(n))
                                s = int(input('Enter Total number of bottom rows you want to show :'))
                                print(df.head(s))
                        elif c==3:
                                print("\nThe Column labels of Dataframe:")
                                print(df.columns)
                                print('\n\n\n Hit any key to continue....')
                                wait=input()
                        elif c==4:
                                newcol_name = input('Enter new Column name to add:')
                                newcol_values = eval(input('Enter new Column default values :'))
                                df[newcol_name]=newcol_values
                                print("New Dataframe after Column addition:")
                                print(df)
                                print('\n\n\n Hit any key to continue....')
                                wait=input()
                        elif c==5:
                                print("\nThe Column labels of Dataframe are as follows:")
                                print(df.columns)
                                col_name =input('Enter column Name to be deleted :')
                                df.drop(col_name,axis=1,inplace=True)
                                print("New Dataframe after Column Deletion:")
                                print(df)
                                print('\n\n\n Hit any key to continue....')
                                wait=input()
                        elif c==6:
                                ind_lbl =input('Enter the States code that You want to delete :')
                                df = df.drop(ind_lbl)
                                print("New Dataframe after Record Deletion:")
                                print(df)
                                print('\n\n\n Hit any key to continue....')
                                wait = input()
                        elif c==7:
                                d=input("Enter States Code to make changes")
                                n=input("Enter column label in which the value to be changed")
                                val=int(input("Enter new value"))
                                df[n][d]=val
                                print("New Dataframe after Updation:")
                                print(df)
                        elif c==8:
                                print("The Column labels of Dataframe are as follows:")
                                print(df.columns)
                                n=input("Enter column label by which the Dataframe to be sorted")
                                df.sort_values(by=n,axis=0,inplace=True)
                                print("New Dataframe after Sorting:")
                                print(df)
                        elif c==9:
                                d=input("Enter States Code from which slicing to be started: ")
                                n=input("Enter States Code upto which slicing to be ended: ")
                                print("Selectd Rows are given below")
                                print(df.loc[d:n])
                        elif c==10:
                                print("The Column labels of Dataframe are as follows:")
                                print(df.columns)
                                print("Column Selection Menu")
                                print("1. Single column")
                                print("2. Multiple columns")
                                print("3. Range of columns")
                                print("4. Exit")
                                while True:
                                        f=int(input("Enter the choice"))
                                        if f==1:
                                                col_name =input('Enter column Name to be Displayed :')
                                                print(df[col_name])
                                        elif f==2:
                                                col_name_list =eval(input('Enter column Names to be Displayed as a list:'))
                                                print(df[col_name_list])
                                        elif f==3:
                                                start_row,end_row=input('Enter Start States Name :'),input('Enter End States Name :')
                                                start_col,end_col=input('Enter Start Column Name :'),input('Enter End Column Name :')
                                                print(df.loc[start_row:end_row,start_col:end_col])
                                        elif f==4:
                                                print("\n\n\n\nBack to Main Menu")
                                                break
                                print('\n\n\n\nHit any key to continue....')
                                wait = input()
                        elif c==11:
                                print("\nIteration Menu")
                                print("1.States Wise Series Objects(Row-wise Iteration) :")
                                print("2.Extract data Column Wise (Column-wise Iteration) :")
                                print("3.Back to Main Menu")
                                print()
                                while True:
                                        f=int(input("Enter the choice"))
                                        if f==1:                                                
                                                print("**************************************")
                                                print("\nStates wise Series Ojects:\n")
                                                for i,v in df.iterrows():
                                                        print("Dictrict Code :",i)
                                                        print("Row values are as follows :")
                                                        print(v)
                                                print("***************************************")
                                        elif f==2:
                                                print("\nColumn wise Series Ojects:\n")
                                                for i,v in df.iteritems():
                                                        print("Column Name:",i)
                                                        print("Column values are as follows:")
                                                        print(v)
                                                print("********************************************")
                                        elif f==3:
                                                print("\n\n\n\nBack to Main Menu")
                                                break
                                print('\n\n\n\nHit any key to continue....')
                                wait = input()
                        elif c==12:
                                ans=input("\nDo you want to export it to CSV File/ Update CSV file --- Y/N")
                                if ans=='Y' or 'y':
                                          df.to_csv("covid-19kerala_updated.csv")
                                          print("CSV file updated Successfully")
                        elif c==13:
                                print("\n\nDataFrame is as follows:\n\n")
                                print(df)
                                break
                        elif c==14:
                                print("\n\n\n\nBack to Main Menu")
                                break
                        else:
                                print("Invalid Choice!!!!")
        
        elif ch==3:
                print("%%%%%%%%%%DATA VISUALISATION MENU%%%%%%%%%%%%%")
                print("*"*50)
                df=pd.read_csv('iphonesales-us.csv')
                df.drop(14,axis=0,inplace=True)
                print("\n\nDataFrame is as follows:\n\n")
                print(df)
                df['States'] = ['ARI','CAL','FLO','GEO','IDA','IND','KAN','KEN','TEX','ALA','WAS','PEN','MIC','MAS']
                States=df["States"]
                Iphone12=df["Iphone12"]
                Iphone12mini=df["Iphone12mini"]
                Iphone12pro=df["Iphone12mini"]
                Iphone12promax=df["Iphone12promax"]
                plt.xlabel("States")
                while True:
                        print("1. Line Chart ")
                        print("2. Bar Graph ")
                        print("3. Exit")
                        f=int(input("Enter the choice"))
                        if f==1:
                                while True:
                                        print("%%%%%%%%%%LINE CHART MENU%%%%%%%%%%")
                                        print("\t\t\tHit A to print the data for Iphone12 Sales as per States.")
                                        print("\t\t\tHit B to print the data for Iphone12mini Sales as per States.")
                                        print("\t\t\tHit C to print the data for Iphone12mini Sales as per States.")
                                        print("\t\t\tHit D to print the data for Iphone12promax Sales as per States.")
                                        print("\t\t\tHit E to Display Complete Data.")
                                        print(" ")
                                        d=input("Enter your choice to continue:")
                                        if d=='A':
                                                plt.ylabel("Iphone12 Sales")
                                                plt.title("States Wise Iphone12 Sales")
                                                plt.plot(States, Iphone12, color='r')
                                                plt.show()
                                        elif d=='B':
                                                plt.ylabel("Iphone12mini Sales")
                                                plt.title("States Wise Iphone12mini Sales")
                                                plt.plot(States, Iphone12mini, color='g')
                                                plt.show()
                                        elif d=='C':
                                                plt.ylabel("Iphone12mini Sales")
                                                plt.title("States Wise Iphone12mini Sales")
                                                plt.plot(States, Iphone12pro, color='y')
                                                plt.show()
                                        elif d=='D':
                                                plt.ylabel("Iphone12promax Sales")
                                                plt.title("States Wise Iphone12promax Sales")
                                                plt.plot(States, Iphone12promax, color='c')
                                                plt.show()
                                        elif d=='E':
                                                plt.ylabel("Number of Sales")
                                                plt.plot(States, Iphone12, color='b', label = "States Wise Iphone12 Sales")
                                                plt.plot(States, Iphone12mini, color='g', label = "States Wise Iphone12mini Sales")
                                                plt.plot(States, Iphone12pro, color='r', label = "States Wise Iphone12mini Sales")
                                                plt.plot(States, Iphone12promax, color='c', label = "States Wise Iphone12promax Sales")
                                                plt.legend()
                                                plt.show()
                                        else:
                                                print("\n\n\n\nBack to Main Menu\n\n\n")
                                                break
                                print('\n\n\n\nHit any key to continue....')
                                wait = input()
                        elif f==2:
                                while True:
                                        print("%%%%%%%%%%BAR CHART MENU%%%%%%%%%%")
                                        print("\t\t\tHit 1 to print the data for Iphone12 Sales as per States.")
                                        print("\t\t\tHit 2 to print the data for Iphone12mini Sales as per States.")
                                        print("\t\t\tHit 3 to print the data for Iphone12mini Sales as per States.")
                                        print("\t\t\tHit 4 to print the data for Iphone12promax Sales as per States.")
                                        print("\t\t\tHit 5 to print the data in form of stack bar chart")
                                        print("\t\t\tHit 6 to print the data in form of multi bar chart")
                                        print(" ")
                                        YC=int(input("Enter the number representing your preferred bar graph from the above choices:"))
                                        if YC == 1:
                                                plt.ylabel("Iphone12 Sales")
                                                plt.title("States Wise Iphone12 Sales")
                                                plt.bar(States, Iphone12, color='b', width = 0.5)
                                                plt.show()
                                        elif YC == 2:
                                                plt.ylabel("Iphone12mini Sales")
                                                plt.title("States Wise Iphone12mini Sales")
                                                plt.bar(States, Iphone12mini, color='g', width = 0.5)
                                                plt.show()
                                        elif YC == 3:
                                                plt.ylabel("Iphone12mini Sales")
                                                plt.title("States Wise Iphone12mini Sales")
                                                plt.bar(States, Iphone12pro, color='r', width = 0.5)
                                                plt.show()
                                        elif YC == 4:
                                                plt.ylabel("Iphone12promax Sales")
                                                plt.title("States Wise Iphone12promax Sales")
                                                plt.bar(States, Iphone12promax, color='c', width = 0.5)
                                                plt.show()
                                        elif YC == 5:
                                                plt.bar(States, Iphone12, color='b', width = 0.5, label = "States Wise Iphone12 Sales")
                                                plt.bar(States, Iphone12mini, color='g', width = 0.5, label = "States Wise Iphone12mini Sales")
                                                plt.bar(States, Iphone12pro, color='r', width = 0.5, label = "States Wise Iphone12mini Sales")
                                                plt.bar(States, Iphone12promax, color='c',width = 0.5, label = "States Wise Iphone12promax Sales")
                                                plt.legend()
                                                plt.show()
                                        elif YC == 6:
                                                D=np.arange(len(States))
                                                width=0.25
                                                plt.bar(D,Iphone12, width, color='b', label = "States Wise Iphone12 Sales")
                                                plt.bar(D+0.25, Iphone12mini, width, color='g', label = "States Wise Iphone12mini Sales")
                                                plt.bar(D+0.50, Iphone12pro, width, color='r', label = "States Wise Iphone12mini Sales")
                                                plt.bar(D+0.75, Iphone12promax ,width, color='c', label = "States Wise Iphone12promax Sales")
                                                plt.legend()
                                                plt.show()
                                        else:
                                                print("\n\n\n\nBack to Main Menu\n\n\n")
                                                break             
                                print('\n\n\n\nHit any key to continue....\n\n')
                                wait = input()
                        elif f==3:
                                print("\n\n\n\nBack to Main Menu")
                                break
                        else:
                                print("Incorrect Choice!")
                print('\n\n\n\nHit any key to continue....')
                wait = input()    
        elif ch==4:
                break
        else:
                print("The choice you have entered is invalid")
        



