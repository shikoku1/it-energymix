import csv
import dateutil.parser
import numpy as np
import os
from datetime import datetime, timedelta


def load_csv(file):
    with open(file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                pass
                #print(f'Column names are {", ".join(row)}')
            else:
                #date=dateutil.parser.isoparse(row[0])

                #row[0]=date
                #row[1]=float(row[1].replace(',','.'))
                yield float(row[1])
            line_count += 1
    


def load_generation_csv(file):
    gen=load_csv(os.path.join(os.path.dirname(__file__), file))
    gen=np.array(list(gen))
    assert gen.size == 24*365
    return gen

class Terna:
    time: np.array
    consumo: np.array
    gen_geothermal: ...
    gen_hydro: ...
    gen_pv: ...
    gen_pv_re: np.array
    gen_thermal: ...
    gen_wind_re: np.array
    gen_wind: ...
    #pumping_consumption: ...
    #exchange: ...
    selfc: ...

    def __init__(self):
        # measure loading time
        start_time = datetime.now()

        self.time = list(map(lambda i: datetime(2022, 1, 1, 0, 0, 0) + timedelta(hours=i), range(24*365)))
        self.time = np.array(self.time)

        assert len(self.time) == 24*365

        data_dir = "data/"

        self.gen_pv_re=load_generation_csv(data_dir + 'fotovoltaico_re.csv')
        self.gen_wind_re=load_generation_csv(data_dir + 'eolico_re.csv')
        self.gen_geothermal=load_generation_csv(data_dir + 'actual_geothermal.csv')
        self.gen_hydro=load_generation_csv(data_dir + 'actual_hydro.csv')
        self.gen_pv=load_generation_csv(data_dir + 'actual_pv.csv')
        self.gen_thermal=load_generation_csv(data_dir + 'actual_thermal.csv')
        self.gen_wind=load_generation_csv(data_dir + 'actual_wind.csv')
        self.selfc=load_generation_csv(data_dir + 'actual_selfconsumption.csv')
        

        # consumo
        self.consumo = np.array([])

        cons=load_csv(os.path.join(os.path.dirname(__file__), data_dir + 'load.csv'))
        cons=list(cons)
        for ora in range(24*365):
            self.consumo = np.append(self.consumo, (cons[ora*4] + cons[ora*4+1] + cons[ora*4+2] + cons[ora*4+3])/4/1000)

        end_time = datetime.now()
        print(f'Loading time (s): {(end_time - start_time).total_seconds()}')

        assert len(self.consumo) == 24*365
    
    def scale_pv(self, new_installed_capacity):
        return self.gen_pv_re / 24.20 * new_installed_capacity

    def scale_wind(self, new_installed_capacity):
        return self.gen_wind_re / 11.70 * new_installed_capacity
