Welcome to Razz Tunes! 
Vision Statement:
We want our users to listen to THEIR music anywhere they have Internet access.

*Have your very own uploadable Playlist.
*Play the song you want by clicking our using the "Next" Button.
*Enjoy! 

Instructions for running RazzTunes:
Gather required packages
1. sudo apt-get install python-mysqldb

Clone the repository using:
2. git clone https://github.com/stge0958/RT.git
3. change directory to the cloned repository called 'RT'

Import the database included in the repository
4. mysql create database RT;
5. mysql -u root -p 3308 RT < RT.sql;

Launch python server
6. python -m CGIHTTPServer
7. Open web browser and visit: 127.0.0.1:8000/cgi-bin/maintest.py



Auto-Doc Source files can be found: RT/Project Information/RazzTunes_Part_7/Source/ 
Location of Doxygen Auto-doc: RT/Project Information/RazzTunes_Part_7/latex/refman.pdf
