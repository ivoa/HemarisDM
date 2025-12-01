"""
this script does an initial rough conversion from OpenAPI to VO-DML - it is tuned for execution broker,
but even then there is much hand editing required as VO-DML is semantically richer than OpenAPI and there
are some OpenAPI constructs that do not map easily to VO-DML
"""

import os,sys
import yaml


def getname(ref):
    return ref.split("/")[-1]

def translate(infile, outfile):
    with open(infile) as f:
        oai = yaml.load(f,yaml.BaseLoader)
        print(oai)
        with open(outfile,"w") as of:
            of.write( """
model execbroker (1.0) "the data model for execution broker"
author "Dave Morris"

include "../build/tmp/IVOA-v1.0.vodsl"

            """)
            schemas = oai["components"]["schemas"]
            for name, defn in schemas.items():
                #print(name)
                if defn["type"] == "object":
                    of.write(f"\notype {name} ")
                    if "allOf" in defn and len(defn["allOf"]) == 2 and  "$ref" in defn["allOf"][0]:
                        of.write(f" -> {getname(defn["allOf"][0]["$ref"])} ")
                    of.write(" \""+defn.get("description","")+"\"\n {")
                    props={}
                    if "properties" in defn:
                        props = defn["properties"]
                    elif "allOf" in defn and len(defn["allOf"]) == 2 and  "$ref" in defn["allOf"][0] and "type"  in defn["allOf"][1] :
                        props = defn["allOf"][1]["properties"]
                    else:
                        print(f"did not understand content of {name}\n")
                    for pname, pdefn in props.items():
                        if "type" in pdefn:
                            if pdefn["type"] == "array":
                                items = pdefn["items"]
                                if "type" in items :
                                     of.write(f"\n {pname} : ivoa:{items["type"]} @+ \"{pdefn.get("description","")}\";") #FIXME for types
                                elif "$ref" in items:
                                     of.write(f"\n {pname}  : {getname(items["$ref"])} @+ \"{pdefn.get("description","")}\"; // ref originally") #FIXME for types
                                else:
                                    print(f"{name} property {pname} not understood\n")
                            else:
                                of.write(f"\n {pname} : ivoa:{pdefn["type"]} \"{pdefn.get("description","")}\"; ") #FIXME for types & multiplicities
                        elif "$ref" in pdefn:
                            of.write(f"\n {pname} : {getname(pdefn["$ref"])} \"{pdefn.get("description","")}\"; //ref originally") #FIXME for multitplicities - also perhaps not always semantically a reference - probably more often a containment
                        else:
                            print(f"{name} property {pname} not understood\n")
                    of.write("\n}\n")
                elif defn["type"] == "array":
                    print(f"{name}: of type {defn["type"]} not processed")
                else:
                    match defn["type"]:
                       case "string":
                           if "enum" in defn:
                               of.write(f"\nenum {name} \"{defn.get("description","")}\" {{\n")
                               of.write(",\n".join(val+" \"\"" for val in defn["enum"]))
                               of.write("\n}\n")
                           else:
                               of.write(f"\nprimitive {name} -> ivoa:string \"{defn.get("description","")}\"\n")
                       case _:
                        print(f"{name}: of type {defn["type"]} not processed")


if __name__ == '__main__':
    translate("calycopis.yaml", "model/ExecutionBrokerDM-v1.vodsl")