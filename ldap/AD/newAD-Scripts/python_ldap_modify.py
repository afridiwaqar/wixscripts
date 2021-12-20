import ldap
import ldap.modlist as modlist

# make Connection

try:
	conn = ldap.initialize('ldap://<IP>:389')
	conn.simple_bind_s('adadadad', 'adadadadad')

except ldap.LDAPError, e:
	print e

# The dn of the user you want to modify

distinguishedName = "cn=adadad,OU=adadadad,DC=adadad,DC=adadad,DC=adadad"
CN=adadad,CN=adadad,DC=adadad,DC=adadad,DC=adad

# A dict to help build the "body" of the object

old = {
	'sn':'dadad',
	'givenName':'adadad',
	'description':'Just a Test User, Delete if found',
	}

new = {
	'sn':'adada',
	'givenName':'adadad',
	'description':'This would be the new discription',
	'userPassword': "adadadad"
	}

# Convert place-holders for modify-operation using modlist-module
ldif = modlist.modifyModlist(old,new)

# Do the actual modification 
conn.modify_s(distinguishedName,ldif)

# Its nice to the server to disconnect and free resources when done
conn.unbind_s()
