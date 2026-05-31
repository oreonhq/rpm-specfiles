%global source0_hash none

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
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
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
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.20100531-31
- Import
