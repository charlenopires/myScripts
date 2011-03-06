# -*- coding: utf-8 -*-

#TODO: Informar em qual diretório está atualizando
#TODO: Mostrar em porcentagem o andamento da atualização

import os, subprocess, sys

dirname = sys.argv[1]

def message(dir):
	return "\n\n" + "#"*80 + "\n" + dir + "\n" + "#"*80

dirs = [f for f in os.listdir(dirname) if os.path.isdir(os.path.join(dirname, f))]
for d in dirs:
	dr = os.path.join(dirname, d)
	if os.path.isdir(dr):
		ds = os.listdir(dr)
		if '.git' in ds:
			print message(dr)
			subprocess.call('cd %s && git pull' % dr, shell=True)
		elif '.hg' in ds:
			print message(dr)
			subprocess.call('cd %s && hg pull && hg update' % dr, shell=True)
		elif '.svn' in ds:
			print message(dr)
			subprocess.call('cd %s && svn update' % dr, shell=True)
		else:
			print "O diretório %s não possui controle de versão" % dr
			pass