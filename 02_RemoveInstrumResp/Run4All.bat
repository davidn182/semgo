@echo off

for %%f in (.\Data\001*) do (
    rem echo %%~nf
    rem echo %%f
    python DoInstrumentCor.py %%f 
)
