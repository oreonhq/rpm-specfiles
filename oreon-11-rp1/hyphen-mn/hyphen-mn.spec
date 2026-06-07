%global source0_hash none

Name: hyphen-mn
Summary: Mongolian hyphenation rules
%global upstreamid 20100531
Version: 0.%{upstreamid}
Release: 31%{?dist}
Source: https://raw.githubusercontent.com/hyphenation/tex-hyphen/master/hyph-utf8/tex/generic/hyph-utf8/patterns/tex/hyph-mn-cyrl.tex
URL: http://www.ctan.org/tex-archive/help/Catalogue/entries/mnhyphn.html
License: LPPL-1.3a
BuildArch: noarch
BuildRequires: hyphen-devel
Requires: hyphen
Supplements: (hyphen and langpacks-mn)

%description
Mongolian hyphenation rules.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | cut -d' ' -f1); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -T -q -c -n hyphen-mn
cp -p %{SOURCE0} .
%build
substrings.pl hyph-mn-cyrl.tex hyph_mn_MN.dic UTF-8
echo "Created with substring.pl by substrings.pl hyph-mn-cyrl.tex hyph_mn_MN.dic UTF-8" > README
echo "Original in-line credits were:" >> README
echo "" >> README
head -n 83 hyph-mn-cyrl.tex >> README

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/hyphen
cp -p hyph_mn_MN.dic $RPM_BUILD_ROOT/%{_datadir}/hyphen


%files
%doc README
%{_datadir}/hyphen/*

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.20100531-31
- Import
