#!/usr/bin/python3

from pathlib import Path
import json
import os
import subprocess
import sys

if len(sys.argv) != 2:
    sys.stderr.write('usage: %s <buildroot-sitelib>\n' % sys.argv[0])

buildroot_sitelib_dir = sys.argv[1]
sys.path.insert(0, buildroot_sitelib_dir)

from tldextract.cache import get_cache_dir, DiskCache

if 'TLDEXTRACT_CACHE' not in os.environ:
    raise ValueError('must set "TLDEXTRACT_CACHE" environment variable')

local_cache = Path('/usr/share/publicsuffix/public_suffix_list.dat')
if not local_cache.exists():
    raise FileNotFoundError(local_cache)

url_local_cache = f'file://{local_cache}'
subprocess.run(['/usr/bin/tldextract', '--update', f'--suffix_list_url={url_local_cache}'], check=True)

cache = DiskCache(cache_dir=get_cache_dir())
namespace = 'publicsuffix.org-tlds'
cache_with_local_data = cache._key_to_cachefile_path(namespace, {'urls': (url_local_cache,), 'fallback_to_snapshot': True})
func = lambda **kwargs: json.loads(Path(cache_with_local_data).read_text())

kwargs = {
    'cache': cache,
    'urls': ('https://publicsuffix.org/list/public_suffix_list.dat', 'https://raw.githubusercontent.com/publicsuffix/list/master/public_suffix_list.dat'),
    'fallback_to_snapshot': True,
}
cache.run_and_cache(func, namespace=namespace, kwargs=kwargs, hashed_argnames=('urls', 'fallback_to_snapshot'))

