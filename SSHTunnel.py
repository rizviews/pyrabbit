import os,signal,subprocess


class SSHTunnel():
    """Class to create SSH tunneling"""
    def __init__(self, **kwargs):
        self.ssh_host = kwargs.get('ssh_host','')
        self.username = kwargs.get('username','')
        self.pasword = kwargs.get('password','')
        self.key_file = kwargs.get('key_file','')
        self.local_address = kwargs.get('local','')
        self.remote_address = kwargs.get('remote','')
        self.process = None
        self.key = ''
    def forward(self):
        try:
            if self.key_file != '':
                print ("Starting SSH tunnelling with parameters {},{},{},{}".format(self.key_file,self.local_address,self.remote_address,self.username+'@'+self.ssh_host))
                ssh = ['C:\\Program Files\\Git\\usr\\bin\\ssh.exe','-f','-N','-i',self.key_file,'-L',self.local_address+":"+self.remote_address+':5672',self.username+'@'+self.ssh_host]
                print (ssh)
                ssh2 = ['C:\\Program Files\\Git\\usr\\bin\\ssh.exe']
                process = subprocess.Popen(ssh)
                process.communicate()
                print ("Completed SSH tunnelling successfully")
        except Exception as e:
            print ("Failed to establish tunnelling, error occurred: "+repr(e))
           

    def terminate(self):
        try:
            import psutil
            PROCNAME = "ssh.exe"
            print ("Terminating SSH tunnel")
            for proc in psutil.process_iter():
                # check whether the process name matches
                if proc.name()==PROCNAME:
                    proc.kill()
                    break;
            print ("Terminated SSH tunnel successfully")
        except Exception as e:
            print ("Failed to terminate tunnelling, error occurred: "+repr(e))
