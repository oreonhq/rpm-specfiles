#!/bin/sh
jq -r '."shell-version" | map("gnome-shell(api) = \(.)") | join(" or ") | "(\(.))"' $@
