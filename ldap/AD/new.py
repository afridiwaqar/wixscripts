import sys
import ldap

ldap.set_option(ldap.OPT_X_TLS_REQUIRE_CERT, 0)
Server = 'ldap://<IP>:389'

username=''
password = ''

#Change this to the DN of the Users, this will be unique for each group of students
DN = "cn="+username+",OU=123,DC=456,DC=789,DC=jjj"

Base = "dc=456,dc=789,dc=jjj"
Scope = ldap.SCOPE_SUBTREE
Filter = "(&(objectClass=user)(sAMAccountName="+username+"))"
Attrs = ["displayName"]

l = ldap.initialize(Server)
l.protocol_version = 3

#If this returns true, the user cridentials are correct
result = l.simple_bind_s(DN, password)

print result

r = l.search(Base, Scope, Filter, Attrs)
Type,user = l.result(r,60)
Name,Attrs = user[0]
if hasattr(Attrs, 'has_key') and Attrs.has_key('displayName'):
  displayName = Attrs['displayName'][0]
  print displayName

sys.exit()
