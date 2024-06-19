#!/usr/bin/env python3

import argparse
import os,sys
import subprocess,pexpect,signal
import argcomplete

import colorama
from colorama import Fore
from colorama import Style

def printclear(result):
    for c in result:
        output = c.strip()
        if output == []:
            error = ssh.stderr.readlines()
            print >>sys.stderr, "ERROR: %s" % error
        else:
            l1=['fail','ostkcd','error','FAILURE']
            print (output)

def sshfunction(listofhosts):
    my_list=listofhosts.split("\n")
    sshCmd = 'ssh -C -o ControlMaster=auto -o ControlPersist=60s -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null -o ForwardAgent=yes '
    for i in my_list:
        print(Fore.BLUE + i +  Style.RESET_ALL)
        if i.startswith('its'):
            ssh = subprocess.Popen(["ssh",  "%s" % i, 'uptime ; last -n 5 | grep ostkcd ; systemctl status neutron-dhcp-agent.service --lines=1 ; systemctl status neutron-dhcpd.service neutron-dhcpd-restart.timer'],shell=False,stdout=subprocess.PIPE,stderr=subprocess.PIPE,universal_newlines=True)
            result = ssh.stdout.readlines()
            printclear(result)
        elif 'mq' in i:
            ssh = subprocess.Popen(["ssh",  "%s" % i, 'uptime ; last -n 5 | grep ostkcd ; systemctl status rabbitmq*'],shell=False,stdout=subprocess.PIPE,stderr=subprocess.PIPE,universal_newlines=True)
            result = ssh.stdout.readlines()
            printclear(result)
        elif 'api' in i:
            ssh = subprocess.Popen(["ssh",  "%s" % i, 'uptime ; last -n 5 | grep ostkcd ; systemctl status ironic-api.service neutron-server.service nova-conductor.service --lines=1'],shell=False,stdout=subprocess.PIPE,stderr=subprocess.PIPE,universal_newlines=True)
            result = ssh.stdout.readlines()
            printclear(result)
        elif i.startswith('ic'):
            ssh = subprocess.Popen(["ssh",  "%s" % i, 'uptime ; last -n 5 | grep ostkcd ; systemctl status ironic-conductor.service --lines=2'],shell=False,stdout=subprocess.PIPE,stderr=subprocess.PIPE,universal_newlines=True)
            result = ssh.stdout.readlines()
            printclear(result)
        else:
            ssh = subprocess.Popen(["ssh",  "%s" % i, 'uptime ; last -n 5 | grep ostkcd'],shell=False,stdout=subprocess.PIPE,stderr=subprocess.PIPE,universal_newlines=True)
            result = ssh.stdout.readlines()
            printclear(result)

# getting hostlist from openstack role
def host_list(cluster):
    if (len(cluster) == 12) and (cluster.startswith('dv1') or cluster.startswith('cl1') or cluster.startswith('cl3')):
        print("Touch Yubikey if flashing")
        a=subprocess.check_output(["rocl "+"-m "+"-r "+"openstack.prod."+cluster + " 2>/dev/null " + "| grep -v hv" ],shell=True).decode('utf-8').strip()
        sshfunction(a)
    elif (len(cluster) == 12) and (cluster.startswith('bm2')):
        print("Touch Yubikey if flashing")
        a=subprocess.check_output(["rocl "+"-m "+"-r "+"openstack.prod."+cluster + " 2>/dev/null "],shell=True).decode('utf-8').strip()
        sshfunction(a)
    else:
        print("Please enter a valid cluster name")

#enabling touchless
def yinit():
    system_name = os.getenv('HOSTNAME')
    subprocess.run('/bin/init -remote --touchlessSudoTime 240 --touchlessSudoHosts ' + system_name  , shell=True)

def main():
    parser=argparse.ArgumentParser(usage="""clustercheck {clustername} [-s]""",description="""To check on clusterstatus and each host process status""")
    parser.add_argument('-c', action='store', dest='cluster', help='cluster name', required=True)
    parser.add_argument('-s', '--skip', dest='skip',action='store',help='Skip touchless')
    try:
        args, unparsed = parser.parse_known_args()
    except:
        sys.exit(0)
    #parser.print_help()
    cluster2 = args.cluster.replace("_",".").replace("-",".")
    if args.skip:
        host_list(cluster2)
    else:
        yinit()
        host_list(cluster2)


if __name__ == "__main__":
    main()
