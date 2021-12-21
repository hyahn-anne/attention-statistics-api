from datetime import date as date_type, timedelta

LENGTH_DATE = 10

def get_ndays_ago(date: date_type, days: int) -> date_type:
    """
    get date before n days

    parameters :
        date (date): basis date
        days (int): n days
    
    return :
        date: date before n days
    """
    delta = timedelta(days=days)
    ndays_ago_date = date - delta
    return ndays_ago_date


def convert_tuplelist_to_dict(tlist: list, fields: list):
    """
    1) groupping values of tuple by key of tuple
    2) converting tuple list of 1) to dictionary list 

    parameters :
        tlist (list): tuple list
        fields (list): key list
    
    return :
        list: dictionary list
    """
    group_dict = {}
    for k, v in tlist:
        group_dict.setdefault(k, []).append(v)
    group_list = list(group_dict.items())
    dict_list = [dict(zip(fields, t)) for t in group_list]
    return dict_list