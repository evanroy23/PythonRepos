import sys
import dbLib

dbObj = dbLib.DBHelper()

try:    

    print("--- execute -----------------------------------------")    
    dataRes = dbObj.execute('update ProductionSites set sitename="가고파여행2(주)" where productionSitesId = "53e07e8d-5871-f787-13e7-dfa0ca49ddbf "')    

    print( dataRes )


    print("--- fetch -------------------------------------------")   
    dataRes = dbObj.fetch('SELECT * from ProductionSites')
    for row in dataRes:
        #print(row)
        key = row.keys()
        value = row.values()
        print("productionSitesId : ", row['productionSitesId'], "\t sitename : ", row["sitename"])
        #print(key)
        #print(value)    
        
        #print(row['dataRes'])
        #break


    print("--- fetchOne -----------------------------------------")    
    dataRes = dbObj.fetchOne('SELECT * from ProductionSites where productionSitesId = "53e07e8d-5871-f787-13e7-dfa0ca49ddbf "')    

    print("productionSitesId : ", dataRes['productionSitesId'], "\t sitename : ", dataRes["sitename"])

except:
	sys.exit('db Connection Errors !!')