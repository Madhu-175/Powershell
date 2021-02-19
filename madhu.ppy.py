#practicing conditional statement
#Linux Practice
#Author-Madhu
#Modification History- None

read -p "enter first no " first

#if statement
if [ $((first%2)) -eq 0 ]
then
echo "number is even"
fi
echo "-------"

#if else statement
if [ $((first%2)) -eq 0 ]
then
echo "number is even"
else
echo "the no is odd"
fi
echo "-------"

#if elif
if [ $((first%2)) -eq 0 ]
then
echo "number is EVEN"
elif [ $((first%2)) -eq 1 ]
then
echo "number is ODD"
else
echo "input ivalid"
fi

"----------------------------------------------------------------------------------"
#practice for loop


for i in 1 2 3 4 5 6 7 
do 
   echo $i             #print all values of i
      if [ $((i%2)) -eq 0 ]
       then
           echo "$i is an even number"
       fi

       if [ $((i%2)) -ne 0 ]
       then
          echo "$i is an odd no"
       fi
done

for ((i=1;i<8;i++))    #loop till value of i less than 8
do
   echo $i
done

"---------------------------------------------------------------------------------------"
#operator practice with string


read -p "enter first word " firstw
read -p "enter second word "  secondw

if [ $firstw ==  $secondw ]
then
echo "both words are equal"
fi

if [ $firstw !=  $secondw ]   #check if string values are not equal
then
echo "both words are not  equal"
fi

read -p "enter third  word " thirdw

if [ -z $thirdw ]    #check if string is null
then
echo "third  word is  null"
else
echo "third  word  is not null"
fi

if [ -n $thirdw ]   #check if string is not null
then
echo "third  word is not null/size of string is not-zero"
else
echo "third  word  is null/size of string is zero"
fi


file="operator_script.sh"

if [ -f $file ]    #check for the file if it exist in current directory
then
echo "file exist"
else
echo "file not exist"
fi

"----------------------------------------------------------------------------------------"
#how to work with operators 


read -p "enter first number" number1
read -p "enter second number" number2
echo "sum of" $number1 "and" $number2 "is" `expr $number1 + $number2`

echo "sum of" $number1 "and" $number2 "is" $((number1+number2))
echo "subtraction of" $number1 "and" $number2 "is" $((number1-number2))
echo "multiplication of" $number1 "and" $number2 "is" $((number1*number2))
echo "division of" $number1 "and" $number2 "is" $((number1/number2))
echo "modulus of" $number1 "and" $number2 "is" $((number1%number2))

if [ $number1 -eq $number2 ]  # check if 1st  number is equal to 2nd number
then
echo "both the numbers are equal"
fi

if [ $number1 -ne $number2 ]   #checks if 1no is not equal to  2no
then
echo "both the numbers are not equal"
fi

if [ $number1 -gt $number2 ]  #check 1no > 2no 
then
echo "1 no is > 2nd no"
fi

if [ $number1 -ge $number2 ]  #check if 1no >= 2no 
then
echo "1 no is >= 2nd no"
fi

if [ $number1 -lt $number2 ]  #check if 1no<2no 
then
echo "1 no is < 2nd no"
fi

if [ $number1 -le $number2 ]  #check if 1no <= 2no 
then
echo "1 no is <= 2nd no"
fi

"--------------------------------------------------------------------------------------"
#practice switch case



read -p "enter your name " name

case $name in

"honey") echo "Everything is fine"   #if user input honey this value is printed
;;
"suman") echo "everything is good"
;;
"anita") echo "everything is super"
;;

*) echo "invalid input please  give input honey or suman or anita"

esac
echo "---"

read -p "enter the character " exp

case $exp in
  [A-Z])  echo "is an uppercase letter"
  ;;
  [a-z])  echo "is an lowecase letter"
  ;;
  [0-9]) echo "is a number"
  ;;

  *)  
       echo   "invalid expression"

esac

"---------------------------------------------------------------------------------------------"
#variables practice and take input from user


echo "hello my name is Aany"

number_1=10
number_2=30

echo "first no is" $number_1 "and second no is" $number_2 

echo "enter your fav number"
read number3
echo "your fav no  is" $number3

read -p "enter your fav colour " favcolour
echo "your fav colour is " $favcolour

read -p "enter your first name " fname
read -p "enter your last name  " lname
echo "your full name is" $fname $lname

"---------------------------------------------------------------------------------------------------"
#practice while loop 


count=1
while [ $count -lt 5 ]   #loop till value of count is less than 5 
do
  echo " $count "
  count=`expr $count + 1`
done

echo "----"

count1=0
while [ $count1 -lt 5 ]
do
  echo " $count1 "
   if [ $count1 -eq 2 ]
   then
        break        #end the while loop when value of count is 2
   fi
   count1=`expr $count1 + 1`
done
echo "-----"
