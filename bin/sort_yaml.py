import yaml,sys
with open(sys.argv[1], 'r') as file:
  yd = yaml.safe_load(file)

print(yaml.dump(yd,Dumper=yaml.Dumper))
