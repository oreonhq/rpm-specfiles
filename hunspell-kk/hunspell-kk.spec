%if 0%{?fedora} >= 36 || 0%{?rhel} > 9
%global dict_dirname hunspell
%else
%global dict_dirname myspell
%endif

Name: hunspell-kk
Summary: Kazakh hunspell dictionaries
Version: 1.1
Release: 33%{?dist}
Source: https://downloads.sourceforge.net/project/aoo-extensions/1172/12/dict-kk.oxt
URL: http://extensions.services.openoffice.org/project/dict-kk
License: GPL-2.0-or-later OR LGPL-2.1-or-later OR MPL-1.1
BuildArch: noarch

Requires: hunspell-filesystem
Supplements: (hunspell and langpacks-kk)

%description
Kazakh hunspell dictionaries.

%prep
%autosetup -c -n hunspell-kk

%build
for i in README_kk_KZ.txt; do
  tr -d '\r' < $i > $i.new
  touch -r $i $i.new
  mv -f $i.new $i
done

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}
cp -p kk_KZ.* $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}


%files
%doc README_kk_KZ.txt
%{_datadir}/%{dict_dirname}/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.1-33
- Prepare for Oreon 11 (RP1)
