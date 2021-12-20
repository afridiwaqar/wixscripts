import ldap

# make Connection

try:
	conn = ldap.initialize('ldap://<IP>:389')
	conn.simple_bind_s('asdadad', 'asdadada')

except ldap.LDAPError, e:
	print e

#performing a simple search just to make sure things are doing ok

delete_DN = "cn=asdadad,OU=asdad,OU=adad,DC=adada,DC=adadad"
try:
	# you can safely ignore the results returned as an exception 
	# will be raised if the delete doesn't work.
	conn.delete_s(delete_DN)
	print 'User Deleted'
except ldap.LDAPError, e:
	print e
	## handle error however you like


