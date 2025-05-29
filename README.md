I needed to run the following to set up timezone info:

mysql_tzinfo_to_sql /usr/share/zoneinfo | mysql -D mysql -u root -p
mysql -u root -p -e "flush tables;" mysql