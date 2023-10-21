def drugEntity(drug: dict) -> dict:
    """maping value from database
    Args:
        drug (dict): entity schema
    Returns:
        dict: get field database
    """
    return {
        "id": drug.id,
        "name": drug.name,
        "stock": drug.stock,
        "receipt": drug.receipt,
        "created_at": drug.created_at,
        "updated_at": drug.updated_at,
    }


def drugListEntity(drug_list: list) -> list:
    """response when data need to mapping is morethan one
    Args:
        drug_list (list): list entities schema
    Returns:
        list: get list field from database
    """
    return [drugEntity(drug) for drug in drug_list]
