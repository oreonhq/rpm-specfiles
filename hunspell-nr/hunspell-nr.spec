%if 0%{?fedora} >= 36 || 0%{?rhel} > 9
%global dict_dirname hunspell 
%else
%global dict_dirname myspell
%endif

Name: hunspell-nr
Summary: Southern Ndebele hunspell dictionaries
%global upstreamid 20091030
Version: 0.%{upstreamid}
Release: 34%{?dist}
Source: https://downloads.sourceforge.net/project/aoo-extensions/3141/0/dict-nr_za-2009.10.30.oxt
URL: https://extensions.openoffice.org/en/project/ndebele-south-spell-checker
License: LGPL-2.1-or-later
BuildArch: noarch

Requires: hunspell
Supplements: (hunspell and langpacks-nr)

%description
Southern Ndebele hunspell dictionaries.

%prep
%autosetup -c -n hunspell-nr

%build
for i in README-nr_ZA.txt release-notes-nr_ZA.txt package-description.txt; do
  if ! iconv -f utf-8 -t utf-8 -o /dev/null $i > /dev/null 2>&1; then
    iconv -f ISO-8859-2 -t UTF-8 $i > $i.new
    touch -r $i $i.new
    mv -f $i.new $i
  fi
  tr -d '\r' < $i > $i.new
  touch -r $i $i.new
  mv -f $i.new $i
done

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}
cp -p *.dic *.aff $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}


%files
%doc README-nr_ZA.txt release-notes-nr_ZA.txt package-description.txt
%{_datadir}/%{dict_dirname}/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.%{upstreamid}-34
- Prepare for Oreon 11 (RP1)
