Name: hyphen-hsb
Summary: Upper Sorbian hyphenation rules
%global upstreamid 20110620
Version: 0.%{upstreamid}
Release: 30%{?dist}
#? in a url causes trouble
#http://tug.org/svn/texhyphen/trunk/hyph-utf8/tex/generic/hyph-utf8/patterns/tex/hyph-hsb.tex?view=co
Source0: hyph-hsb.tex
URL: http://tug.org/tex-hyphen
License: LPPL-1.3a
BuildArch: noarch
BuildRequires: hyphen-devel
Requires: hyphen
Supplements: (hyphen and langpacks-hsb)
Patch0: hyphen-hsb-cleantex.patch

%description
Upper Sorbian hyphenation rules.

%prep
%setup -T -q -c -n hyphen-hsb
cp -p %{SOURCE0} .
%patch -P0 -p0 -b .clean

%build
substrings.pl hyph-hsb.tex hyph_hsb_DE.dic UTF-8
echo "created with substring.pl by substrings.pl hyph-hsb.tex hyph_hsb_DE.dic UTF-8" > README
echo "---" >> README
head -n 70 hyph-hsb.tex >> README

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/hyphen
cp -p hyph_hsb_DE.dic $RPM_BUILD_ROOT/%{_datadir}/hyphen


%files
%doc README
%{_datadir}/hyphen/*

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.20110620-30
- Import
