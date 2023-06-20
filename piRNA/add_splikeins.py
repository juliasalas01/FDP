# -*- coding: utf-8 -*-
import sys

in_file_2 = sys.argv[1] # spike-ins
out_file = sys.argv[2] # genome to add
with open(out_file, "a+") as o:
        with open(in_file_2, "r") as f:
                lines = f.read().rstrip("\n").split("\n")
                for line in lines:
                        if line.startswith(">"):
                                o.write(line + "\n")
                        else:
                                o.write(line.upper() + "\n")
        f.close()
o.close()