%global source0_hash 87240ddede144913f8300d2fe8fe81ee41026e1dc6514b475ae4ad69fb701268

%global git_commit a3e413489ccdd05431401357bf21690536425012
%global git_date 20201227

Summary:        Uncompress the Apple compressed disk image files
Name:           dmg2img
Version:        1.6.7
Release:        %autorelease -s %{git_date}git%{sub %git_commit 0 7}
# dmg2img is GPL without specific version
# vfdecrypt is MIT licensed
# Automatically converted from old format: GPL+ and MIT - review is highly recommended.
License:        GPL-1.0-or-later AND LicenseRef-Callaway-MIT
URL:            http://vu1tur.eu.org/tools/
Source0:        https://github.com/Lekensteyn/%{name}/archive/%{git_commit}/%{name}-%{version}.git.tar.gz
BuildRequires:  gcc
# FIXME Basically all Big-Endian arches but we have only one at this moment
%ifnarch s390x
BuildRequires:  lzfse-devel
%endif
BuildRequires:  make
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(zlib)

%description
This package contains dmg2img utility that is able to uncompress compressed dmg
files into plain disk or filesystem images.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{git_commit}

%build
# FIXME Basically all Big-Endian arches but we have only one at this moment
%ifnarch s390x
make CC="%{__cc}" HAVE_LZFSE=1 CFLAGS="%{optflags}" %{_smp_mflags}
%else
make CC="%{__cc}" CFLAGS="%{optflags}" %{_smp_mflags}
%endif

%install
install -D -p -m 0755 dmg2img %{buildroot}%{_bindir}/dmg2img
install -D -p -m 0755 vfdecrypt %{buildroot}%{_bindir}/vfdecrypt
install -D -p -m 0644 vfdecrypt.1 %{buildroot}%{_mandir}/man1/vfdecrypt.1

%files
%license COPYING
%doc README
%{_bindir}/dmg2img
%{_bindir}/vfdecrypt
%{_mandir}/man1/vfdecrypt.1*

%changelog
%autochangelog
