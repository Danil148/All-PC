import platform,socket,re,uuid,json,psutil,logging,pymysql
from tkinter.messagebox import showinfo, askyesno
import time

def getSystemInfo():
    try:
        info={}
        info['platform']=platform.system()
        info['platform-release']=platform.release()
        info['platform-version']=platform.version()
        info['architecture']=platform.machine()
        info['hostname']=socket.gethostname()
        info['ip-address']=socket.gethostbyname(socket.gethostname())
        info['mac-address']=':'.join(re.findall('..', '%012x' % uuid.getnode()))
        info['processor']=platform.processor()
        info['ram']=str(round(psutil.virtual_memory().total / (1024.0 **3)))+" GB"
        return json.dumps(info)
    except Exception as e:
        logging.exception(e)

connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             database='test',
                             port=3306)

with connection:
    with connection.cursor() as cursor:
        # Create a new record
        sql = "\
        INSERT INTO `users` (`platform`, `platform-release`, `platform-version`, `architecture`, `hostname`, `ip-address`, `mac-address`, `processor`, `ram`, `times`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)\
        "
        cursor.execute(sql, (json.loads(getSystemInfo())['platform'], json.loads(getSystemInfo())['platform-release'],json.loads(getSystemInfo())['platform-version'], json.loads(getSystemInfo())['architecture'],json.loads(getSystemInfo())['hostname'], json.loads(getSystemInfo())['ip-address'],json.loads(getSystemInfo())['mac-address'], json.loads(getSystemInfo())['processor'],json.loads(getSystemInfo())['ram'], time.strftime('%Y:%D:%H:%M:%S')))
        
        connection.commit()
        
result = askyesno(title="Microsoft", message="Something went wrong do you want to fix the problem?")

if result:
    showinfo(title="Microsoft", message="Fixing the problem")
    time.sleep(5)
    # There may be your code here 
else:
    pass
    # There may be your code here
