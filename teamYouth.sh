#!/bin/bash 
Installingpackages () {
yum install epel-release -y
yum install wget -y
yum install git -y
yum install httpd -y 
yum install zip -y
yum install unzip -y 
yum install vim -y
yum install tree -y
}

downloadApache () {
#wget https://www.free-css.com/assets/files/free-css-templates/download/page256/it-next.zip
#unzip it-next.zip
#mv it-next/* /var/www/html/
echo "Team Youth" > /var/www/html/index.html
}

stert () {
  read -p "What would you like to start? :" system
  sudo systemctl start $system
  sudo systemctl enable $system
  sudo systemctl restart $system
}

titlechanger () {
    cat /var/www/html/index.html | sed 's/Youth/Youth Engineers/'
#    sed 's/$1/ $2/' $3 

    sudo systemctl restart httpd
}

Installingpackages
downloadApache 
stert
titlechanger
