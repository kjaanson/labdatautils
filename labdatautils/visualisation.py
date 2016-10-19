import ipywidgets as widgets

def results_widget_tabs(dfs_dict):
    'Updates result tab widgets with new dataframes.'

    html_widgets = []
    for table in dfs_dict:
        df = dfs_dict[table]
        html_widgets.append(widgets.HTML(value=df.reset_index().style.set_table_attributes('class="table"').render()))

    tabs = widgets.Tab(children=html_widgets)
    for i, name in enumerate(dfs_dict):
        tabs.set_title(i, name)

    return tabs