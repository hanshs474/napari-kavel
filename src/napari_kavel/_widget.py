"""Kavel image widget: type a prompt, get a new RGB image layer.

Without an API key calls run on Kavel's free tier (a small daily allowance,
watermarked images). Paste a key from https://www.kavel.ai/settings/apikeys
or set KAVEL_API_KEY to use your account's credits.
"""
from typing import TYPE_CHECKING

from magicgui import magic_factory

if TYPE_CHECKING:
    import napari


def _download(url: str):
    import urllib.request

    import imageio.v3 as iio

    # The CDN turns away urllib's default user agent, so name ourselves.
    req = urllib.request.Request(url, headers={"User-Agent": "napari-kavel/1.0 (+https://www.kavel.ai)"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return iio.imread(r.read(), extension=".webp" if url.endswith(".webp") else None)


def _fetch(prompt: str, aspect_ratio: str, api_key: str):
    import kavel

    url = kavel.generate(prompt, aspect_ratio=aspect_ratio, api_key=api_key or None)
    return url, _download(url)


@magic_factory(
    call_button="Generate",
    prompt={"widget_type": "LineEdit", "tooltip": "Name the subject, the light and the composition."},
    aspect_ratio={"choices": ["1:1", "16:9", "9:16", "4:3", "3:4"]},
    api_key={"widget_type": "Password", "tooltip": "Optional. Leave empty for the free tier."},
)
def generate_image(prompt: str = "", aspect_ratio: str = "1:1", api_key: str = "") -> "napari.types.LayerDataTuple":
    """Generate an image from the prompt and add it as a layer (takes about a minute)."""
    if not prompt.strip():
        raise ValueError("Type a prompt first.")
    url, data = _fetch(prompt.strip(), aspect_ratio, api_key)
    return (data, {"name": prompt.strip()[:40], "rgb": True, "metadata": {"kavel_url": url}}, "image")
