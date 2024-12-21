# 1. Preprocessing Data


```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
```


```python
file_path = r"C:\Users\Darryl\Documents\File Materi Binus\BOOTCAMP DATA ANALYTICS BINUS\Capston Data Analitycs\online_retail(in).csv"
df = pd.read_csv(file_path)
```


```python
df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>InvoiceNo</th>
      <th>StockCode</th>
      <th>Description</th>
      <th>Quantity</th>
      <th>InvoiceDate</th>
      <th>UnitPrice</th>
      <th>CustomerID</th>
      <th>Country</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>536365</td>
      <td>85123A</td>
      <td>WHITE HANGING HEART T-LIGHT HOLDER</td>
      <td>6</td>
      <td>12/1/2010 8:26</td>
      <td>2.55</td>
      <td>17850.0</td>
      <td>United Kingdom</td>
    </tr>
    <tr>
      <th>1</th>
      <td>536365</td>
      <td>71053</td>
      <td>WHITE METAL LANTERN</td>
      <td>6</td>
      <td>12/1/2010 8:26</td>
      <td>3.39</td>
      <td>17850.0</td>
      <td>United Kingdom</td>
    </tr>
    <tr>
      <th>2</th>
      <td>536365</td>
      <td>84406B</td>
      <td>CREAM CUPID HEARTS COAT HANGER</td>
      <td>8</td>
      <td>12/1/2010 8:26</td>
      <td>2.75</td>
      <td>17850.0</td>
      <td>United Kingdom</td>
    </tr>
    <tr>
      <th>3</th>
      <td>536365</td>
      <td>84029G</td>
      <td>KNITTED UNION FLAG HOT WATER BOTTLE</td>
      <td>6</td>
      <td>12/1/2010 8:26</td>
      <td>3.39</td>
      <td>17850.0</td>
      <td>United Kingdom</td>
    </tr>
    <tr>
      <th>4</th>
      <td>536365</td>
      <td>84029E</td>
      <td>RED WOOLLY HOTTIE WHITE HEART.</td>
      <td>6</td>
      <td>12/1/2010 8:26</td>
      <td>3.39</td>
      <td>17850.0</td>
      <td>United Kingdom</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.info()
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 541909 entries, 0 to 541908
    Data columns (total 8 columns):
     #   Column       Non-Null Count   Dtype  
    ---  ------       --------------   -----  
     0   InvoiceNo    541909 non-null  object 
     1   StockCode    541909 non-null  object 
     2   Description  540455 non-null  object 
     3   Quantity     541909 non-null  int64  
     4   InvoiceDate  541909 non-null  object 
     5   UnitPrice    541909 non-null  float64
     6   CustomerID   406829 non-null  float64
     7   Country      541909 non-null  object 
    dtypes: float64(2), int64(1), object(5)
    memory usage: 33.1+ MB
    


```python
df.drop(columns=["index"], inplace=True)
```


```python
df_cleaned = df.dropna(subset=["CustomerID"])
```


```python
df_cleaned.loc[:, "InvoiceDate"] = pd.to_datetime(df_cleaned["InvoiceDate"])
df_cleaned = df_cleaned[(df_cleaned["Quantity"] > 0) & (df_cleaned["UnitPrice"] > 0)]
df_cleaned.loc[:, "TotalPrice"] = df_cleaned["Quantity"] * df_cleaned["UnitPrice"]
```


```python
df_cleaned.info()
```

    <class 'pandas.core.frame.DataFrame'>
    Index: 397884 entries, 0 to 541908
    Data columns (total 9 columns):
     #   Column       Non-Null Count   Dtype  
    ---  ------       --------------   -----  
     0   InvoiceNo    397884 non-null  object 
     1   StockCode    397884 non-null  object 
     2   Description  397884 non-null  object 
     3   Quantity     397884 non-null  int64  
     4   InvoiceDate  397884 non-null  object 
     5   UnitPrice    397884 non-null  float64
     6   CustomerID   397884 non-null  float64
     7   Country      397884 non-null  object 
     8   TotalPrice   397884 non-null  float64
    dtypes: float64(3), int64(1), object(5)
    memory usage: 30.4+ MB
    

# 2. Analisis Eksploratif dan Statistik Deskriptif


```python
print(df_cleaned.describe())
```

                Quantity      UnitPrice     CustomerID     TotalPrice
    count  397884.000000  397884.000000  397884.000000  397884.000000
    mean       12.988238       3.116488   15294.423453      22.397000
    std       179.331775      22.097877    1713.141560     309.071041
    min         1.000000       0.001000   12346.000000       0.001000
    25%         2.000000       1.250000   13969.000000       4.680000
    50%         6.000000       1.950000   15159.000000      11.800000
    75%        12.000000       3.750000   16795.000000      19.800000
    max     80995.000000    8142.750000   18287.000000  168469.600000
    


```python
plt.figure()
```




    <Figure size 640x480 with 0 Axes>




    <Figure size 640x480 with 0 Axes>



```python
plt.figure(figsize=(8, 5))
sns.histplot(df_cleaned["TotalPrice"], bins=50, color="green")
```




    <Axes: xlabel='TotalPrice', ylabel='Count'>




    
![png](IT%20Data%20Analytics%20Bootcamp%20Capstone%20Project%20Data%20Visualization_files/IT%20Data%20Analytics%20Bootcamp%20Capstone%20Project%20Data%20Visualization_12_1.png)
    



```python
plt.figure(figsize=(8, 5))
sns.histplot(df_cleaned["TotalPrice"], bins=50, color="green")
plt.title("Distribusi total Harga Transaksi")
plt.xlabel("TotalHarga")
plt.ylabel("Frekuensi")
plt.show()
```


    
![png](IT%20Data%20Analytics%20Bootcamp%20Capstone%20Project%20Data%20Visualization_files/IT%20Data%20Analytics%20Bootcamp%20Capstone%20Project%20Data%20Visualization_13_0.png)
    


# 3. Visualisasi Data


```python
df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>InvoiceNo</th>
      <th>StockCode</th>
      <th>Description</th>
      <th>Quantity</th>
      <th>InvoiceDate</th>
      <th>UnitPrice</th>
      <th>CustomerID</th>
      <th>Country</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>536365</td>
      <td>85123A</td>
      <td>WHITE HANGING HEART T-LIGHT HOLDER</td>
      <td>6</td>
      <td>12/1/2010 8:26</td>
      <td>2.55</td>
      <td>17850.0</td>
      <td>United Kingdom</td>
    </tr>
    <tr>
      <th>1</th>
      <td>536365</td>
      <td>71053</td>
      <td>WHITE METAL LANTERN</td>
      <td>6</td>
      <td>12/1/2010 8:26</td>
      <td>3.39</td>
      <td>17850.0</td>
      <td>United Kingdom</td>
    </tr>
    <tr>
      <th>2</th>
      <td>536365</td>
      <td>84406B</td>
      <td>CREAM CUPID HEARTS COAT HANGER</td>
      <td>8</td>
      <td>12/1/2010 8:26</td>
      <td>2.75</td>
      <td>17850.0</td>
      <td>United Kingdom</td>
    </tr>
    <tr>
      <th>3</th>
      <td>536365</td>
      <td>84029G</td>
      <td>KNITTED UNION FLAG HOT WATER BOTTLE</td>
      <td>6</td>
      <td>12/1/2010 8:26</td>
      <td>3.39</td>
      <td>17850.0</td>
      <td>United Kingdom</td>
    </tr>
    <tr>
      <th>4</th>
      <td>536365</td>
      <td>84029E</td>
      <td>RED WOOLLY HOTTIE WHITE HEART.</td>
      <td>6</td>
      <td>12/1/2010 8:26</td>
      <td>3.39</td>
      <td>17850.0</td>
      <td>United Kingdom</td>
    </tr>
  </tbody>
</table>
</div>




```python
# a. Tren Penjualan
df_cleaned["InvoiceDate"] = pd.to_datetime(df_cleaned["InvoiceDate"], errors='coerce')
print(df_cleaned["InvoiceDate"].dtype)
df_cleaned["YearMonth"] = df_cleaned["InvoiceDate"].dt.to_period("M")
sales_trend = df_cleaned.groupby("YearMonth")["TotalPrice"].sum()
```

    datetime64[ns]
    


```python
plt.figure()
```




    <Figure size 640x480 with 0 Axes>




    <Figure size 640x480 with 0 Axes>



```python
plt.figure(figsize=(12, 6))
sales_trend.plot(kind="line", marker="o", color="green", markerfacecolor="yellow")
plt.title("Tren Penjualan Bulanan")
plt.xlabel("Bulan-Tahun")
plt.ylabel("Total Pendapatan")
plt.grid(True)
plt.show()
```


    
![png](IT%20Data%20Analytics%20Bootcamp%20Capstone%20Project%20Data%20Visualization_files/IT%20Data%20Analytics%20Bootcamp%20Capstone%20Project%20Data%20Visualization_18_0.png)
    



```python
# b. Distribusi Berdasarkan Negara
sales_by_country = df_cleaned.groupby("Country")["TotalPrice"].sum().sort_values(ascending=False).head(20)
```


```python
plt.figure(figsize=(12, 6))
sales_by_country.plot(kind="bar", color="green")
plt.title("Distribusi Penjualan Berdasarkan Negara")
plt.xlabel("Negara")
plt.ylabel("Total Pendapatan")
plt.xticks(rotation=45)
plt.show()
```


    
![png](IT%20Data%20Analytics%20Bootcamp%20Capstone%20Project%20Data%20Visualization_files/IT%20Data%20Analytics%20Bootcamp%20Capstone%20Project%20Data%20Visualization_20_0.png)
    



```python
# c. Analisis Produk

# Produk Terlaris di Pasaran
top_products = df_cleaned.groupby("Description")["Quantity"].sum().sort_values(ascending=False).head(20)
```


```python
plt.figure(figsize=(12, 6))
top_products.plot(kind="bar", color="green")
plt.title("Produk Terlaris")
plt.xlabel("Deskripsi Produk")
plt.ylabel("Jumlah Terjual")
plt.xticks(rotation=45, ha="right")
plt.show()
```


    
![png](IT%20Data%20Analytics%20Bootcamp%20Capstone%20Project%20Data%20Visualization_files/IT%20Data%20Analytics%20Bootcamp%20Capstone%20Project%20Data%20Visualization_22_0.png)
    



```python
# Produk Kurang Laris di Pasaran
least_products = df_cleaned.groupby("Description")["Quantity"].sum().sort_values(ascending=True).head(20)
```


```python
plt.figure(figsize=(12, 6))
least_products.plot(kind="bar", color="red")
plt.title("Produk Kurang Laris")
plt.xlabel("Deskripsi Produk")
plt.ylabel("Jumlah Terjual")
plt.xticks(rotation=45, ha="right")
plt.show()
```


    
![png](IT%20Data%20Analytics%20Bootcamp%20Capstone%20Project%20Data%20Visualization_files/IT%20Data%20Analytics%20Bootcamp%20Capstone%20Project%20Data%20Visualization_24_0.png)
    



```python
# d. Analisis Pelanggan
customer_by_country = df_cleaned.groupby("Country")["CustomerID"].nunique().sort_values(ascending=False).head(20)
```


```python
plt.figure(figsize=(12, 6))
customer_by_country.plot(kind="bar", color="blue")
plt.title("Distribusi Pelanggan Berdasarkan Negara")
plt.xlabel("Negara")
plt.ylabel("Jumlah Pelanggan Unik")
plt.xticks(rotation=45)
plt.show()
```


    
![png](IT%20Data%20Analytics%20Bootcamp%20Capstone%20Project%20Data%20Visualization_files/IT%20Data%20Analytics%20Bootcamp%20Capstone%20Project%20Data%20Visualization_26_0.png)
    



```python
# Pelanggan Berdasarkan Pengeluaran
customer_analysis = df_cleaned.groupby("CustomerID")["TotalPrice"].sum().sort_values(ascending=False).head(20)
```


```python
plt.figure(figsize=(12, 6))
customer_analysis.plot(kind="bar", color="purple")
plt.title("Pelanggan Berdasarkan Total Pengeluaran")
plt.xlabel("Customer ID")
plt.ylabel("Total Pengeluaran")
plt.xticks(rotation=45)
plt.show()
```


    
![png](IT%20Data%20Analytics%20Bootcamp%20Capstone%20Project%20Data%20Visualization_files/IT%20Data%20Analytics%20Bootcamp%20Capstone%20Project%20Data%20Visualization_28_0.png)
    



```python
# e. Korelasi dan Hubungan
plt.figure(figsize=(8, 5))
sns.scatterplot(data=df_cleaned, x="UnitPrice", y="Quantity", alpha=1)
plt.title("Korelasi Harga dan Kuantitas")
plt.xlabel("Harga per Unit")
plt.ylabel("Kuantitas Terjual")
plt.grid(True)
plt.show()
```


    
![png](IT%20Data%20Analytics%20Bootcamp%20Capstone%20Project%20Data%20Visualization_files/IT%20Data%20Analytics%20Bootcamp%20Capstone%20Project%20Data%20Visualization_29_0.png)
    



```python
!jupyter nbconvert --to markdown --TemplateExporter.exclude_input_prompt=True"IT Data Analytics Bootcamp Capstone Project Data Visualization.ipynb"
```

    This application is used to convert notebook files (*.ipynb)
            to various other formats.
    
            WARNING: THE COMMANDLINE INTERFACE MAY CHANGE IN FUTURE RELEASES.
    
    Options
    =======
    The options below are convenience aliases to configurable class-options,
    as listed in the "Equivalent to" description-line of the aliases.
    To see all configurable class-options for some <cmd>, use:
        <cmd> --help-all
    
    --debug
        set log level to logging.DEBUG (maximize logging output)
        Equivalent to: [--Application.log_level=10]
    --show-config
        Show the application's configuration (human-readable format)
        Equivalent to: [--Application.show_config=True]
    --show-config-json
        Show the application's configuration (json format)
        Equivalent to: [--Application.show_config_json=True]
    --generate-config
        generate default config file
        Equivalent to: [--JupyterApp.generate_config=True]
    -y
        Answer yes to any questions instead of prompting.
        Equivalent to: [--JupyterApp.answer_yes=True]
    --execute
        Execute the notebook prior to export.
        Equivalent to: [--ExecutePreprocessor.enabled=True]
    --allow-errors
        Continue notebook execution even if one of the cells throws an error and include the error message in the cell output (the default behaviour is to abort conversion). This flag is only relevant if '--execute' was specified, too.
        Equivalent to: [--ExecutePreprocessor.allow_errors=True]
    --stdin
        read a single notebook file from stdin. Write the resulting notebook with default basename 'notebook.*'
        Equivalent to: [--NbConvertApp.from_stdin=True]
    --stdout
        Write notebook output to stdout instead of files.
        Equivalent to: [--NbConvertApp.writer_class=StdoutWriter]
    --inplace
        Run nbconvert in place, overwriting the existing notebook (only
                relevant when converting to notebook format)
        Equivalent to: [--NbConvertApp.use_output_suffix=False --NbConvertApp.export_format=notebook --FilesWriter.build_directory=]
    --clear-output
        Clear output of current file and save in place,
                overwriting the existing notebook.
        Equivalent to: [--NbConvertApp.use_output_suffix=False --NbConvertApp.export_format=notebook --FilesWriter.build_directory= --ClearOutputPreprocessor.enabled=True]
    --coalesce-streams
        Coalesce consecutive stdout and stderr outputs into one stream (within each cell).
        Equivalent to: [--NbConvertApp.use_output_suffix=False --NbConvertApp.export_format=notebook --FilesWriter.build_directory= --CoalesceStreamsPreprocessor.enabled=True]
    --no-prompt
        Exclude input and output prompts from converted document.
        Equivalent to: [--TemplateExporter.exclude_input_prompt=True --TemplateExporter.exclude_output_prompt=True]
    --no-input
        Exclude input cells and output prompts from converted document.
                This mode is ideal for generating code-free reports.
        Equivalent to: [--TemplateExporter.exclude_output_prompt=True --TemplateExporter.exclude_input=True --TemplateExporter.exclude_input_prompt=True]
    --allow-chromium-download
        Whether to allow downloading chromium if no suitable version is found on the system.
        Equivalent to: [--WebPDFExporter.allow_chromium_download=True]
    --disable-chromium-sandbox
        Disable chromium security sandbox when converting to PDF..
        Equivalent to: [--WebPDFExporter.disable_sandbox=True]
    --show-input
        Shows code input. This flag is only useful for dejavu users.
        Equivalent to: [--TemplateExporter.exclude_input=False]
    --embed-images
        Embed the images as base64 dataurls in the output. This flag is only useful for the HTML/WebPDF/Slides exports.
        Equivalent to: [--HTMLExporter.embed_images=True]
    --sanitize-html
        Whether the HTML in Markdown cells and cell outputs should be sanitized..
        Equivalent to: [--HTMLExporter.sanitize_html=True]
    --log-level=<Enum>
        Set the log level by value or name.
        Choices: any of [0, 10, 20, 30, 40, 50, 'DEBUG', 'INFO', 'WARN', 'ERROR', 'CRITICAL']
        Default: 30
        Equivalent to: [--Application.log_level]
    --config=<Unicode>
        Full path of a config file.
        Default: ''
        Equivalent to: [--JupyterApp.config_file]
    --to=<Unicode>
        The export format to be used, either one of the built-in formats
                ['asciidoc', 'custom', 'html', 'latex', 'markdown', 'notebook', 'pdf', 'python', 'qtpdf', 'qtpng', 'rst', 'script', 'slides', 'webpdf']
                or a dotted object name that represents the import path for an
                ``Exporter`` class
        Default: ''
        Equivalent to: [--NbConvertApp.export_format]
    --template=<Unicode>
        Name of the template to use
        Default: ''
        Equivalent to: [--TemplateExporter.template_name]
    --template-file=<Unicode>
        Name of the template file to use
        Default: None
        Equivalent to: [--TemplateExporter.template_file]
    --theme=<Unicode>
        Template specific theme(e.g. the name of a JupyterLab CSS theme distributed
        as prebuilt extension for the lab template)
        Default: 'light'
        Equivalent to: [--HTMLExporter.theme]
    --sanitize_html=<Bool>
        Whether the HTML in Markdown cells and cell outputs should be sanitized.This
        should be set to True by nbviewer or similar tools.
        Default: False
        Equivalent to: [--HTMLExporter.sanitize_html]
    --writer=<DottedObjectName>
        Writer class used to write the
                                            results of the conversion
        Default: 'FilesWriter'
        Equivalent to: [--NbConvertApp.writer_class]
    --post=<DottedOrNone>
        PostProcessor class used to write the
                                            results of the conversion
        Default: ''
        Equivalent to: [--NbConvertApp.postprocessor_class]
    --output=<Unicode>
        Overwrite base name use for output files.
                    Supports pattern replacements '{notebook_name}'.
        Default: '{notebook_name}'
        Equivalent to: [--NbConvertApp.output_base]
    --output-dir=<Unicode>
        Directory to write output(s) to. Defaults
                                      to output to the directory of each notebook. To recover
                                      previous default behaviour (outputting to the current
                                      working directory) use . as the flag value.
        Default: ''
        Equivalent to: [--FilesWriter.build_directory]
    --reveal-prefix=<Unicode>
        The URL prefix for reveal.js (version 3.x).
                This defaults to the reveal CDN, but can be any url pointing to a copy
                of reveal.js.
                For speaker notes to work, this must be a relative path to a local
                copy of reveal.js: e.g., "reveal.js".
                If a relative path is given, it must be a subdirectory of the
                current directory (from which the server is run).
                See the usage documentation
                (https://nbconvert.readthedocs.io/en/latest/usage.html#reveal-js-html-slideshow)
                for more details.
        Default: ''
        Equivalent to: [--SlidesExporter.reveal_url_prefix]
    --nbformat=<Enum>
        The nbformat version to write.
                Use this to downgrade notebooks.
        Choices: any of [1, 2, 3, 4]
        Default: 4
        Equivalent to: [--NotebookExporter.nbformat_version]
    
    Examples
    --------
    
        The simplest way to use nbconvert is
    
                > jupyter nbconvert mynotebook.ipynb --to html
    
                Options include ['asciidoc', 'custom', 'html', 'latex', 'markdown', 'notebook', 'pdf', 'python', 'qtpdf', 'qtpng', 'rst', 'script', 'slides', 'webpdf'].
    
                > jupyter nbconvert --to latex mynotebook.ipynb
    
                Both HTML and LaTeX support multiple output templates. LaTeX includes
                'base', 'article' and 'report'.  HTML includes 'basic', 'lab' and
                'classic'. You can specify the flavor of the format used.
    
                > jupyter nbconvert --to html --template lab mynotebook.ipynb
    
                You can also pipe the output to stdout, rather than a file
    
                > jupyter nbconvert mynotebook.ipynb --stdout
    
                PDF is generated via latex
    
                > jupyter nbconvert mynotebook.ipynb --to pdf
    
                You can get (and serve) a Reveal.js-powered slideshow
    
                > jupyter nbconvert myslides.ipynb --to slides --post serve
    
                Multiple notebooks can be given at the command line in a couple of
                different ways:
    
                > jupyter nbconvert notebook*.ipynb
                > jupyter nbconvert notebook1.ipynb notebook2.ipynb
    
                or you can specify the notebooks list in a config file, containing::
    
                    c.NbConvertApp.notebooks = ["my_notebook.ipynb"]
    
                > jupyter nbconvert --config mycfg.py
    
    To see all available configurables, use `--help-all`.
    
    


```python

```
