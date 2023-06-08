def search_partner(custom_fields_values):
    for field in custom_fields_values:
        if field['field_id'] == 14987:
            return field['values'][0]['value']
