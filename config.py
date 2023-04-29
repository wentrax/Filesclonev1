import os
import logging

class Config:
    
    API_ID = 7961171
    API_HASH = "b2d798626afaf5f1e4bdb33988e3d377"
    BOT_TOKEN = "5852172455:AAEkw9wLRP1d0SJkOaVlwU9MOiJOzrPkAnE"
    BOT_SESSION = "bot" 
    CAPTION = "@HQFilms4U"
    FROM_CHANNEL = "@llmovie_backup"
    FILTER_TYPE = "document"
    OWNER_ID = "1533128706"
    SESSION = "AgBhYhxp4jWuWmEleNXw6R6YXmljsqXg8g63ivSDFF3X-faEBIQ-f4Xgn2xRwqqQLzIorFAPXS0kEm-9Ir3GirIN8-Z2ZD1sMvZuulFzZz6L2zwrZ7fLbZSzx4_JlynyoRba39ZkvrKuIjdWUD3bxj-judNSt3dNy45poY289HkCeEYaAWiNnjit7iMHtDQiMVxCoF8HiNzKMUMm9xKej9Y2gjWhap_xA5V6LPSiDFByNEN_skvszLvi-FcywHNCOxbNOYokT6t09KpJcudsD13bnbrzd5mRbaPycbUod_tZIQ5MvbFO88_AM3MEfiVmXa-wPUNa2PcCuGPCILy3A9Q8AAAAATPH6AEA"
    TO_CHANNEL = -1001506021749
def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
