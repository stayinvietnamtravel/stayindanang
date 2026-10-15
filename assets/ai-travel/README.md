# Travel artwork library

Twenty-nine original ChatGPT-generated HD PNG illustrations are preserved here. Eleven branded posters contain English typography; eighteen destination and editorial scenes use native HTML titles so the same artwork works in all 13 language editions. These are AI illustrations, not documentary photographs or verified hotel imagery.

- Central Vietnam: Ba Na Hills, Marble Mountains, Hoi An and Hue (portrait).
- Editorial covers: coastal Vietnam, separate Hanoi/Ho Chi Minh City walks, trip planning and generic Da Nang hotel-area inspiration.
- Regional inspiration: Kyoto, Venice, San Francisco and Sydney.
- New editorial scenes: Ha Long Bay, Japan/Paris travel inspiration, Hai Van road trips and airport flight planning.
- New hotel covers: separate Da Nang and Hanoi city scenes, combined with each property’s native HTML name.
- New text posters: Ninh Binh, Sa Pa and Phu Quoc.
- International itinerary posters: Kyoto, Paris, New York and Sydney; Vietnam additions: Hue and Ha Long/Cat Ba.
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
