%global source0_hash 03f2616f11de380a28bb9a10cfa957378116a0d1240756e48e3da9e98600abc8
Name: mythes-uk
Summary:        Ukrainian thesaurus
Version: 1.6.5
Release:        1%{?dist}
Source0:        https://download.documentfoundation.org/libreoffice/src/25.2.3/libreoffice-dictionaries-25.2.3.2.tar.xz#/libreoffice-25.2.3.2.tar.xz
URL: http://sourceforge.net/projects/ispell-uk
License: ( GPL-2.0-or-later OR LGPL-2.1-or-later ) AND ( GPL-2.0-or-later OR LGPL-2.1-or-later OR MPL-1.1 ) AND GPL-2.0-or-later
BuildArch: noarch
Requires: mythes
Supplements: (mythes and langpacks-uk)
# oreon:deps
BuildRequires:  mythes-devel
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Ukrainian thesaurus.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir libreoffice-25.2.3.2
%oreon_prep
%build

cd dictionaries/uk_UA
cp -f th_uk_UA.dat th_uk_UA_v2.dat
th_gen_idx.pl < th_uk_UA_v2.dat > th_uk_UA_v2.idx
%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/mythes
cp -p dictionaries/uk_UA/th_uk_UA_v2.* $RPM_BUILD_ROOT/%{_datadir}/mythes
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.6.5-32
- Import
