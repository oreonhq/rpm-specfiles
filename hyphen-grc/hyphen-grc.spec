Name: hyphen-grc
Summary: Ancient Greek hyphenation rules
%global upstreamid 20110913
Version: 0.%{upstreamid}
Release: 31%{?dist}
#? in a url causes trouble
#http://tug.org/svn/texhyphen/trunk/hyph-utf8/tex/generic/hyph-utf8/patterns/tex/hyph-grc.tex?view=co
Source: hyph-grc.tex
URL: http://tug.org/tex-hyphen
License: LPPL-1.3a
BuildArch: noarch
BuildRequires: hyphen-devel
BuildRequires: glibc-langpack-el

Requires: hyphen
Supplements: (hyphen and langpacks-grc)
Patch0: hyphen-grc-cleantex.patch

%description
Ancient Greek hyphenation rules.

%prep
%setup -T -q -c -n hyphen-grc
cp -p %{SOURCE0} hyph-grc.tex
%patch -P0 -p0 -b .clean

%build
grep -v "^%" hyph-grc.tex | tr ' ' '\n' > temp.tex
substrings.pl temp.tex temp.dic UTF-8
LANG=el_GR.utf8 uniq temp.dic > hyph_grc_GR.dic
echo "created with substring.pl by substrings.pl hyph-grc.tex hyph_grc_GR.dic UTF-8" > README
echo "---" >> README
head -n 37 hyph-grc.tex >> README

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/hyphen
cp -p hyph_grc_GR.dic $RPM_BUILD_ROOT/%{_datadir}/hyphen


%files
%doc README
%{_datadir}/hyphen/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.%{upstreamid}-31
- Prepare for Oreon 11 (RP1)
