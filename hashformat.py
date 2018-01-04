# -*- coding: utf-8 -*-
__author__ = 'essepuntato'
import re


def process_hashformat(file_path):
    result = []

    with open(file_path, "rU") as f:
        first_field_name = None
        cur_object = None
        cur_field_name = None
        cur_field_content = None
        for line in f.readlines():
            cur_matching = re.search("^#([^\s]+)\s(.+)$", line, re.DOTALL)
            if cur_matching is not None:
                cur_field_name = cur_matching.group(1)
                cur_field_content = cur_matching.group(2)

                # If both the name and the content are defined, continue to process
                if cur_field_name and cur_field_content:
                    # Identify the separator key
                    if first_field_name is None:
                        first_field_name = cur_field_name

                    # If the current field is equal to the separator key,
                    # then create a new object
                    if cur_field_name == first_field_name:
                        # If there is an already defined object, add it to the
                        # final result
                        if cur_object is not None:
                            result += [cur_object]
                        cur_object = {}

                    # Add the new key to the object
                    cur_object[cur_field_name] = cur_field_content
            elif cur_object is not None and len(cur_object) > 0:
                cur_object[cur_field_name] += line

        # Insert the last object in the result
        if cur_object is not None and len(cur_object) > 0:
            result += [cur_object]

    # Clean the final \n
    for item in result:
        for key in item:
            item[key] = item[key].rstrip()

    return result