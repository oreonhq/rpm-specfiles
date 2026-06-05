%global source0_hash df931a605537f5d4bc3168a4b5e6c76e359805e444ababb93253ee070f6ab774

%if 0%{?fedora} >= 36 || 0%{?rhel} > 9 || (0%{?oreon} >= 11)
%global dict_dirname hunspell
%else
%global dict_dirname myspell
%endif

Name: hunspell-tk
Summary: Turkmen hunspell dictionaries
Version: 0.02
Epoch: 1
Release: 31%{?dist}
# Following link is dead now
# Do not report bugs to fix it
URL: http://borel.slu.edu/crubadan/apps.html
License: GPL-2.0-or-later
BuildArch: noarch

Requires: hunspell-filesystem
Supplements: (hunspell and langpacks-tk)

Source0:        https://github.com/openela-main/hunspell-tk/raw/el9/SOURCES/turkmen_spell_checker-0.02-tb+fx+sm.xpi

%description
Turkmen hunspell dictionaries.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -c -n hunspell-tk

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}
cp -p dictionaries/tk-TM.aff $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}/tk.aff
cp -p dictionaries/tk-TM.dic $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}/tk.dic

%files
%doc dictionaries/README_tk_TM.txt
%{_datadir}/%{dict_dirname}/*

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1:0.02-31
- Import
