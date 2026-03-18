Name: hyphen-sv
Summary: Swedish hyphenation rules
Version: 1.00.1
Release: 38%{?dist}
Source: https://downloads.sourceforge.net/project/aoo-extensions/1966/4/hyph_sv_se.oxt
URL: http://extensions.services.openoffice.org/node/1968
License: LGPL-2.1-or-later OR GPL-2.0-or-later
BuildArch: noarch
Requires: hyphen
Supplements: (hyphen and langpacks-sv)

%description
Swedish hyphenation rules.

%prep
%autosetup -c -n hyphen-sv

%build
chmod -x *.dic *.txt
for i in README_sv_SE.txt; do
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
cp -p hyph_sv_SE.dic $RPM_BUILD_ROOT/%{_datadir}/hyphen

pushd $RPM_BUILD_ROOT/%{_datadir}/hyphen
sv_SE_aliases="sv_FI"
for lang in $sv_SE_aliases; do
        ln -s hyph_sv_SE.dic hyph_$lang.dic
done
popd


%files
%doc README_sv_SE.txt
%{_datadir}/hyphen/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.00.1-38
- Prepare for Oreon 11 (RP1)
