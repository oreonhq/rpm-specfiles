%global source0_hash none

%if 0%{?fedora} >= 36 || 0%{?rhel} > 9 || (0%{?oreon} >= 11)
%global dict_dirname hunspell
%else
%global dict_dirname myspell
%endif

Name: hunspell-fa
Summary: Farsi hunspell dictionaries
%global upstreamid 20070116
Version: 0.%{upstreamid}
Release: 38%{?dist}
Source0:        https://deb.debian.org/debian/pool/main/libr/libreoffice-dictionaries/libreoffice-dictionaries_25.2.3.orig.tar.xz#/libreoffice-dictionaries-25.2.3.tar.xz
URL:            https://github.com/LibreOffice/dictionaries
License: GPL-2.0-or-later
BuildArch: noarch

Requires: hunspell-filesystem
Supplements: (hunspell and langpacks-fa)

%description
Farsi hunspell dictionaries.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n libreoffice-25.2.3.2

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}
install -pm 0644 dictionaries/fa_IR/fa-IR.dic $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}/fa_IR.dic
install -pm 0644 dictionaries/fa_IR/fa-IR.aff $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}/fa_IR.aff

%files
%doc dictionaries/fa_IR/README_fa_IR.txt
%{_datadir}/%{dict_dirname}/*

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.20070116-38
- Import
