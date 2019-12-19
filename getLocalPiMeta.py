import subprocess
import pprint

def pi_meta():
    cmd = ['cat', '/proc/cpuinfo']
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    o, e = proc.communicate()
    o = o.decode('ascii')
    o = o.replace('\t','')
    o = o.replace('\n','~')
    o= o.split('~')
    olist = []
    for ln in o:
        if len(ln.strip()) > 0 and ln.find(':') !=1 :
            olist.append(ln.split(':'))
    odict = {}
    for elem in olist:
        odict[elem[0]] = elem[1]

    return {"Output": odict, "Error": e.decode('ascii'), "Code": str(proc.returncode)}

if __name__ == "__main__":
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint( pi_meta() )

