"""Small consistent inline icons; no font or image request required."""
PATHS={
'hotels':'<path d="M3 18v-9m18 9v-7H3m3 0V6h5v5m1 0V6h6a3 3 0 0 1 3 3v2M3 15h18"/>',
'flights':'<path d="m3 10 7 2 5-8 3 1-3 8 5 3-1 2-6-2-4 5-2-1 2-6-6-2z"/>',
'tours':'<path d="M4 5h16v5a2 2 0 0 0 0 4v5H4v-5a2 2 0 0 0 0-4V5zM14 5v3m0 3v2m0 3v3"/>',
'transfers':'<path d="M5 14V7a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2v7M5 10h14M5 14h14v4H5zM8 18v2m8-2v2M8 14h.1M16 14h.1M9 2h6"/>',
'cars':'<path d="m5 10 2-5h10l2 5M4 10h16v8H4zM7 18v2m10-2v2M7 14h.1M17 14h.1"/>'}
def icon(key):return '<svg viewBox="0 0 24 24" width="24" height="24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'+PATHS[key]+'</svg>'
