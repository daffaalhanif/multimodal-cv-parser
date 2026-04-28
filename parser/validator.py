from pydantic import ValidationError

from models.schema import CVOutput


def validate(raw_dict: dict) -> CVOutput:
    """Validasi output LLM terhadap schema CVOutput.

    Args:
        raw_dict: Dict mentah dari LLM parser.

    Returns:
        Instance CVOutput yang sudah tervalidasi.

    Raises:
        ValueError: Jika dict tidak sesuai schema CVOutput.
    """
    try:
        return CVOutput(**raw_dict)
    except ValidationError as e:
        raise ValueError(f"Validasi output gagal:\n{e}")
    