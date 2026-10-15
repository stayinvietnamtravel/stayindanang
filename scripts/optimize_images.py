"""Export responsive WebP variants; original HD artwork is never modified."""
from pathlib import Path
from PIL import Image,ImageOps
import json
from hashlib import sha256
ROOT=Path(__file__).resolve().parents[1]
TARGETS={480:70_000,960:190_000,1536:340_000,1600:340_000}
def optimize():
    outputs={}
    manifest=ROOT/'assets/image-variants.json'
    previous=json.loads(manifest.read_text()) if manifest.exists() else {}
    sources=sorted((ROOT/'assets/ai-travel').glob('*.png'))+sorted((ROOT/'assets/hotel-deals').glob('*.png'))+sorted((ROOT/'assets/hanoi-hotels').glob('*.png'))
    for source in sources:
        path=source.relative_to(ROOT).as_posix();variants=[]
        digest=sha256(source.read_bytes()).hexdigest()
        existing=previous.get(path)
        if existing and existing.get('sha256')==digest and all((ROOT/v['file']).exists() for v in existing['variants']):
            outputs[path]=existing;continue
        with Image.open(source) as original:
            image=ImageOps.exif_transpose(original).convert('RGB')
            widths=sorted({min(width,image.width) for width in (480,960,image.width)})
            for width in widths:
                scaled=image.resize((width,round(image.height*width/image.width)),Image.Resampling.LANCZOS)
                output=source.with_name(source.stem+f'-{width}.webp')
                target=TARGETS.get(width,340_000)
                for quality in (82,78,74,70,66,62):
                    scaled.save(output,'WEBP',quality=quality,method=6)
                    if output.stat().st_size<=target:break
                variants.append({'file':output.relative_to(ROOT).as_posix(),'width':width,'height':scaled.height,'bytes':output.stat().st_size,'quality':quality})
            outputs[path]={'width':image.width,'height':image.height,'original_bytes':source.stat().st_size,'sha256':digest,'variants':variants}
    (ROOT/'assets/image-variants.json').write_text(json.dumps(outputs,ensure_ascii=False,indent=2)+'\n')
    print(f'Exported {sum(len(entry["variants"]) for entry in outputs.values())} WebP variants for {len(outputs)} originals.')
if __name__=='__main__':optimize()
