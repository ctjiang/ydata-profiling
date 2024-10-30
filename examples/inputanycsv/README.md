IISI 資料品質執行檔

***prompt>*** inputanycsv(.exe) src.csv [src.html]

產出inputanycsv執行檔方式

- 建立開發環境
  - 使用Python venv
    - ***prompt>*** python venv
    - 建立app folder
    - pull source code of ydata-profiling from IISI repository
    - 安裝基本 python packages by requirments.txt
  - 使用.devcontainer
    - Open Command Palette
    - 執行Dev Container: Reopen
    - 切換到ydada-profiling folder下
  - 執行ydata-profiling下的makefile
    - Windows下，`make.bat all` or `make.bat install`
    - Linux，MacOS下，`make all` or `make install`
- 開發inputanycsv主程式
  - 切換到 ydata-profiling/examples/inputanycsv
  - 修改inputanycsv.py
- 編譯執行檔
  - pyinstaller inputanycsv.py --collect-all ydata_profiling -F
- 產出結果
  - dist/inputanycsv(.exe) Native executable file，(.exe)表示在Windows下執行檔
  - inputanycsv.spec 執行pyinstaller所需要的spec檔
