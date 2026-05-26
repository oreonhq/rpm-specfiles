Name: mythes-fr
Summary: French thesaurus
Version: 2.3
Release: 29%{?dist}
Source: http://www.dicollecte.org/download/fr/thesaurus-v%{version}.zip
# oreon url source checksums begin
%global source0_sha256 61ec17d669a21e75969a2050a4615d7cea612ffd66d35fe9f4a8259c6d4bcd91
%global source0_file thesaurus-v2.3.zip
# oreon url source checksums end
URL: http://www.dicollecte.org/home.php?prj=fr
License: LGPL-2.1-or-later
BuildArch: noarch
Requires: mythes
Supplements: (mythes and langpacks-fr)

%description
French thesaurus.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/thesaurus-v2.3.zip; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "61ec17d669a21e75969a2050a4615d7cea612ffd66d35fe9f4a8259c6d4bcd91" || { echo "oreon: Source0 SHA256 mismatch for thesaurus-v2.3.zip" >&2; exit 1; })
# oreon verify url source checksums end
%setup -q -c

%build
for i in README_thes_fr.txt; do
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
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/mythes
cp -p thes_fr.dat $RPM_BUILD_ROOT/%{_datadir}/mythes/th_fr_FR_v2.dat
cp -p thes_fr.idx $RPM_BUILD_ROOT/%{_datadir}/mythes/th_fr_FR_v2.idx


%files
%doc README_thes_fr.txt
%{_datadir}/mythes/*

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.3-29
- Import
