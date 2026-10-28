%global source0_hash ee55d3edf80167e48ea11a923c7386f4669df67d7994554387f84e7d8b0a2bf0
%global oreon_bootstrap %{nil}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: python3-markupsafe
Version: 3.0.2
Release: 8%{?dist}
Summary: Safe string implementation for Python
License: BSD-3-Clause
URL: https://github.com/pallets/markupsafe
Source0: https://files.pythonhosted.org/packages/source/m/markupsafe/markupsafe-%{version}.tar.gz

BuildRequires: oreon-rpm-macros
%if %{without bootstrap} && !0%{?bootstrap}
BuildRequires: python3
%endif
Requires: python3

%description
Safe string implementation for Python.

%prep
%oreon_sha256
%autosetup -n markupsafe-%{version} -p1

%build

%install
sitelib=$(python3 -c 'import sysconfig; print(sysconfig.get_path("purelib"))')
mkdir -p %{buildroot}$sitelib
cp -a src/markupsafe %{buildroot}$sitelib/
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
%license LICENSE.txt
