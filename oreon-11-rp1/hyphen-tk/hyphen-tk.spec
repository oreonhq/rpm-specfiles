Name: hyphen-tk
Summary: Turkmen hyphenation rules
%global upstreamid 20210322
Version: 0.%{upstreamid}
Release: 8%{?dist}
Source: http://mirror.ctan.org/language/hyph-utf8/tex/generic/hyph-utf8/patterns/tex/hyph-tk.tex
URL: http://tug.org/tex-hyphen
License: MIT
BuildArch: noarch
BuildRequires: hyphen-devel
Requires: hyphen
Supplements: (hyphen and langpacks-tk)
Patch0: hyphen-tk-cleantex.patch

%description
Turkmen hyphenation rules.

%prep
%setup -T -q -c -n hyphen-tk
cp -p %{SOURCE0} .
%patch -P0 -p0 -b .clean

%build
substrings.pl hyph-tk.tex hyph_tk_TM.dic UTF-8
echo "Created with substring.pl by substrings.pl hyph-tk.tex hyph_tk_TM.dic UTF-8" > README
echo "Original in-line credits were:" >> README
echo "" >> README
head -n 33 hyph-tk.tex >> README

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/hyphen
cp -p hyph_tk_TM.dic $RPM_BUILD_ROOT/%{_datadir}/hyphen


%files
%doc README
%{_datadir}/hyphen/hyph_tk_TM.dic

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.20210322-8
- Import
