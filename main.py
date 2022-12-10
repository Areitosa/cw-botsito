fromfrom functions import main
import ast
import os
import logging
import time
#logging.basicConfig(level=logging.INFO)

api_id = int(os.environ.get("27960451"))
api_hash = str(os.environ.get("ab2d2853e472645d01c5b5b55b72c022"))
api_session = str(os.environ.get("SESSION"))

try:
    api_session = api_session.strip('][').split(', ') 
except:
    api_session = [api_session]

try:
    cw_ids = str(os.environ.get("CW_IDS"))
    cw_ids = ast.literal_eval(cw_ids)
    if len(cw_ids) == 1:
        cw_ids += [cw_ids[0] for i in range(len(api_session)-len(cw_ids))]
    else:
        cw_ids += [{} for i in range(len(api_session)-len(cw_ids))]
except:
    cw_ids = [{} for i in api_session]    
    
if isinstance(api_session, list):
    cuentas = [
        main(api_id,api_hash,str(api_session[i]),cw_ids[i]) for i in range(len(api_session))]
else:
    cuenta = main(api_id, api_hash, api_session, cw_ids)
    print (cuenta)
from