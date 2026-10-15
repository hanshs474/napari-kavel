# napari-kavel

Kavel is a free AI video generator and AI image generator — 4K clips with sound, and images you can run without an account or a card. This napari plugin adds a **Kavel AI image** widget: type a prompt, press Generate, and the result lands in your viewer as a new RGB image layer (the source URL is kept in the layer's metadata).

Useful for test images, figure backgrounds and teaching material when you need a picture of something and don't have one.

No API key is needed to start: without one the widget runs on [Kavel](https://www.kavel.ai/?utm_source=napari&utm_medium=readme)'s free tier (a small daily allowance, watermarked images). Paste a key from [kavel.ai/settings/apikeys](https://www.kavel.ai/settings/apikeys) into the widget, or set `KAVEL_API_KEY`, to use your account's credits.

## Install

```
pip install napari-kavel
```

or search for "Kavel" in **Plugins → Install/Uninstall Plugins**.

## Use

**Plugins → Kavel AI Image → Kavel AI image**, type a prompt, pick an aspect ratio (1:1, 16:9, 9:16, 4:3, 3:4), press **Generate**. A run takes about a minute.

## Models

The free tier runs Kavel's own image model. With an API key you can reach the larger ones, such as [Seedream 4.0](https://www.kavel.ai/image/seedream-4?utm_source=napari&utm_medium=readme), which charges the same at 1K or 4K.

## License

MIT
