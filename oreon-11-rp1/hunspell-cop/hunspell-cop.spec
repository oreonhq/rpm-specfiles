%global source0_hash none

%if 0%{?fedora} >= 36 || 0%{?rhel} > 9 || (0%{?oreon} >= 11)
%global dict_dirname hunspell
%else
%global dict_dirname myspell
%endif

Name: hunspell-cop
Summary: Coptic hunspell dictionaries
Version: 0.3
Release: 32%{?dist}
Source:        dict-cop_EG_v03.oxt
URL: http://www.moheb.de/coptic_oo.html
License: GPL-3.0-or-later
BuildArch: noarch

Requires: hunspell-filesystem
Supplements: (hunspell and langpacks-cop)

%description
Coptic hunspell dictionaries.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -c -T -n %{name}-%{version}
unzip -q %{SOURCE0}

%build
for i in README.txt; do
  tr -d '\r' < $i > $i.new
  touch -r $i $i.new
  mv -f $i.new $i
done

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}
cp -p cop_EG-Bohairic/cop_EG.* $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}


%files
%doc README.txt
%license license-gpl.txt
%{_datadir}/%{dict_dirname}/*

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.3-32
- Import
