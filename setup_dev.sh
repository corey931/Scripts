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
sudo apt-get install python3.7 --yes
sudo update-alternatives --config python3
sudo apt install python-pip --yes

# azure client: https://docs.microsoft.com/en-us/cli/azure/install-azure-cli-apt?view=azure-cli-latest
curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash
sudo apt-get update
sudo apt-get install ca-certificates curl apt-transport-https lsb-release gnupg
curl -sL https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor | sudo tee /etc/apt/trusted.gpg.d/microsoft.gpg > /dev/null
AZ_REPO=$(lsb_release -cs)
echo "deb [arch=amd64] https://packages.microsoft.com/repos/azure-cli/ $AZ_REPO main" | sudo tee /etc/apt/sources.list.d/azure-cli.list
sudo apt-get update
sudo apt-get install azure-cli
az login