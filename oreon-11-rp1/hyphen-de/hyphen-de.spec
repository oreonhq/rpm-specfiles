Name: hyphen-de
Summary: German hyphenation rules
%global upstreamid 20060120
Version: 0.%{upstreamid}
Release: 37%{?dist}
Source: http://download.services.openoffice.org/contrib/dictionaries/hyph_de_DE.zip
URL: http://wiki.services.openoffice.org/wiki/Dictionaries
License: LGPL-2.1-or-later
BuildArch: noarch
Requires: hyphen
Supplements: (hyphen and langpacks-de)

%description
German hyphenation rules.

%prep
%autosetup -c -n hyphen-de

%build
for i in README_hyph_de_DE.txt; do
  if ! iconv -f utf-8 -t utf-8 -o /dev/null $i > /dev/null 2>&1; then
    iconv -f ISO-8859-1 -t UTF-8 $i > $i.new
    touch -r $i $i.new
    mv -f $i.new $i
  fi
  tr -d '\r' < $i > $i.new
  touch -r $i $i.new
  mv -f $i.new $i
done

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/hyphen
cp -p hyph_de_DE.dic $RPM_BUILD_ROOT/%{_datadir}/hyphen

pushd $RPM_BUILD_ROOT/%{_datadir}/hyphen/
de_DE_aliases="de_AT de_BE de_CH de_LI de_LU"
for lang in $de_DE_aliases; do
        ln -s hyph_de_DE.dic hyph_$lang.dic
done
popd


%files
%doc README_hyph_de_DE.txt
%{_datadir}/hyphen/*

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.20060120-37
- Import
