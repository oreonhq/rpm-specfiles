#!/bin/bash
# dist.sh: print the %{dist} tag for the running Oreon system.
# Reads ID and VERSION_ID from /etc/os-release.
# Output: .or<major> (for example .or11). Prints nothing if unknown.

OSREL=/etc/os-release
[ -r "$OSREL" ] || OSREL=/usr/lib/os-release

ID=$(. "$OSREL" 2>/dev/null; echo "$ID")
DISTNUM=$(. "$OSREL" 2>/dev/null; echo "${VERSION_ID%%.*}")

DISTTYPE=
[ "$ID" = "oreon" ] && DISTTYPE=or

DISTTAG=
[ -n "$DISTTYPE" ] && [ -n "$DISTNUM" ] && DISTTAG=".${DISTTYPE}${DISTNUM}"

case "$1" in
    --or) [ -n "$DISTTYPE" ] && echo -n "$DISTNUM" ;;
    --distnum) echo -n "$DISTNUM" ;;
    --disttype) echo -n "$DISTTYPE" ;;
    --help)
	printf "Usage: $0 [OPTIONS]\n"
	printf " Default mode is --dist. Possible options:\n"
	printf " --or\t\tfor Oreon version (if Oreon)\n"
	printf " --dist\t\tfor distribution tag\n"
	printf " --distnum\tfor distribution number (major)\n"
	printf " --disttype\tfor distribution type\n" ;;
    *) echo -n "$DISTTAG" ;;
esac
