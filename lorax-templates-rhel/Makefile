NAME=lorax-templates-rhel
# RHEL version these templates are designed for
RHELVER=11.0
RHPKG=fedpkg --release=eln

# Previous release, override this when new commits are already on branch
PREV ?= origin/eln

# git user.email and user.name must be setup
GITEMAIL := $(shell git config user.email)
GITNAME := $(shell git config user.name)

# Serial number for this release
SERIAL=$(shell [ -f SERIAL ] && cat SERIAL || echo 0)

SPEC=${NAME}.spec
TARBALL=${NAME}-${RHELVER}-${SERIAL}.tar.gz

tar: ${TARBALL}

${TARBALL}: 80-rhel
	git archive --prefix='${NAME}-${RHELVER}/' HEAD $</ | gzip -c9 > $@

bump: bump-serial

bump-serial:
	echo $$((${SERIAL}+1)) > SERIAL
	git add SERIAL

update-spec: clog
	sed -r -i \
	    -e 's/^(Release:\s+)[^%]+(%.*)$$/\1${SERIAL}\2/' \
	    -e 's/^(Version:\s+).*$$/\1${RHELVER}/' \
	    -e 's/^(Source0:\s+).*$$/\1${TARBALL}/' \
	    -e '/%changelog/ r clog-spec' \
	    ${SPEC}

clog:
	@echo "* $(shell date '+%a %b %d %Y') ${GITNAME} <${GITEMAIL}> - ${RHELVER}-${SERIAL}" > clog-spec
	./tools/git-changelog -t ${PREV} > clog
	cat clog >> clog-spec

# These need to rerun make to pick up the bumped serial number
release:
	$(MAKE) bump-serial && $(MAKE) tar && $(MAKE) update-spec && $(MAKE) commit

release-merge:
	$(MAKE) bump-serial && $(MAKE) tar && $(MAKE) update-spec && $(MAKE) amend


commit:
	$(RHPKG) new-sources ${TARBALL}
	git add -u
	git commit -F clog

amend:
	$(RHPKG) new-sources ${TARBALL}
	git add -u
	git commit --amend


.PHONY: tar ${TARBALL} bump-serial update-spec release clog commit
