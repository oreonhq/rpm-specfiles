%global source0_hash 7c37b9bde78054e43365b488a13859094c88bc66664b5b7a7bb073626454b38e
%global source1_hash 215fd73aa47b11e7fdd2e4d655e9fe37be4acdae16ff833badcfdfce79110aad
%if 0%{?fedora} >= 36 || 0%{?rhel} > 9 || (0%{?oreon} >= 11)
%global dict_dirname hunspell 
%else
%global dict_dirname myspell
%endif
Name: hunspell-pl
Summary: Polish hunspell dictionaries
%global upstreamid 20240901
Version: 0.%{upstreamid}
Release: 4%{?dist}
Source0:        https://github.com/LibreOffice/dictionaries/raw/refs/heads/master/pl_PL/pl_PL.aff
Source1:        https://github.com/LibreOffice/dictionaries/raw/refs/heads/master/pl_PL/pl_PL.dic
URL: https://sjp.pl/sl/ort/
License: LGPL-2.1-or-later OR GPL-1.0-or-later OR MPL-1.1 OR Apache-2.0 OR CC-BY-SA-4.0
BuildArch: noarch

Requires: hunspell
Supplements: (hunspell and langpacks-pl)

%description
Polish hunspell dictionaries.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
test "%{source1_hash}" = "none" || { f="%{SOURCE1}"; test -f "$f" || { echo "oreon: missing Source1 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source1_hash}" || { echo "oreon: Source1 hash mismatch" >&2; exit 1; }; }
%autosetup -c -T

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}
install -p -m 0644 %{SOURCE0} $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}/pl_PL.aff
install -p -m 0644 %{SOURCE1} $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}/pl_PL.dic


%files
%{_datadir}/%{dict_dirname}/*

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.20240901-4
- Import
