%global source0_hash 421028e1585556086d6686c7f2080c4ad6809c6f73d8497cbc8d66668981b04b
%if 0%{?fedora} > 35 || (0%{?oreon} >= 11)
%global dict_dirname hunspell 
%else
%global dict_dirname myspell
%endif
Name: hunspell-quh
Summary:        Quechua, South Bolivia hunspell dictionaries
%global upstreamid 20110816
Version: 0.%{upstreamid}
Release:        1%{?dist}
URL: http://www.runasimipi.org/blanco-en.php?file=desarrollar-orto
License: GPL-2.0-or-later
BuildArch: noarch
Requires: hunspell
Supplements: (hunspell and langpacks-quh)
Source0:        https://www.runasimipi.org/quh_BO-pack.zip
# oreon:deps

# /oreon:deps
%description
Quechua South Bolivia hunspell dictionaries.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n quh_BO-pack
unzip -qq quh_BO.zip

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}
cp -p quh_BO/quh_BO.* $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}/
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.20110816-32
- Import
