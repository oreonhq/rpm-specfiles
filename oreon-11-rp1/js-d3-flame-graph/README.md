# js-d3-flame-graph
The js-d3-flame-graph package

## Upgrade instructions
* update `Version`, `Release`, `%changelog` and tarball NVRs in the specfile
* create bundles and manifest: `make clean all`
* update specfile with contents of the `.manifest` file
* run local build: `rpkg local`
* run rpm linter: `rpkg lint -r js-d3-flame-graph.rpmlintrc`
* run a scratch build: `fedpkg scratch-build --srpm`
* upload new source tarballs: `fedpkg new-sources *.tar.gz *.tar.xz`
* commit new `sources` file

## Backporting
* create the patch
* declare and apply (`%prep`) the patch in the specfile
* if the patch affects Node.js dependencies
  * create new tarballs
  * update the specfile with new tarball path and contents of the `.manifest` file

Note: the Makefile automatically applies patches before creating the tarballs

## Patches
* `*.patch`: regular patches applied to the source, applied in the Makefile before vendoring and in the specfile (e.g. updating dependencies)
* `*.vendor.patch`: patches applied to the vendor tarball (e.g. patching vendored sources before generating a webpack)
* `*.cond.patch`: conditionally applied patches in the specfile
