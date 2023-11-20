def append_jecna_postfix(name):

    return name + "@spsejecna.cz"




def append_seznam_postfix(name):

    return name + "@seznam.cz"

def create_email(appender_function, name):
    email = appender_function(name)
    return email



appender_postfix = append_jecna_postfix
print(create_email(appender_postfix, "novak"))
#ma vratit novak@spsejecna.cz
appender_postfix = append_seznam_postfix
print(create_email(appender_postfix, "novak"))
#ma vratit novak@seznam.cz


