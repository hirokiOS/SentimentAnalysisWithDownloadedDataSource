from accern_data import create_data_client
import pandas as pd
import accern_data
import os
# this module is intended for third party use of accern_data module
# please also refer to  https://pypi.org/project/accern-data/

def DFConcatenator(url='< Ask the vendor or author for the web source >', 
                        token='< Ask the vendor or author for the web source >', 
                        start_date="2022-05-01", end_date="2022-05-02", 
                        output_pattern="oct31", output_path="./accern_raw_json/", 
                        mode = "json", split_dates=False):
    # arguments are as follows
    # start_date = "2022-05-01" #Define Historical Date Range
    # end_date = "2022-05-02"
    # output_pattern = "oct30"    # Mandatory in case of (csv/df, False)
    # output_path = "./accern_raw_json/" #Define filepath
    # url : vendor provided url
    # token : vender provided token
    # mode can be either "json" or "csv/df"
    # split_dates effective if you are exporting as csv when mode is "csv/df"
 
    # Creating the client using user credentials
    client = create_data_client(
        url=url,
        token=token,
        indicator="message")
    
    # Setting up the mode.
    client.set_mode(mode=mode, split_dates=split_dates)
    
   
    # Progress bar
    client.download_range(
        start_date=start_date,
        output_path=output_path,               # By default: current working directory.
        output_pattern= output_pattern,
        end_date=end_date)              
    
    # By default: None (In that case data will get downloaded for start_date only.)
    
    
    main_json = []
    for fname in os.listdir(output_path):
        if fname.startswith(output_pattern) and fname.endswith(".json") and (fname.split('.')[-2][-10:] <= end_date) and  (fname.split('.')[-2][-10:] >= start_date):
            print("Processing JSON file:", fname)
            fpath = os.path.join(output_path, fname)
            main_json.append(pd.read_json(fpath))
    
    df = pd.concat(main_json).reset_index(drop=True)
    df.to_json(os.path.join(output_path, output_pattern+".json"), orient="records")

    return df