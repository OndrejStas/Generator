# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 15:31:59 2016

@author: os
"""
import testrun

def  GenInsert(inp, classname):
        str = inp.split('}')
        var=[]
        definitions=[]
        params=[]
        commands=[]
        insertstring = ''        
        finalstring0= """
        using (SqlCommand command = connection.CreateCommand()) 
    { 
        command.CommandText ="""
        for i in str:
            t=i.strip()
            tt = t.split(" ")
            if len(tt)>=3:
                definitions.append(tt[1].strip())
                var.append(tt[2].strip())
#            print tt[0]
#        i=0
#        for y in definitions:
#            print (definitions[i] +'-'+ var[i])
#            i+=1
        varstring = ','.join(var)
        for e in var:
            params.append( '@'+e)
        paramstring = ','.join(params)
        i=0
        for ee in var:
            if definitions[i]=='string':
                commands.append(' command.Parameters.AddWithValue("@{}",string.IsNullOrEmpty({}) ? Convert.DBNull : {});'.format(ee, classname.strip()+'.'+ee, classname.strip()+'.'+ee)+'\n')
            elif definitions[i].lower()=='DateTime'.lower(): 
                commands.append('command.Parameters.Add("@{}", SqlDbType.DateTime).Value = {} == DateTime.MinValue ? Convert.DBNull :{}; \n'.format(ee,classname.strip()+'.'+ee,classname.strip()+'.'+ee))
            else:
                commands.append(' command.Parameters.AddWithValue("@{}", {});'.format(ee, classname.strip()+'.'+ee)+'\n')
            i+=1
        insertstring = ' INSERT INTO {}({}) VALUES({}) '.format(classname,varstring, paramstring)
        finalstring0 +='"'+insertstring+'";\n'+' '.join(commands) + '\n' + """
                        command.CommandTimeout = 100;
                        object reso = command.ExecuteScalar();
                        command.Dispose();
                        connection.Close();        
                        \n\n }
        """
        print finalstring0
#        print len(str)
        
        
  


classname = 'extzad'
GenInsert(testrun.inp, classname)   