Name: hyphen-lt
Summary: Lithuanian hyphenation rules
%global upstreamid 20100531
Version: 0.%{upstreamid}
Release: 31%{?dist}
Source: http://tug.org/svn/texhyphen/trunk/hyph-utf8/tex/generic/hyph-utf8/patterns/tex/hyph-lt.tex?view=co#/hyph-lt.tex
URL: http://tug.org/tex-hyphen
License: LPPL-1.3a
BuildArch: noarch
BuildRequires: hyphen-devel
Requires: hyphen
Supplements: (hyphen and langpacks-lt)
Patch0: hyphen-lt-cleantex.patch

%description
Lithuanian hyphenation rules.

%prep
%setup -T -q -c -n hyphen-lt
cp -p %{SOURCE0} .
%patch -P0 -p0 -b .clean

%build
substrings.pl hyph-lt.tex hyph_lt_LT.dic UTF-8
echo "Created with substring.pl by substrings.pl hyph-lt.tex hyph_lt_LT.dic UTF-8" > README
echo "Original in-line credits were:" >> README
echo "" >> README
head -n 45 hyph-lt.tex >> README

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/hyphen
cp -p hyph_lt_LT.dic $RPM_BUILD_ROOT/%{_datadir}/hyphen


%files
%doc README
%{_datadir}/hyphen/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.%{upstreamid}-31
- Prepare for Oreon 11 (RP1)
