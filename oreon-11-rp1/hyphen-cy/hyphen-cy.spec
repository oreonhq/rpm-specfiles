%global source0_hash 22c4d441e790c035bd208c4cccbe9a8254ab81c3da0ca0a8b062f8ed34f3e14c

Name: hyphen-cy
Summary: Welsh hyphenation rules
%global upstreamid 20110620
Version: 0.%{upstreamid}
Release: 30%{?dist}
Source0:        https://github.com/hyphenation/tex-hyphen/raw/master/hyph-utf8/tex/generic/hyph-utf8/patterns/tex/hyph-cy.tex
URL: http://tug.org/tex-hyphen
License: LPPL-1.3a
BuildArch: noarch
BuildRequires: hyphen-devel
Requires: hyphen
Supplements: (hyphen and langpacks-cy)
%description
Welsh hyphenation rules.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | cut -d' ' -f1); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -T -q -c -n hyphen-cy
cp -p %{SOURCE0} .

%build
substrings.pl hyph-cy.tex hyph_cy_GB.dic ISO8859-1
echo "Created with substring.pl by substrings.pl hyph-cy.tex hyph_cy_GB.dic ISO8859-1" > README
echo "---" >> README
head -n 25 hyph-cy.tex >> README

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/hyphen
cp -p hyph_cy_GB.dic $RPM_BUILD_ROOT/%{_datadir}/hyphen


%files
%doc README
%{_datadir}/hyphen/*

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.20110620-30
- Import
