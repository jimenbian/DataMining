import java.awt.List;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Iterator;




public class Main {
  public static void main (String[] args) throws IOException{
	  BufferedWriter writer = new BufferedWriter(new FileWriter(new File("/Users/hakuri/Desktop/data2.txt")));
      BufferedReader reader=new BufferedReader(new FileReader(new File("/Users/hakuri/Desktop/final.txt")));
      String lineTxt = null;
      int i=1;
    //  ArrayList<String> brand = new ArrayList<String>();
      HashMap<String,ArrayList> custom=new HashMap<String,ArrayList>();
      

      while((lineTxt = reader.readLine()) != null){
    	  //System.out.println(lineTxt);
    	     String line=lineTxt.trim();
    	     String[] part=line.split(",");
    	     if(!custom.containsKey(part[0])){
    	    	 custom.put(part[0],new ArrayList());
    	      custom.get(part[0]).add(part[1]);
    	     }
    	     else{
    	    	 custom.get(part[0]).add(part[1]);
    	     }
    	    //	 custom.put(part[0], part[1]); 
      }
   //System.out.print(custom);
   Iterator<String> it=custom.keySet().iterator();
   while( it.hasNext()){
	   String key=(String)it.next();
	   ArrayList value=custom.get(key);
	   System.out.println(key+"--"+value);
   }
   //System.out.println(custom.keySet().iterator());
  }
 
  }

