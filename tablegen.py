# -*- coding: utf-8 -*-
"""
Created on Fri Sep 02 18:48:09 2016

@author: os
"""

# -*- coding: utf-8 -*-
import os

def createClass(strin,classname):
    try:   
        cr = strin.find('CREATE') 
        strin = strin[cr:]
        cr = strin.find('(')
        strin = strin[cr+1:]
#        str = strin.split("\n")
        str = strin.split(",")
        if (len(str))<2 :
            return 'Zlý vstup'
    #    print len(str) 
        it=0
        zac =0 
        konec = 0
        for i in str:
            it=it+1
            if "CREATE" in i:
    #            print "Radek:%d - %s "%(it,i)
                zac = it
            if "ON [PRIMARY]" in i:
    #            print "Radek:%d - %s "%(it,i)
                konec = it
        if konec ==0:
            konec = len(str)
        print konec
        str= str[zac:konec]
#        print str[zac:konec-1]
        var=[]
        definitions=[]
        nulls=[]
        for i in str:
            st0 = i.split(" ")
            if len(st0)<2: continue
#            print len(st0) 
            st0[0] = st0[0].replace("[","")
            st0[0] = st0[0].replace("]","")
            var.append(st0[0])
            definitions.append(getDatatype(st0[1]))
            if "NOT NULL" in st0:
                nulls.append("true")
            else:
                nulls.append("false")
        it=0
        result = "public class %s {"%(classname)
        for i in var:  
            result = result+"\n" + "public %s %s { get; set; }" %(definitions[it],var[it])
            it=it+1
        result = result + "\n}"
        return result
    except Exception:
        print 'Vyskytla sa chyba'
        return 'Vyskytla sa chyba'
        
def getDefinitions(strin):
    try:   
        cr = strin.find('CREATE') 
        strin = strin[cr:]
        cr = strin.find('(')
        strin = strin[cr+1:]
        str = strin.split(",")
        if (len(str))<2 :
            return 'Zlý vstup'
        it=0
        zac =0 
        konec = 0
        for i in str:
            it=it+1
            if "CREATE" in i:
                zac = it
            if "ON [PRIMARY]" in i:
                    konec = it
        if konec ==0:
            konec = len(str)
        print konec
        str= str[zac:konec-1]
        var=[]
        for i in str:
            st0 = i.split(" ")
            st0[0] = st0[0].replace("[","")
            st0[0] = st0[0].replace("]","")
            var.append(st0[0])
        return var
    except Exception:
        print 'Vyskytla sa chyba'
        return 'Vyskytla sa chyba'

def generateHtmlTable(inpt):
#        print inpt 
        res = " <table id=\"example\" class=\"display\" cellspacing=\"0\" width=\"100%\"> \r\n <thead> \r\n  <tr>"
        for i in inpt:
            res +="\n<th>%s</th>\n"%(i.strip())
        res+="</tr>\r\n</thead>\r\n<tfoot>\r\n<tr>"            
        for i in inpt:
            res +="\n<th>%s</th>\n"%(i.strip())
        res+="</tr>\n</tfoot>\n</table>"
#        print res
        return res
        
def generateJTable(inpt,tempfilename):
        tempfile = open(tempfilename, 'r')
        res = tempfile.readlines()
        tempfile.close()   
        columns=""
        for i in inpt:
            columns += " \n{ \"data\": \"%s\" },"%(i.strip())
        columns=columns[:-1]
        res = ''.join(res).replace("%s",columns)
        return res
        
        
def getDatatype(val):
        if "int" in val:
            return "int"
        if "char" in val:
            return "string"
        if "datetime" in val:
            return "DateTime"
        if "bit" in val:
            return "bool"
        

def mainprocedure(file,classname,tempfile):
        result = createClass(file,classname)
        varnames = getDefinitions(file) 
        htmlTable = generateHtmlTable(varnames)
        filename, file_extension = os.path.splitext(file)
        jTable = generateJTable(varnames,tempfile)
        outfilename ="%s.out"%(filename)
        outfile = open(outfilename, 'w')
        outfile.write(result)
        outfile.write("\n\n\n\n"+htmlTable)
        outfile.write("\n\n\n\n"+jTable)
        outfile.close()