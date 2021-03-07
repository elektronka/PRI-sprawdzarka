import re, subprocess, os
from .models import TeacherTask, StudentTask

def promela_funck():
    pattern = re.compile(r'^ltl\s(.+?)\s\{')
    List_of_files = StudentTask.objects.filter(has_been_tested=False).all()
    for file in List_of_files:
        ltl = TeacherTask.objects.get(id = file.task_id.id)
        ltl_list = []
        for i, line in enumerate(open(ltl.file.name)):
            for match in re.finditer(pattern, line):
                all_found = match.group()
                ltl_temp = re.findall(r'ltl\s(.+)\s\{', all_found)
                sss = ltl_temp[0]
                ltl_list.append(sss)
        print(ltl_list)

        file_new = str(file.task_file.name)
        file.output_file.name=file_new.replace(".pml", "_result.txt") 
        file_new = file_new.replace(".pml", "_result.txt")
        open(file_new, 'w').close()

        file.has_been_tested = True
        ltl_cos_1="C:\\PRI-sprawdzarka\\sprawdzarka\\"
        ltl_cos_1+=ltl.file.name.replace('/','\\')

        ltl_cos_2="C:\\PRI-sprawdzarka\\sprawdzarka\\"
        ltl_cos_2+=file.task_file.name.replace('/','\\')

        subprocess.run(f'spin -a -N {ltl_cos_1} {ltl_cos_2}', shell=True)
        out = subprocess.Popen('gcc -o pan pan.c',
                               stdout=subprocess.PIPE,
                               stderr=subprocess.STDOUT,
                               shell=True)
        stdout, stderr = out.communicate()
        print(stdout)
        if stdout == b'':
            temp = 0
            if len(ltl_list) == 0:
                command_no_ltl = "C:\\PRI-sprawdzarka\\sprawdzarka\\pan -m400000"
                subprocess.run(command_no_ltl, shell=True)
            else:
                for ltl_number in ltl_list:
                    command_ltl = f'C:\\PRI-sprawdzarka\\sprawdzarka\\pan -a -N {ltl_number} >> {file_new}'
                    subprocess.run(command_ltl, shell=True)
                    print(command_ltl)
        ww = []
        with open(file_new) as f:
            ww = f.read().splitlines()
            f.close()
        for a in ww:
            b = re.search(r'errors: [123456789]', a)
            print(b)
            if b:
                file.points = 0
                break
            else:
                file.points = ltl.max_points

        file.has_been_tested=True
        file.save()