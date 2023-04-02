# DSCI550 Team 7 - Homework 2: Large Scale Social Media Extraction and Analysis for Pixstory

https://github.com/egunadi/dsci550-hw-extract

See intro section of our report for overview of project.

## Dependencies

```
name: python37
channels:
  - conda-forge
  - defaults
dependencies:
  - alabaster=0.7.12=py37_0
  - anyio=3.5.0=py37hecd8cb5_0
  - applaunchservices=0.3.0=pyhd8ed1ab_2
  - appnope=0.1.2=py37hecd8cb5_1001
  - argon2-cffi=21.3.0=pyhd3eb1b0_0
  - argon2-cffi-bindings=21.2.0=py37hca72f7f_0
  - arrow=1.2.3=pyhd8ed1ab_0
  - astroid=2.14.2=py37hecd8cb5_0
  - atomicwrites=1.4.1=pyhd8ed1ab_0
  - attrs=22.1.0=py37hecd8cb5_0
  - autopep8=1.6.0=pyhd8ed1ab_1
  - babel=2.11.0=py37hecd8cb5_0
  - backcall=0.2.0=pyhd3eb1b0_0
  - beautifulsoup4=4.11.1=py37hecd8cb5_0
  - binaryornot=0.4.4=py_1
  - black=22.10.0=py37hf985489_1
  - blas=1.0=mkl
  - bleach=4.1.0=pyhd3eb1b0_0
  - bottleneck=1.3.5=py37h67323c0_0
  - brotli=1.0.9=hca72f7f_7
  - brotli-bin=1.0.9=hca72f7f_7
  - brotlipy=0.7.0=py37h9ed2024_1003
  - ca-certificates=2023.01.10=hecd8cb5_0
  - certifi=2022.12.7=py37hecd8cb5_0
  - cffi=1.15.1=py37h6c40b1e_3
  - chardet=4.0.0=py37hecd8cb5_1003
  - charset-normalizer=2.0.4=pyhd3eb1b0_0
  - click=8.1.3=py37hf985489_0
  - cloudpickle=2.0.0=pyhd3eb1b0_0
  - colorama=0.4.6=py37hecd8cb5_0
  - cookiecutter=2.1.1=pyh6c4a22f_0
  - cryptography=39.0.1=py37hf6deb26_0
  - cycler=0.11.0=pyhd3eb1b0_0
  - debugpy=1.5.1=py37he9d5cce_0
  - decorator=5.1.1=pyhd3eb1b0_0
  - defusedxml=0.7.1=pyhd3eb1b0_0
  - diff-match-patch=20200713=pyh9f0ad1d_0
  - dill=0.3.6=py37hecd8cb5_0
  - docutils=0.18.1=py37hecd8cb5_3
  - editdistance=0.6.1=py37hcec6c5f_0
  - entrypoints=0.4=py37hecd8cb5_0
  - fftw=3.3.9=h9ed2024_1
  - filelock=3.9.0=py37hecd8cb5_0
  - flake8=4.0.1=pyhd3eb1b0_1
  - flit-core=3.6.0=pyhd3eb1b0_0
  - fonttools=4.25.0=pyhd3eb1b0_0
  - freetype=2.12.1=hd8bbffd_0
  - future=0.18.3=py37hecd8cb5_0
  - gettext=0.21.0=h7535e17_0
  - giflib=5.2.1=h6c40b1e_3
  - glib=2.69.1=hfff2838_2
  - gst-plugins-base=1.14.1=hcec6c5f_1
  - gstreamer=1.14.1=h6c40b1e_1
  - huggingface_hub=0.10.1=py37hecd8cb5_0
  - icu=58.2=h0a44026_3
  - idna=3.4=py37hecd8cb5_0
  - imagesize=1.4.1=py37hecd8cb5_0
  - importlib_metadata=4.2.0=hd8ed1ab_0
  - importlib_resources=5.2.0=pyhd3eb1b0_1
  - inflection=0.5.1=pyh9f0ad1d_0
  - intel-openmp=2021.4.0=hecd8cb5_3538
  - intervaltree=3.0.2=py_0
  - ipykernel=6.15.2=py37hecd8cb5_0
  - ipython=7.31.1=py37hecd8cb5_1
  - ipython_genutils=0.2.0=pyhd3eb1b0_1
  - ipywidgets=7.6.5=pyhd3eb1b0_1
  - isort=5.9.3=pyhd3eb1b0_0
  - jedi=0.18.1=py37hecd8cb5_1
  - jellyfish=0.9.0=py37h69ee0a8_1
  - jinja2=3.1.2=py37hecd8cb5_0
  - jinja2-time=0.2.0=pyhd8ed1ab_3
  - joblib=1.1.1=py37hecd8cb5_0
  - jpeg=9e=h6c40b1e_1
  - json5=0.9.6=pyhd3eb1b0_0
  - jsonschema=4.17.3=py37hecd8cb5_0
  - jupyter=1.0.0=py37hecd8cb5_8
  - jupyter_client=7.4.9=py37hecd8cb5_0
  - jupyter_console=6.4.4=py37hecd8cb5_0
  - jupyter_core=4.11.2=py37hecd8cb5_0
  - jupyter_server=1.23.4=py37hecd8cb5_0
  - jupyterlab=3.5.3=py37hecd8cb5_0
  - jupyterlab_pygments=0.1.2=py_0
  - jupyterlab_server=2.15.2=pyhd8ed1ab_0
  - jupyterlab_widgets=1.0.0=pyhd3eb1b0_1
  - keyring=23.4.0=py37hecd8cb5_0
  - kiwisolver=1.4.4=py37hcec6c5f_0
  - krb5=1.19.4=hdba6334_0
  - lazy-object-proxy=1.6.0=py37h9ed2024_0
  - lcms2=2.12=hf1fd2bf_0
  - lerc=3.0=he9d5cce_0
  - libbrotlicommon=1.0.9=hca72f7f_7
  - libbrotlidec=1.0.9=hca72f7f_7
  - libbrotlienc=1.0.9=hca72f7f_7
  - libclang=12.0.0=default_hbc2896b_2
  - libcxx=14.0.6=h9765a3e_0
  - libdeflate=1.17=hb664fd8_0
  - libedit=3.1.20221030=h6c40b1e_0
  - libffi=3.4.2=hecd8cb5_6
  - libgfortran=5.0.0=11_3_0_hecd8cb5_28
  - libgfortran5=11.3.0=h9dfd629_28
  - libiconv=1.16=hca72f7f_2
  - libllvm12=12.0.0=h9b2ccf5_3
  - libopenblas=0.3.21=h54e7dc3_0
  - libpng=1.6.39=h6c40b1e_0
  - libpq=12.9=h1c9f633_3
  - libprotobuf=3.20.3=hfff2838_0
  - libsodium=1.0.18=h1de35cc_0
  - libspatialindex=1.9.3=he49afe7_4
  - libtiff=4.5.0=hcec6c5f_2
  - libuv=1.44.2=h6c40b1e_0
  - libwebp=1.2.4=hf6ce154_1
  - libwebp-base=1.2.4=h6c40b1e_1
  - libxml2=2.9.14=hbf8cd5e_0
  - libxslt=1.1.35=h5b33f42_0
  - llvm-openmp=14.0.6=h0dcd299_0
  - lxml=4.9.1=py37h65b224f_0
  - lz4-c=1.9.4=hcec6c5f_0
  - markupsafe=2.1.1=py37hca72f7f_0
  - matplotlib=3.5.1=py37hf985489_0
  - matplotlib-base=3.5.1=py37hfb0c5b7_1
  - matplotlib-inline=0.1.6=py37hecd8cb5_0
  - mccabe=0.7.0=pyhd3eb1b0_0
  - mistune=0.8.4=py37h1de35cc_0
  - mkl=2021.4.0=hecd8cb5_637
  - mkl-service=2.4.0=py37h9ed2024_0
  - mkl_fft=1.3.1=py37h4ab4a9b_0
  - mkl_random=1.2.2=py37hb2f4e1b_0
  - munkres=1.1.4=py_0
  - mypy_extensions=1.0.0=pyha770c72_0
  - nbclassic=0.5.2=py37hecd8cb5_0
  - nbclient=0.5.13=py37hecd8cb5_0
  - nbconvert=6.5.4=py37hecd8cb5_0
  - nbformat=5.7.0=py37hecd8cb5_0
  - ncurses=6.4=hcec6c5f_0
  - nest-asyncio=1.5.6=py37hecd8cb5_0
  - ninja=1.10.2=hecd8cb5_5
  - ninja-base=1.10.2=haf03e11_5
  - notebook=6.5.2=py37hecd8cb5_0
  - notebook-shim=0.2.2=py37hecd8cb5_0
  - nspr=4.33=he9d5cce_0
  - nss=3.74=h47edf6a_0
  - numexpr=2.8.4=py37he696674_0
  - numpy=1.21.5=py37h2e5f0a9_3
  - numpy-base=1.21.5=py37h3b1a694_3
  - numpydoc=1.5.0=pyhd8ed1ab_0
  - openssl=1.1.1t=hca72f7f_0
  - packaging=22.0=py37hecd8cb5_0
  - pandas=1.3.5=py37h743cdd8_0
  - pandocfilters=1.5.0=pyhd3eb1b0_0
  - parso=0.8.3=pyhd3eb1b0_0
  - pathspec=0.11.0=pyhd8ed1ab_0
  - pcre=8.45=h23ab428_0
  - pexpect=4.8.0=pyhd3eb1b0_3
  - pickleshare=0.7.5=pyhd3eb1b0_1003
  - pillow=9.4.0=py37hcec6c5f_0
  - pip=22.3.1=py37hecd8cb5_0
  - pkgutil-resolve-name=1.3.10=py37hecd8cb5_0
  - platformdirs=2.5.2=py37hecd8cb5_0
  - pluggy=1.0.0=py37hf985489_3
  - ply=3.11=py37_0
  - prometheus_client=0.14.1=py37hecd8cb5_0
  - prompt-toolkit=3.0.36=py37hecd8cb5_0
  - prompt_toolkit=3.0.36=hd3eb1b0_0
  - psutil=5.9.0=py37hca72f7f_0
  - ptyprocess=0.7.0=pyhd3eb1b0_2
  - pycodestyle=2.8.0=pyhd8ed1ab_0
  - pycparser=2.21=pyhd3eb1b0_0
  - pydocstyle=6.2.0=pyhd8ed1ab_0
  - pyflakes=2.4.0=pyhd8ed1ab_0
  - pygments=2.11.2=pyhd3eb1b0_0
  - pylint=2.16.2=py37hecd8cb5_0
  - pyls-spyder=0.4.0=pyhd8ed1ab_0
  - pyobjc-core=8.5.1=py37h11f76f7_0
  - pyobjc-framework-cocoa=8.5=py37h721a674_0
  - pyobjc-framework-coreservices=8.5=py37h994c40b_1
  - pyobjc-framework-fsevents=8.5=py37hf985489_1
  - pyopenssl=23.0.0=py37hecd8cb5_0
  - pyparsing=3.0.9=py37hecd8cb5_0
  - pyqt=5.15.7=py37he9d5cce_0
  - pyqt5-sip=12.11.0=py37he9d5cce_0
  - pyqtwebengine=5.15.7=py37he9d5cce_0
  - pyrsistent=0.18.0=py37hca72f7f_0
  - pysocks=1.7.1=py37hecd8cb5_0
  - python=3.7.16=h218abb5_0
  - python-dateutil=2.8.2=pyhd3eb1b0_0
  - python-fastjsonschema=2.16.2=py37hecd8cb5_0
  - python-lsp-black=1.2.1=pyhd8ed1ab_0
  - python-lsp-jsonrpc=1.0.0=pyhd8ed1ab_0
  - python-lsp-server=1.5.0=py37hecd8cb5_0
  - python-slugify=8.0.1=pyhd8ed1ab_0
  - python.app=3=py37hca72f7f_0
  - python_abi=3.7=2_cp37m
  - pytoolconfig=1.2.5=py37hecd8cb5_1
  - pytorch=1.12.1=cpu_py37h64f2f56_1
  - pytz=2022.7=py37hecd8cb5_0
  - pyyaml=6.0=py37h6c40b1e_1
  - pyzmq=23.2.0=py37he9d5cce_0
  - qdarkstyle=3.0.3=pyhd8ed1ab_0
  - qstylizer=0.2.2=pyhd8ed1ab_0
  - qt-main=5.15.2=h719ae48_7
  - qt-webengine=5.15.9=h90a370e_4
  - qtawesome=1.2.2=py37hecd8cb5_0
  - qtconsole=5.3.2=pyhd8ed1ab_0
  - qtconsole-base=5.3.2=pyha770c72_0
  - qtpy=2.2.0=py37hecd8cb5_0
  - qtwebkit=5.212=h24dc246_4
  - readline=8.2=hca72f7f_0
  - regex=2022.7.9=py37hca72f7f_0
  - requests=2.28.1=py37hecd8cb5_0
  - rope=1.7.0=py37hecd8cb5_0
  - rtree=1.0.1=py37hf13911c_0
  - scikit-learn=1.0.2=py37hae1ba45_1
  - scipy=1.7.3=py37h214d14d_2
  - seaborn=0.12.2=py37hecd8cb5_0
  - send2trash=1.8.0=pyhd3eb1b0_1
  - sip=6.6.2=py37he9d5cce_0
  - six=1.16.0=pyhd3eb1b0_1
  - sniffio=1.2.0=py37hecd8cb5_1
  - snowballstemmer=2.2.0=pyhd3eb1b0_0
  - sortedcontainers=2.4.0=pyhd8ed1ab_0
  - soupsieve=2.3.2.post1=py37hecd8cb5_0
  - sphinx=1.8.5=py37_0
  - sphinxcontrib-applehelp=1.0.2=pyhd3eb1b0_0
  - sphinxcontrib-devhelp=1.0.2=pyhd3eb1b0_0
  - sphinxcontrib-htmlhelp=2.0.0=pyhd3eb1b0_0
  - sphinxcontrib-jsmath=1.0.1=pyhd3eb1b0_0
  - sphinxcontrib-qthelp=1.0.3=pyhd3eb1b0_0
  - sphinxcontrib-serializinghtml=1.1.5=pyhd3eb1b0_0
  - sphinxcontrib-websupport=1.2.4=pyhd8ed1ab_1
  - spyder=5.3.3=py37hf985489_0
  - spyder-kernels=2.3.3=py37hf985489_0
  - spyder-vim=0.1.0=pyhd8ed1ab_0
  - sqlite=3.40.1=h880c91c_0
  - terminado=0.17.1=py37hecd8cb5_0
  - text-unidecode=1.3=py_0
  - textdistance=4.5.0=pyhd8ed1ab_0
  - threadpoolctl=2.2.0=pyh0d69192_0
  - three-merge=0.1.1=pyh9f0ad1d_0
  - tinycss2=1.2.1=py37hecd8cb5_0
  - tk=8.6.12=h5d9f67b_0
  - tokenizers=0.11.4=py37h8776b5c_1
  - toml=0.10.2=pyhd3eb1b0_0
  - tomli=2.0.1=py37hecd8cb5_0
  - tomlkit=0.11.1=py37hecd8cb5_0
  - tornado=6.2=py37hca72f7f_0
  - tqdm=4.64.1=py37hecd8cb5_0
  - traitlets=5.7.1=py37hecd8cb5_0
  - transformers=4.24.0=py37hecd8cb5_0
  - typed-ast=1.4.3=py37h9ed2024_1
  - typing-extensions=4.4.0=py37hecd8cb5_0
  - typing_extensions=4.4.0=py37hecd8cb5_0
  - ujson=5.5.0=py37hac51a3e_0
  - unidecode=1.3.6=pyhd8ed1ab_0
  - urllib3=1.26.14=py37hecd8cb5_0
  - watchdog=2.1.9=py37h5ce5e91_0
  - wcwidth=0.2.5=pyhd3eb1b0_0
  - webencodings=0.5.1=py37_1
  - websocket-client=0.58.0=py37hecd8cb5_4
  - whatthepatch=1.0.4=pyhd8ed1ab_0
  - wheel=0.38.4=py37hecd8cb5_0
  - widgetsnbextension=3.5.2=py37hecd8cb5_0
  - wrapt=1.14.1=py37hca72f7f_0
  - wurlitzer=3.0.2=py37hecd8cb5_0
  - xz=5.2.10=h6c40b1e_1
  - yaml=0.2.5=haf1e3a3_0
  - yapf=0.32.0=pyhd8ed1ab_0
  - zeromq=4.3.4=h23ab428_0
  - zipp=3.11.0=py37hecd8cb5_0
  - zlib=1.2.13=h4dc903c_0
  - zstd=1.5.2=hcb37349_0
  - pip:
      - hirlite==0.3.1
      - importlib-metadata==2.1.3
      - iso8601==1.1.0
      - python-magic==0.4.27
      - setuptools==59.5.0
      - watermark==2.3.0
prefix: /Users/egunadi/anaconda3/envs/python37
```

## Installation

The environment.yml file in GitHub can be used to recreate our environment.

The following modules also need to be installed, along with their dependencies:

- Tika-Python <http://github.com/chrismattmann/tika-python>
- Google’s LangDetect <https://pypi.org/project/langdetect>
- RTG (Reader Translator Generator) <https://gowda.ai/posts/2021/04/mtdata-nlcodec-rtg-many-english>
- GeoTopicParser <https://cwiki.apache.org/confluence/display/tika/GeoTopicParser>
- Detoxify <https://pypi.org/project/detoxify>
- Tika Dockers `uscdatascience/im2txt-rest-tika` and `uscdatascience/inception-rest-tika`
  - <https://github.com/USCDataScience/tika-dockers> and 
  - <https://hub.docker.com/r/uscdatascience/im2txt-rest-tika>

### Notes on Docker Setup

- The following Docker settings were used
  - CPUs: 8
  - Memory: 8 GB
  - Swap: 1 GB
- Docker commands used can be seen in `docker-commands.sh`

## Running the project

If downloading from GitHub, the "data/pixstory" folder will be empty due to proprietary concerns. A "pixstory_v2.tsv" file should be present, which is a copy of "pixstory_final.tsv" from homework #1.

Results can be reproduced via "code/main.py", which runs the following functions in order:

### Data Consolidation

- consolidate_pixstory_data.convert_tsv_to_csv()
  - Uses "data/pixstory/pixstory_v2.tsv" to create "data/pixstory/pixstory_v2.csv"
  - Worked on by Eben Gunadi 
- media_urls.get_urls()
  - Uses "data/pixstory/pixstory_v2.csv" to create "data/pixstory/media_urls.csv", a list of Media URLs
  - Worked on by Eben Gunadi 
- media_images.download_images()
  - Uses "data/pixstory/media_urls.csv" to download all pixstory Media images into directory "data/pixstory/media_files"
  - For convenience, our paper contains a link for downloading these media images
  - Worked on by Eben Gunadi 

### Functions that adds features to the dataset

- im2text.get_caption_files()
  - Uses media files in "data/pixstory/media_files" to output captions in "data/pixstory/media_captions" 
  - To run:
    - Docker instance of "im2txt-rest-tika" must be running on port 8764
    - Images in "data/pixstory/media_files" must be served using `python -m http.server` on port 8000
  - For convenience, our paper contains a link for downloading these caption files
  - Worked on by Eben Gunadi 
- im2text.flag_pixstory_captions()
  - Uses captions in "data/pixstory/media_captions" to create "data/pixstory/pixstory_captions.csv"
  - Worked on by Eben Gunadi
- inception.get_object_files()
  - Uses media files in "data/pixstory/media_files" to output objects in "data/pixstory/media-objects" 
  - To run:
    - Docker instance of "inception-rest-tika" must be running on port 8764
    - Images in "data/pixstory/media_files" must be served using `python -m http.server` on port 8000
  - For convenience, our paper contains a link for downloading these object files
  - Worked on by Eben Gunadi 
- inception.flag_pixstory_objects()
  - Uses objects in "data/pixstory/media_objects" to create "data/pixstory/pixstory_objects.csv"
  - Worked on by Eben Gunadi
- language_code.run_google_lan_det()
  - Uses "data/pixstory/pixstory_objects.csv" to create "data/pixstory/pixstory_langdetect.csv"
  - Worked on by Shih-Min (Julia) Huang
- google_translate.get_clean_narratives()
  - Uses "data/pixstory/pixstory_langdetect.csv" to generate "data/pixstory/clean_narratives.csv"
  - Worked on by Eben Gunadi 
- google_translate.get_translation_files()
  - Uses "data/pixstory/clean_narratives.csv" to output translations in "data/pixstory/narratives_translated"
  - For convenience, our paper contains a link for downloading these translation files
  - Worked on by Eben Gunadi, Yi Chang, and Annie Chang 
- google_translate.flag_pixstory_translations()
  - Uses translations in "data/pixstory/narratives_translated" to create "data/pixstory/pixstory_translations.csv"
  - Worked on by Eben Gunadi
- geotopic_parsing.create_geo_df()
  - Uses "data/pixstory/pixstory_translations.csv" to create "data/pixstory/geo_df.csv"
  - Worked on by Lesly Escobar

### Analysis

TBD
