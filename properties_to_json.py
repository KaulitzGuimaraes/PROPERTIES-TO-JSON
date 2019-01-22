import os
'''
:author: Kaulitz.Guimaraes@ibm.com
'''
def create_json_config() :
    '''
    This method creates  the config file with path destinations
    :return: void
    '''
    content = '''{"src": "./", "dist": "./"}'''
    open( "config.json", 'w').write(content)

def call_npm_to_tranform_json_in_properties() :
    '''
    This method call the npm command to parse properties to json
    :return:
    '''
    try:
        os.system("npm install json-to-properties -g")
        os.system(" json-to-properties -c config.json -r ")
        os.system("rm -rf config.json config.properties")
    except :
        print("You probably does not have npm installed !!!!!!")


if __name__ == '__main__' :
     '''
     Main method
     '''
     create_json_config()
     call_npm_to_tranform_json_in_properties()