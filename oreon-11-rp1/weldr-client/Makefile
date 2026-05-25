SPEC ?= weldr-client.spec

update-vendor:
	go_vendor_archive create --config go-vendor-tools.toml ${SPEC}
	go_vendor_license --config go-vendor-tools.toml --path ${SPEC} \
		report --update-spec --prompt --autofill=auto

.PHONY: update-vendor
