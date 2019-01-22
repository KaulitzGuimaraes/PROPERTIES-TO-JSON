# PROPERTIES-TO-JSON

You MUST have npm installed

- link :https://docs.npmjs.com/cli/install

Npm library documentation :


Into the script, you can change the path folders, changing the method create_json_config content variable :

```python
def create_json_config() :
    ...
    content = '''{"src": "./", "dist": "./"}'''
    ...
```

If you don't change it, the script MUST be runned into the folder with .properties file(s).
