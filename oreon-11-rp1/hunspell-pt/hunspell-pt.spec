%global source0_hash 2700674e9fe644151362c32a78bb816fc844a37be690cfad6ee18e2bc744deb9
%global source1_hash none

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
Source0: http://natura.di.uminho.pt/download/sources/Dictionaries/hunspell/hunspell-pt_PT-20130125.tar.gz
Source1: https://pt-br.libreoffice.org/assets/Uploads/PT-BR-Documents/VERO/ptBR-2013-10-30AOC-2.zip
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
test "%{source1_hash}" = "none" || { f="%{SOURCE1}"; test -f "$f" || { echo "oreon: missing Source1 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source1_hash}" || { echo "oreon: Source1 hash mismatch" >&2; exit 1; }; }
%setup -q -n hunspell-pt_PT-20130125
unzip -q -o %{SOURCE1}
for i in README_pt_BR.TXT README_pt_PT.txt; do
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
cp -p pt*.dic pt*.aff $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}

pushd $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}/
pt_PT_aliases="pt_AO"
for lang in $pt_PT_aliases; do
        ln -s pt_PT.aff $lang.aff
        ln -s pt_PT.dic $lang.dic
done
popd


%files
%doc README_pt_PT.txt
%license COPYING
%{_datadir}/%{dict_dirname}/*
%exclude %{_datadir}/%{dict_dirname}/pt_BR.*

%files BR
%doc README_pt_BR.TXT README_en.TXT
%{_datadir}/%{dict_dirname}/pt_BR.*

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.20131030-16
- Import
