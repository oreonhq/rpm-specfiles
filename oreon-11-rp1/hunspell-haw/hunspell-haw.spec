%global source0_hash 6f4d77e60e348fff1f912af14193e753534c8786bc5a593c56527dca8c79f6ee

%if 0%{?fedora} >= 36 || 0%{?rhel} > 9 || (0%{?oreon} >= 11)
%global dict_dirname hunspell
%else
%global dict_dirname myspell
%endif

Name: hunspell-haw
Summary: Hawaiian hunspell dictionaries
Version: 0.03
Release: 20%{?dist}
URL: http://borel.slu.edu/crubadan/
License: GPL-2.0-or-later
BuildArch: noarch
Requires: hunspell-filesystem
Supplements: (hunspell and langpacks-haw)

Source0:        https://github.com/openela-main/hunspell-haw/raw/el9/SOURCES/hawaiian_spell_checker-0.03-tb+fx+fn+sm.xpi

%description
Hawaiian hunspell dictionaries.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -c -T
unzip -q %{SOURCE0}

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}
cp -p dictionaries/haw-US.aff $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}/haw.aff
cp -p dictionaries/haw-US.dic $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}/haw.dic

%files
%doc dictionaries/README_haw_US.txt
%{_datadir}/%{dict_dirname}/*

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.03-20
- Import
