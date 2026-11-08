# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 2e9ad7dd851bf45fab9f75cbff4cb493fee9979e8d8c7c9c3ee119022518edd6
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: python3-markupsafe
Version: 3.0.4
Release: 1%{?dist}
Summary: Safe string implementation for Python
License: BSD-3-Clause
URL: https://github.com/pallets/markupsafe
Source0: https://files.pythonhosted.org/packages/source/m/markupsafe/markupsafe-%{version}.tar.gz

BuildRequires: oreon-rpm-macros
BuildRequires: python3
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
