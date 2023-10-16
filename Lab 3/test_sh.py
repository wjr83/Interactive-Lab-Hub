import subprocess
from subprocess import Popen, PIPE
from subprocess import check_output
from flask import Flask

def get_shell_script_output_using_communicate():
    session = Popen(['./test_qna.sh'], stdout=PIPE, stderr=PIPE)
    stdout, stderr = session.communicate()
    if stderr:
        raise Exception("Error "+str(stderr))
    return stdout.decode('utf-8')

def get_shell_script_output_using_check_output():
    stdout = check_output(['./test_qna.sh']).decode('utf-8')
    return stdout

app = Flask(__name__)

@app.route('/',methods=['GET',])
def home():
    return '<pre>'+get_shell_script_output_using_check_output()+'</pre>'

app.run(debug=True)