%global source0_hash e080a1e42ac443d8451df46d9d6628e64e8317aa53d826f99099652aaba613d0

Name: hyphen-eu
Summary: Basque hyphenation rules
# I found 2 sources www.tug.org and mirrors.ctan.org with same file
# let's choose older timestamp here
%global upstreamid 20190406
Version: 0.%{upstreamid}
Release: 13%{?dist}
Source:        https://raw.githubusercontent.com/hyphenation/tex-hyphen/master/hyph-utf8/tex/generic/hyph-utf8/patterns/tex/hyph-eu.tex
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
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
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
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.20190406-13
- Import
