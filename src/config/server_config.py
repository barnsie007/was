# wsadmin script generated by binaryAppScanner
# This configuration was migrated on 3/17/21 at 11:31:29 PM from the following location: /opt/IBM/WebSphere/AppServer/profiles/AppSrv03
# The binary scanner does not support the migration of all WebSphere traditional configuration elements. Check the binary scanner documentation for the list of supported configuration elements.

Cell=AdminConfig.getid('/Cell:' + AdminControl.getCell() + '/')
Node=AdminConfig.getid('/Cell:' + AdminControl.getCell() + '/Node:' + AdminControl.getNode() + '/')
Server=AdminConfig.getid('/Cell:' + AdminControl.getCell() + '/Node:' + AdminControl.getNode() + '/Server:server1')
NodeName=AdminControl.getNode()

# The following variables are used to replace sensitive data in the configuration for the application.
# The values for these variables were not collected because the includeSensitiveData option was not specified.
# ============================================================
ldapRegistry_bindDN_1=''
ldapRegistry_bindPassword_1=''
userRegistry_primaryAdminId_1=''
userRegistry_serverPassword_2=''
whydah1Node04_db2_password_1=''
whydah1Node04_db2_user_1=''
# ============================================================

print 'Starting Creating JVM Properties'
# Properties are migrated from server whydah1Node04/server1.

print 'Starting Creating LDAP Security'
AdminTask.createIdMgrLDAPRepository(['-id', 'LDAP1', '-ldapServerType', 'IDS', '-loginProperties', 'uid', '-primaryServerQueryTimeInterval', '15', '-returnToPrimaryServer', 'true'])
AdminTask.addIdMgrLDAPServer(['-id', 'LDAP1', '-host', 'bluepages.ibm.com', '-port', '389', '-bindDN', ldapRegistry_bindDN_1, '-bindPassword', ldapRegistry_bindPassword_1])
AdminTask.addIdMgrRepositoryBaseEntry(['-id', 'LDAP1', '-name', 'o=ibm.com', '-nameInRepository', 'o=ibm.com'])
AdminTask.deleteIdMgrLDAPEntityType(['-id', 'LDAP1', '-name', 'Group'])
AdminTask.addIdMgrLDAPEntityType(['-id', 'LDAP1', '-name', 'Group', '-objectClasses', 'groupOfNames', '-searchBases', 'ou=memberList,ou=ibmgroups,o=ibm.com'])
AdminTask.deleteIdMgrLDAPEntityType(['-id', 'LDAP1', '-name', 'OrgContainer'])
AdminTask.addIdMgrLDAPEntityType(['-id', 'LDAP1', '-name', 'OrgContainer', '-objectClasses', 'organization;organizationalUnit;domain;container', '-searchBases', 'ou=memberList,ou=ibmgroups,o=ibm.com'])
AdminTask.addIdMgrLDAPEntityTypeRDNAttr(['-id', 'LDAP1', '-entityTypeName', 'OrgContainer', '-name', 'o', '-objectClass', 'organization'])
AdminTask.addIdMgrLDAPEntityTypeRDNAttr(['-id', 'LDAP1', '-entityTypeName', 'OrgContainer', '-name', 'ou', '-objectClass', 'organizationalUnit'])
AdminTask.addIdMgrLDAPEntityTypeRDNAttr(['-id', 'LDAP1', '-entityTypeName', 'OrgContainer', '-name', 'dc', '-objectClass', 'domain'])
AdminTask.addIdMgrLDAPEntityTypeRDNAttr(['-id', 'LDAP1', '-entityTypeName', 'OrgContainer', '-name', 'cn', '-objectClass', 'container'])
AdminTask.deleteIdMgrLDAPEntityType(['-id', 'LDAP1', '-name', 'PersonAccount'])
AdminTask.addIdMgrLDAPEntityType(['-id', 'LDAP1', '-name', 'PersonAccount', '-objectClasses', 'ibmPerson', '-searchBases', 'ou=bluepages,o=ibm.com'])

AdminTask.addIdMgrRealmBaseEntry(['-name', 'defaultWIMFileBasedRealm', '-baseEntry', 'o=ibm.com'])
AdminTask.configureAdminWIMUserRegistry(['-verifyRegistry', 'false', '-autoGenerateServerId', 'true', '-serverId', 'wsadmin', '-serverIdPassword', userRegistry_serverPassword_2, '-primaryAdminId', userRegistry_primaryAdminId_1])
AdminTask.setAdminActiveSecuritySettings(['-enableGlobalSecurity', 'true', '-appSecurityEnabled', 'true', '-activeUserRegistry', 'WIMUserRegistry'])

print 'Starting Creating Authentication Alias'
GlobalSecurityVar=AdminConfig.getid('/Cell:' + AdminControl.getCell() + '/' + 'Security:/')
AdminConfig.create('JAASAuthData', GlobalSecurityVar, [['userId', whydah1Node04_db2_user_1], ['description', ''], ['password', whydah1Node04_db2_password_1], ['alias', 'whydah1Node04/db2']])

print 'Starting Creating Queues'

print 'Starting Creating Topics'

print 'Starting Creating Activation Specifications'

print 'Starting Creating Connection Factories'

print 'Starting Creating JDBC Providers'
AdminConfigVar_0=AdminConfig.create('JDBCProvider', Node, [['name', 'DB2_Universal_JDBC_Driver_Provider'], ['implementationClassName', 'com.ibm.db2.jcc.DB2ConnectionPoolDataSource'], ['providerType', 'DB2 Universal JDBC Driver Provider'], ['description', 'One-phase commit DB2 JCC provider that supports JDBC 3.0. Data sources that use this provider support only 1-phase commit processing, unless you use driver type 2 with the application server for z/OS. If you use the application server for z/OS, driver type 2 uses RRS and supports 2-phase commit processing.'], ['classpath', '/work/config/lib/db2jcc.jar'], ['xa', 'false']])
AdminConfigVar_1=AdminTask.createDatasource(AdminConfigVar_0, ["-name", "DB2 Universal JDBC Driver DataSource", "-jndiName", "jndi/db2", "-dataStoreHelperClassName", "com.ibm.websphere.rsadapter.DB2UniversalDataStoreHelper", "-componentManagedAuthenticationAlias", "whydah1Node04/db2", "-configureResourceProperties", "[[databaseName java.lang.String testdb] [driverType java.lang.Integer 4] [serverName java.lang.String 9.46.76.40] [portNumber java.lang.Integer 50000] ]"])
AdminConfigVar_2=AdminConfig.showAttribute(AdminConfigVar_1, 'propertySet')
AdminConfig.create('J2EEResourceProperty', AdminConfigVar_2, [['name', 'beginTranForResultSetScrollingAPIs'], ['type', 'java.lang.Boolean'], ['value', 'false']])
AdminConfig.create('J2EEResourceProperty', AdminConfigVar_2, [['name', 'beginTranForVendorAPIs'], ['type', 'java.lang.Boolean'], ['value', 'false']])
AdminConfig.create('J2EEResourceProperty', AdminConfigVar_2, [['name', 'connectionSharing'], ['type', 'java.lang.Integer'], ['value', '1']])
AdminConfig.create('J2EEResourceProperty', AdminConfigVar_2, [['name', 'deferPrepares'], ['type', 'java.lang.Boolean'], ['value', 'true']])
AdminConfig.create('J2EEResourceProperty', AdminConfigVar_2, [['name', 'enableClientInformation'], ['type', 'java.lang.Boolean'], ['value', 'false']])
AdminConfig.create('J2EEResourceProperty', AdminConfigVar_2, [['name', 'enableMultithreadedAccessDetection'], ['type', 'java.lang.Boolean'], ['value', 'false']])
AdminConfig.create('J2EEResourceProperty', AdminConfigVar_2, [['name', 'errorDetectionModel'], ['type', 'java.lang.String'], ['value', 'ExceptionMapping']])
AdminConfig.create('J2EEResourceProperty', AdminConfigVar_2, [['name', 'fullyMaterializeLobData'], ['type', 'java.lang.Boolean'], ['value', 'true']])
AdminConfig.create('J2EEResourceProperty', AdminConfigVar_2, [['name', 'jmsOnePhaseOptimization'], ['type', 'java.lang.Boolean'], ['value', 'false']])
AdminConfig.create('J2EEResourceProperty', AdminConfigVar_2, [['name', 'loginTimeout'], ['type', 'java.lang.Integer'], ['value', '0']])
AdminConfig.create('J2EEResourceProperty', AdminConfigVar_2, [['name', 'name'], ['type', 'java.lang.String'], ['value', 'DB2 Universal JDBC Driver DataSource']])
AdminConfig.create('J2EEResourceProperty', AdminConfigVar_2, [['name', 'nonTransactionalDataSource'], ['type', 'java.lang.Boolean'], ['value', 'false']])
AdminConfig.create('J2EEResourceProperty', AdminConfigVar_2, [['name', 'preTestSQLString'], ['type', 'java.lang.String'], ['value', 'SELECT CURRENT SQLID FROM SYSIBM.SYSDUMMY1']])
AdminConfig.create('J2EEResourceProperty', AdminConfigVar_2, [['name', 'propagateClientIdentityUsingTrustedContext'], ['type', 'java.lang.Boolean'], ['value', 'false']])
AdminConfig.create('J2EEResourceProperty', AdminConfigVar_2, [['name', 'readOnly'], ['type', 'java.lang.Boolean'], ['value', 'false']])
AdminConfig.create('J2EEResourceProperty', AdminConfigVar_2, [['name', 'reauthentication'], ['type', 'java.lang.Boolean'], ['value', 'false']])
AdminConfig.create('J2EEResourceProperty', AdminConfigVar_2, [['name', 'resultSetHoldability'], ['type', 'java.lang.Integer'], ['value', '2']])
AdminConfig.create('J2EEResourceProperty', AdminConfigVar_2, [['name', 'retrieveMessagesFromServerOnGetMessage'], ['type', 'java.lang.Boolean'], ['value', 'true']])
AdminConfig.create('J2EEResourceProperty', AdminConfigVar_2, [['name', 'traceFileAppend'], ['type', 'java.lang.Boolean'], ['value', 'false']])
AdminConfig.create('J2EEResourceProperty', AdminConfigVar_2, [['name', 'traceLevel'], ['type', 'java.lang.Integer'], ['value', '-1']])
AdminConfig.create('J2EEResourceProperty', AdminConfigVar_2, [['name', 'unbindClientRerouteListFromJndi'], ['type', 'java.lang.Boolean'], ['value', 'false']])
AdminConfig.create('J2EEResourceProperty', AdminConfigVar_2, [['name', 'useTransactionRedirect'], ['type', 'java.lang.Boolean'], ['value', 'false']])
AdminConfig.create('J2EEResourceProperty', AdminConfigVar_2, [['name', 'validateNewConnection'], ['type', 'java.lang.Boolean'], ['value', 'false']])
AdminConfig.create('J2EEResourceProperty', AdminConfigVar_2, [['name', 'validateNewConnectionRetryCount'], ['type', 'java.lang.Integer'], ['value', '100']])
AdminConfig.create('J2EEResourceProperty', AdminConfigVar_2, [['name', 'validateNewConnectionRetryInterval'], ['type', 'java.lang.Long'], ['value', '3']])
AdminConfigVar_3=AdminConfig.showAttribute(AdminConfigVar_1, 'connectionPool')
AdminConfig.modify(AdminConfigVar_3, [['stuckThreshold', '0'], ['reapTime', '180'], ['testConnectionInterval', '0'], ['connectionTimeout', '180'], ['surgeCreationInterval', '0'], ['surgeThreshold', '-1'], ['stuckTimerTime', '0'], ['numberOfFreePoolPartitions', '0'], ['minConnections', '0'], ['unusedTimeout', '1800'], ['agedTimeout', '0'], ['numberOfSharedPoolPartitions', '0'], ['purgePolicy', 'EntirePool'], ['maxConnections', '10'], ['freePoolDistributionTableSize', '0'], ['stuckTime', '0'], ['testConnection', 'false'], ['numberOfUnsharedPoolPartitions', '0']])

print 'Starting Creating Variables'

print 'Starting Saving Configuration Changes Before Application Deployment'
AdminConfig.save()
print 'Starting Application Deployment'
AdminConfig.create('Library', Server, [['name', 'globalSharedLibrary'], ['classPath',  '/work/config/lib']])
appServer = AdminConfig.list('ApplicationServer',Server)
classLoader1 = AdminConfig.create('Classloader', appServer, [['mode',  'PARENT_FIRST']])
AdminConfig.create('LibraryRef', classLoader1, [['libraryName', 'globalSharedLibrary']])
#AdminApp.install('/path/to/DB2App-1.war', ["-node", NodeName, "-server", "server1", "-appname", "DB2App-1.war", "-contextroot", "/db2", "-CtxRootForWebMod", [["Simple Servlet Application", "DB2App-1.war,WEB-INF/web.xml", "/db2"]]])
AdminConfig.save()
