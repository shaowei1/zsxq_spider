# ubuntu install chromedriver
sudo 
sudo

wget -N http://chromedriver.storage.googleapis.com/2.26/chromedriver_linux64.zip

unzip chromedriver_linux64.zip
sudo mv -f chromedriver /usr/local/share/chromedriver
sudo ln -s /usr/local/share/chromedriver /usr/local/bin/chromedriver
sudo ln -s /usr/local/share/chromedriver /usr/bin/chromedriver
