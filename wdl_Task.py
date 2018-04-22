import os, sys, json, re
from glob import glob

class Task_GATK(object):
    
    def __init__(self):
        self.workflow_file = "./SimpleWorkflow.wdl"
        self.input_json = "./SimpleWorkflow_inputs.json"        
        wdl_cmd = "java -jar Cromwell.jar run %s --inputs %s" %(self.workflow_file, self.input_json)
    
    def create_input_json(self):
        wdl_input_cmd = "java -jar wdltool.jar inputs %s > %s" %(self.workflow_file, self.input_json)
        os.system(wdl_input_cmd)
        with open(self.input_json) as ij:
            JSON_file = json.load(ij)
        return JSON_file
    
    def dict_writer(self, JSON_dict, keyword, valueword):
        for key in JSON_dict.keys():
            if keyword in key:
                JSON_dict[key] = valueword        
    
    def edit_input_json(self, JSON_dict):
        with open(self.input_json, 'w') as ij:
            json.dump(JSON_dict, ij) # json encoding and file out

            
if __name__=="__main__":
    task1 = Task_GATK()
    jsonTodict = task1.create_input_json()
    task1.dict_writer(jsonTodict, ".name", "SimpleTask")
    task1.dict_writer(jsonTodict, ".refFasta","/home/seonwhee/Bioinformatics/Pipeline/Reference/STARindex/hg38/hg38.fasta")
    task1.edit_input_json(jsonTodict)   