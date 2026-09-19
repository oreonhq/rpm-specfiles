%global source0_hash 987ba0f4f8f14836ae006e8ea9a3794e6f20af396660d00ee5c3094db5d46985

Name: virt-bootstrap
Version: 1.1.1
Release: 30%{?dist}
Summary: System container rootfs creation tool

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License: GPL-3.0-or-later
URL: https://github.com/virt-manager/virt-bootstrap
Source0: http://virt-manager.org/download/sources/virt-bootstrap/%{name}-%{version}.tar.gz

# Upstream patches

# Fix for Python 3.11
Patch100: virt_bootstrap-Fix-build-with-Python-3.11.patch

BuildRequires: /usr/bin/pod2man
BuildRequires: /usr/bin/git
BuildRequires: python3-devel
BuildRequires: python3-libguestfs
BuildRequires: python3-passlib
BuildRequires: python3-setuptools
BuildRequires: fdupes

Requires: python3-libguestfs
Requires: python3-passlib
Requires: skopeo
Requires: libvirt-sandbox

BuildArch: noarch

%description
Provides a way to create the root file system to use for
libvirt containers.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -S git

%build
%py3_build

%install
%py3_install
%fdupes %{buildroot}%{_prefix}

# Replace '#!/usr/bin/env python3' with '#!/usr/bin/python3'
# The format is ideal for upstream, but not a distro. See:
# https://fedoraproject.org/wiki/Features/SystemPythonExecutablesUseSystemPython
for f in $(find %{buildroot} -type f -executable -print); do
    sed -i '1 s/^#!\/usr\/bin\/env python3/#!%{__python3}/' $f || :
done

# Delete '#!/usr/bin/env python'
# The format is ideal for upstream, but not a distro. See:
# https://fedoraproject.org/wiki/Features/SystemPythonExecutablesUseSystemPython
for f in $(find %{buildroot} -type f \! -executable -print); do
    sed -i '/^#!\/usr\/bin\/env python/d' $f || :
done

%files
%license LICENSE
%doc README.md ChangeLog AUTHORS
%{_bindir}/virt-bootstrap
%{python3_sitelib}/virtBootstrap
%{python3_sitelib}/virt_bootstrap-*.egg-info
%{_mandir}/man1/virt-bootstrap*

%changelog
%autochangelog
