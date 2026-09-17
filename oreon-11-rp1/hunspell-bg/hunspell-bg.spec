%global source0_hash none

%if 0%{?fedora} >= 36 || 0%{?rhel} > 9 || (0%{?oreon} >= 11)
%global dict_dirname hunspell
%else
%global dict_dirname myspell
%endif

Name: hunspell-bg
Summary: Bulgarian hunspell dictionaries
Version: 25.2.3
Release: 33%{?dist}
License: GPL-2.0-or-later OR LGPL-2.1-or-later OR MPL-1.1
URL: https://cgit.freedesktop.org/libreoffice/dictionaries/tree/bg_BG
Source0: https://deb.debian.org/debian/pool/main/libr/libreoffice-dictionaries/libreoffice-dictionaries_25.2.3.orig.tar.xz#/libreoffice-dictionaries-25.2.3.tar.xz
BuildArch: noarch

Requires: hunspell-filesystem
Supplements: (hunspell and langpacks-bg)

%description
Bulgarian hunspell dictionaries

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n libreoffice-25.2.3.2

%build

%install
mkdir -p %{buildroot}%{_datadir}/%{dict_dirname}
install -pm 0644 dictionaries/bg_BG/bg_BG.aff dictionaries/bg_BG/bg_BG.dic %{buildroot}%{_datadir}/%{dict_dirname}/

%files
%doc dictionaries/bg_BG/README_hyph_bg_BG.txt
%license dictionaries/bg_BG/COPYING
%{_datadir}/%{dict_dirname}/*



%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 25.2.3-1
- Import
