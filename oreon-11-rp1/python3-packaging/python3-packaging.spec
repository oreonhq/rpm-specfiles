# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 94edc256424af38762eb31306eed28beb9f0efc50a8837492c9d6fd6004aed79
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: python3-packaging
Version: 26.3
Release: 1%{?dist}
Summary: Core utilities for Python packages
License: Apache-2.0 OR BSD-2-Clause
URL: https://github.com/pypa/packaging
Source0: https://files.pythonhosted.org/packages/source/p/packaging/packaging-%{version}.tar.gz

BuildRequires: oreon-rpm-macros
BuildRequires: python3
Requires: python3

%description
Core utilities for Python packages.

%prep
%oreon_sha256
%autosetup -n packaging-%{version} -p1

%build

%install
sitelib=$(python3 -c 'import sysconfig; print(sysconfig.get_path("purelib"))')
mkdir -p %{buildroot}$sitelib
cp -a src/packaging %{buildroot}$sitelib/
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
%license LICENSE LICENSE.APACHE LICENSE.BSD
