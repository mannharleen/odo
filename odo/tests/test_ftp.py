import os
from odo import odo, drop
import pandas as pd
import pytest, json
from odo.tests.utils import open

#  test setup
#  create two files
FTP_CONN = os.environ.get('FTP_CONN', 'ftp://ftpuser1:ftpuser1@localhost:21')
with open(FTP_CONN + '/del1.csv', 'w') as f:
    f.write('a,b,c\n1,2,3\n')
with open(FTP_CONN + '/del1.json', 'w') as f:
    f.write('{  "a": 1,  "b": 2,  "c": 3}')


def test_json_to_csv():
    # source = pd.DataFrame({'col1': [1, 2, 3]})
    source = FTP_CONN + '/del1.json'
    target = FTP_CONN + '/del2.csv'
    try:
        drop(target)
    except:
        pass
    odo(source, target, header=True)

    f_t = open(target)
    assert f_t.read() == 'a,b,c\n1,2,3\n'
    f_t.close()


def test_csv_to_json():
    source = FTP_CONN + '/del1.csv'
    target = FTP_CONN + '/del2.json'
    try:
        drop(target)
    except:
        pass
    odo(source, target)

    f_t = open(target)
    assert json.loads(f_t.read()) == json.loads('{  "a": 1,  "b": 2,  "c": 3}')
    f_t.close()


def test_df_to_json():
    source = pd.DataFrame([{"a": 1,  "b": 2,  "c": 3}])
    target = FTP_CONN + '/del2.json'
    try:
        drop(target)
    except:
        pass
    odo(source, target)

    f_t = open(target)
    assert json.loads(f_t.read()) == json.loads('{  "a": 1,  "b": 2,  "c": 3}')
    f_t.close()

