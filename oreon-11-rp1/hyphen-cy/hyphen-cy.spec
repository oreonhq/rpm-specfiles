Name: hyphen-cy
Summary: Welsh hyphenation rules
%global upstreamid 20110620
Version: 0.%{upstreamid}
Release: 30%{?dist}
#? in a url causes trouble
#http://tug.org/svn/texhyphen/trunk/hyph-utf8/tex/generic/hyph-utf8/patterns/tex/hyph-cy.tex?view=co
Source: hyph-cy.tex
URL: http://tug.org/tex-hyphen
License: LPPL-1.3a
BuildArch: noarch
BuildRequires: hyphen-devel
Requires: hyphen
Supplements: (hyphen and langpacks-cy)
Patch0: hyphen-cy-cleantex.patch

%description
Welsh hyphenation rules.

%prep
%setup -T -q -c -n hyphen-cy
cp -p %{SOURCE0} .
%patch -P0 -p0 -b .clean

%build
substrings.pl hyph-cy.tex hyph_cy_GB.dic ISO8859-1
echo "Created with substring.pl by substrings.pl hyph-cy.tex hyph_cy_GB.dic ISO8859-1" > README
echo "---" >> README
head -n 25 hyph-cy.tex >> README

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/hyphen
cp -p hyph_cy_GB.dic $RPM_BUILD_ROOT/%{_datadir}/hyphen


%files
%doc README
%{_datadir}/hyphen/*

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.20110620-30
- Import
