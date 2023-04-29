import os
import logging

class Config:
    
    API_ID = 7961171
    API_HASH = "b2d798626afaf5f1e4bdb33988e3d377"
    BOT_TOKEN = "5999015933:AAGtX7pTHSRd413HWUsH4zApx41Grsn5LCA"
    BOT_SESSION = "bot" 
    CAPTION = "@HQFilms4U"
    FROM_CHANNEL = -1001739094949
    FILTER_TYPE = "document"
    OWNER_ID = "1533128706"
    SESSION = "AgAhksdbWyZWg0c7gJrBQCdr_pv40Kr11hG82925DPQQ4sso9H4nQDTWbnIsxDaf_kFuK3VULwLjOPL7h-dF5abqNLSii1vFB-O8izutF7VIg6HAc77no2HrHRQDj5V9IWFND6_gTJndGS4nagfJWTM_9ixHh8O3i0bKs2QBj3r9iMe7jOv3TUaRfA-sdowvPckdyGLTbchbWReJHfI7EQW1jgGi4Xzfx9vwsPkF8yOkUhqFpZywfLfwpxhishz51ykc_y9nDrkPP2QmQ45CgtdDhEl-nt5n3xOapdfgDl1n9qKXUbiQtzbKtUGCgrlJhIeFIpxVHsf9Z1dnOS_FdajvAAAAATPH6AEA"
    TO_CHANNEL = -1001506021749
def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
