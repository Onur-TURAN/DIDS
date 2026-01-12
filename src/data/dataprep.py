import re
import itertools
import pandas as pd

SPECIAL_CHARS = list(" '\"=()%;#,*+!@^&/\\|<>?:.-[]{}")

INJECTION_PATTERNS = pd.read_csv("data/pattern/injection.csv", header=None)[0].tolist()

ENCODED_PATTERNS = pd.read_csv("data/pattern/encoded.csv", header=None)[0].tolist()