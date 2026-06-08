%global source0_hash 38870c0292b1937517dd1709c5af5b1200f7a15a25469f5389a1783579abaf6a

Name: hyphen-grc
Summary: Ancient Greek hyphenation rules
%global upstreamid 20110913
Version: 0.%{upstreamid}
Release: 31%{?dist}
#? in a url causes trouble
#http://tug.org/svn/texhyphen/trunk/hyph-utf8/tex/generic/hyph-utf8/patterns/tex/hyph-grc.tex?view=co
Source0: https://github.com/hyphenation/tex-hyphen/raw/master/hyph-utf8/tex/generic/hyph-utf8/patterns/tex/hyph-grc.tex
URL: http://tug.org/tex-hyphen
License: LPPL-1.3a
BuildArch: noarch
BuildRequires: hyphen-devel
BuildRequires: glibc-langpack-el

Requires: hyphen
Supplements: (hyphen and langpacks-grc)

%description
Ancient Greek hyphenation rules.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f"  | cut -d' ' -f1); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -T -q -c -n hyphen-grc
cp -p %{SOURCE0} hyph-grc.tex
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
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.20110913-31
- Import
