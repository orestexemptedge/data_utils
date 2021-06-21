def phone_split(df, phone='phone', main='phone_main', ext='phone_ext'):
    """this function sanitizes phone numbers and appends any digits beyond 10 to a separate column"""
    df[phone].replace(to_replace='[^0-9]+', value='', inplace=True, regex=True)
    df[main] = df[phone].str[:10]
    df[ext] = df[phone].str[11:]
    df.drop(phone, axis=1, inplace=True)

def clean_col(name):
    """this function cleans clean column name and replaces empty spaces with underscores"""
    return (
      name.strip().lower().replace(" ", "_")
  )

def unique_dataframe(df):
    """this function creates a dataframe with only unique values in each column"""
    dict(zip([i for i in df.columns], [pd.DataFrame(df[i].unique(), columns=[i]) for i in df.columns]))

def trim_all_columns(df):
    """this function trims whitespaces from ends of each value across all series in dataframe"""
    trim_strings = lambda x: x.strip() if isinstance(x, str) else x
    return df.applymap(trim_strings)

def generate_temp_id(row, secondary_keys, drop_empty_values=True):
    """this function generates a temp_id by passing desired columns into secondary_keys value"""
    sec_key_column_values = []
    for key in secondary_keys:
        val = str(row[key])

        if drop_empty_values:
            if val.strip() != '':
                sec_key_column_values.append(val.strip())
        else:
            sec_key_column_values.append(val.strip())
    temp_id = '-'.join(sec_key_column_values)
    return temp_id