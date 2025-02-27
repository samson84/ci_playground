def validate_animal_data(data):
    if not data:
        return "No input data provided"

    required_fields = ['name', 'species', 'habitat']
    for field in required_fields:
        if field not in data:
            return f"Missing field: {field}"

    return None
