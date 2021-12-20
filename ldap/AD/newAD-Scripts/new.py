
import ldap
import ldap.modlist as modlist

server = '<IP>'
admin_username = 'adadadd'

#        connection = ldap.initialize('ldap://{0}'.format(server))

connection = ldap.initialize('<IP>:389')
connection.protocol_version = 3
connection.set_option(ldap.OPT_REFERRALS, 0)
connection.simple_bind_s('adadad', 'adadadada')  

search_username = 'adadad'
base_dn = 'DC=adad,DC=adadad,DC=adadad'
ldap_filter = '(sAMAccountName={0})'.format(search_username)

#        attribs = ['sAMAccountName']

attribs = ['*']
results = connection.search_s(base_dn, ldap.SCOPE_SUBTREE, ldap_filter, attribs)
filter_dect =  results[0][1]
print "Attributes", filter_dect

user =  str(filter_dect['sAMAccountName']).strip('[]').replace("'","")
print "User----------->", user

givenName =  str(filter_dect['givenName']).strip('[]').replace("'","")
print "User----------->", givenName       

#self.assertIsNotNone(results)
#self.assertGreaterEqual(len(results), 2)
match = results[0]
print "User DN Address", match[0]

distinguishedName = match[0]
givenname = match[0][0]
print "CCCCCCCCCCCCCCCCCc", givenname

# A dict to help build the "body" of the object

'''
old = {
		'unicodePwd': "adadadadad"
		}

new = {
		'unicodePwd': "adadadad"
		}

'''
new_pwd = "adadadadad"

unicode_pass = unicode('\"' + str(new_pwd) + '\"', 'iso-8859-1')
password_value = unicode_pass.encode('utf-16-le')
add_pass = [(ldap.MOD_REPLACE, 'userPassword', [password_value])]

# Convert place-holders for modify-operation using modlist-module
#ldif = modlist.modifyModlist(old,new)
#mod_list = [(ldap.MOD_REPLACE, "unicodePwd", newpwd_utf16)]

print "--------------------------------------------------------------"
# Do the actual modification 
#connection.modify_s(distinguishedName,ldif)
a = connection.modify_s(distinguishedName,add_pass)
print a

print "--------------------------------------------------------------"
connection.unbind()
