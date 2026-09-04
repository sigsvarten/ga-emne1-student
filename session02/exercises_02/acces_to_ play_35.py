# tilgang tiø et spill med boolske verdier

has_username = True
accepted_rules = True
is_blocked = False


if has_username and accepted_rules and not is_blocked: # not betyr ikkje falsk, motsatt av variabel is_blocked
    print('You have access')
else:
    print('No access')