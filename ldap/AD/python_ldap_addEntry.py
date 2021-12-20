import ldap
import ldap.modlist as modlist

# make Connection

try:
#	ldap.set_option(ldap.OPT_X_TLS_REQUIRE_CERT, 0)
	conn = ldap.initialize('ldap://<IP>:389')
	conn.simple_bind_s('cn=someuser,dc=asasas,dc=asasas', '')

except ldap.LDAPError, e:
	print e

# The Distinguished Name of the new entry/object to be made

distinguishedName = "CN=someuser,OU=asas,OU=asas,DC=asasa,DC=asaasa"

# A dict to help build the "body" of the object
attrs = {}
attrs['objectclass'] = ['top','person','organizationalPerson','user']
attrs['cn'] = ''
attrs['sn'] = ''
attrs['givenName'] = ''
attrs['userPassword'] = ''
attrs['description'] = 'Just a Test User, Delete if found'

print "CN" + attrs['cn']
print attrs['sn']
print attrs['givenName']
print attrs['userPassword']
print attrs['description']

# Convert our dict to nice syntax for the add-function using modlist-module
ldif = modlist.addModlist(attrs)

# Do the actual synchronous add-operation to the ldapserver
conn.add_s(distinguishedName,ldif)

# Its nice to the server to disconnect and free resources when done
conn.unbind_s()
