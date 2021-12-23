# Program that converts nested dictionary into its dot notation counterpart

dict_notation = {} # Assume here is the original dictionary
result = {}  # Where result is stored
initial_str, separator = "", "."


def dot_notation_recursive(prefix, dict_to_process):
    for key in dict_to_process:
        concated = prefix + separator + key if prefix != initial_str else key
        if isinstance(dict_to_process[key], dict):
            dot_notation_recursive(concated, dict_to_process[key])
        else:
            result[concated] = dict_to_process[key]


dot_notation_recursive(initial_str, dict_notation)



