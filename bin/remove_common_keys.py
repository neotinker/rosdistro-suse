import yaml,sys
with open(sys.argv[1], 'r') as ofile:
  oyd = yaml.safe_load(ofile)
with open(sys.argv[2], 'r') as sfile:
  syd = yaml.safe_load(sfile)

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

# Look at keys in stripped yaml and remove them if they match the entry in the original yaml
nyd = {}
for item in syd:
  #print("Item {}".format(item))
  if item in oyd:
    #print("Found {} in original yaml".format(item))
    if selected_os in oyd[item] and syd[item][selected_os] == oyd[item][selected_os]:
      #print("   {} Same with original yaml ".format(item))  
      continue
  #else:
    #print("Missing {} in original yaml".format(item))
  nyd[item] = syd[item]
  #print("new entry '{}' = {}".format(item,nyd[item]))

#print(nyd)
for item in nyd:
  if isinstance(nyd[item][selected_os],dict):
    print('{}:'.format(item))
    print('  {}:'.format(selected_os))
    for release in nyd[item][selected_os]:
      if is_number(release):
        print('    \'{}\': {}'.format(release,yaml.dump(nyd[item][selected_os][release], default_flow_style=True, width=2147483647)),end='')
      else:
        print('    {}: {}'.format(release,yaml.dump(nyd[item][selected_os][release], default_flow_style=True, width=2147483647)),end='')
  else:
    print('{}:'.format(item))
    print('  {}: {}'.format(selected_os, yaml.dump(nyd[item][selected_os], default_flow_style=True, width=2147483647)),end='')
