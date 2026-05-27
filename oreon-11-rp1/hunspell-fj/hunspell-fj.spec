%global source0_hash none

%if 0%{?fedora} >= 36 || 0%{?rhel} > 9 || 0%{?oreon}
%global dict_dirname hunspell
%else
%global dict_dirname myspell
%endif

Name: hunspell-fj
Summary: Fijian hunspell dictionaries
Version: 1.2
Release: 34%{?dist}
#Source: http://www.foss.usp.ac.fj/OOo_fj/OOo_fj_FJ.zip
Source: https://addons.mozilla.org/firefox/downloads/file/84397/fijian_spelling_dictionary-%{version}-fx+tb+sm.xpi
URL: http://www.iosn.net/pacific-islands/usp-microgrants/fijian-spellchecker
License: LGPL-2.1-or-later OR GPL-2.0-or-later OR MPL-1.1
BuildArch: noarch
BuildRequires: hunspell-devel

Requires: hunspell-filesystem
Supplements: (hunspell and langpacks-fj)

%description
Fijian hunspell dictionaries.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -c

%build
cd dictionaries
for i in README_fj_FJ.txt; do
  tr -d '\r' < $i > $i.new
  touch -r $i $i.new
  mv -f $i.new $i
done
chmod -x fj_FJ.*

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}
cp -p dictionaries/fj_FJ.aff $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}/fj.aff
cp -p dictionaries/fj_FJ.dic $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}/fj.dic


%files
%doc dictionaries/README_fj_FJ.txt
%{_datadir}/%{dict_dirname}/*

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.2-34
- Import
