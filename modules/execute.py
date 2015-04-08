#!/usr/bin/python
def hello():
	print 'hello world'
	
def execute(command):
	proc = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
	stdoutput = proc.stdout.read() + proc.stderr.read()
	return stdoutput
