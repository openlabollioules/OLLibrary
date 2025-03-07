"""
This module provides multiple functions to work with JSON data.
"""
import re
import json

def extract_json(data: any) -> dict:
    """
    Extract and return a JSON object from the given input 'data'.

    If `data` is already a dict or list, it is returned as-is.
    If `data` is a string:
      - First, it attempts to parse it entirely as JSON.
      - If that fails, it uses two alternative methods:
        
        Method 1: Regex-based extraction.
          - Uses a regex pattern to extract a substring that looks like JSON.
          - Advantage: Very simple and concise.
          - Drawback: It may fail or capture too little/much if the string contains extra text
            or if the JSON has nested structures with inner braces/brackets.

        Method 2: Decoder-based extraction.
          - Iterates over the string and uses JSONDecoder.raw_decode() to try to decode a JSON
            object from positions where a '{' or '[' appears.
          - Advantage: Leverages the JSON parser’s own grammar, making it more robust for nested objects or arrays.
          - Drawback: Slightly less intuitive than a one-line regex.

    Parameters
    ----------
    data : any
        The input data to extract JSON from. Can be a dict, list, or str.

    Returns
    -------
    dict or list
        A parsed JSON object (usually a dict or list).

    Raises
    ------
    ValueError
        If no valid JSON can be extracted from the input.
    """
    if isinstance(data, (dict, list)):
        return data

    if not isinstance(data, str):
        data = str(data)

    data = data.strip()

    # First attempt: Try to parse the whole string as JSON.
    try:
        return json.loads(data)
    except json.JSONDecodeError:
        print("Not a pure JSON string, so we try to extract the JSON part.")

    # --- Method 1: Regex-based extraction ---
    regex_pattern = r'(\{.*\}|\[.*\])'
    match = re.search(regex_pattern, data, re.DOTALL)
    if match:
        candidate = match.group(0)
        try:
            return json.loads(candidate)
        except json.JSONDecodeError:
            print("If the candidate isn't valid JSON, we try the next method.")

    # --- Method 2: Using JSONDecoder's raw_decode method ---
    decoder = json.JSONDecoder()
    for i in range(len(data)):
        if data[i] in ['{', '[']:
            try:
                obj, idx = decoder.raw_decode(data[i:])
                return obj
            except json.JSONDecodeError:
                continue

    print("No valid JSON found in the input data.")
