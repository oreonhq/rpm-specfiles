%global source0_hash 87a054194ddd2e073d50c15b0c4f7cf1373b1a5a82e78d9a8f16f13ade7ee00e
Name:       beakerlib
Summary:        A shell-level integration testing library
Version:    1.33.3
Release:        1%{?dist}
License:    GPL-2.0-only
BuildArch:  noarch
URL:        https://github.com/%{name}
Autoreq:    0
Requires:   nfs-utils
Requires:   /bin/bash
Requires:   /bin/sh
Requires:   /usr/bin/python
Requires:   /usr/bin/perl
Requires:   wget
Requires:   python-lxml
Requires:   /usr/bin/xmllint
Requires:   grep
Requires:   sed
Requires:   iproute
Requires:   coreutils
Requires:   tar
Requires:   gzip
Requires:   util-linux
Requires:   which
Requires:   yum-utils
Requires:   /usr/bin/bc
Requires:   /usr/bin/time
Recommends: beakerlib-redhat
Conflicts:  beakerlib-redhat < 1-30
Source0:        https://github.com/beakerlib/beakerlib/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:    %{name}-tmpfiles.conf
Patch0: bugzilla-links.patch
Patch1: bugzilla-links-epel.patch
Patch2: python3.patch
Patch3: python-platform.patch
# oreon:deps
BuildRequires:  /usr/bin/pod2man
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  util-linux
BuildRequires:  vim-common
# /oreon:deps
%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -N
# rhel
# Patch1: bugzilla-links-epel.patch
%patch -P 1 -p1

%build

make build
%install
%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}-%{version}}
%{!?_tmpfilesdir: %global _tmpfilesdir %{_prefix}/lib/tmpfiles.d/}
rm -rf $RPM_BUILD_ROOT
make PKGDOCDIR=%{buildroot}/%{_pkgdocdir} DESTDIR=%{buildroot}/usr install
find %{buildroot} -type f -print0 | xargs -0 grep -l -x '#!/usr/bin/env python' | xargs -r sed -i '1s|#!/usr/bin/env python$|#!/usr/bin/python3|'
mkdir -p %{buildroot}/%{_tmpfilesdir}
install -m 0644 %{SOURCE1} %{buildroot}/%{_tmpfilesdir}/%{name}.conf
%oreon_autofiles beakerlib-vim-syntax usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%description
The BeakerLib project means to provide a library of various helpers, which
could be used when writing operating system level integration tests.

%package vim-syntax
Summary: Files for syntax highlighting BeakerLib tests in VIM editor
Requires: vim-common
BuildRequires: vim-common
BuildRequires: make
%description vim-syntax
Files for syntax highlighting BeakerLib tests in VIM editor

%files -f %{oreon_filedir}/main.list
%files -n beakerlib-vim-syntax -f %{oreon_filedir}/beakerlib-vim-syntax.list

%changelog

%autochangelog
