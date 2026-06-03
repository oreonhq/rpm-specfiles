%global source0_hash d188ccc49f06ce50ccb80ab9f3d08808dfb5caeb039c09cde55c8664ca6d8643
%global source1_hash d6ce8cef2bbf184459bb3073d2ddc246afa914efaf8fc438b32e8d7724abfcfd

%if 0%{?fedora} >= 36 || 0%{?rhel} > 9 || (0%{?oreon} >= 11)
%global dict_dirname hunspell 
%else
%global dict_dirname myspell
%endif

Name: hunspell-si
Summary: Sinhala hunspell dictionaries
Version: 0.2.1
Release: 36%{?dist}
Source0:        https://github.com/LibreOffice/dictionaries/raw/refs/heads/master/si_LK/si_LK.aff
Source1:        https://github.com/LibreOffice/dictionaries/raw/refs/heads/master/si_LK/si_LK.dic
URL: http://www.sandaru1.com/2009/08/29/sinhala-spell-checker-for-firefox/
License: GPL-2.0-or-later
BuildArch: noarch
Requires: hunspell
Supplements: (hunspell and langpacks-si)

%description
Sinhala hunspell dictionaries.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
test "%{source1_hash}" = "none" || { f="%{SOURCE1}"; test -f "$f" || { echo "oreon: missing Source1 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source1_hash}" || { echo "oreon: Source1 hash mismatch" >&2; exit 1; }; }
%autosetup -c -T

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}
install -p -m 0644 %{SOURCE0} $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}/si_LK.aff
install -p -m 0644 %{SOURCE1} $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}/si_LK.dic

%files
%{_datadir}/%{dict_dirname}/*

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.2.1-36
- Import
