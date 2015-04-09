#!/usr/bin/python
import os 
import subprocess

def shell_command(command):
	proc = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
	stdoutput = proc.stdout.read() + proc.stderr.read()
	return stdoutput
