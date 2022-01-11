import os

def main():
 
 print("--------------------------------------------")
 myPath = input("Enter your Path: ")
 list = os.listdir(myPath) 
 number_files = len(list)
 print ("You have <" + str(number_files) + "> files in your active directory.")
 print("--------------------------------------------")
 index = int(input("Enter Index number to add to your filesname: "))
 print("--------------------------------------------")
 answer = input("Enter your postfix to add to your filesname: ")
 
 for count, filename in enumerate(os.listdir(myPath)):
  
  myPath = myPath + "/"
  
  src = myPath + filename
  
  fileExtension = " "
  
  if os.path.isfile(src):
   fileExtension = filename[filename.rfind('.'):]
   filename = filename[:filename.rfind('.')]
  
  dst = str(index) + "_" + filename + answer + fileExtension
  dst = myPath + dst
  
  os.rename(src, dst)
  index = index + 1
  mySter = str(index) + " and " + answer + " added to file number "+ str(count+1) 
  print(mySter)
 print("********************************")  
 print("All Done!!") 
# Driver Code
#if __name__ == '__main__':
#main()
    

