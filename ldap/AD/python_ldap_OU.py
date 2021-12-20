import ldap
import ldap.modlist as modlist

# make Connection

try:
	conn = ldap.initialize('ldap://<IP>:389')
	conn.simple_bind_s('adadadad', 'adadadad')

except ldap.LDAPError, e:
	print e

# The Distinguished Name of the new entry/object to be made

distinguishedName = "cn=adadad,dc=adadad,dc=adadad"

# A dict to help build the "body" of the object
attrs = {}
attrs['objectclass'] = ['top','person','organizationalPerson','user']
attrs['cn'] = 'adadad'
attrs['sn'] = 'adadad'
attrs['givenName'] = 'adadad'
attrs['userPassword'] = 'adadadad'
attrs['description'] = 'Just a Test User, Delete if found'


# Convert our dict to nice syntax for the add-function using modlist-module
ldif = modlist.addModlist(attrs)

# Do the actual synchronous add-operation to the ldapserver
conn.add_s(distinguishedName,ldif)

# Its nice to the server to disconnect and free resources when done
conn.unbind_s()
