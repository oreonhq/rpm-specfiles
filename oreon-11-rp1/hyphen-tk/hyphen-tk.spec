%global source0_hash 801ef59c14dab4fec0a9ae178632e63b8ef9f0362dcea74f4a3689a4a7908690

Name: hyphen-tk
Summary: Turkmen hyphenation rules
%global upstreamid 20210322
Version: 0.%{upstreamid}
Release: 8%{?dist}
Source:        https://raw.githubusercontent.com/hyphenation/tex-hyphen/master/hyph-utf8/tex/generic/hyph-utf8/patterns/tex/hyph-tk.tex
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
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
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
