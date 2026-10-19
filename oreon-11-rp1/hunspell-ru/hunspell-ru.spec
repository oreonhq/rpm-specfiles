%global source0_hash 03f2616f11de380a28bb9a10cfa957378116a0d1240756e48e3da9e98600abc8
%if 0%{?fedora} > 35 || (0%{?oreon} >= 11)
%global dict_dirname hunspell 
%else
%global dict_dirname myspell
%endif
Name: hunspell-ru
Summary:        Russian hunspell dictionaries
Version: 0.99g5
Release:        1%{?dist}
Epoch: 1
Source0:        https://deb.debian.org/debian/pool/main/libr/libreoffice-dictionaries/libreoffice-dictionaries_25.2.3.orig.tar.xz#/libreoffice-dictionaries-25.2.3.tar.xz
URL: https://github.com/LibreOffice/dictionaries
License: BSD-3-Clause-Modification
BuildArch: noarch
Requires: hunspell
Supplements: (hunspell and langpacks-ru)
# oreon:deps

# /oreon:deps
%description
Russian hunspell dictionaries.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n libreoffice-25.2.3.2

%build

chmod -x dictionaries/ru_RU/ru_RU.dic dictionaries/ru_RU/ru_RU.aff
%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}
install -pm 0644 dictionaries/ru_RU/ru_RU.dic $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}/ru_RU.dic
install -pm 0644 dictionaries/ru_RU/ru_RU.aff $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}/ru_RU.aff
pushd $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}/
ru_RU_aliases="ru_UA"
for lang in $ru_RU_aliases; do
        ln -s ru_RU.aff $lang.aff
        ln -s ru_RU.dic $lang.dic
done
popd
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1:0.99g5-32
- Import
