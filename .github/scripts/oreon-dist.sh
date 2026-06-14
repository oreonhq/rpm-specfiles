#!/bin/bash
pkg=${1:?}
seg=$(echo "$pkg" | grep -Eo 'oreon-[0-9]+-rp[0-9]+' | head -1) || exit 0
ver=${seg#oreon-}
ver=${ver%%-*}
printf '.or%s' "$ver"
