Class dc.DataViz.Util Extends %RegisteredObject
{

ClassMethod getNameSpaces() As %String
{
 set statement=##class(%SQL.Statement).%New()
 set status=statement.%PrepareClassQuery("%SYS.Namespace","List")
 if $$$ISERR(status) { do $system.OBJ.DisplayError(status) }
 set resultset=statement.%Execute()
 set results = "1"
 while resultset.%Next() {
	//zw resultset    
    if results = "1" {
	    set results = resultset.%Get("Nsp")
	    }
    else
    {
    	set results = results _ "," _ resultset.%Get("Nsp")
    }
 }
 return results
}

}
