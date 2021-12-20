from datetime import date as date_type, timedelta

def get_ndays_ago(date: date_type, days: int) -> date_type:
    delta = timedelta(days=days)
    ndays_ago_date = date - delta
    return ndays_ago_date


def convert_tuplelist_to_dict(tlist: list, fields: list):
    group_dict = {}
    for k, v in tlist:
        group_dict.setdefault(k, []).append(v)
    group_list = list(group_dict.items())
    dict_list = [dict(zip(fields, t)) for t in group_list]
    return dict_list