from pyopenms import MzMLFile, MSExperiment
import os
import pandas as pd
import click

CONTEXT_SETTINGS = dict(help_option_names=["-h", "--help"])
@click.group(context_settings=CONTEXT_SETTINGS)
def cli():
    pass

@click.command("mzml_dataframe")
@click.option("--mzml_folder", "-d")
@click.pass_context
    

def mzml_dataframe(ctx, mzml_folder):

    file_columns = ['File_Name', 'SpectrumID', 'MSLevel', 'Charge', 'MS2_peaks', 'Base_Peak_Intensity']
    mzml_df = pd.DataFrame(columns = file_columns)
    mzml_paths = list(i for i in os.listdir(mzml_folder))
    
    def parse_mzml(file_name, file_columns):
        info = []
        exp = MSExperiment()
        MzMLFile().load(file_name, exp)
        for i in exp:
            name = os.path.split(file_name)[1]
            id = i.getNativeID()
            if i.getMSLevel() == 2:
                charge_state = i.getPrecursors()[0].getCharge()
                info_list = [name, id, 2, charge_state, len(i.get_peaks()[0]), i.getMetaValue("base peak intensity")]
            else:
                info_list = [name, id, i.getMSLevel(), 'null', 'null', 'null']

            info.append(info_list)

        return pd.DataFrame(info, columns = file_columns)
    
    
    for i in mzml_paths:
        mzml_df = pd.concat([mzml_df, parse_mzml(mzml_folder + i, file_columns)])
    
    mzml_df.to_csv('mzml_info.csv', sep=',', index = False, header = True)



cli.add_command(mzml_dataframe)

if __name__ == "__main__":
    cli()
