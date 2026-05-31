%global source0_hash none

%if 0%{?fedora} >= 36 || 0%{?rhel} > 9 || (0%{?oreon} >= 11)
%global dict_dirname hunspell
%else
%global dict_dirname myspell
%endif

Name: hunspell-lt
Summary: Lithuanian hunspell dictionaries
Version: 1.2.1
Release: 37%{?dist}
## Note that upstream is dead and there is no download link available
## so please don't report FTBFS bugs for this package.
Source:        https://www.akl.lt/ispell-lt/lt_LT-%{version}.zip
URL: https://ftp.akl.lt/ispell-lt/
License: BSD-3-Clause
BuildArch: noarch

Requires: hunspell-filesystem
Supplements: (hunspell and langpacks-lt)

%description
Lithuanian hunspell dictionaries.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n lt_LT-%{version}

%build
chmod -x *
for i in INSTRUKCIJOS.txt; do
  tr -d '\r' < $i > $i.new
  touch -r $i $i.new
  mv -f $i.new $i
done

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}
cp -p *.dic *.aff $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}


%files
%doc README.EN INSTRUKCIJOS.txt
%{_datadir}/%{dict_dirname}/*

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.2.1-37
- Import
