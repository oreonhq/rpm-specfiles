%global source0_hash 03f2616f11de380a28bb9a10cfa957378116a0d1240756e48e3da9e98600abc8

%if 0%{?fedora} >= 36 || 0%{?rhel} > 9 || (0%{?oreon} >= 11)
%global dict_dirname hunspell
%else
%global dict_dirname myspell
%endif

Name: hunspell-pl
Summary: Polish hunspell dictionaries
Version: 20260901
Release: 1%{?dist}
License: LGPL-2.1-or-later OR GPL-2.0-or-later OR MPL-1.1
URL: https://cgit.freedesktop.org/libreoffice/dictionaries/tree/pl_PL
Source0: https://deb.debian.org/debian/pool/main/libr/libreoffice-dictionaries/libreoffice-dictionaries_25.2.3.orig.tar.xz#/libreoffice-dictionaries-25.2.3.tar.xz
BuildArch: noarch

Requires: hunspell-filesystem
Supplements: (hunspell and langpacks-pl)

%description
Polish hunspell dictionaries

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n libreoffice-25.2.3.2

%build

%install
mkdir -p %{buildroot}%{_datadir}/%{dict_dirname}
install -pm 0644 dictionaries/pl_PL/pl_PL.aff %{buildroot}%{_datadir}/%{dict_dirname}/
install -pm 0644 dictionaries/pl_PL/pl_PL.dic %{buildroot}%{_datadir}/%{dict_dirname}/


%files
%{_datadir}/%{dict_dirname}/*



%changelog
* Fri Sep 04 2026 Oreon Packaging Team <packaging@oreonhq.com> - 20260901-1
- Update to 20260901

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 25.2.3-1
- Import
