#! /usr/bin/python

Ada, C, GUI, SIMULINK, VHDL, OG, RTDS, SYSTEM_C, SCADE6, VDM, CPP = range(11)
thread, passive, unknown = range(3)
PI, RI = range(2)
synch, asynch = range(2)
param_in, param_out = range(2)
UPER, NATIVE, ACN = range(3)
cyclic, sporadic, variator, protected, unprotected = range(5)
enumerated, sequenceof, sequence, set, setof, integer, boolean, real, choice, octetstring, string = range(11)
functions = {}

functions['joystickdriver'] = {
    'name_with_case' : 'JoystickDriver',
    'runtime_nature': thread,
    'language': OG,
    'zipfile': '',
    'interfaces': {},
    'functional_states' : {}
}

functions['joystickdriver']['interfaces']['step'] = {
    'port_name': 'step',
    'parent_fv': 'joystickdriver',
    'direction': PI,
    'in': {},
    'out': {},
    'synchronism': asynch,
    'rcm': cyclic,
    'period': 100,
    'wcet_low': 0,
    'wcet_low_unit': 'ms',
    'wcet_high': 10,
    'wcet_high_unit': 'ms',
    'distant_fv': '',
    'calling_threads': {},
    'distant_name': '',
    'queue_size': 1
}

functions['joystickdriver']['interfaces']['step']['paramsInOrdered'] = []

functions['joystickdriver']['interfaces']['step']['paramsOutOrdered'] = []

functions['joystickdriver']['interfaces']['cmd'] = {
    'port_name': 'cmd',
    'parent_fv': 'joystickdriver',
    'direction': RI,
    'in': {},
    'out': {},
    'synchronism': asynch,
    'rcm': sporadic,
    'period': 0,
    'wcet_low': 0,
    'wcet_low_unit': '',
    'wcet_high': 0,
    'wcet_high_unit': '',
    'distant_fv': 'cmddispatcher',
    'calling_threads': {},
    'distant_name': 'cmd',
    'queue_size': 1
}

functions['joystickdriver']['interfaces']['cmd']['paramsInOrdered'] = ['cmd_val']

functions['joystickdriver']['interfaces']['cmd']['paramsOutOrdered'] = []

functions['joystickdriver']['interfaces']['cmd']['in']['cmd_val'] = {
    'type': 'Base_commands_Motion2D',
    'asn1_module': 'Base_Types',
    'basic_type': sequence,
    'asn1_filename': '/home/taste/esrocos_workspace/tutorial_integration_bip/dataview-uniq.asn',
    'encoding': NATIVE,
    'interface': 'cmd',
    'param_direction': param_in
}

functions['cmddispatcher'] = {
    'name_with_case' : 'CmdDispatcher',
    'runtime_nature': thread,
    'language': OG,
    'zipfile': '',
    'interfaces': {},
    'functional_states' : {}
}

functions['cmddispatcher']['interfaces']['cmd'] = {
    'port_name': 'cmd',
    'parent_fv': 'cmddispatcher',
    'direction': PI,
    'in': {},
    'out': {},
    'synchronism': asynch,
    'rcm': sporadic,
    'period': 10,
    'wcet_low': 0,
    'wcet_low_unit': 'ms',
    'wcet_high': 10,
    'wcet_high_unit': 'ms',
    'distant_fv': '',
    'calling_threads': {},
    'distant_name': '',
    'queue_size': 1
}

functions['cmddispatcher']['interfaces']['cmd']['paramsInOrdered'] = ['cmd_val']

functions['cmddispatcher']['interfaces']['cmd']['paramsOutOrdered'] = []

functions['cmddispatcher']['interfaces']['cmd']['in']['cmd_val'] = {
    'type': 'Base_commands_Motion2D',
    'asn1_module': 'Base_Types',
    'basic_type': sequence,
    'asn1_filename': '/home/taste/esrocos_workspace/tutorial_integration_bip/dataview-uniq.asn',
    'encoding': NATIVE,
    'interface': 'cmd',
    'param_direction': param_in
}

functions['cmddispatcher']['interfaces']['log_cmd'] = {
    'port_name': 'log_cmd',
    'parent_fv': 'cmddispatcher',
    'direction': RI,
    'in': {},
    'out': {},
    'synchronism': asynch,
    'rcm': sporadic,
    'period': 0,
    'wcet_low': 0,
    'wcet_low_unit': '',
    'wcet_high': 0,
    'wcet_high_unit': '',
    'distant_fv': 'logger',
    'calling_threads': {},
    'distant_name': 'log_cmd',
    'queue_size': 1
}

functions['cmddispatcher']['interfaces']['log_cmd']['paramsInOrdered'] = ['cmd_val']

functions['cmddispatcher']['interfaces']['log_cmd']['paramsOutOrdered'] = []

functions['cmddispatcher']['interfaces']['log_cmd']['in']['cmd_val'] = {
    'type': 'Base_commands_Motion2D',
    'asn1_module': 'Base_Types',
    'basic_type': sequence,
    'asn1_filename': '/home/taste/esrocos_workspace/tutorial_integration_bip/dataview-uniq.asn',
    'encoding': NATIVE,
    'interface': 'log_cmd',
    'param_direction': param_in
}

functions['cmddispatcher']['interfaces']['test_cmd'] = {
    'port_name': 'test_cmd',
    'parent_fv': 'cmddispatcher',
    'direction': RI,
    'in': {},
    'out': {},
    'synchronism': asynch,
    'rcm': sporadic,
    'period': 0,
    'wcet_low': 0,
    'wcet_low_unit': '',
    'wcet_high': 0,
    'wcet_high_unit': '',
    'distant_fv': 'watchdog',
    'calling_threads': {},
    'distant_name': 'test_cmd',
    'queue_size': 1
}

functions['cmddispatcher']['interfaces']['test_cmd']['paramsInOrdered'] = ['cmd_val']

functions['cmddispatcher']['interfaces']['test_cmd']['paramsOutOrdered'] = []

functions['cmddispatcher']['interfaces']['test_cmd']['in']['cmd_val'] = {
    'type': 'Base_commands_Motion2D',
    'asn1_module': 'Base_Types',
    'basic_type': sequence,
    'asn1_filename': '/home/taste/esrocos_workspace/tutorial_integration_bip/dataview-uniq.asn',
    'encoding': NATIVE,
    'interface': 'test_cmd',
    'param_direction': param_in
}

functions['watchdog'] = {
    'name_with_case' : 'Watchdog',
    'runtime_nature': thread,
    'language': CPP,
    'zipfile': '',
    'interfaces': {},
    'functional_states' : {}
}

functions['watchdog']['interfaces']['test_cmd'] = {
    'port_name': 'test_cmd',
    'parent_fv': 'watchdog',
    'direction': PI,
    'in': {},
    'out': {},
    'synchronism': asynch,
    'rcm': sporadic,
    'period': 10,
    'wcet_low': 0,
    'wcet_low_unit': 'ms',
    'wcet_high': 10,
    'wcet_high_unit': 'ms',
    'distant_fv': '',
    'calling_threads': {},
    'distant_name': '',
    'queue_size': 1
}

functions['watchdog']['interfaces']['test_cmd']['paramsInOrdered'] = ['cmd_val']

functions['watchdog']['interfaces']['test_cmd']['paramsOutOrdered'] = []

functions['watchdog']['interfaces']['test_cmd']['in']['cmd_val'] = {
    'type': 'Base_commands_Motion2D',
    'asn1_module': 'Base_Types',
    'basic_type': sequence,
    'asn1_filename': '/home/taste/esrocos_workspace/tutorial_integration_bip/dataview-uniq.asn',
    'encoding': NATIVE,
    'interface': 'test_cmd',
    'param_direction': param_in
}

functions['watchdog']['interfaces']['purge'] = {
    'port_name': 'purge',
    'parent_fv': 'watchdog',
    'direction': PI,
    'in': {},
    'out': {},
    'synchronism': asynch,
    'rcm': cyclic,
    'period': 80,
    'wcet_low': 0,
    'wcet_low_unit': 'ms',
    'wcet_high': 10,
    'wcet_high_unit': 'ms',
    'distant_fv': '',
    'calling_threads': {},
    'distant_name': '',
    'queue_size': 1
}

functions['watchdog']['interfaces']['purge']['paramsInOrdered'] = []

functions['watchdog']['interfaces']['purge']['paramsOutOrdered'] = []

functions['watchdog']['interfaces']['mot_cmd'] = {
    'port_name': 'mot_cmd',
    'parent_fv': 'watchdog',
    'direction': RI,
    'in': {},
    'out': {},
    'synchronism': asynch,
    'rcm': sporadic,
    'period': 0,
    'wcet_low': 0,
    'wcet_low_unit': '',
    'wcet_high': 0,
    'wcet_high_unit': '',
    'distant_fv': 'blsclient',
    'calling_threads': {},
    'distant_name': 'mot_cmd',
    'queue_size': 1
}

functions['watchdog']['interfaces']['mot_cmd']['paramsInOrdered'] = ['cmd_val']

functions['watchdog']['interfaces']['mot_cmd']['paramsOutOrdered'] = []

functions['watchdog']['interfaces']['mot_cmd']['in']['cmd_val'] = {
    'type': 'Base_commands_Motion2D',
    'asn1_module': 'Base_Types',
    'basic_type': sequence,
    'asn1_filename': '/home/taste/esrocos_workspace/tutorial_integration_bip/dataview-uniq.asn',
    'encoding': NATIVE,
    'interface': 'mot_cmd',
    'param_direction': param_in
}

functions['logger'] = {
    'name_with_case' : 'Logger',
    'runtime_nature': thread,
    'language': OG,
    'zipfile': '',
    'interfaces': {},
    'functional_states' : {}
}

functions['logger']['interfaces']['log_cmd'] = {
    'port_name': 'log_cmd',
    'parent_fv': 'logger',
    'direction': PI,
    'in': {},
    'out': {},
    'synchronism': asynch,
    'rcm': sporadic,
    'period': 10,
    'wcet_low': 0,
    'wcet_low_unit': 'ms',
    'wcet_high': 10,
    'wcet_high_unit': 'ms',
    'distant_fv': '',
    'calling_threads': {},
    'distant_name': '',
    'queue_size': 1
}

functions['logger']['interfaces']['log_cmd']['paramsInOrdered'] = ['cmd_val']

functions['logger']['interfaces']['log_cmd']['paramsOutOrdered'] = []

functions['logger']['interfaces']['log_cmd']['in']['cmd_val'] = {
    'type': 'Base_commands_Motion2D',
    'asn1_module': 'Base_Types',
    'basic_type': sequence,
    'asn1_filename': '/home/taste/esrocos_workspace/tutorial_integration_bip/dataview-uniq.asn',
    'encoding': NATIVE,
    'interface': 'log_cmd',
    'param_direction': param_in
}

functions['blsclient'] = {
    'name_with_case' : 'BLSClient',
    'runtime_nature': thread,
    'language': OG,
    'zipfile': '',
    'interfaces': {},
    'functional_states' : {}
}

functions['blsclient']['interfaces']['mot_cmd'] = {
    'port_name': 'mot_cmd',
    'parent_fv': 'blsclient',
    'direction': PI,
    'in': {},
    'out': {},
    'synchronism': asynch,
    'rcm': sporadic,
    'period': 10,
    'wcet_low': 0,
    'wcet_low_unit': 'ms',
    'wcet_high': 10,
    'wcet_high_unit': 'ms',
    'distant_fv': '',
    'calling_threads': {},
    'distant_name': '',
    'queue_size': 1
}

functions['blsclient']['interfaces']['mot_cmd']['paramsInOrdered'] = ['cmd_val']

functions['blsclient']['interfaces']['mot_cmd']['paramsOutOrdered'] = []

functions['blsclient']['interfaces']['mot_cmd']['in']['cmd_val'] = {
    'type': 'Base_commands_Motion2D',
    'asn1_module': 'Base_Types',
    'basic_type': sequence,
    'asn1_filename': '/home/taste/esrocos_workspace/tutorial_integration_bip/dataview-uniq.asn',
    'encoding': NATIVE,
    'interface': 'mot_cmd',
    'param_direction': param_in
}
