%global source0_hash 03f2616f11de380a28bb9a10cfa957378116a0d1240756e48e3da9e98600abc8
Name:           hyphen-it
Summary:        Italian hyphenation rules
Version:        5.1.1
Release:        1%{?dist}
License:        LGPL-2.1-only
URL:            https://extensions.libreoffice.org/
Source0:        https://download.documentfoundation.org/libreoffice/src/25.2.3/libreoffice-dictionaries-25.2.3.2.tar.xz#/libreoffice-25.2.3.2.tar.xz
BuildArch:      noarch
Requires:       hyphen
Supplements:    (hyphen and langpacks-it)
Provides:       hyphen-la = %{version}
# oreon:deps

# /oreon:deps
%description
Italian hyphenation rules.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n libreoffice-25.2.3.2

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/hyphen
cp -p dictionaries/it_IT/hyph_it_IT.dic $RPM_BUILD_ROOT/%{_datadir}/hyphen
pushd $RPM_BUILD_ROOT/%{_datadir}/hyphen/
it_IT_aliases="it_CH la_VA"
for lang in $it_IT_aliases; do
        ln -s hyph_it_IT.dic "hyph_"$lang".dic"
done
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 5.1.1-1
- Prepare for Oreon 11 (RP1)
