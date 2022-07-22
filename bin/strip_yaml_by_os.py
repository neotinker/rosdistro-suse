import yaml,sys
with open(sys.argv[1], 'r') as file:
  yd = yaml.safe_load(file)

def is_number(s):
  if type(s) in [float, int, complex]:
    return True
  if s.is_numeric():
    return True
  else:
    try:
      float(s)
      return True
    except ValueError:
      return False


newyd = {}
for item in yd:
  if 'opensuse' in yd[item]:
    newyd[item] = {}
    if isinstance(yd[item]['opensuse'],dict):
      newyd[item]['opensuse'] = {}
      newyd[item]['opensuse'] = yd[item]['opensuse']
      print('{}:'.format(item))
      print('  opensuse:')
      for release in yd[item]['opensuse']:
        if is_number(release):
          print('    \'{}\': {}'.format(release,yaml.dump(newyd[item]['opensuse'][release], default_flow_style=True, width=2147483647)),end='')
        else:
          print('    {}: {}'.format(release,yaml.dump(newyd[item]['opensuse'][release], default_flow_style=True, width=2147483647)),end='')
    else:
      newyd[item]['opensuse'] = yd[item]['opensuse']
      print('{}:'.format(item))
      print('  opensuse: {}'.format(yaml.dump(newyd[item]['opensuse'], default_flow_style=True, width=2147483647)),end='')
#print(newyd)
#print(yaml.dump(newyd, default_flow_style=True))
