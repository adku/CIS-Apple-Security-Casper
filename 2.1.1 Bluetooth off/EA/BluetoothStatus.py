#!/usr/bin/python

# EA to check for Bluetooth Status

import CoreFoundation

domain = 'com.apple.Bluetooth'
key = 'ControllerPowerState'

key_value = CoreFoundation.CFPreferencesCopyAppValue(key, domain)

if key_value == 1:
    print "<result>Enabled</result>"
else:
    print "<result>Disabled</result>" 