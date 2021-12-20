import csv
import ldap
import ldap.modlist as modlist

try:
	conn = ldap.initialize('ldap://<IP>:389')
	conn.simple_bind_s('cn=adadad,dc=adadad,dc=adadad', 'adadadad')

except ldap.LDAPError, e:
	print e


with open('filename.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    uid = 1000
    for row in readCSV:
		print "Adding " + str( row[0] + " " + row[1] + " " + row[2])
		
		dn = "uid="+str(row[1]) + ",ou=adadad,dc=adadad,dc=adadad"

		attrs = {}
		attrs['objectclass'] = ['top','posixAccount','inetOrgPerson']
		attrs['sn'] = str(row[0])
		attrs['displayName'] = str(row[0])
		attrs['givenName'] = str(row[1])
		attrs['uid'] = str(row[1])
		attrs['uidNumber'] = str(uid)
		attrs['gidNumber'] = '0'
		attrs['homeDirectory'] = str(row[1])

		attrs['cn'] = str(row[1])
		attrs['userPassword'] = str(row[2])
		attrs['description'] = str(row[1]) + " Staff Member of Instutue of Management Sciences"

#		print "CN" + attrs['cn']
#		print attrs['sn']
#		print attrs['givenName']
#		print attrs['userPassword']
#		print attrs['description']

		# Convert our dict to nice syntax for the add-function using modlist-module
		ldif = modlist.addModlist(attrs)
		print "ldif " + str(ldif)

		# Do the actual synchronous add-operation to the ldapserver
		conn.add_s(dn,ldif)

		uid = uid + 1
		
conn.unbind_s()
print "All Done"

