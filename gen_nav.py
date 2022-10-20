#!/usr/bin/env python

import toml

config_file = "config.toml"
config = toml.load(config_file)

i = 1
if "menu" in config:
   for entry in config["menu"]["main"]:
      entry["weight"] = i
      i += 1
else:
   print('no menu entry found in ' + config_file)


with open(config_file, "w") as toml_file:
    toml.dump(config, toml_file)


