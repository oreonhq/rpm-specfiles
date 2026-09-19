%global source0_hash 6a26af1c121cf2a275168f6f31594ad61e3fc72cdb0ae83c1a07494678821c11

Name:           wiggle
Version:        1.3
Release:        6%{?dist}
Summary:        A tool for applying patches with conflicts

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://neil.brown.name/wiggle/
Source0:        http://neil.brown.name/wiggle/%{name}-%{version}.tar.gz
Patch0:         wiggle-fix-build.patch

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  groff
BuildRequires:  time
BuildRequires:  ncurses-devel

# The source tarball used, is obtained by visiting the URL above and
# getting a snapshot that contains the latest sources.  This can be
# done by clicking the 'snapshot' link listed on the gitweb interface
# This snapshot was the latest commit on the 'master' branch.
# 
# RPM doesn't particularly like this link as a 'Source', so I'll paste
# is here for posterity:
#
# http://neil.brown.name/git?p=wiggle;a=snapshot;h=1c5bfa7ce4de088e3b942463bb11cdc553a92b97;sf=tgz
#

%description
Wiggle is a program for applying patches that 'patch' cannot apply due
to conflicting changes in the original.

Wiggle will always apply all changes in the patch to the original.  If
it cannot find a way to cleanly apply a patch, it inserts it in the
original in a manner similar to 'merge', and reports an unresolvable
conflict.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1 -b .build

%build
export CFLAGS="$RPM_OPT_FLAGS"
%make_build

%check
make test

%install
%make_install

%files
%license COPYING
%doc ANNOUNCE TODO
/usr/bin/wiggle
%{_mandir}/man1/wiggle.1*

%changelog
%autochangelog
