import yaml,sys
with open(sys.argv[1], 'r') as file:
  yd = yaml.safe_load(file)

def is_number(s):
  if type(s) in [float, int, complex]:
    return True
  if s.isnumeric():
    return True
  else:
    try:
      float(s)
      return True
    except ValueError:
      return False


selected_os = "opensuse"

newyd = {}
for item in yd:
  if selected_os in yd[item]:
    newyd[item] = {}
    if isinstance(yd[item][selected_os],dict):
      newyd[item][selected_os] = {}
      newyd[item][selected_os] = yd[item][selected_os]
      print('{}:'.format(item))
      print('  {}:'.format(selected_os))
      for release in yd[item][selected_os]:
        if is_number(release):
          print('    \'{}\': {}'.format(release,yaml.dump(newyd[item][selected_os][release], default_flow_style=True, width=2147483647)),end='')
        else:
          print('    {}: {}'.format(release,yaml.dump(newyd[item][selected_os][release], default_flow_style=True, width=2147483647)),end='')
    else:
      newyd[item][selected_os] = yd[item][selected_os]
      print('{}:'.format(item))
      print('  {}: {}'.format(selected_os, yaml.dump(newyd[item][selected_os], default_flow_style=True, width=2147483647)),end='')
