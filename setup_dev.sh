# sudo apt-get update & upgrade --yes 
# sudo apt-get install git-core
# mkdir /home/$usr/github
# cd /home/$usr/github 
# git clone https://github.com/corey931/scripts
# cd scripts
# chmod +x config_git.sh
# sudo ./config_git.sh

usr="AzureUser"
git --version
git config --global user.name "Sese"
git config --global user.email "sese_simon@gmx.net"

# xrdp
sudo apt-get -y install xfce4
sudo apt-get -y install xrdp

vm="AzureVM"
sudo systemctl enable xrdp
echo xfce4-session >~/.xsession
sudo service xrdp restart

sudo passwd 
az vm open-port --resource-group myResourceGroup --name $vm --port 3389

# upgrade python
sudo apt-get install python3.7
sudo update-alternatives --config python3
sudo apt install python-pip --yes