import PySimpleGUI as sg
import pandas as pd


def table_example():
    sg.set_options(auto_size_buttons=True)
    name_of_file = sg.popup_get_file(
        'filename to open', no_window=True, file_types=(("CSV Files", "*.csv"),))
    if name_of_file == '':
        return

    data = []
    header_list = []
    button = sg.popup_ok('Do you wish to continue?')

    if name_of_file is not None:
        try:
            df = pd.read_csv(name_of_file, sep=',', engine='python', header=None)
            data = df.values.tolist()
            if button == 'OK':
                header_list = df.iloc[0].tolist()
                data = df[1:].values.tolist()
        except:
            sg.popup_error('Error reading file')
            return

    layout = [
        [sg.Table(values=data,
                  headings=header_list,
                  display_row_numbers=True,
                  auto_size_columns=False,
                  num_rows=min(40, len(data)))]
    ]

    window = sg.Window('Table', layout, grab_anywhere=False)
    _, values = window.read()
    window.close()


table_example()
