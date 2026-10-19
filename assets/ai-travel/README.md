# Travel artwork library

Thirty-one original ChatGPT-generated HD PNG illustrations are preserved here. Eleven branded posters contain English typography; twenty destination and editorial scenes use native HTML titles so the same artwork works in all 13 language editions. These are AI illustrations, not documentary photographs or verified hotel imagery.

- Central Vietnam: Ba Na Hills, Marble Mountains, Hoi An and Hue (portrait).
- Editorial covers: coastal Vietnam, separate Hanoi/Ho Chi Minh City walks, trip planning and generic Da Nang hotel-area inspiration.
- Regional inspiration: Kyoto, Venice, San Francisco and Sydney.
- New editorial scenes: Ha Long Bay, Japan/Paris travel inspiration, Hai Van road trips and airport flight planning.
- New hotel covers: separate Da Nang and Hanoi city scenes, combined with each property’s native HTML name.
- New text posters: Ninh Binh, Sa Pa and Phu Quoc.
- International itinerary posters: Kyoto, Paris, New York and Sydney; Vietnam additions: Hue and Ha Long/Cat Ba.
- Additional regional hotel scenes: Ho Chi Minh City and a generic southern Vietnam coast for Vung Tau, Ho Tram and Long Hai guides.
- Original posters: Discover Vietnam and Taste Vietnam.
- `manifest.json` records topics, original dimensions and creation details.

The standalone homepage artwork/download section has been removed. Artwork appears in destination cards, regional guide covers and contextual blog illustrations for tours, car rentals and flights. Cards use lazy loading, responsive WebP variants and native AI attribution. Original PNGs remain in this repository. Generic hotel-area artwork must never be described as a photograph of an individual property or its amenities.

To add artwork, generate an original PNG with ChatGPT, save it here, update the manifest and topic mapping, then run:

```sh
python3 -m pip install Pillow
python3 scripts/optimize_images.py
python3 scripts/build_site.py
python3 scripts/check_site.py
```

The exporter also processes existing hotel text cards. It preserves PNG originals, avoids upscaling and caches unchanged sources in `assets/image-variants.json`. Regular site builds only read that registry and do not require Pillow or an image API key. Prefer clear compositions, safe title areas, consistent navy/turquoise/warm accents and no fabricated prices, rankings or property details.

`thailand-seven-days.png` (17 October 2026) illustrates the separate Bangkok and Chiang Mai sections of the seven-day Thailand guide. It is AI editorial artwork, not a location photograph. WebP derivatives preserve its full text.

`hotel-phu-quoc-scene.png` (19 October 2026) is generic island-accommodation artwork. It is not a verified depiction of any named hotel. Property-specific text is overlaid accessibly in HTML; use the responsive WebP derivatives on the website.
