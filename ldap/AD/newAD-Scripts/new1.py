
import ldap
import ldap.modlist as modlist

user_dn = "CN=asdad,CN=Usadadaders,DC=adadad,DC=adadad,DC=adadad"
old_password = "dadad"
new_password = "asasasas"
	
ldap.set_option(ldap.OPT_X_TLS_REQUIRE_CERT, ldap.OPT_X_TLS_NEVER)
l = ldap.initialize('ldap://<IP>:389')
l.set_option(ldap.OPT_REFERRALS,0)
l.set_option(ldap.OPT_PROTOCOL_VERSION,3)
l.set_option(ldap.OPT_X_TLS,ldap.OPT_X_TLS_DEMAND)
l.set_option(ldap.OPT_X_TLS_DEMAND,True)
l.set_option(ldap.OPT_DEBUG_LEVEL,255)
l.simple_bind_s('dadadad', 'adadadad') 

# Reset Password
unicode_pass = unicode('\"' + str(new_password) + '\"', 'iso-8859-1')
password_value = unicode_pass.encode('utf-16-le')
add_pass = [(ldap.MOD_REPLACE, 'userPassword', [password_value])]

a = l.modify_s(user_dn,add_pass)
print a

# Its nice to the server to disconnect and free resources when done
l.unbind_s()
