from future.types import newdict


def create_dict_from_lists(keys, values):
    """
    This function returns a dict made from two lists.
    """
    new_dict = dict(zip(keys, values))
    return new_dict

def merge_two_dicts(d1, d2):
    """
    Merge two Python dictionaries into one
    """
    d1.update(d2)  #update modifies one dict by adding or updating key-value pairs from another dict
    return d1

def init_dict_with_values(lst, d1):
    """
    Create a dict with default values for each key listed.

    new_dict = dict.fromkeys(lst, d1) if using this method the second
    value need to be immutable or empty or there will be problems.
    """
    new_dict = dict.fromkeys(lst, d1)
    return new_dict

def extract_keys_to_dict(datadict, keylist):
    """
    Create a dictionary by extracting the keylist from a given dictionary
    """
    return {kl: datadict[kl] for kl in keylist}


def delete_keys_from_dict(datadict, keylist):
    """
    Delete a list of keys from a dictionary
    """
    for i in keylist:
        datadict.pop(i, None)
    return datadict

def check_dict_for_key(datadict, key):
    """
    Check if a value exists in a dictionary
    (NO FOR loops!)
    """
    pass

def get_key_of_min_value(ddd):
    """
    Get the key of the minimum value from a dictionary
    """
    pass

def get_key_of_max_value(ddd):
    """
    Get the key of the maximum value from a dictionary
    """
    pass