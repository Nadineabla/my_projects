def add_setting(settings,tup):
    key, value = tup
    key , value = key.lower() , value.lower()
    if key in settings.keys() :
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    settings[key] = value
    return f"Setting '{key}' added with value '{value}' successfully!"

def update_setting(settings, tup) :
    key, value = tup
    key , value = key.lower() , value.lower()
    if key in settings.keys() :
        settings[key] = value
        return f"Setting '{key}' updated to '{value}' successfully!"
    else:
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."

def delete_setting(settings, key) :
    key = key.lower()
    if key in settings.keys() :
        del settings[key]
        return f"Setting '{key}' deleted successfully!"
    else:
        return "Setting not found!"

def view_settings(settings) :
    if not settings :
        return "No settings available."
    else:
        output = "Current User Settings:\n"
        for key, value in settings.items() :
            output += f"{key.capitalize()}: {value}\n"
        return output
test_settings ={}
bulk_data =[
    ('theme','light'),
    ('volume','high'),
    ('THEME','dark')
]
for setting in bulk_data:
    add_setting(test_settings, setting)
print(add_setting(test_settings , ('notifications','enable')))
print(view_settings(test_settings))