Name: mythes-fr
Summary: French thesaurus
Version: 2.3
Release: 29%{?dist}
Source: http://www.dicollecte.org/download/fr/thesaurus-v%{version}.zip
URL: http://www.dicollecte.org/home.php?prj=fr
License: LGPL-2.1-or-later
BuildArch: noarch
Requires: mythes
Supplements: (mythes and langpacks-fr)

%description
French thesaurus.

%prep
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
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.3-29
- Prepare for Oreon 11 (RP1)
