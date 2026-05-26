Name: hyphen-bg
Summary: Bulgarian hyphenation rules
Version: 4.3
Release: 250%{?dist}
Source: http://downloads.sourceforge.net/bgoffice/OOo-hyph-bg-%{version}.zip
# oreon url source checksums begin
%global source0_sha256 496d08c5eb25f794f32dfce7352e349420bf40a1a92c7bc15e2f7a1e8c5106c7
%global source0_file OOo-hyph-bg-4.3.zip
# oreon url source checksums end
URL: http://bgoffice.sourceforge.net/
License: GPL-2.0-or-later OR LGPL-2.1-or-later OR MPL-1.1
BuildArch: noarch

Requires: hyphen
Supplements: (hyphen and langpacks-bg)

%description
Bulgarian hyphenation rules.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/OOo-hyph-bg-4.3.zip; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "496d08c5eb25f794f32dfce7352e349420bf40a1a92c7bc15e2f7a1e8c5106c7" || { echo "oreon: Source0 SHA256 mismatch for OOo-hyph-bg-4.3.zip" >&2; exit 1; })
# oreon verify url source checksums end
%setup -q -n OOo-hyph-bg-%{version}

%build
for i in ChangeLog Copyright GPL-2.0.txt LGPL-2.1.txt MPL-1.1.txt README.bulgarian; do
  if ! iconv -f utf-8 -t utf-8 -o /dev/null $i > /dev/null 2>&1; then
    iconv -f ISO-8859-2 -t UTF-8 $i > $i.new
    touch -r $i $i.new
    mv -f $i.new $i
  fi
  tr -d '\r' < $i > $i.new
  touch -r $i $i.new
  mv -f $i.new $i
done
echo "UTF-8" > hyph_bg_BG.dic.new
tail -n +2 hyph_bg_BG.dic | iconv -f WINDOWS-1251 -t UTF-8 | tr -d '\r' >> hyph_bg_BG.dic.new
mv hyph_bg_BG.dic.new hyph_bg_BG.dic

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/hyphen
cp -p *.dic $RPM_BUILD_ROOT/%{_datadir}/hyphen


%files
%doc ChangeLog Copyright GPL-2.0.txt LGPL-2.1.txt MPL-1.1.txt README.bulgarian
%{_datadir}/hyphen/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 4.3-250
- Prepare for Oreon 11 (RP1)
