import ldap
import ldap.modlist as modlist

# make Connection

try:
	conn = ldap.initialize('ldap://<IP>:389')
	conn.simple_bind_s('adadad', 'adadad')

except ldap.LDAPError, e:
	print e

# The dn of the user you want to modify

distinguishedName = "cn=adadad,OU=adadad,OU=adadad,DC=adadad,DC=adadad"

# A dict to help build the "body" of the object

old = {
	'sn':'adad',
	'givenName':'adada',
	'description':'Just a Test User, Delete if found',
	}

new = {
	'sn':'adadad',
	'givenName':'adada',
	'description':'This would be the new discription',
	'userPassword': "adadad"
	}

# Convert place-holders for modify-operation using modlist-module
ldif = modlist.modifyModlist(old,new)

# Do the actual modification 
conn.modify_s(distinguishedName,ldif)

# Its nice to the server to disconnect and free resources when done
conn.unbind_s()
