Name: hyphen-eu
Summary: Basque hyphenation rules
# I found 2 sources www.tug.org and mirrors.ctan.org with same file
# let's choose older timestamp here
%global upstreamid 20190406
Version: 0.%{upstreamid}
Release: 13%{?dist}
Source: http://mirrors.ctan.org/language/hyph-utf8/tex/generic/hyph-utf8/patterns/tex/hyph-eu.tex
URL: http://tp.lc.ehu.es/jma/basque.html
License: MIT
BuildArch: noarch
BuildRequires: hyphen-devel
Requires: hyphen
Supplements: (hyphen and langpacks-eu)
Patch0: hyphen-eu-cleantex.patch

%description
Basque hyphenation rules.

%prep
%setup -T -q -c -n hyphen-eu
cp -p %{SOURCE0} .
%patch -P0 -p0 -b .clean

%build
grep -v "^%" hyph-eu.tex | tr ' ' '\n' > temp.tex
substrings.pl temp.tex hyph_eu_ES.dic ISO8859-1
echo "Created with substring.pl by substrings.pl hyph-eu.tex hyph_eu_ES.dic ISO8859-1" > README
echo "---" >> README
head -n 34 hyph-eu.tex >> README

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/hyphen
cp -p hyph_eu_ES.dic $RPM_BUILD_ROOT/%{_datadir}/hyphen


%files
%doc README
%{_datadir}/hyphen/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.%{upstreamid}-13
- Prepare for Oreon 11 (RP1)
