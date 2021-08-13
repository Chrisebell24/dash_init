def create_download_link_from_pd_df(df, index=False, header=True):
  csv_string = df.to_csv(index=index, encoding='utf-8', header=header)
  return "data:text/csv;charset=utf-8,"+csv_string      
