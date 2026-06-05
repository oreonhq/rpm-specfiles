%global source0_hash none

%if 0%{?fedora} > 35 || (0%{?oreon} >= 11)
%global dict_dirname hunspell 
%else
%global dict_dirname myspell
%endif
Name: hunspell-pt
Summary: Portuguese hunspell dictionaries
%global upstreamid 20131030
Version: 0.%{upstreamid}
Release: 16%{?dist}
Source0:        https://deb.debian.org/debian/pool/main/libr/libreoffice-dictionaries/libreoffice-dictionaries_25.2.3.orig.tar.xz#/libreoffice-dictionaries-25.2.3.tar.xz
URL: https://download.documentfoundation.org/libreoffice/src/projetos/vero
# pt_BR dicts are under LGPLv3 or MPL, pt_PT under GPLv2 or LGPLv2 or MPLv1.1
License: ( ( LGPL-3.0-only OR MPL-1.1 ) AND LGPL-2.1-only ) AND ( GPL-2.0-only OR LGPL-2.1-only OR MPL-1.1 )
BuildArch: noarch

Requires: hunspell
Supplements: (hunspell and langpacks-pt)

%description
Portuguese hunspell dictionaries.

%package BR
Summary: Brazilian Portuguese hunspell dictionaries
Requires: hunspell
Supplements: (hunspell and langpacks-pt_BR)

%description BR
Brazilian Portuguese hunspell dictionaries

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n libreoffice-25.2.3.2
for i in dictionaries/pt_BR/package-description.txt dictionaries/pt_PT/README_pt_PT.txt; do
  if ! iconv -f utf-8 -t utf-8 -o /dev/null $i > /dev/null 2>&1; then
    iconv -f ISO-8859-1 -t UTF-8 $i > $i.new
    touch -r $i $i.new
    mv -f $i.new $i
  fi
  tr -d '\r' < $i > $i.new
  touch -r $i $i.new
  mv -f $i.new $i
done

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}
cp -p dictionaries/pt_PT/pt_PT.dic dictionaries/pt_PT/pt_PT.aff dictionaries/pt_BR/pt_BR.dic dictionaries/pt_BR/pt_BR.aff $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}

pushd $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}/
pt_PT_aliases="pt_AO"
for lang in $pt_PT_aliases; do
        ln -s pt_PT.aff $lang.aff
        ln -s pt_PT.dic $lang.dic
done
popd


%files
%doc dictionaries/pt_PT/README_pt_PT.txt
%{_datadir}/%{dict_dirname}/*
%exclude %{_datadir}/%{dict_dirname}/pt_BR.*

%files BR
%doc dictionaries/pt_BR/package-description.txt
%{_datadir}/%{dict_dirname}/pt_BR.*

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.20131030-16
- Import
