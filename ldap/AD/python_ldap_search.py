import ldap

# make Connection

try:
#	ldap.set_option(ldap.OPT_X_TLS_REQUIRE_CERT, 0)
	conn = ldap.initialize('ldap://<IP>:389')
	conn.simple_bind_s('cn=adadad,dc=adadad,dc=adadad', 'adadadad')

except ldap.LDAPError, e:
	print e

#performing a simple search just to make sure things are doing ok

search_result = conn.search('dc=adadad,dc=adadad',ldap.SCOPE_SUBTREE,'(cn=adadadad)')
print search_result
