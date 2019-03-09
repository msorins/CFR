from typing import Tuple, List, Dict, NewType
import requests
import json

from API.config import Config


Correction = NewType('Correction', Tuple[int, int, str, str])


def _get_corrections(corrections: List[Dict]) -> List[Correction]:
    """
    Args:
        corrections: Bing API response contatining spelling suggestions
    Return:
        List of Corrections; each contains a mistake and its suggestion
    """

    ans = []
    for c in corrections:
        old = c['token']
        suggestion = c['suggestions'][0]['suggestion']
        ans.append((old, suggestion))

    return ans


def _correct(text: str, corrections: List[Correction]) -> str:
    """
    Args:
        text: Text to be corrected
        corrections: Corrections to be applied
    Returns:
        The corrected text
    """

    for c in corrections:
        old, suggestion = c
        text = text.replace(old, suggestion)

    return text


def spellcheck(text: str) -> str:
    """
    Args:
        text: Text to be corrected
    Returns:
        The corrected text
    """

    data = {'text': text}
    params = {'mkt': 'en-us', 'mode': 'proof'}

    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Ocp-Apim-Subscription-Key': Config.BING_SPELLCHECK_KEY,
    }

    response = requests.post(
        Config.BING_SPELLCHECK_ENDPOINT,
        headers=headers,
        params=params,
        data=data
    )

    response = response.json()
    print(json.dumps(response, indent=4))
    corrections = response["flaggedTokens"]

    corrections = _get_corrections(corrections)
    text = _correct(text, corrections)

    return text
