%global source0_hash 12934d021558bf001c0bcaf0a1fc6f08ce6c7e8b7d48a8cb0bfe31763f0f5988

%if 0%{?fedora} >= 36 || 0%{?rhel} > 9
%global dict_dirname hunspell
%else
%global dict_dirname myspell
%endif

Name: hunspell-eu
Summary: Basque hunspell dictionaries
Version: 5.1
Release: 15%{?dist}
URL: http://xuxen.eus
License: LGPL-3.0-or-later
BuildArch: noarch

Requires: hunspell-filesystem
Supplements: (hunspell and langpacks-eu)

Source0:        https://xuxen.eus/static/hunspell/xuxen_5.1_hunspell.zip

%description
Basque hunspell dictionaries.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -c -n hunspell-eu

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}
cp -p eu-ES/eu-ES.dic $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}/eu_ES.dic
cp -p eu-ES/eu-ES.aff $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}/eu_ES.aff

%files
%doc XUXEN_kode_irekia_eskuliburua-LINUX-OO.pdf
%{_datadir}/%{dict_dirname}/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 5.1-15
- Prepare for Oreon 11 (RP1)
