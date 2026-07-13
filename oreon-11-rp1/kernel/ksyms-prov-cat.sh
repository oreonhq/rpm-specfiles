#!/bin/bash
while read -r f; do
	[ -f "$f" ] || continue
	cat -- "$f"
done
