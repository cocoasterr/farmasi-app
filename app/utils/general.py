from fastapi import (HTTPException, status)

def exception_message(e):
    message = e
    if isinstance(e, HTTPException):
        message = e.detail
    raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                        detail=f'Failed! {message}')
async def general_response(
        status: str,
        data: list = [],
        total: int = 0,
        current_page: int = 1) -> dict:
    """
    helping all function response

    Args:
        status (str): status code
        data (list): data
        total (int, optional): total data from database. Defaults to 0.
        current_page (int, optional): page pagination. Defaults to 1.
        message (str, optional): response message. Defaults to None.

    Returns:
        dict: dict {status, data, message, total, and current_pag}
    """
    res = {
        "status": status,
        "data" : [],
    }
    if data:
        res['data'] = data
    if total:
        res['total'] = total
    if current_page:
        res['current_page'] = current_page
    return res
