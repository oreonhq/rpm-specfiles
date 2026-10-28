%global source0_hash 3ff6c5d8b43e8c37bb6e6dd5085658d658a7a0bdcd20b6a07b1fcfc1c4e9d632
%global oreon_bootstrap %{nil}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: python3-pefile
Version: 2024.8.26
Release: 8%{?dist}
Summary: Python PE file parser
License: MIT
URL: https://github.com/erocarrera/pefile
Source0: https://files.pythonhosted.org/packages/source/p/pefile/pefile-%{version}.tar.gz

BuildRequires: oreon-rpm-macros
%if %{without bootstrap} && !0%{?bootstrap}
BuildRequires: python3
%endif
Requires: python3

%description
Python PE file parser.

%prep
%oreon_sha256
%autosetup -n pefile-%{version} -p1

%build

%install
sitelib=$(python3 -c 'import sysconfig; print(sysconfig.get_path("purelib"))')
mkdir -p %{buildroot}$sitelib
cp -a pefile.py peutils.py ordlookup %{buildroot}$sitelib/
find %{buildroot} -type f -exec grep -I -l -E '^#! */usr/bin/env python' {} + | while read -r f; do
  sed -i '1s|^#! */usr/bin/env python.*|#!/usr/bin/python3|' "$f"
done
%oreon_filelist
while read -r f; do
  case "$f" in
    *.py) printf '%s\n' "$(dirname "$f")/__pycache__/*" ;;
  esac
done < %{_builddir}/%{name}.files | sort -u >> %{_builddir}/%{name}.files

%files -f %{_builddir}/%{name}.files
%license LICENSE
