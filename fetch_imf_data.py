# documentation: https://datasupport.imf.org/knowledge?sys_kb_id=b849dc6b47294ad8805d07c4f16d4311&id=kb_article_view&sysparm_rank=1&sysparm_tsqueryId=bf8c5b1293ede6106f7e30747aba109f

import sdmx

 
IMF_DATA = sdmx.Client('IMF_DATA')

data_msg = IMF_DATA.data('CPI', key='USA+CAN.CPI.CP01.IX.M', params={'startPeriod': 2018})

cpi_df = sdmx.to_pandas(data_msg)
print(cpi_df.head())
print(cpi_df.tail())
