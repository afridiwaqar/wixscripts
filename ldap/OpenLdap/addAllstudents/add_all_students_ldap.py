import csv
import ldap
import ldap.modlist as modlist

try:
	conn = ldap.initialize('ldap://<IP>:389')
	conn.simple_bind_s('cn=adadad,dc=adadad,dc=adadad,dc=adadad', 'SomePassword')

except ldap.LDAPError, e:
	print e


with open('filename.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    uid = 1000
    for row in readCSV:
		print "Adding " + str( row[0] + " " + row[1] + " " + row[2])
		
		dn = "uid="+str(row[5]) + ",ou="+str(row[4])+",ou="+str(row[3])+",ou=adadadad,dc=adadad,dc=adadad,dc=adadad"

		attrs = {}
		attrs['objectclass'] = ['top','posixAccount','inetOrgPerson']
		attrs['sn'] = str(row[0])
		attrs['displayName'] = str(row[0])
		attrs['givenName'] = str(row[5])
		attrs['uid'] = str(row[5])
		attrs['uidNumber'] = str(uid)
		attrs['gidNumber'] = '0'
		attrs['homeDirectory'] = str(row[5])

		attrs['cn'] = str(row[5])
		attrs['userPassword'] = str(row[6])
		attrs['description'] = str(row[0]) + " son/daughter of " + str(row[1]) + " is student of Instutue of Management Sciences in Program " + str(row[3]) + " Group " + str(row[4])

#		print "CN" + attrs['cn']
#		print attrs['sn']
#		print attrs['givenName']
#		print attrs['userPassword']
#		print attrs['description']

		# Convert our dict to nice syntax for the add-function using modlist-module
		ldif = modlist.addModlist(attrs)
		print "ldif " + str(ldif)

		# Do the actual synchronous add-operation to the ldapserver
		try:
			conn.add_s(dn,ldif)
		
		except ldap.ALREADY_EXISTS:
			print "Value Already Exists"

		uid = uid + 1
		
conn.unbind_s()
print "All Done"

		
