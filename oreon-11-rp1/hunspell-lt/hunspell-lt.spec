%global source0_hash none

%if 0%{?fedora} >= 36 || 0%{?rhel} > 9 || (0%{?oreon} >= 11)
%global dict_dirname hunspell
%else
%global dict_dirname myspell
%endif

Name: hunspell-lt
Summary: Lithuanian hunspell dictionaries
Version: 1.3.2
Release: 38%{?dist}
Source0:        https://deb.debian.org/debian/pool/main/libr/libreoffice-dictionaries/libreoffice-dictionaries_25.2.3.orig.tar.xz#/libreoffice-dictionaries-25.2.3.tar.xz
URL: https://github.com/LibreOffice/dictionaries
License: BSD-3-Clause
BuildArch: noarch

Requires: hunspell-filesystem
Supplements: (hunspell and langpacks-lt)

%description
Lithuanian hunspell dictionaries.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n libreoffice-25.2.3.2

%build
chmod -x dictionaries/lt_LT/lt.dic dictionaries/lt_LT/lt.aff

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}
install -pm 0644 dictionaries/lt_LT/lt.dic dictionaries/lt_LT/lt.aff $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}/

%files
%license dictionaries/lt_LT/COPYING
%{_datadir}/%{dict_dirname}/*

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.3.2-38
- Import
