# #!/bin/bash

# echo "Starting program at $(cat names.txt)" 

# echo "Running program $0 with $# arguments with pid $$"

# if  [ "$#" -eq 0 ]; then
#   echo "Please input at least 1 argument"
# else
#   for file in "$@"; do 
#     mkdir $file && touch $file/intro.txt
#     echo "This is $file, he is okay" > $file/intro.txt
#   done
# fi

 
#  write script that promts you for name; if the name in 
#  inside a list of names you have then print out the name was 
#  enrolled otherwise not enorolled


read -p "Enter a name: " name

for student in $(cat names.txt); do
  if [ $student == $name ]; then
    echo "$name was enrolled"
    exit
  fi 
done

echo "$name is not enrolled"