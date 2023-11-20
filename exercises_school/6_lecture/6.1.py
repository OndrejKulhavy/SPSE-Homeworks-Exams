def append_jecna_postfix(name):

    return name + "@spsejecna.cz"




def append_seznam_postfix(name):

    return name + "@seznam.cz"

appender_postfix = append_jecna_postfix


print(appender_postfix("novak"))

appender_postfix = append_seznam_postfix
print(appender_postfix("novak"))


