*** Settings ***
Library  SeleniumLibrary
Library  DatabaseLibrary
Resource  common.robot

*** Variables ***
${dbname}   opencart
${dbuser}   ocuser
${dbpasswd}     PASSWORD
${dbhost}   localhost
${dbport}   3306
#${rowCount}    100
@{queryResults}

*** Keywords ***

Add Product
    Click Link      //*[@id="menu-catalog"]/a
    Click Link      //*[@id="collapse1"]/li[2]/a
    Click Link      //*[@id="content"]/div[1]/div/div/a
    Input Text      id:input-name1  test_product
    Input Text      id:input-meta-title1   test_product
    Click Link      //*[@id="form-product"]/ul/li[2]/a
    Input Text      id:input-model      test_product
    Click Button    css:button[data-original-title='Save']

Delete Product
    Click Link      //*[@id="menu-catalog"]/a
    Click Link      //*[@id="collapse1"]/li[2]/a
    Select Checkbox      //*[@id="form-product"]/div/table/tbody/tr[20]/td[1]/input
    Click Button    css:button[data-original-title='Delete']
    Alert Should Be Present     action=ACCEPT

Get number of products
    connect to database  dbConfigFile=default.cfg
    table must exist  oc_product
    check if exists in database  SELECT * FROM oc_product
    ${rowCount1}     row count   SELECT * FROM oc_product
    disconnect from database
    ${rowCount}=     set global variable   ${rowCount1}

Check the test product is deleted
    connect to database  dbConfigFile=default.cfg
    table must exist  oc_product
    check if exists in database  SELECT * FROM oc_product
    row count is less than x  SELECT * FROM oc_product  ${rowCount}
    disconnect from database

Check the test product is present in Database
    connect to database  dbConfigFile=default.cfg
    table must exist  oc_product
    check if exists in database  SELECT * FROM oc_product WHERE model='test_product'
    @{queryResults}     Query   SELECT * FROM oc_product WHERE model='test_product'
    Log     @{queryResults}
    disconnect from database

*** Test Cases ***
Check the test product is present in Database
        User Login  admin
        Add Product
        Check the test product is present in Database
        Close Browser
The user with admin role can add another user
        User Login  admin
        connect to database  dbConfigFile=default.cfg
        table must exist  oc_product
        check if exists in database  SELECT * FROM oc_product
        ${rowCount1}     row count   SELECT * FROM oc_product
        Delete Product
        ${rowCount2}     row count   SELECT * FROM oc_product
        should not be equal as integers     ${rowCount1}    ${rowCount2}
        disconnect from database
        Close Browser
#The user with admin role can add another user
#        User Login  admin
#        Get number of products
#        Delete Product
#        Check the test product is deleted
#        Close Browser