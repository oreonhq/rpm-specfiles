%global source0_hash none

Name: hyphen-ia
Summary: Interlingua hyphenation rules
%global upstreamid 20050628
Version: 0.%{upstreamid}
Release: 32%{?dist}
Source: http://www.ctan.org/get/language/hyphenation/iahyphen.tex
URL: http://www.ctan.org/tex-archive/help/Catalogue/entries/iahyphen.html
License: LPPL-1.3a
BuildArch: noarch
BuildRequires: hyphen-devel
Requires: hyphen
Supplements: (hyphen and langpacks-ia)
Patch0: hyphen-ia-cleantex.patch

%description
Interlingua hyphenation rules.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%setup -T -q -c -n hyphen-ia
cp -p %{SOURCE0} .
%patch -P0 -p0 -b .clean

%build
substrings.pl iahyphen.tex hyph_ia.dic ISO8859-1
echo "Created with substring.pl by substrings.pl iahyphen.tex hyph_ia.dic ISO8859-1" > README
echo "---" >> README
head -n 25 iahyphen.tex >> README

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/hyphen
cp -p hyph_ia.dic $RPM_BUILD_ROOT/%{_datadir}/hyphen


%files
%doc README
%{_datadir}/hyphen/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.%{upstreamid}-32
- Prepare for Oreon 11 (RP1)
