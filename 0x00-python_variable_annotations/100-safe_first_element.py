from typing import Sequence, Optional

# The types of the elements of the input are not known
def safe_first_element(lst: Sequence[object]) -> Optional[object]:
    if lst:
        return lst[0]
    else:
        return None
