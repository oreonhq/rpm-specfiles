%global source0_hash 4012832dfaecbd9b1b4c244307f4c24833c26161622ff1f7bb51b8ba4208dc12

%if 0%{?fedora} > 35 || (0%{?oreon} >= 11)
%global dict_dirname hunspell 
%else
%global dict_dirname myspell
%endif
Name: hunspell-sc
Summary: Sardinian hunspell dictionaries
%global upstreamid 20081101
Version: 0.%{upstreamid}
Release: 38%{?dist}
URL: http://extensions.services.openoffice.org/project/Dict_sc
#The license included is AGPLv3 and pkg-desc/pkg-description.txt
#says AGPLv3 or later, but the sc_IT.aff header states "GPLv2"
License: AGPL-3.0-or-later AND GPL-2.0-only
BuildArch: noarch
BuildRequires: hunspell-devel

Requires: hunspell
Supplements: (hunspell and langpacks-sc)

Source0:        https://downloads.sourceforge.net/project/aoo-extensions/1446/2/dict_sc_it03.oxt

%description
Sardinian hunspell dictionaries.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -c -n hunspell-sc

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}
cp -p sc_IT.aff $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}/sc_IT.aff
cp -p sc_it.dic $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}/sc_IT.dic

%files
%license registration/agpl3-en.txt
%{_datadir}/%{dict_dirname}/*

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.20081101-38
- Import
