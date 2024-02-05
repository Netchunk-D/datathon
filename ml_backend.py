import pandas as pd
import numpy as np
import models.localizor_model as localizor_model
import models.detector_model as detector_model

no_fault_msg = "No fault detected on line: "
fault_msg = "Fault detected on line: "
try_msg = "Trying to localize the fault..."
localization_msg = "Fault localized at a distance: "


def analyze_data(st,data,time):
    response_dict = {
    'fault': False,
    'dist': 0
    }
    show_time = f'[{time}]: '
    df = data       # data is a pandas dataframe asuumption
    fault = detector_model.predict(df)
    if fault:
        response_dict['fault'] = True
        yield show_time + fault_msg + str(st)
        loc = localizor_model.predict(df)
        response_dict['dist'] = loc
        yield show_time + localization_msg + str(loc) + " km from station: " + str(st)
    else:
        yield show_time + no_fault_msg + str(st)
    yield response_dict