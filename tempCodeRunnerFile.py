o adjust column width to fit content
for adjust_each_column in ws["1"]:
    ws.column_dimensions[adjust_each_column.column_letter].width=get_maximin_width(adjust_each_column.column_letter)
    