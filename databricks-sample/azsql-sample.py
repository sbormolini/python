# requires spark-mssql-connector_2.12-1.2.0.jar

import adal

# authentication info
resource_app_id_url = "https://database.windows.net/"
service_principal_id = "<client-id>"
service_principal_secret = dbutils.secrets.get(scope="<databricks-secret-scope>",key="<client-secret>")
tenant_id = "<tenant-id>"
authority = "https://login.windows.net/" + tenant_id

# sql server info
azure_sql_url = "jdbc:sqlserver://<azure-sql-server-name>.database.windows.net"
database_name = "<database-name>"
db_table = "<table-name>" 
db_table_sink = "<table-name>"
encrypt = "true"
host_name_in_certificate = "*.database.windows.net"

# get token
context = adal.AuthenticationContext(authority)
token = context.acquire_token_with_client_credentials(resource_app_id_url, service_principal_id, service_principal_secret)
access_token = token["accessToken"]

# read data
addressDf = spark.read \
             .format("com.microsoft.sqlserver.jdbc.spark") \
             .option("url", azure_sql_url) \
             .option("dbtable", db_table) \
             .option("databaseName", database_name) \
             .option("accessToken", access_token) \
             .option("encrypt", "true") \
             .option("hostNameInCertificate", "*.database.windows.net") \
             .load()

# show data
display(addressDf)

# transform (just stupid showcase)
forcastDf = addressDf["AddressID", "PostalCode"]
forcastDf = forcastDf.withColumnRenamed('AddressID', 'SalesOrderID')
forcastDf = forcastDf.withColumnRenamed('PostalCode', 'Forcast')
display(forcastDf)

# write forcast
try:
    forcastDf.write \
        .format("com.microsoft.sqlserver.jdbc.spark") \
        .mode("append") \
        .option("url", azure_sql_url) \
        .option("databaseName", database_name) \
        .option("dbtable", db_table_sink) \
        .option("accessToken", access_token) \
        .option("encrypt", "true") \
        .option("hostNameInCertificate", "*.database.windows.net") \
        .save()
except ValueError as error :
    print("Connector write failed", error)
