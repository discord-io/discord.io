from ..embed import Embed as Embed
from typing import Dict, List, Union

def parse_embed(embed: Union[Dict, Embed]): ...
def parse_embeds(embeds: List[Union[Dict, Embed]]): ...