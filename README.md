# IBM Functions.    Skuratova Nina.     IBA

1. Cloning into a repo:

    git clone https://github.com/skuratovaN/skuratova_ibm_functions.git

2. Change directory:

    cd skuratova_ibm_functions
    
3. Create action from existing file __\_\_main\_\_.py__:

    ibmcloud fn action create act \_\_main__.py

4. Update action __act__ with parameters from an existing action:

    ibmcloud fn action update act -a web_export true -a final true -a require-whisk-auth c99cea7e-2df8-49b2-9e6c-428039691a0a --web true
     
5. Create API:

    ibmcloud fn api create //skuratova //currency post act --response-type json

6. Viewing packages, actions, triggers, and rules in the namespace (to make sure that action and API are already here):

    ibmcloud fn list
