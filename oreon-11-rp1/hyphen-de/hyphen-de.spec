%global source0_hash 731a87fb5ed128341b4178b1dee11819fd5e7392e4ac0526c318d9ab28cf61c9

Name: hyphen-de
Summary: German hyphenation rules
%global upstreamid 20060120
Version: 0.%{upstreamid}
Release: 37%{?dist}
Source:        hyph_de_DE.zip
URL: http://wiki.services.openoffice.org/wiki/Dictionaries
License: LGPL-2.1-or-later
BuildArch: noarch
Requires: hyphen
Supplements: (hyphen and langpacks-de)

%description
German hyphenation rules.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
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
