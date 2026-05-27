%global source0_hash none

%if 0%{?fedora} >= 36 || 0%{?rhel} > 9
%global dict_dirname hunspell
%else
%global dict_dirname myspell
%endif

Name: hunspell-cv
Summary: Chuvash hunspell dictionaries
Version: 1.06
Release: 20%{?dist}
Source: http://hunspell.chv.su/files/Chuvash_Spell-1.06.oxt
URL: http://hunspell.chv.su/download.shtml
License: GPL-3.0-or-later OR LGPL-3.0-or-later OR MPL-1.1
BuildArch: noarch
Requires: hunspell-filesystem
Supplements: (hunspell and langpacks-cv)

%description
Chuvash hunspell dictionaries.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -c

%build
for i in README_cv_RU.txt; do
  tr -d '\r' < $i > $i.new
  touch -r $i $i.new
  mv -f $i.new $i
done

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}
cp -p cv_RU.* $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}/


%files
%doc README_cv_RU.txt
%license GPLv3.txt LGPLv3.txt MPL-1.1.txt
%{_datadir}/%{dict_dirname}/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.06-20
- Prepare for Oreon 11 (RP1)
