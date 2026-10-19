%global source0_hash 03f2616f11de380a28bb9a10cfa957378116a0d1240756e48e3da9e98600abc8
%if 0%{?fedora} >= 36 || 0%{?rhel} > 9 || (0%{?oreon} >= 11)
%global dict_dirname hunspell
%else
%global dict_dirname myspell
%endif
Name: hunspell-af
Summary:        Afrikaans hunspell dictionary
%global upstreamid 20080825
Version: 0.%{upstreamid}
Release:        1%{?dist}
Source0:        https://deb.debian.org/debian/pool/main/libr/libreoffice-dictionaries/libreoffice-dictionaries_25.2.3.orig.tar.xz#/libreoffice-dictionaries-25.2.3.tar.xz
URL: http://www.translate.org.za/
License: LGPL-2.1-or-later
BuildArch: noarch
Requires: hunspell-filesystem
Supplements: (hunspell and langpacks-af)
# oreon:deps

# /oreon:deps
%description
Afrikaans hunspell dictionary

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n libreoffice-25.2.3.2

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}
cp -p dictionaries/af_ZA/*.dic dictionaries/af_ZA/*.aff $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}
pushd $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}/
af_ZA_aliases="af_NA"
for lang in $af_ZA_aliases; do
        ln -s af_ZA.aff $lang.aff
        ln -s af_ZA.dic $lang.dic
done
popd
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.20080825-35
- Import
