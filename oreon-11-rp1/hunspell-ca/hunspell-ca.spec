%global source0_hash none

%if 0%{?fedora} >= 36 || 0%{?rhel} > 9 || (0%{?oreon} >= 11)
%global dict_dirname hunspell
%else
%global dict_dirname myspell
%endif

Name: hunspell-ca
Summary: Catalan hunspell dictionaries
Version: 25.2.3
Release: 7%{?dist}
License: GPL-2.0-or-later OR LGPL-2.1-or-later
URL: https://cgit.freedesktop.org/libreoffice/dictionaries/tree/ca
Source0: https://deb.debian.org/debian/pool/main/libr/libreoffice-dictionaries/libreoffice-dictionaries_25.2.3.orig.tar.xz#/libreoffice-dictionaries-25.2.3.tar.xz
BuildArch: noarch

Requires: hunspell-filesystem
Supplements: (hunspell and langpacks-ca)

%description
Catalan hunspell dictionaries

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n libreoffice-25.2.3.2

%build

%install
mkdir -p %{buildroot}%{_datadir}/%{dict_dirname}
install -pm 0644 dictionaries/ca/dictionaries/ca.aff %{buildroot}%{_datadir}/%{dict_dirname}/ca_ES.aff
install -pm 0644 dictionaries/ca/dictionaries/ca.dic %{buildroot}%{_datadir}/%{dict_dirname}/ca_ES.dic
pushd %{buildroot}%{_datadir}/%{dict_dirname}/
for lang in ca_AD ca_FR ca_IT; do
    ln -s ca_ES.aff $lang.aff
    ln -s ca_ES.dic $lang.dic
done
popd

%files
%doc dictionaries/ca/README_ca.txt
%{_datadir}/%{dict_dirname}/*



%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 25.2.3-1
- Import
