## short-notations
A very simple script to write special symbols in a Mathematica-like format, by typing `~`+code+`~`. The script works directly with the keyboard input.

Simply type `~!=~` and it will be converted into `≠`. Powers are implemented as `10~^2.3+1-2~` ⇒ `10²⋅³⁺¹⁻²`. To stop the execution, type `~stop~`.

#### Executing:
1) Clone the repository
2) Install dependencies
```
pip install -r requirements.txt
```
3) Adjust `notations.py` for your taste.
4) Run the script
```
python short-notations.py
```
5) *Optionally*: set the script to run at system start up. To be written...
