%global source0_hash 66bc8c38758801d5a1330588589b6e81f4d7272a6fbdad0cd4cfcd266848e160
Name:    mallard-rng
Version: 1.1.0
Release:        16%{?dist}
Summary:        RELAX NG schemas for all Mallard versions
License: MIT
URL:     http://projectmallard.org/download/
Source0:        https://deb.debian.org/debian/pool/main/m/%{name}/%{name}_%{version}.orig.tar.bz2
BuildArch:        noarch
Requires(post):   /usr/bin/xmlcatalog
Requires(post):   xml-common
Requires(postun): /usr/bin/xmlcatalog
Requires(postun): xml-common
# oreon:deps
BuildRequires:  make
# /oreon:deps
%description
RELAX NG schemas for all Mallard versions and extensions that have been marked
final.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%configure
%make_build
%install
%make_install
%oreon_autofiles main

%post

xmlcatalog --noout --add 'nextCatalog' 'file://%{_sysconfdir}/xml/mallard/catalog' "" %{_sysconfdir}/xml/catalog &> /dev/null || :
%postun

xmlcatalog --noout --del 'file://%{_sysconfdir}/xml/mallard/catalog' %{_sysconfdir}/xml/catalog &> /dev/null || :
%files -f %{oreon_filedir}/main.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.1.0-16
- Import
